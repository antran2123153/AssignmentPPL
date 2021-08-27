from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple, Type
from AST import *
from StaticError import *
from functools import *

from main.d95.utils.AST import AssocExp


class IntType:
    pass
class FloatType:
    pass
class StringType:
    pass
class BoolType:
    pass
class VoidType:
    pass
class NoneType:
    pass
class ArrayType:
    def __init__(self, indexType, type):
        self.indexType = indexType
        self.type = type


class Variable:
    def __init__(self, name, type):
        self.name = name
        self.type = type
class Constant:
    def __init__(self, name, type):
        self.name = name
        self.type = type
class Parameter:
    def __init__(self, name, type):
        self.name = name
        self.type = type
class Function:
    def __init__(self, name, type, param):
        self.name = name
        self.type = type
        self.param = param


def isUniqueTypeArray(arr):
    n = len(arr)
    if n < 2:
        return True
    if type(arr[0]) is tuple:
        while n > 1:
            if type(arr[n - 1][0]) is not type(arr[n - 2][0]) or type(arr[n - 1][1]) is not type(arr[n - 2][1]):
                return False
            n = n - 1
        return True
    else:
        while n > 1:
            if type(arr[n - 1]) is not type(arr[n - 2]):
                return False
            n = n - 1
        return True


def compareArray(lst, arr):
    n = len(lst)
    if n != len(arr):
        return False
    while n > 0:
        if (type(lst[n - 1].type) is FloatType and (type(arr[n - 1]) is IntType or type(arr[n - 1]) is BoolType)) or (type(lst[n - 1].type) is IntType and type(arr[n - 1]) is BoolType):
            n = n - 1
        elif type(lst[n - 1].type) is not NoneType and type(lst[n - 1].type) is not type(arr[n - 1]):
            return False
        else:
            n = n - 1
    return True



class Visitor(ABC):
    def visit(self, ctx, o):
        return ctx.accept(self, o)


class StaticChecker(Visitor):
    def __init__(self, asttree):
        self.asttree = asttree
    
    def check(self):
        self.visitProgram(self.asttree, [[]])

    def visitProgram(self, ctx, o):
        # const: List[ConstDecl]
        # nonconst: List[NonConstDecl]
        o = [[]]
        self.currentStmt = None
        self.currentFunc = None
        for const in ctx.const:
            self.visit(const, o)
        for nonconst in ctx.nonconst:
            self.visit(nonconst, o)
        if "_main" not in [decl.name for u in o for decl in u]:
            raise NoEntryPoint()


    def visitConstDecl(self, ctx, o):
        # id: Id
        # value: Exp
        if ctx.id.name in [decl.name for u in o for decl in u]:
            raise Redeclared(Const(), ctx.id.name)
        typ = self.visit(ctx.value, o)
        if type(typ) is NoneType or type(typ) is VoidType:
            raise TypeCannotBeInferred(ctx)
        o[0] += [Constant(ctx.id.name, typ)]


    def visitAssign(self, ctx, o):
        # lhs: LHS --- id / array access
        # rhs: Exp --- type / arraylit
        self.currentStmt = ctx
        rhs = self.visit(ctx.rhs, o)
        if type(ctx.lhs) is Id:
            if ctx.lhs.name in [decl.name for u in o for decl in u]:
                lhs = self.visit(ctx.lhs, o)
                if type(lhs) is NoneType:
                    if type(rhs) is NoneType:
                        raise TypeCannotBeInferred(self.currentStmt)
                    for param in self.currentFunc.param:
                        if param.name == ctx.lhs.name:
                            param.type = rhs
                            break
                    for decl in [decl for u in o for decl in u]:
                        if decl.name == ctx.lhs.name:
                            decl.type = rhs
                            return
                elif type(rhs) is NoneType and type(ctx.rhs) is Id:
                    for param in self.currentFunc.param:
                        if param.name == ctx.rhs.name:
                            param.type = lhs
                            break
                    for decl in [decl for u in o for decl in u]:
                        if decl.name == ctx.rhs.name:
                            decl.type = lhs
                            return
                elif (type(rhs) is IntType or type(rhs) is BoolType) and type(lhs) is FloatType:
                    return
                elif  type(rhs) is BoolType and type(lhs) is IntType:
                    return
                elif type(lhs) is not type(rhs):
                    raise TypeMismatchInStmt(ctx)
            else:
                if type(rhs) is NoneType:
                    raise TypeCannotBeInferred(ctx)
                elif type(rhs) is VoidType:
                    raise TypeMismatchInStmt(ctx)
                o[0] += [Variable(ctx.lhs.name, rhs)]
        else:
            lhs = self.visit(ctx.lhs, o)
            if type(lhs) is VoidType:
                raise TypeMismatchInStmt(ctx)
            if type(lhs) is NoneType:
                if type(rhs) is NoneType:
                    raise TypeCannotBeInferred(ctx)
                for param in self.currentFunc.param:
                    if param.name == ctx.lhs.name:
                        param.type = rhs
                        break
                for decl in [decl for u in o for decl in u]:
                    if decl.name == ctx.lhs.name:
                        decl.type = rhs
                        return
            elif type(rhs) is NoneType and type(ctx.rhs) is Id:
                for param in self.currentFunc.param:
                    if param.name == ctx.rhs.name:
                        param.type = lhs
                        break
                for decl in [decl for u in o for decl in u]:
                    if decl.name == ctx.rhs.name:
                        decl.type = lhs
                        return
            elif type(lhs) is not type(rhs):
                    raise TypeMismatchInExpr(ctx)


    def visitParamDecl(self, ctx, o):
        # id: Id
        if ctx.id.name in [decl.name for decl in o[0]]:
            raise Redeclared(Param(), ctx.id.name)
        o[0] += [Parameter(ctx.id.name, NoneType())]


    def visitFuncDecl(self, ctx, o):
        # name: Id
        # param: List[ParamDecl]
        # body: List[Statement]
        if ctx.name.name in ["_echo", "_read"] or ctx.name.name in [decl.name for u in o for decl in u]:
            raise Redeclared(Func(), ctx.name.name)
        o1 = [[]]
        for param in ctx.param:
            self.visit(param, o1)
        param = []
        for i in o1[0]:
            param += [Parameter(i.name, NoneType())]
        self.currentFunc = Function(ctx.name.name, VoidType(), param)
        o1 = o1 + o
        for body in ctx.body:
            self.currentStmt = body
            self.visit(body, o1)
        o[0] += [self.currentFunc]
        self.currentFunc = None
             

    def visitForEach(self, ctx, o):
        # arr: Exp
        # key: Id
        # value: Id
        # body: List[Stmt]
        arr = self.visit(ctx.arr, o)
        if type(arr) is NoneType:
            raise TypeCannotBeInferred(ctx)
        elif type(arr) is not ArrayType:
            raise TypeMismatchInStmt(ctx)
        elif type(arr.indexType) is NoneType or type(arr.type) is NoneType:
            raise TypeCannotBeInferred(ctx)
        o1 = [[]] + o
        o1[0] += [Variable(ctx.key.name, arr.indexType)]
        o1[0] += [Variable(ctx.value.name, arr.type)]
        for body in ctx.body:
            self.currentStmt = body
            self.visit(body, o1)


    def visitWhile(self, ctx, o):
        # cond: Exp
        # body: List[Stmt]
        if type(self.visit(ctx.cond, o)) is not BoolType:
            raise TypeMismatchInStmt(ctx)
        for body in ctx.body:
            self.currentStmt = body
            self.visit(body, o)


    def visitBreak(self, ctx, o):
        pass


    def visitContinue(self, ctx, o):
        pass


    def visitReturn(self, ctx, o):
        # exp: Exp or None if empty
        if ctx.exp:
            exp = self.visit(ctx.exp, o)
            if type(exp) is NoneType:
                raise TypeCannotBeInferred(ctx)
            self.currentFunc.type = exp


    def visitId(self, ctx, o):
        # name: str
        for decl in [decl for u in o for decl in u]:
            if decl.name == ctx.name:
                return decl.type
        raise UndeclaredIdentifier(ctx.name)


    def visitArrayAccess(self, ctx, o):
        # id: Id
        # idx: List[Expr]
        arr = self.visit(ctx.id, o)
        if type(arr) is not ArrayType:
            raise TypeMismatchInExpr(ctx)
        for exp in ctx.idx: 
            typ = self.visit(exp, o)
            if type(typ) is NoneType:
                raise TypeCannotBeInferred(self.currentStmt)
            if type(arr) is not ArrayType:
                raise TypeMismatchInExpr(ctx)
            if type(typ) is not type(arr.indexType):
                raise TypeMismatchInExpr(ctx)
            arr = arr.type
        if type(arr) is ArrayType:
            raise TypeMismatchInExpr(ctx)
        return arr


    def visitBinExp(self, ctx, o):
        # op: str
        # left: Exp
        # right: Exp
        op = ctx.op
        left = self.visit(ctx.left, o)
        right = self.visit(ctx.right, o)

        if type(left) is NoneType and type(right) is NoneType:
            if op in ["+", "-", "*", "/", "%", "==", "!=", "<", ">", ">=", "<="]:
                for param in self.currentFunc.param:
                    if param.name == ctx.left.name:
                        param.type = FloatType()
                        break
                for decl in [decl for u in o for decl in u]:
                    if decl.name == ctx.left.name:
                        decl.type = FloatType()
                        break
                for param in self.currentFunc.param:
                    if param.name == ctx.right.name:
                        param.type = FloatType()
                        break
                for decl in [decl for u in o for decl in u]:
                    if decl.name == ctx.right.name:
                        decl.type = FloatType()
                        break
                if op in ["==", "!=", "<", ">", ">=", "<="]:
                    return BoolType()
                return FloatType()
            raise TypeCannotBeInferred(self.currentStmt)
        elif type(left) is NoneType:
            for param in self.currentFunc.param:
                if param.name == ctx.left.name:
                    param.type = right
                    break
            for decl in [decl for u in o for decl in u]:
                if decl.name == ctx.left.name:
                    decl.type = right
                    return
            left = right
        elif type(right) is NoneType:
            for param in self.currentFunc.param:
                if param.name == ctx.right.name:
                    param.type = left
                    break
            for decl in [decl for u in o for decl in u]:
                if decl.name == ctx.right.name:
                    decl.type = left
                    return
            right = left

        if op in ["+.", "==."]:
            if type(left) is not StringType or type(right) is not StringType:
                raise TypeMismatchInExpr(ctx)
            if op == "+.":
                return StringType()
            return BoolType()
        elif op in ["==", "!=", "<", ">", ">=", "<="]:
            if (type(left) is not IntType and type(left)is not FloatType) or (type(right) is not IntType and type(right) is not FloatType):
                raise TypeMismatchInExpr(ctx)
            return BoolType()
        elif op in ["&&", "||"]:
            if type(left) is not BoolType or type(right) is not BoolType:
                raise TypeMismatchInExpr(ctx)
            return BoolType
        elif op in ["+", "-", "*", "/", "%"]:
            if (type(left) is not IntType and type(left) is not FloatType) or (type(right) is not IntType and type(right) is not FloatType):
                raise TypeMismatchInExpr(ctx)
            if type(left) is FloatType or type(right) is FloatType:
                return FloatType()
            return IntType()


    def visitUnExp(self, ctx, o):
        # op: str
        # exp: Exp
        op = ctx.op
        exp = self.visit(ctx.exp, o)
        if type(exp) is NoneType:
            raise TypeCannotBeInferred(self.currentStmt)
        if op == "!":
            if type(exp) is not BoolType:
                raise TypeMismatchInExpr(ctx)
            return exp
        elif op == "-":
            if type(exp) is not IntType and type(exp) is not FloatType:
                raise TypeMismatchInExpr(ctx)
            return exp
        elif op == "str2int":
            if type(exp) is not StringType:
                raise TypeMismatchInExpr(ctx)
            return IntType()
        elif op == "int2str":
            if type(exp) is not IntType:
                raise TypeMismatchInExpr(ctx)
            return StringType()
        elif op == "float2str":
            if type(exp) is not FloatType:
                raise TypeMismatchInExpr(ctx)
            return StringType()
        elif op == "str2float":
            if type(exp) is not StringType:
                raise TypeMismatchInExpr(ctx)
            return FloatType()
        elif op == "bool2str":
            if type(exp) is not BoolType:
                raise TypeMismatchInExpr(ctx)
            return StringType()
        elif op == "str2bool":
            if type(exp) is not StringType:
                raise TypeMismatchInExpr(ctx)
            return BoolType()
        

    def visitAssocExp(self, ctx, o):
        # key: Exp
        # value: Exp
        return (self.visit(ctx.key, o), self.visit(ctx.value, o))


    def visitArrayLit(self, ctx, o):
        # value: List[Exp]
        n = len(ctx.value)
        if n == 0:
            return ArrayType(NoneType(), NoneType())
        elif type(ctx.value[0]) is not ArrayLit:
            lstValue = [self.visit(value, o) for value in ctx.value]
            if isUniqueTypeArray(lstValue):
                if type(lstValue[0]) is tuple:
                    if type(lstValue[0][0]) is NoneType:
                        raise TypeCannotBeInferred(self.currentStmt)
                    if type(lstValue[0][0]) is not IntType and type(lstValue[0][0]) is not StringType:
                        raise InvalidArrayLiteral(ctx)
                    return ArrayType(lstValue[0][0], lstValue[0][1])
                return ArrayType(IntType(), lstValue[0])
            raise InvalidArrayLiteral(ctx)
        else:
            while n > 1:
                if type(ctx.value[n - 1]) is not ArrayLit:
                    raise InvalidArrayLiteral(ctx)
                if len(ctx.value[n - 1].value) != len(ctx.value[n - 2].value):
                    raise InvalidArrayLiteral(ctx)
                if type(self.visit(ctx.value[n - 1], o).type) is not type(self.visit(ctx.value[n - 2], o).type):
                    raise InvalidArrayLiteral(ctx)
                n = n - 1
            return ArrayType(IntType(), self.visit(ctx.value[0], o))
            

    def visitCall(self, ctx, o):
        # id: Id
        # param: List[Exp]
        func = None
        if self.currentFunc and self.currentFunc.name == ctx.id.name:
            func = self.currentFunc
        else:
            for decl in [decl for u in o for decl in u]:
                if decl.name == ctx.id.name:
                    func = decl
                    break
        if func:
            param = []
            for pr in ctx.param:
                temp = self.visit(pr, o)
                if type(temp) is NoneType:
                    raise TypeCannotBeInferred(self.currentStmt)
                param += [temp]
            if compareArray(func.param, param):
                if type(self.currentStmt) is Call and type(func.type) is not VoidType:
                    raise TypeMismatchInStmt(self.currentStmt)
                return func.type
            elif type(self.currentStmt) is Call:
                raise TypeMismatchInStmt(self.currentStmt)
            raise TypeMismatchInExpr(ctx)
        raise UndeclaredIdentifier(ctx.id.name)


    def visitIf(self, ctx, o):
        # ifthenStmt: List[Tuple[Expr, List[Stmt]]]
        # elseStmt: List[Stmt]  # for Else branch, empty list if no Else
        for ifthen in ctx.ifthenStmt:
            if type(self.visit(ifthen[0], o)) is not BoolType:
                raise TypeMismatchInStmt(ctx)
            for stmt in ifthen[1]:
                self.currentStmt = stmt
                self.visit(stmt, o)
        for stmt in ctx.elseStmt:
            self.currentStmt = stmt
            self.visit(stmt, o)


    def visitIntLit(self, ctx, o):
        # value: int
        return IntType()


    def visitFloatLit(self, ctx, o):
        #value: float
        return FloatType()


    def visitBoolLit(self, ctx, o):
        # value: bool
        return BoolType()


    def visitStringLit(self, ctx, o):
        # value: str
        return StringType()
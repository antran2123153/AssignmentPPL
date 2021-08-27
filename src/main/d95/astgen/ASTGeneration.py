from D95Visitor import D95Visitor
from D95Parser import D95Parser
from AST import *

class ASTGeneration(D95Visitor):
    # Visit a parse tree produced by D95Parser#program.
    def visitProgram(self, ctx:D95Parser.ProgramContext):
        return Program(self.visit(ctx.declaration_constants()), self.visit(ctx.body()))


    # Visit a parse tree produced by D95Parser#body.
    def visitBody(self, ctx:D95Parser.BodyContext):
        if ctx.getChildCount() == 2:
            if ctx.function():
                return [self.visit(ctx.function())] + self.visit(ctx.body())
            return [self.visit(ctx.declaration_variable())] + self.visit(ctx.body())
        elif ctx.getChildCount() == 1:
            if ctx.function():
                return [self.visit(ctx.function())]
            return [self.visit(ctx.declaration_variable())]
        return []


    # Visit a parse tree produced by D95Parser#declaration_constants.
    def visitDeclaration_constants(self, ctx:D95Parser.Declaration_constantsContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.declaration_constant())] + self.visit(ctx.declaration_constants())
        elif ctx.getChildCount() == 1:
            return [self.visit(ctx.declaration_constant())]
        return []


    # Visit a parse tree produced by D95Parser#declaration_constant.
    def visitDeclaration_constant(self, ctx:D95Parser.Declaration_constantContext):
        return ConstDecl(Id(ctx.CONSTANT_IDENTIFIER().getText()), self.visit(ctx.expression()))


    # Visit a parse tree produced by D95Parser#declaration_variable.
    def visitDeclaration_variable(self, ctx:D95Parser.Declaration_variableContext):
        return self.visit(ctx.assignment_stmt())


    # Visit a parse tree produced by D95Parser#function.
    def visitFunction(self, ctx:D95Parser.FunctionContext):
        if ctx.parameter():
            return FuncDecl(Id(ctx.FUNCTION_IDENTIFIER().getText()), self.visit(ctx.parameter()), self.visit(ctx.statements()))
        return FuncDecl(Id(ctx.FUNCTION_IDENTIFIER().getText()), [], self.visit(ctx.statements()))


    # Visit a parse tree produced by D95Parser#parameter.
    def visitParameter(self, ctx:D95Parser.ParameterContext):
        if ctx.getChildCount() == 1:
            return [ParamDecl(Id(ctx.VARIABLE_IDENTIFIER().getText()))]
        return [ParamDecl(Id(ctx.VARIABLE_IDENTIFIER().getText()))] + self.visit(ctx.parameter())


    # Visit a parse tree produced by D95Parser#statements.
    def visitStatements(self, ctx:D95Parser.StatementsContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.statement())] + self.visit(ctx.statements())
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.statement())]
        return []


    # Visit a parse tree produced by D95Parser#statement.
    def visitStatement(self, ctx:D95Parser.StatementContext):
        if ctx.assignment_stmt():
            return self.visit(ctx.assignment_stmt())

        elif ctx.if_stmt():
            return self.visit(ctx.if_stmt())

        elif ctx.foreach_stmt():
            return self.visit(ctx.foreach_stmt())

        elif ctx.while_stmt():
            return self.visit(ctx.while_stmt())
            
        elif ctx.break_stmt():
            return self.visit(ctx.break_stmt())

        elif ctx.continue_stmt():
            return self.visit(ctx.continue_stmt())
            
        elif ctx.call_stmt():
            return self.visit(ctx.call_stmt())

        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())


    # Visit a parse tree produced by D95Parser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:D95Parser.Assignment_stmtContext):
        if ctx.expression_index():
            return Assign(self.visit(ctx.expression_index()), self.visit(ctx.expression()))
        return Assign(Id(ctx.VARIABLE_IDENTIFIER().getText()), self.visit(ctx.expression()))


    # Visit a parse tree produced by D95Parser#if_stmt.
    def visitIf_stmt(self, ctx:D95Parser.If_stmtContext):
        return If([(self.visit(ctx.expression()), self.visit(ctx.statements()))] + self.visit(ctx.elseif_stmt()), self.visit(ctx.else_stmt()))


    # Visit a parse tree produced by D95Parser#elseif_stmt.
    def visitElseif_stmt(self, ctx:D95Parser.Elseif_stmtContext):
        if ctx.getChildCount == 7:
            return [(self.visit(ctx.expression()), self.visit(ctx.statements()))]
        elif ctx.getChildCount() == 8:
            return [(self.visit(ctx.expression()), self.visit(ctx.statements()))] + self.visit(ctx.elseif_stmt())
        return []


    # Visit a parse tree produced by D95Parser#else_stmt.
    def visitElse_stmt(self, ctx:D95Parser.Else_stmtContext):
        if ctx.getChildCount() == 4:
            return self.visit(ctx.statements())
        return []


    # Visit a parse tree produced by D95Parser#foreach_stmt.
    def visitForeach_stmt(self, ctx:D95Parser.Foreach_stmtContext):
        return ForEach(self.visit(ctx.expression()), Id(ctx.VARIABLE_IDENTIFIER(0).getText()), 
                    Id(ctx.VARIABLE_IDENTIFIER(1).getText()), self.visit(ctx.statements()))


    # Visit a parse tree produced by D95Parser#while_stmt.
    def visitWhile_stmt(self, ctx:D95Parser.While_stmtContext):
        return While(self.visit(ctx.expression()), self.visit(ctx.statements()))


    # Visit a parse tree produced by D95Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D95Parser.Break_stmtContext):
        return Break()


    # Visit a parse tree produced by D95Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D95Parser.Continue_stmtContext):
        return Continue()


    # Visit a parse tree produced by D95Parser#call_stmt.
    def visitCall_stmt(self, ctx:D95Parser.Call_stmtContext):
        return self.visit(ctx.function_call())


    # Visit a parse tree produced by D95Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D95Parser.Return_stmtContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        return Return()


    # Visit a parse tree produced by D95Parser#expression.
    def visitExpression(self, ctx:D95Parser.ExpressionContext):
        if ctx.getChildCount() == 3 and ctx.OPEN_ROUND():
            return self.visit(ctx.expression(0))

        elif ctx.coercions():
            return UnExp(self.visit(ctx.coercions()), self.visit(ctx.expression(0)))

        elif ctx.function_call():
            return self.visit(ctx.function_call())

        elif ctx.expression_index():
            return self.visit(ctx.expression_index())

        elif ctx.MINUS():
            return UnExp(ctx.MINUS().getText(), self.visit(ctx.expression(0)))

        elif ctx.NEG():
            return UnExp(ctx.NEG().getText(), self.visit(ctx.expression(0)))

        elif ctx.operator_multiplying():
            return BinExp(self.visit(ctx.operator_multiplying()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

        elif ctx.operator_adding():
            return BinExp(self.visit(ctx.operator_adding()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

        elif ctx.operator_logical():
            return BinExp(self.visit(ctx.operator_logical()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

        elif ctx.operator_relational():
            return BinExp(self.visit(ctx.operator_relational()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

        elif ctx.operator_string():
            return BinExp(self.visit(ctx.operator_string()), self.visit(ctx.expression(0)), self.visit(ctx.expression(1)))

        elif ctx.operands():
            return self.visit(ctx.operands())


    # Visit a parse tree produced by D95Parser#operands.
    def visitOperands(self, ctx:D95Parser.OperandsContext):
        if ctx.VARIABLE_IDENTIFIER():
            return Id(ctx.VARIABLE_IDENTIFIER().getText())

        elif ctx.CONSTANT_IDENTIFIER():
            return Id(ctx.CONSTANT_IDENTIFIER().getText()) 

        elif ctx.types():
            return self.visit(ctx.types())

        elif ctx.array():
            return self.visit(ctx.array())


    # Visit a parse tree produced by D95Parser#operator_multiplying.
    def visitOperator_multiplying(self, ctx:D95Parser.Operator_multiplyingContext):
        if ctx.MUL():
            return ctx.MUL().getText()

        elif ctx.DIV():
            return ctx.DIV().getText()

        elif ctx.MOD():
            return ctx.MOD().getText()


    # Visit a parse tree produced by D95Parser#operator_adding.
    def visitOperator_adding(self, ctx:D95Parser.Operator_addingContext):
        if ctx.MINUS():
            return ctx.MINUS().getText()

        elif ctx.ADD():
            return ctx.ADD().getText()


    # Visit a parse tree produced by D95Parser#operator_logical.
    def visitOperator_logical(self, ctx:D95Parser.Operator_logicalContext):
        if ctx.AND():
            return ctx.AND().getText()

        elif ctx.OR():
            return ctx.OR().getText()


    # Visit a parse tree produced by D95Parser#operator_relational.
    def visitOperator_relational(self, ctx:D95Parser.Operator_relationalContext):
        if ctx.ASSIGN_ASSIGN():
            return ctx.ASSIGN_ASSIGN().getText()

        elif ctx.NEG_ASSIGN():
            return ctx.NEG_ASSIGN().getText()
        
        elif ctx.LESS():
            return ctx.LESS().getText()

        elif ctx.GREATER():
            return ctx.GREATER().getText()
        
        elif ctx.LESS_ASSIGN():
            return ctx.LESS_ASSIGN().getText()

        elif ctx.GREATER_ASSIGN():
            return ctx.GREATER_ASSIGN().getText()


    # Visit a parse tree produced by D95Parser#operator_string.
    def visitOperator_string(self, ctx:D95Parser.Operator_stringContext):
        if ctx.ADD_DOT():
            return ctx.ADD_DOT().getText()

        elif ctx.ASSIGN_ASSIGN_DOT():
            return ctx.ASSIGN_ASSIGN_DOT().getText()


    # Visit a parse tree produced by D95Parser#operator_index.
    def visitOperator_index(self, ctx:D95Parser.Operator_indexContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.operator_index())


    # Visit a parse tree produced by D95Parser#coercions.
    def visitCoercions(self, ctx:D95Parser.CoercionsContext):
        if ctx.STR_INT():
            return ctx.STR_INT().getText()

        elif ctx.INT_STR():
            return ctx.INT_STR().getText()

        elif ctx.FLOAT_STR():
            return ctx.FLOAT_STR().getText()

        elif ctx.STR_FLOAT():
            return ctx.STR_FLOAT().getText()

        elif ctx.BOOL_STR():
            return ctx.BOOL_STR().getText()

        elif ctx.STR_BOOL():
            return ctx.STR_BOOL().getText()


    # Visit a parse tree produced by D95Parser#expression_index.
    def visitExpression_index(self, ctx:D95Parser.Expression_indexContext):
        if ctx.VARIABLE_IDENTIFIER():
            return ArrayAccess(Id(ctx.VARIABLE_IDENTIFIER().getText()), self.visit(ctx.operator_index()))
        return ArrayAccess(Id(ctx.CONSTANT_IDENTIFIER().getText()), self.visit(ctx.operator_index()))


    # Visit a parse tree produced by D95Parser#function_call.
    def visitFunction_call(self, ctx:D95Parser.Function_callContext):
        if ctx.call_parameter():
            return Call(Id(ctx.FUNCTION_IDENTIFIER().getText()), self.visit(ctx.call_parameter()))
        return Call(Id(ctx.FUNCTION_IDENTIFIER().getText()), [])

    # Visit a parse tree produced by D95Parser#call_parameter.
    def visitCall_parameter(self, ctx:D95Parser.Call_parameterContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.call_parameter())


    # Visit a parse tree produced by D95Parser#array.
    def visitArray(self, ctx:D95Parser.ArrayContext):
        return ArrayLit(self.visit(ctx.array_body()))


    # Visit a parse tree produced by D95Parser#array_body.
    def visitArray_body(self, ctx:D95Parser.Array_bodyContext):
        if ctx.array_index():
            return self.visit(ctx.array_index())
        if ctx.array_multidimensional():
            return self.visit(ctx.array_multidimensional())
        if ctx.array_associative():
            return self.visit(ctx.array_associative())
        return []


    # Visit a parse tree produced by D95Parser#array_multidimensional.
    def visitArray_multidimensional(self, ctx:D95Parser.Array_multidimensionalContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.array())]
        return [self.visit(ctx.array())] + self.visit(ctx.array_multidimensional())


    # Visit a parse tree produced by D95Parser#array_associative.
    def visitArray_associative(self, ctx:D95Parser.Array_associativeContext):
        if ctx.getChildCount() == 3:
            return [AssocExp(self.visit(ctx.key_associative()), self.visit(ctx.value_associative()))]
        return [AssocExp(self.visit(ctx.key_associative()), self.visit(ctx.value_associative()))] + self.visit(ctx.array_associative())

    # Visit a parse tree produced by D95Parser#key_associative.
    def visitKey_associative(self, ctx:D95Parser.Key_associativeContext):
        if ctx.INTEGER():
            return IntLit(int(ctx.INTEGER().getText()))
        return StringLit(ctx.STRING().getText())


    # Visit a parse tree produced by D95Parser#value_associative.
    def visitValue_associative(self, ctx:D95Parser.Value_associativeContext):
        if ctx.expression():
            return self.visit(ctx.expression())
        return self.visit(ctx.array())


    # Visit a parse tree produced by D95Parser#array_index.
    def visitArray_index(self, ctx:D95Parser.Array_indexContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expression())]
        return [self.visit(ctx.expression())] + self.visit(ctx.array_index())


    # Visit a parse tree produced by D95Parser#types.
    def visitTypes(self, ctx:D95Parser.TypesContext):
        if ctx.INTEGER():
            return IntLit(int(ctx.INTEGER().getText()))

        elif ctx.FLOAT():
            return FloatLit(float(ctx.FLOAT().getText()))

        elif ctx.STRING():
            return StringLit(ctx.STRING().getText())

        return BoolLit(True if ctx.BOOLEAN().getText() == "true" else False)
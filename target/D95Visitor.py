# Generated from main/d95/parser/D95.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D95Parser import D95Parser
else:
    from D95Parser import D95Parser

# This class defines a complete generic visitor for a parse tree produced by D95Parser.

class D95Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D95Parser#program.
    def visitProgram(self, ctx:D95Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#body.
    def visitBody(self, ctx:D95Parser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#declaration_constants.
    def visitDeclaration_constants(self, ctx:D95Parser.Declaration_constantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#declaration_constant.
    def visitDeclaration_constant(self, ctx:D95Parser.Declaration_constantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#declaration_variable.
    def visitDeclaration_variable(self, ctx:D95Parser.Declaration_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#function.
    def visitFunction(self, ctx:D95Parser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#parameter.
    def visitParameter(self, ctx:D95Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#statements.
    def visitStatements(self, ctx:D95Parser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#statement.
    def visitStatement(self, ctx:D95Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#assignment_stmt.
    def visitAssignment_stmt(self, ctx:D95Parser.Assignment_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#if_stmt.
    def visitIf_stmt(self, ctx:D95Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#elseif_stmt.
    def visitElseif_stmt(self, ctx:D95Parser.Elseif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#else_stmt.
    def visitElse_stmt(self, ctx:D95Parser.Else_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#foreach_stmt.
    def visitForeach_stmt(self, ctx:D95Parser.Foreach_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#while_stmt.
    def visitWhile_stmt(self, ctx:D95Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#break_stmt.
    def visitBreak_stmt(self, ctx:D95Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:D95Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#call_stmt.
    def visitCall_stmt(self, ctx:D95Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#return_stmt.
    def visitReturn_stmt(self, ctx:D95Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#expression.
    def visitExpression(self, ctx:D95Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#operands.
    def visitOperands(self, ctx:D95Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#operator_multiplying.
    def visitOperator_multiplying(self, ctx:D95Parser.Operator_multiplyingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#operator_adding.
    def visitOperator_adding(self, ctx:D95Parser.Operator_addingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#operator_logical.
    def visitOperator_logical(self, ctx:D95Parser.Operator_logicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#operator_relational.
    def visitOperator_relational(self, ctx:D95Parser.Operator_relationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#operator_string.
    def visitOperator_string(self, ctx:D95Parser.Operator_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#operator_index.
    def visitOperator_index(self, ctx:D95Parser.Operator_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#coercions.
    def visitCoercions(self, ctx:D95Parser.CoercionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#expression_index.
    def visitExpression_index(self, ctx:D95Parser.Expression_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#function_call.
    def visitFunction_call(self, ctx:D95Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#call_parameter.
    def visitCall_parameter(self, ctx:D95Parser.Call_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#array.
    def visitArray(self, ctx:D95Parser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#array_body.
    def visitArray_body(self, ctx:D95Parser.Array_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#array_multidimensional.
    def visitArray_multidimensional(self, ctx:D95Parser.Array_multidimensionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#array_associative.
    def visitArray_associative(self, ctx:D95Parser.Array_associativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#key_associative.
    def visitKey_associative(self, ctx:D95Parser.Key_associativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#value_associative.
    def visitValue_associative(self, ctx:D95Parser.Value_associativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#array_index.
    def visitArray_index(self, ctx:D95Parser.Array_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D95Parser#types.
    def visitTypes(self, ctx:D95Parser.TypesContext):
        return self.visitChildren(ctx)



del D95Parser
class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        # program: exp EOF;
        return self.visit(ctx.exp())

    def visitExp(self, ctx: MPParser.ExpContext):
        # exp: term ASSIGN exp | term;
        if ctx.ASSIGN():
            left = self.visit(ctx.term())
            right = self.visit(ctx.exp())
            op = ctx.ASSIGN().getText()
            return Binary(op, left, right)
        else:
            return self.visit(ctx.term())

    def visitTerm(self, ctx: MPParser.TermContext): 
        # term: factor COMPARE factor | factor;
        if ctx.COMPARE():
            left = self.visit(ctx.factor(0))
            right = self.visit(ctx.factor(1))
            op = ctx.COMPARE().getText()
            return Binary(op, left, right)
        else:
            return self.visit(ctx.factor(0))

    def visitFactor(self, ctx: MPParser.FactorContext):
        # factor: factor ANDOR operand | operand;
        if ctx.ANDOR():
            left = self.visit(ctx.factor())
            right = self.visit(ctx.operand())
            op = ctx.ANDOR().getText()
            return Binary(op, left, right)
        else:
            return self.visit(ctx.operand())

    def visitOperand(self, ctx: MPParser.OperandContext):
        # operand: ID | INTLIT | BOOLIT | '(' exp ')';
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText() == "True")
        else:
            return self.visit(ctx.exp())
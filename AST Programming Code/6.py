class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        return self.visit(ctx.exp())

    def visitExp(self, ctx: MPParser.ExpContext):
        # exp: (term ASSIGN)* term;
        terms = [self.visit(t) for t in ctx.term()]
        ops = ctx.ASSIGN()

        # RIGHT-ASSOCIATIVE
        result = terms[-1]
        for i in reversed(range(len(ops))):
            op = ops[i].getText()
            left = terms[i]
            result = Binary(op, left, result)

        return result

    def visitTerm(self, ctx: MPParser.TermContext): 
        if ctx.COMPARE():
            left = self.visit(ctx.factor(0))
            right = self.visit(ctx.factor(1))
            op = ctx.COMPARE().getText()
            return Binary(op, left, right)
        else:
            return self.visit(ctx.factor(0))

    def visitFactor(self, ctx: MPParser.FactorContext):
        # operand (ANDOR operand)*
        operands = [self.visit(o) for o in ctx.operand()]
        ops = ctx.ANDOR()

        # AND/OR vẫn left-associative
        result = operands[0]
        for i in range(len(ops)):
            op = ops[i].getText()
            right = operands[i + 1]
            result = Binary(op, result, right)

        return result

    def visitOperand(self, ctx: MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText() == "True")
        else:
            return self.visit(ctx.exp())
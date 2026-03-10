class StaticCheck(Visitor):

    def visitBinOp(self, ctx: BinOp, o):
        t1 = self.visit(ctx.e1, o)
        t2 = self.visit(ctx.e2, o)
        op = ctx.op

        # + - *
        if op in ["+", "-", "*"]:
            if t1 not in ["int","float"] or t2 not in ["int","float"]:
                raise TypeMismatchInExpression(ctx)
            if t1 == "float" or t2 == "float":
                return "float"
            return "int"

        # /
        if op == "/":
            if t1 not in ["int","float"] or t2 not in ["int","float"]:
                raise TypeMismatchInExpression(ctx)
            return "float"

        # boolean
        if op in ["&&","||"]:
            if t1 != "bool" or t2 != "bool":
                raise TypeMismatchInExpression(ctx)
            return "bool"

        # comparison
        if op in [">","<","==","!="]:
            if t1 != t2:
                raise TypeMismatchInExpression(ctx)
            return "bool"

    def visitUnOp(self, ctx: UnOp, o):
        t = self.visit(ctx.e, o)

        if ctx.op == "-":
            if t not in ["int","float"]:
                raise TypeMismatchInExpression(ctx)
            return t

        if ctx.op == "!":
            if t != "bool":
                raise TypeMismatchInExpression(ctx)
            return "bool"

    def visitIntLit(self, ctx: IntLit, o):
        return "int"

    def visitFloatLit(self, ctx: FloatLit, o):
        return "float"

    def visitBoolLit(self, ctx: BoolLit, o):
        return "bool"
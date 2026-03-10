class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o):
        env = {}
        for d in ctx.decl:
            name, typ = self.visit(d, env)
            env[name] = typ
        return self.visit(ctx.exp, env)

    def visitVarDecl(self, ctx: VarDecl, o):
        typ = self.visit(ctx.typ, o)
        return (ctx.name, typ)

    def visitIntType(self, ctx: IntType, o):
        return IntType()

    def visitFloatType(self, ctx: FloatType, o):
        return FloatType()

    def visitBoolType(self, ctx: BoolType, o):
        return BoolType()

    def visitBinOp(self, ctx: BinOp, o):
        t1 = self.visit(ctx.e1, o)
        t2 = self.visit(ctx.e2, o)
        op = ctx.op

        if op in ["+", "-", "*"]:
            if not isinstance(t1,(IntType,FloatType)) or not isinstance(t2,(IntType,FloatType)):
                raise TypeMismatchInExpression(ctx)
            if isinstance(t1,FloatType) or isinstance(t2,FloatType):
                return FloatType()
            return IntType()

        if op == "/":
            if not isinstance(t1,(IntType,FloatType)) or not isinstance(t2,(IntType,FloatType)):
                raise TypeMismatchInExpression(ctx)
            return FloatType()

        if op in ["&&","||"]:
            if not isinstance(t1,BoolType) or not isinstance(t2,BoolType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

        if op in [">","<","==","!="]:
            if type(t1) != type(t2):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnOp(self, ctx: UnOp, o):
        t = self.visit(ctx.e, o)

        if ctx.op == "-":
            if not isinstance(t,(IntType,FloatType)):
                raise TypeMismatchInExpression(ctx)
            return t

        if ctx.op == "!":
            if not isinstance(t,BoolType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx: FloatLit, o):
        return FloatType()

    def visitBoolLit(self, ctx: BoolLit, o):
        return BoolType()

    def visitId(self, ctx: Id, o):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return o[ctx.name]
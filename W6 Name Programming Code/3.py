class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        env = []
        for decl in ctx.decl:
            env = self.visit(decl, env)
        return env

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return o + [ctx.name]

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return o + [ctx.name]

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        # check function name in current scope
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)

        # create new scope for parameters and body
        local_env = []

        for p in ctx.param:
            local_env = self.visit(p, local_env)

        for d in ctx.body:
            local_env = self.visit(d, local_env)

        return o + [ctx.name]

    def visitIntType(self, ctx: IntType, o: object):
        return o

    def visitFloatType(self, ctx: FloatType, o: object):
        return o

    def visitIntLit(self, ctx: IntLit, o: object):
        return o
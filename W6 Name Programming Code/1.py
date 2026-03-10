class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        env = []
        for decl in ctx.decl:
            env = self.visit(decl, env)
        return env

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        return o + [ctx.name]

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        return o + [ctx.name]

    def visitIntType(self, ctx: IntType, o: object):
        return o

    def visitFloatType(self, ctx: FloatType, o: object):
        return o

    def visitIntLit(self, ctx: IntLit, o: object):
        return o
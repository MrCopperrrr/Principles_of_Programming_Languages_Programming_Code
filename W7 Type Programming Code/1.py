class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o: object):
        env = [set()]  # global scope
        for decl in ctx.decl:
            self.visit(decl, env)
        return env

    def visitVarDecl(self, ctx: VarDecl, o: object):
        if ctx.name in o[0]:
            raise RedeclaredVariable(ctx.name)
        o[0].add(ctx.name)
        self.visit(ctx.typ, o)

    def visitConstDecl(self, ctx: ConstDecl, o: object):
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)
        o[0].add(ctx.name)
        self.visit(ctx.val, o)

    def visitFuncDecl(self, ctx: FuncDecl, o: object):
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)

        o[0].add(ctx.name)

        # new scope for function
        local_env = [set()] + o

        # parameters
        for p in ctx.param:
            self.visit(p, local_env)

        decls, exprs = ctx.body

        # local declarations
        for d in decls:
            self.visit(d, local_env)

        # expressions
        for e in exprs:
            self.visit(e, local_env)

    def visitIntType(self, ctx: IntType, o: object):
        pass

    def visitFloatType(self, ctx: FloatType, o: object):
        pass

    def visitIntLit(self, ctx: IntLit, o: object):
        pass

    def visitId(self, ctx: Id, o: object):
        for scope in o:
            if ctx.name in scope:
                return
        raise UndeclaredIdentifier(ctx.name)
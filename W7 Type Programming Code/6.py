class StaticCheck(Visitor):

    def lookup(self, name, env):
        for scope in reversed(env):
            if name in scope:
                return scope[name]
        return None

    def visitProgram(self, ctx, o):
        env = [{}]
        funcs = {}

        for d in ctx.decl:

            if isinstance(d, VarDecl):
                if d.name in env[0] or d.name in funcs:
                    raise Redeclared(d)
                d.typ = None
                env[0][d.name] = d
        
            if isinstance(d, FuncDecl):
                if d.name in env[0] or d.name in funcs:
                    raise Redeclared(d)
                funcs[d.name] = d

        for d in ctx.decl:
            if isinstance(d, FuncDecl):
                self.visitFuncDecl(d, (env, funcs))

        for s in ctx.stmts:
            self.visit(s, (env, funcs))

    def visitVarDecl(self, ctx, env):
        scope = env[-1]
        if ctx.name in scope:
            raise Redeclared(ctx)
        ctx.typ = None
        scope[ctx.name] = ctx

    def visitFuncDecl(self, ctx, o):
        env, funcs = o
        new_env = env + [{}]

        for p in ctx.param:
            if p.name in new_env[-1]:
                raise Redeclared(p)
            p.typ = None
            new_env[-1][p.name] = p

        for d in ctx.local:
            if isinstance(d, VarDecl):
                if d.name in new_env[-1]:
                    raise Redeclared(d)
                d.typ = None
                new_env[-1][d.name] = d

        for s in ctx.stmts:
            self.visit(s, (new_env, funcs))

    def visitAssign(self, ctx, o):
        env, funcs = o

        lhs = self.lookup(ctx.lhs.name, env)
        if lhs is None:
            raise UndeclaredIdentifier(ctx.lhs.name)

        t_lhs = lhs.typ
        t_rhs = self.visit(ctx.rhs, o)

        if t_lhs is None and t_rhs is None:
            raise TypeCannotBeInferred(ctx)

        if t_lhs is None:
            lhs.typ = t_rhs
            return

        if t_rhs is None:
            if isinstance(ctx.rhs, Id):
                rhs = self.lookup(ctx.rhs.name, env)
                rhs.typ = t_lhs
                return
            raise TypeCannotBeInferred(ctx)

        if t_lhs != t_rhs:
            raise TypeMismatchInStatement(ctx)

    def visitCallStmt(self, ctx, o):
        env, funcs = o

        if ctx.name not in funcs:
            raise UndeclaredIdentifier(ctx.name)

        func = funcs[ctx.name]

        if len(func.param) != len(ctx.args):
            raise TypeMismatchInStatement(ctx)

        for p, a in zip(func.param, ctx.args):

            t_arg = self.visit(a, o)

            if p.typ is None and t_arg is None:
                raise TypeCannotBeInferred(ctx)

            if p.typ is None:
                p.typ = t_arg
                continue

            if t_arg is None:
                if isinstance(a, Id):
                    arg = self.lookup(a.name, env)
                    arg.typ = p.typ
                    continue
                raise TypeCannotBeInferred(ctx)

            if p.typ != t_arg:
                raise TypeMismatchInStatement(ctx)

    def visitId(self, ctx, o):
        env, funcs = o
        var = self.lookup(ctx.name, env)
        if var is None:
            raise UndeclaredIdentifier(ctx.name)
        return var.typ

    def visitIntLit(self, ctx, o):
        return "int"

    def visitFloatLit(self, ctx, o):
        return "float"

    def visitBoolLit(self, ctx, o):
        return "bool"
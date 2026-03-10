class StaticCheck(Visitor):

    # tìm biến trong scope
    def lookup(self, name, env):
        for scope in reversed(env):
            if name in scope:
                return scope
        return None

    def visitProgram(self, ctx, o):
        env = [{}]
        for d in ctx.decl:
            self.visit(d, env)
        for s in ctx.stmts:
            self.visit(s, env)

    def visitVarDecl(self, ctx, o):
        scope = o[-1]
        if ctx.name in scope:
            raise Redeclared(ctx)
        scope[ctx.name] = None

    def visitBlock(self, ctx, o):
        o.append({})
        for d in ctx.decl:
            self.visit(d, o)
        for s in ctx.stmts:
            self.visit(s, o)
        o.pop()

    def visitAssign(self, ctx, o):
        lhs_scope = self.lookup(ctx.lhs.name, o)
        if lhs_scope is None:
            raise UndeclaredIdentifier(ctx.lhs.name)

        t_lhs = self.visit(ctx.lhs, o)
        t_rhs = self.visit(ctx.rhs, o)

        if t_lhs is None and t_rhs is None:
            raise TypeCannotBeInferred(ctx)

        if t_lhs is None:
            lhs_scope[ctx.lhs.name] = t_rhs
            return

        if t_rhs is None:
            if isinstance(ctx.rhs, Id):
                rhs_scope = self.lookup(ctx.rhs.name, o)
                rhs_scope[ctx.rhs.name] = t_lhs
                return
            raise TypeCannotBeInferred(ctx)

        if t_lhs != t_rhs:
            raise TypeMismatchInStatement(ctx)

    def visitBinOp(self, ctx, o):
        t1 = self.visit(ctx.e1, o)
        t2 = self.visit(ctx.e2, o)
        op = ctx.op

        def infer(e, typ):
            if isinstance(e, Id):
                scope = self.lookup(e.name, o)
                if scope[e.name] is None:
                    scope[e.name] = typ

        if op in ["+","-","*","/"]:
            infer(ctx.e1,"int")
            infer(ctx.e2,"int")
            if self.visit(ctx.e1,o) != "int" or self.visit(ctx.e2,o) != "int":
                raise TypeMismatchInExpression(ctx)
            return "int"

        if op in ["+.","-.","*.","/."]:
            infer(ctx.e1,"float")
            infer(ctx.e2,"float")
            if self.visit(ctx.e1,o) != "float" or self.visit(ctx.e2,o) != "float":
                raise TypeMismatchInExpression(ctx)
            return "float"

        if op in [">","="]:
            infer(ctx.e1,"int")
            infer(ctx.e2,"int")
            if self.visit(ctx.e1,o) != "int" or self.visit(ctx.e2,o) != "int":
                raise TypeMismatchInExpression(ctx)
            return "bool"

        if op in [">.","=."]:
            infer(ctx.e1,"float")
            infer(ctx.e2,"float")
            if self.visit(ctx.e1,o) != "float" or self.visit(ctx.e2,o) != "float":
                raise TypeMismatchInExpression(ctx)
            return "bool"

        if op in ["&&","||",">b","=b"]:
            infer(ctx.e1,"bool")
            infer(ctx.e2,"bool")
            if self.visit(ctx.e1,o) != "bool" or self.visit(ctx.e2,o) != "bool":
                raise TypeMismatchInExpression(ctx)
            return "bool"

    def visitUnOp(self, ctx, o):
        t = self.visit(ctx.e, o)

        if ctx.op == "-":
            if isinstance(ctx.e, Id):
                scope = self.lookup(ctx.e.name,o)
                if scope[ctx.e.name] is None:
                    scope[ctx.e.name] = "int"
                    return "int"
            if t != "int":
                raise TypeMismatchInExpression(ctx)
            return "int"

        if ctx.op == "-.":
            if isinstance(ctx.e, Id):
                scope = self.lookup(ctx.e.name,o)
                if scope[ctx.e.name] is None:
                    scope[ctx.e.name] = "float"
                    return "float"
            if t != "float":
                raise TypeMismatchInExpression(ctx)
            return "float"

        if ctx.op == "!":
            if isinstance(ctx.e, Id):
                scope = self.lookup(ctx.e.name,o)
                if scope[ctx.e.name] is None:
                    scope[ctx.e.name] = "bool"
                    return "bool"
            if t != "bool":
                raise TypeMismatchInExpression(ctx)
            return "bool"

        if ctx.op == "i2f":
            if isinstance(ctx.e, Id):
                scope = self.lookup(ctx.e.name,o)
                if scope[ctx.e.name] is None:
                    scope[ctx.e.name] = "int"
                    return "float"
            if t != "int":
                raise TypeMismatchInExpression(ctx)
            return "float"

        if ctx.op == "floor":
            if isinstance(ctx.e, Id):
                scope = self.lookup(ctx.e.name,o)
                if scope[ctx.e.name] is None:
                    scope[ctx.e.name] = "float"
                    return "int"
            if t != "float":
                raise TypeMismatchInExpression(ctx)
            return "int"

    def visitIntLit(self, ctx, o):
        return "int"

    def visitFloatLit(self, ctx, o):
        return "float"

    def visitBoolLit(self, ctx, o):
        return "bool"

    def visitId(self, ctx, o):
        scope = self.lookup(ctx.name, o)
        if scope is None:
            raise UndeclaredIdentifier(ctx.name)
        return scope[ctx.name]
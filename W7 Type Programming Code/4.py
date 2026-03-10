class StaticCheck(Visitor):

    def visitProgram(self, ctx, o):
        env = {}
        for d in ctx.decl:
            self.visit(d, env)
        for s in ctx.stmts:
            self.visit(s, env)

    def visitVarDecl(self, ctx, o):
        o[ctx.name] = None

    def visitAssign(self, ctx, o):
        if ctx.lhs.name not in o:
            raise UndeclaredIdentifier(ctx.lhs.name)
    
        t_lhs = self.visit(ctx.lhs, o)
        t_rhs = self.visit(ctx.rhs, o)
    
        if t_lhs is None and t_rhs is None:
            raise TypeCannotBeInferred(ctx)
    
        if t_lhs is None:
            if ctx.lhs.name in o and o[ctx.lhs.name] is not None and o[ctx.lhs.name] != t_rhs:
                raise TypeMismatchInStatement(ctx)
            o[ctx.lhs.name] = t_rhs
            return
    
        if t_rhs is None:
            if isinstance(ctx.rhs, Id):
                o[ctx.rhs.name] = t_lhs
                return
            raise TypeCannotBeInferred(ctx)
    
        if t_lhs != t_rhs:
            raise TypeMismatchInStatement(ctx)

    def visitBinOp(self, ctx, o):
        t1 = self.visit(ctx.e1, o)
        t2 = self.visit(ctx.e2, o)
        op = ctx.op

        def infer(e, typ):
            if isinstance(e, Id) and o[e.name] is None:
                o[e.name] = typ

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
            if isinstance(ctx.e, Id) and o[ctx.e.name] is None:
                o[ctx.e.name] = "int"
                return "int"
            if t != "int":
                raise TypeMismatchInExpression(ctx)
            return "int"

        if ctx.op == "-.":
            if isinstance(ctx.e, Id) and o[ctx.e.name] is None:
                o[ctx.e.name] = "float"
                return "float"
            if t != "float":
                raise TypeMismatchInExpression(ctx)
            return "float"

        if ctx.op == "!":
            if isinstance(ctx.e, Id) and o[ctx.e.name] is None:
                o[ctx.e.name] = "bool"
                return "bool"
            if t != "bool":
                raise TypeMismatchInExpression(ctx)
            return "bool"

        if ctx.op == "i2f":
            if isinstance(ctx.e, Id) and o[ctx.e.name] is None:
                o[ctx.e.name] = "int"
                return "float"
            if t != "int":
                raise TypeMismatchInExpression(ctx)
            return "float"

        if ctx.op == "floor":
            if isinstance(ctx.e, Id) and o[ctx.e.name] is None:
                o[ctx.e.name] = "float"
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
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return o[ctx.name]
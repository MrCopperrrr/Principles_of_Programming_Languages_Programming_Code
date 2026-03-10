class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        # program: vardecls EOF;
        decls = self.visit(ctx.vardecls())
        return Program(decls)

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        # vardecls: vardecl vardecltail;
        first = self.visit(ctx.vardecl())
        rest = self.visit(ctx.vardecltail())
        return first + rest

    def visitVardecltail(self, ctx: MPParser.VardecltailContext): 
        # vardecltail: vardecl vardecltail | ;
        if ctx.vardecl():
            return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())
        else:
            return []

    def visitVardecl(self, ctx: MPParser.VardeclContext): 
        # vardecl: mptype ids ';'
        var_type = self.visit(ctx.mptype())
        id_list = self.visit(ctx.ids())
        return [VarDecl(i, var_type) for i in id_list]

    def visitMptype(self, ctx: MPParser.MptypeContext):
        # mptype: INTTYPE | FLOATTYPE;
        if ctx.INTTYPE():
            return IntType()
        else:
            return FloatType()

    def visitIds(self, ctx: MPParser.IdsContext):
        # ids: ID ',' ids | ID;
        if ctx.ids():
            return [Id(ctx.ID().getText())] + self.visit(ctx.ids())
        else:
            return [Id(ctx.ID().getText())]
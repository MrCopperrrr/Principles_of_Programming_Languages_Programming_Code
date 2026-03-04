class NonTerminalCount(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        # program: vardecls EOF;
        return 1 + self.visit(ctx.vardecls())

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        # vardecls: vardecl vardecltail;
        return 1 + \
               self.visit(ctx.vardecl()) + \
               self.visit(ctx.vardecltail())

    def visitVardecltail(self, ctx: MPParser.VardecltailContext): 
        # vardecltail: vardecl vardecltail | ;
        if ctx.vardecl():
            return 1 + \
                   self.visit(ctx.vardecl()) + \
                   self.visit(ctx.vardecltail())
        else:
            # epsilon production vẫn là 1 non-terminal node
            return 1

    def visitVardecl(self, ctx: MPParser.VardeclContext): 
        # vardecl: mptype ids ';'
        return 1 + \
               self.visit(ctx.mptype()) + \
               self.visit(ctx.ids())

    def visitMptype(self, ctx: MPParser.MptypeContext):
        # mptype: INTTYPE | FLOATTYPE;
        return 1  # chỉ đếm mptype node

    def visitIds(self, ctx: MPParser.IdsContext):
        # ids: ID ',' ids | ID;
        if ctx.ids():
            return 1 + self.visit(ctx.ids())
        else:
            return 1
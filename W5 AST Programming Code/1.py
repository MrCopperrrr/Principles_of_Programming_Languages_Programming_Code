class Height(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        # program: vardecls EOF;
        return 1 + max(
            self.visit(ctx.vardecls()) if ctx.vardecls() else 0,
            1   # EOF
        )

    def visitVardecls(self, ctx: MPParser.VardeclsContext):
        # vardecls: vardecl vardecltail;
        return 1 + max(
            self.visit(ctx.vardecl()),
            self.visit(ctx.vardecltail())
        )

    def visitVardecltail(self, ctx: MPParser.VardecltailContext): 
        # vardecltail: vardecl vardecltail | ;
        if ctx.vardecl():
            return 1 + max(
                self.visit(ctx.vardecl()),
                self.visit(ctx.vardecltail())
            )
        else:
            # epsilon
            return 1

    def visitVardecl(self, ctx: MPParser.VardeclContext): 
        # vardecl: mptype ids ';'
        return 1 + max(
            self.visit(ctx.mptype()),
            self.visit(ctx.ids()),
            1  # ';'
        )

    def visitMptype(self, ctx: MPParser.MptypeContext):
        # mptype: INTTYPE | FLOATTYPE;
        return 1 + 1  # 1 for mptype node + 1 for terminal

    def visitIds(self, ctx: MPParser.IdsContext):
        # ids: ID ',' ids | ID;
        if ctx.ids():
            return 1 + max(
                1,              # ID
                1,              # ','
                self.visit(ctx.ids())
            )
        else:
            return 1 + 1  # ids node + ID
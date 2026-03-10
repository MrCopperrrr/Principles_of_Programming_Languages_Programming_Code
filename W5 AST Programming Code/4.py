class ASTGeneration(MPVisitor):

    def visitProgram(self, ctx: MPParser.ProgramContext):
        # program: vardecl+ EOF;
        decls = []
        for vd in ctx.vardecl():
            decls += self.visit(vd)
        return Program(decls)

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
        # ids: ID (',' ID)*;
        return [Id(token.getText()) for token in ctx.ID()]
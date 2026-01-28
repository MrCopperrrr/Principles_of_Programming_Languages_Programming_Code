# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#tokens.
    def visitTokens(self, ctx:BKITParser.TokensContext):
        return self.visitChildren(ctx)



del BKITParser
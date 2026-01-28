# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,3,14,2,0,7,0,2,1,7,1,1,0,4,0,6,8,0,11,0,12,0,7,1,0,1,0,1,1,1,
        1,1,1,0,0,2,0,2,0,1,2,0,1,1,3,3,12,0,5,1,0,0,0,2,11,1,0,0,0,4,6,
        3,2,1,0,5,4,1,0,0,0,6,7,1,0,0,0,7,5,1,0,0,0,7,8,1,0,0,0,8,9,1,0,
        0,0,9,10,5,0,0,1,10,1,1,0,0,0,11,12,7,0,0,0,12,3,1,0,0,0,1,7
    ]

class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "PHP_INT", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_tokens = 1

    ruleNames =  [ "program", "tokens" ]

    EOF = Token.EOF
    PHP_INT=1
    WS=2
    ERROR_CHAR=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def tokens(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.TokensContext)
            else:
                return self.getTypedRuleContext(BKITParser.TokensContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.tokens()
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==3):
                    break

            self.state = 9
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokensContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PHP_INT(self):
            return self.getToken(BKITParser.PHP_INT, 0)

        def ERROR_CHAR(self):
            return self.getToken(BKITParser.ERROR_CHAR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_tokens

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokens" ):
                return visitor.visitTokens(self)
            else:
                return visitor.visitChildren(self)




    def tokens(self):

        localctx = BKITParser.TokensContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tokens)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            _la = self._input.LA(1)
            if not(_la==1 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






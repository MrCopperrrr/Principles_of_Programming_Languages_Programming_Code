# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,4,33,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,
        2,1,3,1,3,1,3,0,0,4,1,1,3,2,5,3,7,4,1,0,1,3,0,9,10,13,13,32,32,32,
        0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,1,9,1,0,0,0,3,17,
        1,0,0,0,5,26,1,0,0,0,7,30,1,0,0,0,9,10,5,118,0,0,10,11,5,97,0,0,
        11,12,5,114,0,0,12,13,5,100,0,0,13,14,5,101,0,0,14,15,5,99,0,0,15,
        16,5,108,0,0,16,2,1,0,0,0,17,18,5,102,0,0,18,19,5,117,0,0,19,20,
        5,110,0,0,20,21,5,99,0,0,21,22,5,100,0,0,22,23,5,101,0,0,23,24,5,
        99,0,0,24,25,5,108,0,0,25,4,1,0,0,0,26,27,7,0,0,0,27,28,1,0,0,0,
        28,29,6,2,0,0,29,6,1,0,0,0,30,31,9,0,0,0,31,32,6,3,1,0,32,8,1,0,
        0,0,1,0,2,6,0,0,1,3,0
    ]

class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    WS = 3
    ERROR_CHAR = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'vardecl'", "'funcdecl'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[3] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     



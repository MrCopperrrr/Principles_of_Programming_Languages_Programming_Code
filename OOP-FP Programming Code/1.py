from abc import ABC, abstractmethod

# Base class
class Exp(ABC):
    @abstractmethod
    def eval(self):
        pass


# Integer literal
class IntLit(Exp):
    def __init__(self, val: int):
        self.val = val

    def eval(self):
        return self.val


# Float literal
class FloatLit(Exp):
    def __init__(self, val: float):
        self.val = val

    def eval(self):
        return self.val


# Unary expression: + or -
class UnExp(Exp):
    def __init__(self, op: str, operand: Exp):
        self.op = op
        self.operand = operand

    def eval(self):
        value = self.operand.eval()
        if self.op == '+':
            return +value
        elif self.op == '-':
            return -value
        else:
            raise ValueError(f"Invalid unary operator: {self.op}")


# Binary expression: +, -, *, /
class BinExp(Exp):
    def __init__(self, left: Exp, op: str, right: Exp):
        self.left = left
        self.op = op
        self.right = right

    def eval(self):
        lval = self.left.eval()
        rval = self.right.eval()

        if self.op == '+':
            return lval + rval
        elif self.op == '-':
            return lval - rval
        elif self.op == '*':
            return lval * rval
        elif self.op == '/':
            return lval / rval
        else:
            raise ValueError(f"Invalid binary operator: {self.op}")

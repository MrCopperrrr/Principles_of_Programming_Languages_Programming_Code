from abc import ABC, abstractmethod

class Exp(ABC):
    @abstractmethod
    def eval(self):
        pass

    @abstractmethod
    def printPrefix(self):
        pass


class IntLit(Exp):
    def __init__(self, val: int):
        self.val = val

    def eval(self):
        return self.val

    def printPrefix(self):
        return f"{self.val} "


class FloatLit(Exp):
    def __init__(self, val: float):
        self.val = val

    def eval(self):
        return self.val

    def printPrefix(self):
        return f"{self.val} "


class UnExp(Exp):
    def __init__(self, op: str, operand: Exp):
        self.op = op
        self.operand = operand

    def eval(self):
        val = self.operand.eval()
        if self.op == '+':
            return +val
        elif self.op == '-':
            return -val
        else:
            raise ValueError("Invalid unary operator")

    def printPrefix(self):
        # unary + and - are printed as +. and -.
        return f"{self.op}. " + self.operand.printPrefix()


class BinExp(Exp):
    def __init__(self, left: Exp, op: str, right: Exp):
        self.left = left
        self.op = op
        self.right = right

    def eval(self):
        l = self.left.eval()
        r = self.right.eval()
        if self.op == '+':
            return l + r
        elif self.op == '-':
            return l - r
        elif self.op == '*':
            return l * r
        elif self.op == '/':
            return l / r
        else:
            raise ValueError("Invalid binary operator")

    def printPrefix(self):
        return (
            f"{self.op} "
            + self.left.printPrefix()
            + self.right.printPrefix()
        )

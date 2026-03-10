from abc import ABC, abstractmethod

# ===== Expression classes =====

class Exp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class IntLit(Exp):
    def __init__(self, val):
        self.val = val

    def accept(self, visitor):
        return visitor.visitIntLit(self)


class FloatLit(Exp):
    def __init__(self, val):
        self.val = val

    def accept(self, visitor):
        return visitor.visitFloatLit(self)


class UnExp(Exp):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

    def accept(self, visitor):
        return visitor.visitUnExp(self)


class BinExp(Exp):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def accept(self, visitor):
        return visitor.visitBinExp(self)


# ===== Visitor: Eval =====

class Eval:
    def visitIntLit(self, ctx):
        return ctx.val

    def visitFloatLit(self, ctx):
        return ctx.val

    def visitUnExp(self, ctx):
        val = ctx.operand.accept(self)
        if ctx.op == '+':
            return +val
        elif ctx.op == '-':
            return -val

    def visitBinExp(self, ctx):
        l = ctx.left.accept(self)
        r = ctx.right.accept(self)
        if ctx.op == '+':
            return l + r
        elif ctx.op == '-':
            return l - r
        elif ctx.op == '*':
            return l * r
        elif ctx.op == '/':
            return l / r


# ===== Visitor: PrintPrefix =====

class PrintPrefix:
    def visitIntLit(self, ctx):
        return f"{ctx.val} "

    def visitFloatLit(self, ctx):
        return f"{ctx.val} "

    def visitUnExp(self, ctx):
        return f"{ctx.op}. " + ctx.operand.accept(self)

    def visitBinExp(self, ctx):
        return (
            f"{ctx.op} "
            + ctx.left.accept(self)
            + ctx.right.accept(self)
        )


# ===== Visitor: PrintPostfix =====

class PrintPostfix:
    def visitIntLit(self, ctx):
        return f"{ctx.val} "

    def visitFloatLit(self, ctx):
        return f"{ctx.val} "

    def visitUnExp(self, ctx):
        return ctx.operand.accept(self) + f"{ctx.op}. "

    def visitBinExp(self, ctx):
        return (
            ctx.left.accept(self)
            + ctx.right.accept(self)
            + f"{ctx.op} "
        )

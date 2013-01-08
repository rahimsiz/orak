__author__ = 'ramil'

from ast import parse, NodeVisitor
from checkers import *

class Checker(NodeVisitor):
    model = None

    def __init__(self, klass):
        self.model = klass()

    def visit(self, node):
        methodName = "visit_" + node.__class__.__name__.lower()
        print methodName
        if hasattr(self.model, methodName):
            method = getattr(self.model, methodName)
            if callable(method):
                method(node)
        super(Checker, self).visit(node)


class Orak:
    filename = None
    ast = None

    def __init__(self,  filename):
        self.filename = filename
        with open(filename) as f:
            try:
                self.ast = parse(f.read())
            except SyntaxError as ex:
                print ex.offset

    def check(self):
        visitor = Checker(FuncCallChecker)
        visitor.visit(self.ast)


if __name__ == "__main__":
    Orak('devtests/1.py').check()
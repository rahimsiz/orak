__author__ = 'ramil'

from copy import copy
from defect import Defect

class FuncCallChecker:
    namespace = None

    def __init__(self):
        self.namespace = Namespace()

    def visit_functiondef(self, node):
        args = list()
        for arg in node.args.args:
            args.append({"name": arg.id})

        defaults_start = len(args) - len(node.args.defaults)
        for uk in range(defaults_start, len(args)):
            args[uk]["default"] = True

        self.namespace.addFuncDeclaration(node.name, args)

    def visit_call(self, node):
        #HACK for methods
        if 'id' not in node.func._fields:
            return

        for declaration in self.namespace.findFunc(node.func.id):

            declaration = copy(declaration)
            declaration = declaration[len(node.args):]

            found = True

            for arg in node.keywords:
                params = filter(lambda x: x["name"] == arg.arg, declaration)
                if len(params) < 1:
                    found = False
                    break

                for param in params:
                    declaration.remove(param)

            if not found:
                continue

            if len(declaration) == len(filter(lambda x: x.has_key("default"), declaration)):
                return

        raise Defect("Test")


class Namespace:
    parent = None
    declarations = dict()

    def __init__(self, parent = None):
        self.parent = parent

    def addFuncDeclaration(self, name, params):
        self.declarations[name] = params

    def findFunc(self, name):
        res = []
        if name in self.declarations:
            res.append(self.declarations[name])
        if self.parent != None:
            res += self.parent.findFunc(name)
        return res





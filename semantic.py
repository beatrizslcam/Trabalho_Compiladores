from lark import Lark
from sintaxe import TokenLexer


class SymbolTable:
    def __init__(self):
        self.table = {}

    def add_into_table(self, name, value):
        self.table = {name: value}


class Semantic_Analizer:
    def __init__(self, tree):
        pass

    def type_checker():

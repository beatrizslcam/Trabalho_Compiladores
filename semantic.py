from lark import Lark
from sintaxe import TokenLexer


class Symbol:
    def __init__(self,tipo,escopo):
        self.tipo = tipo;
        self.escopo = escopo;
        

  
class SymbolTable:
    def __init__(self):
        self.tabela = {};
    
  











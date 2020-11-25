from lex import lex
from sintaxe import sintaxe

f = open('exemplo.txt', 'r')
stext = f.read()
tokens = lex(stext)
print(sintaxe(tokens).pretty())


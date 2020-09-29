from lex import lex

f = open('exemplo.txt', 'r')
stext = f.read()
tokens = lex(stext)

if len(tokens) > 0:
    for token in tokens[0:-1]:
        print(token.type, sep='', end=", ")
    print(tokens[-1].type)


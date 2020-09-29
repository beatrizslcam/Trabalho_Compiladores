import lex as l
f = open('exemplo.txt', 'r')
stext = f.read()

print(l.lex(stext))

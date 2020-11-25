from lex import LexToken
from lark import Lark, v_args
from lark.lexer import Lexer, Token

tabela_lookup = {
    "+":            "MAIS",
    "-":            "MENOS",
    "*":            "MULT",
    "/":            "DIV",
    "=":            "ATRIB",
    ">":            "MAIOR",
    "<":            "MENOR",
    ">=":           "MAIORIG",
    "<=":           "MENORIG",
    "==":           "IGUAL",
    "!=":           "NIGUAL",
    ";":            "_SC",
    ",":            "_VIRG",
    "(":            "_PARESQ",
    ")":            "_PARDIR",
    "{":            "_CHAVEESQ",
    "}":            "_CHAVEDIR",
    "[":            "_COLESQ",
    "]":            "_COLDIR",
    "int":          "INT",
    "void":         "VOID",
    "if":           "_IF",
    "else":         "_ELSE",
    "while":        "_WHILE",
    "return":       "_RETURN",
    "whitespace":   "WS",
    "ID":           "ID",
    "NUM":          "NUM",
}

class TokenLexer(Lexer):
    def __init__(self, lexer_conf):
        pass

    def lex(self, data):
        for obj in data:
            if isinstance(obj, LexToken):
                yield Token(tabela_lookup[obj.type], obj)
            else:
                raise TypeError(obj)

parser = Lark("""
    programa:               _declaracao*
    _declaracao:            declaracao_variavel | declaracao_funcao
    declaracao_variavel:    tipo ID _SC | tipo ID _COLESQ NUM _COLDIR
    tipo:                   INT | VOID
    declaracao_funcao:      tipo ID _PARESQ parametros _PARDIR declaracao_composta
    parametros:             lista_parametros | VOID
    lista_parametros:       lista_parametros _VIRG param | param
    param:                  tipo ID
                            | tipo ID _COLESQ _COLDIR -> param_array
    declaracao_composta:    _CHAVEESQ declaracao_variavel* _comando* _CHAVEDIR
    _comando:               declaracao_expressao
                            | declaracao_composta
                            | declaracao_selecao 
                            | declaracao_iteracao 
                            | declaracao_retorno
    declaracao_expressao:   expressao _SC | _SC
    declaracao_selecao:     _IF _PARESQ expressao _PARDIR _comando | _IF _PARESQ expressao _PARDIR _comando _ELSE _comando
    declaracao_iteracao:    _WHILE _PARESQ expressao _PARDIR _comando
    declaracao_retorno:     _RETURN _SC | _RETURN expressao _SC
    expressao:              variavel ATRIB expressao | expressao_simples
    variavel:               ID | ID _COLESQ expressao _COLDIR
    expressao_simples:      soma_expressao op_relacional soma_expressao | soma_expressao
    op_relacional:          IGUAL | NIGUAL | MENORIG | MAIORIG | MENOR | MAIOR 
    soma_expressao:         soma_expressao op_soma termo | termo
    op_soma:                MAIS | MENOS
    termo:                  termo op_mult fator | fator
    op_mult:                MULT | DIV
    fator:                  _PARESQ expressao _PARDIR | variavel | ativacao | NUM
    ativacao:               ID _PARESQ argumentos _PARDIR
    argumentos:             lista_argumentos | 
    lista_argumentos:       lista_argumentos _VIRG expressao 
    
    %declare ID NUM _IF _ELSE _WHILE _RETURN INT VOID MAIS MENOS MULT DIV ATRIB MAIOR MAIORIG MENOR MENORIG IGUAL NIGUAL _SC _VIRG _PARESQ _PARDIR _CHAVEESQ _CHAVEDIR _COLESQ _COLDIR
    %ignore WS
""", parser='lalr', lexer=TokenLexer, start='programa')

def sintaxe(tokens):
    return parser.parse(tokens)
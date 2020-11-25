import unittest
import lex
import sintaxe

class LexTest(unittest.TestCase):
    def test_basecases(self):
        self.assertEqual(lex.lex("if"), [lex.LexToken("if")])
        self.assertEqual(lex.lex("else"), [lex.LexToken("else")])
        self.assertEqual(lex.lex("int"), [lex.LexToken("int")])
        self.assertEqual(lex.lex("void"), [lex.LexToken("void")])
        self.assertEqual(lex.lex("return"), [lex.LexToken("return")])
        self.assertEqual(lex.lex("while"), [lex.LexToken("while")])
        self.assertEqual(lex.lex("+"), [lex.LexToken("+")])
        self.assertEqual(lex.lex("-"), [lex.LexToken("-")])
        self.assertEqual(lex.lex("abc"), [lex.LexToken("ID", "abc")])
        self.assertEqual(lex.lex("12"), [lex.LexToken("NUM", 12)])

    def test_longestmatch(self):
        self.assertEqual(lex.lex("ifif"), [lex.LexToken("ID", "ifif")])
        self.assertEqual(lex.lex("voi"), [lex.LexToken("ID", "voi")])
        self.assertEqual(lex.lex("elsea"), [lex.LexToken("ID", "elsea")])
        self.assertEqual(lex.lex("whilew"), [lex.LexToken("ID", "whilew")])

    def test_example(self):
        self.assertEqual([x.type for x in lex.lex("""
        void main(void)
        { int x; int y;
            int z;
            x = 5;
            y = 10;
        }""")],
        ["void", "ID", "(", "void", ")", 
        "{", "int", "ID", ";", "int", "ID", ";", 
        "int", "ID", ";", 
        "ID", "=", "NUM", ";", 
        "ID", "=", "NUM", ";", 
        "}"])

class SyntaxTest(unittest.TestCase):
    def test_basic(self):
        print(sintaxe.sintaxe(lex.lex("""
                void main(void)
                { int x; int y;
                    int z;
                    x = 5;
                    y = 10;
                }""")).pretty())

if __name__ == '__main__':
    unittest.main()
import unittest
import lex

class LexTest(unittest.TestCase):
    def test_basecases(self):
        self.assertEqual(lex.lex("if"), ["if"])
        self.assertEqual(lex.lex("else"), ["else"])
        self.assertEqual(lex.lex("int"), ["int"])
        self.assertEqual(lex.lex("void"), ["void"])
        self.assertEqual(lex.lex("return"), ["return"])
        self.assertEqual(lex.lex("while"), ["while"])
        self.assertEqual(lex.lex("+"), ["+"])
        self.assertEqual(lex.lex("-"), ["-"])
        self.assertEqual(lex.lex("abc"), ["ID"])
        self.assertEqual(lex.lex("12"), ["NUM"])

    def test_longestmatch(self):
        self.assertEqual(lex.lex("ifif"), ["ID"])
        self.assertEqual(lex.lex("voi"), ["ID"])
        self.assertEqual(lex.lex("elsea"), ["ID"])
        self.assertEqual(lex.lex("whilew"), ["ID"])

    def test_example(self):
        self.assertEqual(lex.lex("""
        void main(void)
        { int x; int y;
            int z;
            x = 5;
            y = 10;
        }"""),
        ["void", "ID", "(", "void", ")", 
        "{", "int", "ID", ";", "int", "ID", ";", 
        "int", "ID", ";", 
        "ID", "=", "NUM", ";", 
        "ID", "=", "NUM", ";", 
        "}"])

if __name__ == '__main__':
    unittest.main()
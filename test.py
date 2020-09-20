import unittest
import lex

class LexTest(unittest.TestCase):
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
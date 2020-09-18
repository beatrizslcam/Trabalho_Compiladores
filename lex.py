import re

def lex(content: str):
    line_n = 0

    # Split file contents by its lines.
    lines = content.splitlines()
    
    # For each line, split its token.
    for line in lines:
        tokens = line.split([" ", "\t"])
        
        # Identify each token.
        for token in tokens:
            t

        line_n += 1
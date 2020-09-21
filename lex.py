import re

def lex(content: str):
    line_n = 1
    result = list()

    # Build match patterns.
    patterns = {
        "ws": re.compile(r"\s*"),
        "if": re.compile(r"if"),
        "else": re.compile(r"else"),
        "int": re.compile(r"int"),
        "void": re.compile(r"void"),
        "return": re.compile(r"return"),
        "while": re.compile(r"while"),
        "operator": re.compile(r"[\+\-\*/<{<=}>{>=}{==}{!=}=;,\(\)\{\}{\\\*}{/\*}]"),
        "NUM": re.compile(r"[0-9]+"),
        "ID": re.compile(r"[a-z]+")
    }

    # Split file contents by its lines.
    lines = content.splitlines()
    
    # For each line, scan 
    for line in lines:
        column_n = 1
        while(column_n <= len(line)):
            cur_match = None
            cur_type = None
            
            # Find longest match.
            for type, pattern in patterns.items():
                match = pattern.match(line, column_n - 1)
                if match != None and (cur_match == None or len(cur_match.group()) < len(match.group())):
                    cur_match = match
                    cur_type = type

            # If no match was found, next character must be invalid
            if cur_match == None:
                print("Error: invalid character at line ", line_n, ", column ", column_n, ".", sep = '')
                column_n += 1
            else:
                if cur_type == "ws":
                    pass
                elif cur_type == "operator":
                    result.append(cur_match.group())
                else:
                    result.append(cur_type)
                column_n += len(cur_match.group())

        line_n += 1
    return result
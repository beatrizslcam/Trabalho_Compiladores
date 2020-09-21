import re

def lex(content: str):
    line_n = 1
    result = list()

    # Build match patterns.
    pattern = re.compile(r"""
    (?P<whitespace>\s)
    |(?P<if>if)
    |(?P<else>else)
    |(?P<int>int)
    |(?P<void>void)
    |(?P<return>return)
    |(?P<while>while)
    |(?P<operator>[\+\-\*/<{<=}>{>=}{==}{!=}=;,\(\)\{\}{\\\*}{/\*}])
    |(?P<ID>[a-z]+)
    |(?P<NUM>[0-9]+)
    """, re.VERBOSE)

    # Split file contents by its lines.
    lines = content.splitlines()
    
    # For each line, scan 
    for line in lines:
        column_n = 1
        while(column_n <= len(line)):
            # Find longest match.
            match = pattern.match(line, column_n - 1)

            # If no match was found, next character must be invalid
            if not match:
                print("Error: invalid character at line ", line_n, ", column ", column_n, ".", sep = '')
                column_n += 1
            else:
                if match.lastgroup == "whitespace":
                    pass
                elif match.lastgroup == "operator":
                    result.append(match.group())
                else:
                    result.append(match.lastgroup)
                column_n += len(match.group())

        line_n += 1
    return result
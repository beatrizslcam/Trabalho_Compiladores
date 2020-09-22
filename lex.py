import regex

def lex(content: str):
    line_n = 1
    result = list()

    # Build match patterns.
    pattern = regex.compile(r"""
    (?p)(?P<whitespace>\s)
    |(?P<if>if)
    |(?P<else>else)
    |(?P<int>int)
    |(?P<void>void)
    |(?P<return>return)
    |(?P<while>while)
    |(?P<operator>[\+\-\*/<{<=}>{>=}{==}{!=}=;,\(\)\{\}{\\\*}{/\*}])
    |(?P<ID>[a-z]+)
    |(?P<NUM>[0-9]+)
    """, regex.VERBOSE)

    # Split file contents by its lines.
    lines = content.splitlines()
    
    # For each line, scan 
    for line in lines:
        column_n = 1
        while(column_n <= len(line)):
            # Find the longest match.
            match = pattern.match(line, column_n - 1)

            # If no match was found, next character must be invalid. Raise a error message and move towards the next character.
            if not match:
                print("Error: invalid character at line ", line_n, ", column ", column_n, ".", sep = '')
                column_n += 1
                continue
            # If whitespace was found, ignore it.
            elif match.lastgroup == "whitespace":
                pass
            # If an operator was found, add the identified operator into the list.
            elif match.lastgroup == "operator":
                result.append(match.group())
            # Otherwise, add the capture group name into the list.
            else:
                result.append(match.lastgroup)

            # Advance the stream towards the character after the matched token.
            column_n += len(match.group())

        line_n += 1
    return result
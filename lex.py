import regex

class LexToken:
    def __init__(self, type, tag = None):
        self.type = type
        self.tag = tag

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
                result.append(LexToken(match.group()))
            # If an ID was found, create a token associated with the idenfier name.
            elif match.lastgroup == "ID":
                result.append(LexToken("ID", match.group()))
            # If a NUM was found, create a token associated with the numeric value as int.
            elif match.lastgroup == "NUM":
                result.append(LexToken("NUM"), int(match.group()))
            # Otherwise, just add the keyword name.
            else:
                result.append(LexToken(match.lastgroup))

            # Advance the stream towards the character after the matched token.
            column_n += len(match.group())

        line_n += 1
    return result
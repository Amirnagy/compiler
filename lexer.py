# Define a function to tokenize the input string
def tokenize(input_string):
    tokens = []
    position = 0

    while position < len(input_string):

        char = input_string[position]

        if char.isdigit():
            # Parse integer
            start = position
            # because if i have more than one intger like 12345 in the begin of the code
            while position < len(input_string) and input_string[position].isdigit():
                position += 1
            tokens.append(('INTEGER', input_string[start:position]))

        elif char == '+':
            tokens.append(('PLUS', '+'))
            position += 1
            
        elif char == '-':
            tokens.append(('MINUS', '-'))
            position += 1
        elif char == '*':
            tokens.append(('MULTIPLY', '*'))
            position += 1
        elif char == '/':
            tokens.append(('DIVIDE', '/'))
            position += 1
        elif char == '(':
            tokens.append(('LPAREN', '('))
            position += 1
        elif char == ')':
            tokens.append(('RPAREN', ')'))
            position += 1
        elif char.isspace():
        # Skip whitespace
            position += 1
        else:
            raise ValueError(f"Invalid character: {char}")
    return tokens

# Test the tokenizer with an example input string
input_string = "3 + 4 * 5 - 6 / 2"
tokens = tokenize(input_string)
print(tokens)


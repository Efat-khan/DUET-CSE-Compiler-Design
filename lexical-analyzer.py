import re

# Token definitions (regex patterns)
token_patterns = [
    ('KEYWORD', r'\b(int|float|if|else|while|return)\b'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('NUMBER', r'\b\d+\b'),
    ('OPERATOR', r'[+\-*/=]'),
    ('SEPARATOR', r'[;,\(\)\{\}]'),
    ('WHITESPACE', r'\s+'),
    ('UNKNOWN', r'.')  # Catch-all for unknown characters
]

def lexical_analyzer(input_code):
    tokens = []
    while input_code:
        for token_type, pattern in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(input_code)
            if match:
                lexeme = match.group(0)
                print (lexeme);
                if token_type != 'WHITESPACE':  # Ignore whitespace
                    tokens.append((token_type, lexeme))
                input_code = input_code[len(lexeme):]
                break
    return tokens

# Example usage
code = "int age = 25;"
tokens = lexical_analyzer(code)
for token in tokens:
    print(token)

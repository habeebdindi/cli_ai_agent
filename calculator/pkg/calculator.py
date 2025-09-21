class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        tokens = self._tokenize(expression)
        return self._evaluate_infix(tokens)

    def _tokenize(self, expression):
        tokens = []
        current_number = ''
        for char in expression:
            if char.isdigit() or char == '.':
                current_number += char
            elif char in self.operators or char in ['(', ')']:
                if current_number:
                    tokens.append(current_number)
                    current_number = ''
                tokens.append(char)
            elif char.isspace():
                if current_number:
                    tokens.append(current_number)
                    current_number = ''
            else:
                raise ValueError(f"Invalid character: {char}")
        if current_number:
            tokens.append(current_number)
        return tokens

    def _evaluate_infix(self, tokens):
        values = []
        operators = []

        for token in tokens:
            if token == '(': # Handle open parenthesis
                operators.append(token)
            elif token == ')': # Handle closing parenthesis
                while operators and operators[-1] != '(': # while there are operators and the top of the stack is not an open parenthesis
                    self._apply_operator(operators, values)
                operators.pop() # Remove open parenthesis
            elif token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        while operators:
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if operator == '(': # if it is a parenthesis, return
            return
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        values.append(self.operators[operator](a, b))

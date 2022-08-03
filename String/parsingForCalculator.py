
class Tokenizer:
    def __init__(self, s):
        self.s = s
        self.current_idx = 0
        self.skip_whitespaces()

    def has_next(self):
        return self.current_idx < len(self.s)

    def next(self):
        self.current_idx += 1
        self.skip_whitespaces()

    def current(self):
        return self.s[self.current_idx]

    def is_digit(self):
        return self.current().isdigit()

    def skip_whitespaces(self):
        # move current_idx to next non empty value
        while self.has_next() and self.current() == ' ':
            self.current_idx += 1

def calculate(s):
    tokenizer = Tokenizer(s)
    op_map = {'+': lambda x, y: x + y,
              '-': lambda x, y: x - y}
    def num():
        n = 0
        while tokenizer.has_next() and tokenizer.is_digit():
            n = (n * 10) + int(tokenizer.current())
        return n

    def factor():
        neg = 1
        if tokenizer.current() == '-':
            neg = -1
            tokenizer.next()

        if tokenizer.current() == '(':
            tokenizer.next()
            n = expr()
            tokenizer.next()
        elif tokenizer.is_digit():
            n = num()
        return n * neg

    def expr():
        acc = factor()

        while tokenizer.has_next() and tokenizer.current() in op_map:
            op = tokenizer.current()
            tokenizer.next()
            acc = op_map[op](acc, factor())
        return acc
    return expr()


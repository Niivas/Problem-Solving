class StockSpanner:
    def __init__(self):
        self.stack = []
    def next(self, price):
        result = 1
        while self.stack and self.stack[-1][0] <= price:
            result += self.stack.pop()[1]
        self.stack.append([price, result])
        return result
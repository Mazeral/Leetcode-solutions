class StockSpanner:
    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        span = 1

        while self.prices and self.prices[-1][0] <= price:

            prev_price, prev_span = self.prices.pop()

            span += prev_span

        self.prices.append((price, span))
        return span

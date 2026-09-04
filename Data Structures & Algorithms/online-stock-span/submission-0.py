class StockSpanner:
    # need to find the last day where the price was higher -
    # keep monotonic (decreasing) stack holding (price, span)
    # if new price is lowest, add it with span 1
    # if new price is higher than previous, keep popping lower/equal prices and sum their spans + 1


    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1][0]:
            span += self.stack[-1][1]
            self.stack.pop()

        self.stack.append((price, span))
        return span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
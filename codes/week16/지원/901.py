class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        stack = self.stack

        if len(stack) == 0:
            stack.append((price, 1))
            self.stack = stack
            return 1
        else:
            count = 1
            # 압축 가능
            while len(stack) and stack[-1][0] <= price:
                popped_price, popped_count = stack.pop()
                count += popped_count
            
            stack.append((price, count))
            self.stack = stack
            return stack[-1][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
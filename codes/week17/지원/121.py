class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        min_price = float('inf')  
        max_price = -float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
                max_price = price
         
            if price > max_price:
                max_price = price
            
            answer = max(answer, max_price - min_price)

        return answer
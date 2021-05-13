"""121. Best Time to Buy and Sell Stock
Easy

8322

361

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104"""


class Solution:
    def maxprofit(self, prices: list[int]) -> int:
        lowest = highest = prices[0]
        lowest_day = 0
        highest_day = 0
        for i, price in enumerate(prices):
            if price < lowest and highest_day <= lowest_day:
                lowest = highest = price
                lowest_day = i
                highest_day = i
                continue
            if price > highest:
                highest = price
                highest_day = i
                continue
            lowest_day = i
        return highest - lowest


my_prices = [3, 2, 6, 5, 0, 3]
solution = Solution()
print(solution.maxprofit(my_prices))

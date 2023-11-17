class Solution:
    def maxProfit(self, prices: List[int], transaction_fee: int) -> int:
        # Initialize current buying price to positive infinity
        current_buy_price = math.inf

        # Get the length of the prices list
        num_prices = len(prices)

        # Initialize profit to 0
        total_profit = 0

        # Iterate over the prices list
        for i in range(num_prices):
            # If the current price is lower than the current buying price,
            # update the current buying price
            if prices[i] < current_buy_price:
                current_buy_price = prices[i]
            else:
                # If selling at this price results in profit greater than the transaction fee,
                # calculate the profit and update the current buying price
                if prices[i] - current_buy_price > transaction_fee:
                    current_profit = prices[i] - current_buy_price - transaction_fee
                    total_profit += current_profit
                    current_buy_price = prices[i] - transaction_fee

        # Return the total profit
        return total_profit

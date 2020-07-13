# Problem #130
#
# Given an array of numbers representing the stock prices of a company in chronological order and an integer k,
# return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it,
# and you must sell the stock before you can buy it again.
#
# For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.


def max_profit(stocks, k, index=0, buys=0, sells=0, profit=0):

    # if there is no stocks or no trades to make (no k), the profit is 0
    if not stocks or k <= 0:
        return 0

    # if there is no more stocks to buy or it is not possible to sell anymore, return profit
    if len(stocks) == index or k == sells:
        return profit

    # there is 3 operations to make: wait (skip the index), buy or sell
    # wait just go to the next index
    wait = max_profit(stocks, k, index + 1, buys, sells, profit)

    # if it is possible to buy, try buy it
    if sells >= buys:
        buy = max_profit(stocks, k, index+1, buys+1, sells, profit - stocks[index])
        return max(buy, wait)

    # try selling the stocks you have
    sell = max_profit(stocks, k, index+1, buys, sells+1, profit + stocks[index])

    return max(sell, wait)


assert (max_profit(None, 2)) == 0
assert (max_profit([5, 2, 4, 0, 1], 0)) == 0
assert (max_profit([5, 2, 4, 0, 1], 2)) == 3
assert (max_profit([5, 2, 4, 0, 1], 1)) == 2
assert (max_profit([0, 1], 1)) == 1
assert (max_profit([1, 0], 1)) == 0
assert (max_profit([0, 1], 2)) == 1

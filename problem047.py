# Problem #47 [Easy]
# Given a array of numbers representing the stock prices of a company in chronological order,
# write a function that calculates the maximum profit you could have made from buying and selling that stock once.
# You must buy before you can sell it.
#
# For example, given [9, 11, 8, 5, 7, 10], you should return 5,
# since you could buy the stock at 5 dollars and sell it at 10 dollars.


# instantly went for this n² time solution, but after i could see a linear one
def maximum_profit(array):
    biggest_profit = 0
    # take one price
    for outer_index in range(len(array[0:])):
        buy_price = array[outer_index]
        # and compare to all other prices
        for inner_index in range(outer_index + 1, len(array)):
            sell_price = array[inner_index]
            # check for profit
            profit = sell_price - buy_price
            # if the profit is bigger, update it
            if profit > biggest_profit:
                biggest_profit = profit
    return biggest_profit


assert maximum_profit([9, 11, 8, 5, 7, 10]) == 5
assert maximum_profit([9, 11, 8, 10, 7, 10]) == 3
assert maximum_profit([6, 11, 8, 10, 7, 1]) == 5
assert maximum_profit([]) == 0
assert maximum_profit([1]) == 0
assert maximum_profit([5, 2]) == 0


def maximum_profit_linear(array):
    biggest_profit = 0

    if not array:
        return biggest_profit

    # take one price
    price_check = array[0]
    # and compare with the next price
    for price in array[1:]:
        # calculate profit
        profit = price - price_check
        # if profit increased, update
        if profit > biggest_profit:
            biggest_profit = profit
        # if there is lower price, update
        if price_check > price:
            price_check = price
    return biggest_profit


assert maximum_profit_linear([9, 11, 8, 5, 7, 10]) == 5
assert maximum_profit_linear([9, 11, 8, 10, 7, 10]) == 3
assert maximum_profit_linear([6, 11, 8, 10, 7, 1]) == 5
assert maximum_profit_linear([]) == 0
assert maximum_profit_linear([1]) == 0
assert maximum_profit_linear([5, 2]) == 0

# easy problem, the first solution came instantly, the second one i need to iterate on the first some times to see that
# nested loops are not necessary. 30 minutes to do everything

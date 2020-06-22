# Problem #109
#
# Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, the 3rd and 4th
# bit should be swapped, and so on.
#
# For example, 10101010 should be 01010101. 11100010 should be 11010001.
#
# Bonus: Can you do this in one line?


def swap_bits(x):
    return (x & 0b10101010) >> 1 | (x & 0b01010101) << 1


assert swap_bits(0b10101010) == 0b01010101
assert swap_bits(0b11100010) == 0b11010001


# i didnt even understand how to represent a unsigned 8-bit int in python, have to google that. i had some multiple
# step ideas on how to do the problem, but no clue on how to do it in one line. after some google i found an
# explanation on the daily coding problem oficial site https://www.dailycodingproblem.com/blog/neat-bitwise-trick/

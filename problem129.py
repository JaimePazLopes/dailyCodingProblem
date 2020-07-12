# Problem #129
#
# Given a real number n, find the square root of n. For example, given n = 9, return 3.


def square_root(n):
    # Base cases
    if n is None:
        return None

    if n == 0 or n == 1:
        return n

    # added a sign to it, so it can cover negative numbers
    sign = 1
    if n < 0:
        sign = -1
        n *= -1

    # Do Binary Search for floor(sqrt(x))
    start = 1
    end = n
    while start <= end:
        mid = (start + end) // 2

        # If x is a perfect square
        if mid * mid == n:
            return mid * sign

        # Since we need floor, we update answer when mid*mid is smaller than x, and move closer to sqrt(x)
        if mid * mid < n:
            start = mid + 1
            ans = mid

        else:

            # If mid*mid is greater than x
            end = mid - 1

    # making approximation
    while abs(ans * ans - n) >= 0.01:
        division = n / ans
        ans = (division + ans) / 2

    ans = round(ans, 3)

    return ans * sign


print(square_root(None))
print(square_root(1))
print(square_root(-1))
print(square_root(9))
print(square_root(-9))
print(square_root(100))
print(square_root(2.5))
print(square_root(10))

# i had no clue on how to do this problem had to google a way. found 2 sources that mixed game me a satisfying answer.
# the first one https://www.geeksforgeeks.org/square-root-of-an-integer/ was a easy way to get a floor square root.
# but for me this was not enough to cover the problem.
# using this http://www.math.com/school/subject1/lessons/S1U1L9DP.html i was able to get the non perfect squares,
# i did a small chance to iterate on it until i got a given precision

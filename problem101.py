# Problem #101
#
# Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.
#
# A solution will always exist. See Goldbach’s conjecture.
#
# Example:
#
# Input: 4 Output: 2 + 2 = 4 If there are more than one solution possible, return the lexicographically smaller solution
#
# If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
#
# [a, b] < [c, d]
# if a < c or a==c and b < d.


def get_2_prime(number):
    if number <= 2 or number % 2 == 1:
        return None

    primes = list()

    # find all prime numbers lower than number
    for each in range(2, number):
        is_prime = True

        # if the number is divided by a prime, it is not prime
        for prime in primes:
            if each % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(each)

    # for each prime
    for prime in primes:
        # get the number - prime to see if it is a prime
        possible = number - prime

        # if number - prime is a prime, that is the answer
        if possible in primes:
            # since it starts by the first prime numbers, the first answer is the lexicographically smaller
            return [prime, possible]

    return None


assert (get_2_prime(-1)) is None
assert (get_2_prime(0)) is None
assert (get_2_prime(1)) is None
assert (get_2_prime(2)) is None
assert (get_2_prime(3)) is None
assert (get_2_prime(11)) is None
assert (get_2_prime(4)) == [2, 2]
assert (get_2_prime(10)) == [3, 7]
assert (get_2_prime(12)) == [5, 7]
assert (get_2_prime(100)) == [3, 97]

# nice problem, i like to work with prime numbers. this problem took a lot of time because i went to study about
# Goldbach’s conjecture, but in reality that it is not necessary to do this problem. finish in about 1 hour, most time
# on youtube watching videos about the conjecture

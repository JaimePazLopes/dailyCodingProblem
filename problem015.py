# Problem #15 [Medium]
# Given a stream of elements too large to store in memory,
# pick a random element from the stream with uniform probability.

import random

# kinda didnt get this problem... what i think was: it is too big to put in memory, so i cant know its size,
# so i just go one by one to count its size and later with its size i can get a random index with uniform probability
def countSize(stream):
    size = 0
    for _ in stream:
        size += 1
    return size

stream = list(range(101))
randomElement = stream[random.randint(0,countSize(stream)-1)]
print("My function")
print(f"Random element from stream: {randomElement}")
print(f"Random element from stream: {randomElement}")
print(f"Random element from stream: {randomElement}")
print()

# then i looked online and found the Reservoir sampling article on wikipedia, i confess that i didnt understand how
# this works, but it works. I did the simple algorithm below for getting only one element

def reservoirSample(stream):
    # r is the result
    r = stream[0]
    # k is the number of elements in r, for this algorithm i am considering that r will always only 1 element
    k = 1
    for i in range(1,len(stream)):
        j = random.randint(1, i)
        if j <= k:
            r = stream[i]
    return r

print("Reservoir sampling")
print(f"Random element from stream: {reservoirSample(stream)}")
print(f"Random element from stream: {reservoirSample(stream)}")
print(f"Random element from stream: {reservoirSample(stream)}")
print()

# for only one element i really dont understand why use this, this algorithm even consider that you know the stream
# size, so just taking a random element with index between 0 and stream size would do
# I think this algorithm is good when you need to take multiplo elements from a stream with uniform probability
# so i will do it

def reservoirSample(stream, k):
    if k <= 0:
        return "This function can take 0 elements or less"
    if len(stream) < k:
        return "The stream dont have that many elements"
    R = []
    for i in range(k):
        R.append(stream[i])

    for i in range(k,len(stream)):
        j = random.randint(0, i)
        if j <= k - 1:
            R[j] = stream[i]
    return R

print("Reservoir sampling getting k elements")
print(f"Random elements from stream: {reservoirSample(stream, 0)}")
print(f"Random elements from stream: {reservoirSample(stream, 2)}")
print(f"Random elements from stream: {reservoirSample(stream, 5)}")
print(f"Random elements from stream: {reservoirSample(stream, 10)}")
print(f"Random elements from stream: {reservoirSample(stream, 20)}")
print(f"Random elements from stream: {reservoirSample(stream, 1000)}")

# this problem took around 1 hour and a half, more them half looking online
# didnt knew this Reservoir sampling but looks useful

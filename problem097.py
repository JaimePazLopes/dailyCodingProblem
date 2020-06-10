# Problem #97
#
# Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.
#
# It should contain the following methods:
#
#     set(key, value, time): # sets key to value for t = time.
#     get(key, time): # gets the key at t = time.
#
# The map should work like this. If we set a key at a particular time, it will maintain that value forever or until
# it gets set at a later time. In other words, when we get a key at a time, it should return the value that was set
# for that key set at the most recent time.
#
# Consider the following examples:
#
# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 2) # set key 1 to value 2 at time 2
# d.get(1, 1) # get key 1 at time 1 should be 1
# d.get(1, 3) # get key 1 at time 3 should be 2
#
# d.set(1, 1, 5) # set key 1 to value 1 at time 5
# d.get(1, 0) # get key 1 at time 0 should be null
# d.get(1, 10) # get key 1 at time 10 should be 1
#
# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 0) # set key 1 to value 2 at time 0
# d.get(1, 0) # get key 1 at time 0 should be 2

from collections import OrderedDict


class Map:

    def __init__(self):
        self.mapping = dict()

    def set(self, key, value, time):
        # if there is no key on the dict, make one
        if key not in self.mapping.keys():
            self.mapping[key] = OrderedDict()

        # add the time to the dict
        self.mapping[key][time] = value
        # order the dict based on the time
        self.mapping[key] = OrderedDict(sorted((self.mapping[key]).items(), key=lambda i: i[0]))

    def get(self, key, time):
        if key not in self.mapping.keys():
            return None

        working_keys: list = list((self.mapping[key]).keys())
        working_values: list = list((self.mapping[key]).values())

        # if the key exists, return it
        if time in working_keys:
            index = working_keys.index(time)
            return working_values[index]

        # if the time is before the first entry, return none
        if time < working_keys[0]:
            return None

        # look for the interval where time is
        for t in range(len(working_keys)-1):
            if working_keys[t] < time < working_keys[t + 1]:
                return working_values[t]

        # the time is more than the last time record, so return the last value
        return working_values[-1]


d = Map()
d.set(1, 1, 0)  # set key 1 to value 1 at time 0
d.set(1, 2, 2)  # set key 1 to value 2 at time 2
assert (d.get(1, 1)) == 1  # get key 1 at time 1 should be 1
assert (d.get(1, 3)) == 2  # get key 1 at time 3 should be 2

d = Map()
d.set(1, 1, 5)  # set key 1 to value 1 at time 5
assert (d.get(1, 0)) is None  # get key 1 at time 0 should be null
assert (d.get(1, 10)) == 1  # get key 1 at time 10 should be 1

d = Map()
d.set(1, 1, 0)  # set key 1 to value 1 at time 0
d.set(1, 2, 0)  # set key 1 to value 2 at time 0
assert (d.get(1, 0)) == 2  # get key 1 at time 0 should be 2

# i dont think that i got to a good solution, i used a ordered dict inside a dict, but i think that can be done in a
# better way. i used a ordered dict because it would make easier get the time intervals, but ordering it costs has a
# cost that is possible avoidable. did it in around 45 minutes to 1 hour, had to google many stuff, including ordered
# dict

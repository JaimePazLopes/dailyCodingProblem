# Problem #16 [Easy]
# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
#
#     record(order_id): adds the order_id to the log
#     get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
#
# You should be as efficient with time and space as possible.

# dont know if list would be the most efficient data in python. if the ids are only numeric, maybe array.array is better
class Log:

    def __init__(self, size):
        self.log = list()
        self.size = size

    def record(self, orderID):
        if len(self.log) >= self.size:
            self.log.pop(0)  # pop seems to be more efficient here because i am taking the first element
        self.log.append(orderID)

    def getLast(self, id):
        return self.log[-id]


log1 = Log(1)
log1.record(1)
log1.record(2)
log1.record(3)
print(log1.log, log1.getLast(1))

log2 = Log(2)
log2.record(1)
log2.record(2)
log2.record(3)
print(log2.log, log2.getLast(1))
print(log2.log, log2.getLast(2))

log3 = Log(3)
log3.record(1)
log3.record(2)
log3.record(3)
log3.record(4)
log3.record(5)
print(log3.log, log3.getLast(1))
print(log3.log, log3.getLast(2))

# quick problem, the code itself took like 5 minutes, but i google a little about data structures in python to see
# if there is a better data them list, I stayed with list because i think its more realistic, i see a lot of id using
# values that are strings or guids, but if you use only numbers, maybe arrray.array would be more efficient
# in total took aroun 30 minutes to finish, but i also keep the log in memory, the problem dont specify if it has to be
# in a file

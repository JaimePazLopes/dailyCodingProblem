# Problem #91
#
# What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?
#
# functions = []
# for i in range(10):
#     functions.append(lambda : i)
#
# for f in functions:
#     print(f())


functions = []
for i in range(10):
    functions.append(lambda x=i: x)

for f in functions:
    print(f())

# before the i was being incremented and the lambda function execute only when call, so its value was only 9
# (max value of i). so if you set i as a default value of another variable, it will be saved and used when executed

# Problem #87
# A rule looks like this:
#
# A NE B
#
# This means this means point A is located northeast of point B.
#
# A SW C
#
# means that point A is southwest of C.
#
# Given a list of rules, check if the sum of the rules validate. For example:
#
# A N B
# B NE C
# C N A
#
# does not validate, since A cannot be both north and south of C.
#
# A NW B
# A N B
#
# is considered valid.


opposite = {"N": "S", "S": "N", "W":"E", "E": "W"}


class Place:
    def __init__(self, name):
        self.name = name
        self.around = { "N": list(), "S": list(), "W": list(), "E": list()}

    def add(self, direction, place):
        if place.name in self.around[direction]:
            return True

        if place.name in self.around[opposite[direction]]:
            return False

        self.around[direction].append(place)

        return True
    

def validate_rules(rules):
    places = dict()

    for rule in rules:
        split: str = rule.split()

        place_1 = None
        place_2 = None

        if split[0] not in places.keys():
            place_1 = Place(split[0])
            places[split[0]] = place_1
        else:
            place_1 = places[split[0]]

        if split[2] not in places.keys():
            place_2 = Place(split[2])
            places[split[2]] = place_2
        else:
            place_2 = places[split[2]]

        directions = list(split[1])

        for direction in directions:
            if not place_1.add(direction, place_2):
                return False
            if not place_2.add(opposite[direction], place_1):
                return False

    # TODO

    return True


rules = ["A N B", "B NE C", "C N A"]
print(validate_rules(rules))

rules = ["A NW B", "A N B"]
print(validate_rules(rules))






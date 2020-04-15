# Problem #41 [Medium]
# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs,
# and a starting airport, compute the person's itinerary. If no such itinerary exists, return null.
# If there are multiple possible itineraries, return the lexicographically smallest one.
# All flights must be used in the itinerary.
#
# For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
# and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
#
# Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.
#
# Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A',
# you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
# However, the first one is lexicographically smaller.


# my solution
def create_itinerary(flights, actual):
    # add the actual airport to the itinerary
    itinerary = [actual]
    # variable to control if there is a flight or not
    flight_found = False
    # sort to get the best solution alphabetically
    sorted(flights, key=lambda x: x[1])
    # for each flight
    for flight in flights:
        # if the actual airport is the origin airport of this flight
        if actual == flight[0]:
            # create a new flight list without this flight
            next_flights = flights.copy()
            next_flights.remove(flight)
            # and try to find a route
            possible_flight = create_itinerary(next_flights, flight[1])
            # if it was found
            if possible_flight is not None:
                # update the control variable
                flight_found = True
                # add to the actual itinerary all the itinerary from this position
                itinerary.extend(possible_flight)
                # if you took all the flights stop everything
                if len(flights) + 1 == len(itinerary):
                    break
    if len(flights) == 0:
        return itinerary
    # if there is no flight return None
    if not flight_found:
        return None
    return itinerary


assert create_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], "YUL") ==\
       ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
assert create_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], "COM") is None
assert create_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], "A") == ['A', 'B', 'C', 'A', 'C']


# daily coding problem solution
# I understand "Given an unordered list of flights taken by someone and a starting airport" as create a function that
# receive a list of flights and a reference to the starting airport, but they put the start airport already as a list
# in the function parameters. Will try to be more open to the problems, event they do different stuff
def get_itinerary(flights, current_itinerary):
    # If we've used up all the flights, we're done
    if not flights:
        return current_itinerary
    last_stop = current_itinerary[-1]
    for i, (origin, destination) in enumerate(flights):
        # Make a copy of flights without the current one to mark it as used
        flights_minus_current = flights[:i] + flights[i + 1:]
        current_itinerary.append(destination)
        if origin == last_stop:
            return get_itinerary(flights_minus_current, current_itinerary)
        current_itinerary.pop()
    return None


assert get_itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], ["YUL"]) ==\
       ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
assert get_itinerary([('SFO', 'COM'), ('COM', 'YYZ')], ["COM"]) is None
assert get_itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], ["A"]) == ['A', 'B', 'C', 'A', 'C']

# easy problem had some problems because the way i try to do it, so i need more ifs the solution from daily coding
# problem is much clearer them mine. Did every thing in one hour

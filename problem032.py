# Problem #32 [Hard]
# Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a
# possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of
# any currency, so that you can end up with some amount greater than A of that currency.
#
# There are no transaction costs and you can trade fractional quantities.

from math import log

base_exchange = [[1, 0.75, 0.62, 0.97],
                [1.31, 1, 0.82, 1.28],
                [1.58, 1.20, 1, 1.54],
                [1.02, 0.77, 0.64, 1]
                ]


def arbitrage(table):
    transformed_graph = [[-log(edge) for edge in row] for row in table]

    # Pick any source vertex -- we can run Bellman-Ford from any vertex and
    # get the right result
    source = 0
    n = len(transformed_graph)
    min_dist = [float('inf')] * n

    min_dist[source] = 0

    # Relax edges |V - 1| times
    for i in range(n - 1):
        for v in range(n):
            for w in range(n):
                if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                    min_dist[w] = min_dist[v] + transformed_graph[v][w]

    # If we can still relax edges, then we have a negative cycle
    for v in range(n):
        for w in range(n):
            if min_dist[w] > min_dist[v] + transformed_graph[v][w]:
                return True

    return False


assert not arbitrage(base_exchange)
base_exchange[1][2] = base_exchange[1][2] * 1.1
assert arbitrage(base_exchange)

# another problem weirdly written, and the first one with absolutely no example. Maybe for english speakers it has more
# sense. i spent more than one hour on it trying to solve a different problem because I understood it in a different way
# the only good part is that they put the solution on their site with an okish explanation
# https://www.dailycodingproblem.com/blog/how-to-find-arbitrage-opportunities-in-python/

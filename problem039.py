# Problem #39 [Medium]
# Conway's Game of Life takes place on an infinite two-dimensional board of square cells.
# Each cell is either dead or alive, and at each tick, the following rules apply:
#
#     Any live cell with less than two live neighbours dies.
#     Any live cell with two or three live neighbours remains living.
#     Any live cell with more than three live neighbours dies.
#     Any dead cell with exactly three live neighbours becomes a live cell.
#
# A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
#
# Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates
# and the number of steps it should run for. Once initialized, it should print out the board state at each step.
# Since it's an infinite board, print out only the relevant coordinates, i.e.
# from the top-leftmost live cell to bottom-rightmost live cell.
#
# You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).

import itertools

# alive and dead char to print
ALIVE = "*"
DEAD = "."


# cell class, most stuff i did to test new python knowledge
class Cell:

    # the only stuff important is here, a tuple for position and a bool to check if it is alive
    def __init__(self, position_tuple):
        self._position = position_tuple
        self._is_alive = True

    @property
    def is_alive(self):
        return self._is_alive

    @property
    def position(self):
        return self._position

    # update status do all checks but create new cells
    def update_status(self, neighbors=[]):
        count_alive = 0
        for cell in neighbors:
            count_alive += 1

        if count_alive < 2 or count_alive > 3:
            self._die()
        elif count_alive == 3 and not self._is_alive:
            self._live()

    def _die(self):
        self._is_alive = False

    def _live(self):
        self._is_alive = True


class ConwayGameOfLife:

    def __init__(self, cells):
        self._cells = cells
        self._step_count = 0
        self._playing = False

    # put it separated from init just for practice reasons
    def game_start(self, steps):
        self._step_count = steps
        self._playing = True
        self._print_board()

    # do all the preparation and checks each step
    def next_step(self):
        # cells to be created
        new_cells = []
        # positions that a cell can be created, all the positions close to on living cell
        possible_cells_positions = set()
        # for each cell i take all positions around it
        for cell in self._cells:
            neighbor_positions = set(itertools.product(range(cell.position[0]-1, cell.position[0]+2),
                                                       range(cell.position[1]-1, cell.position[1]+2)))
            possible_cells_positions.update(neighbor_positions)
        # remove the positions already occupied by a cell
        for cell in self._cells:
            possible_cells_positions.remove(cell.position)
        # check if there is 3 cells close to each possible new cell
        for position in possible_cells_positions:
            neighbor_cells = []
            neighbor_positions = list(itertools.product(range(position[0]-1, position[0]+2),
                                                        range(position[1]-1, position[1]+2)))
            neighbor_positions.remove(position)
            for another_cell in self._cells:
                if another_cell.position in neighbor_positions:
                    neighbor_cells.append(another_cell)
            if len(neighbor_cells) == 3:
                new_cells.append(Cell(position))

        # update all living cells
        for cell in self._cells:
            # check the cell
            neighbor_cells = []
            neighbor_positions = set(itertools.product(range(cell.position[0] - 1, cell.position[0] + 2),
                                                       range(cell.position[1] - 1, cell.position[1] + 2)))
            for another_cell in self._cells:
                if cell == another_cell:
                    continue
                if another_cell.position in neighbor_positions:
                    neighbor_cells.append(another_cell)
            cell.update_status(neighbor_cells)

        # remove dead cells and add the new ones
        self._cells = list(filter(lambda x: x.is_alive, self._cells))
        self._cells.extend(new_cells)

        # if there is no more cell the game is over
        if not self._cells:
            self._playing = False

        self._print_board()

        # if there is no more steps the game is over
        self._step_count -= 1
        if self._step_count == 0:
            print("The steps are over")
            self._playing = False

    def still_playing(self):
        return self._playing

    def _print_board(self):
        if not self._playing:
            print("There is no alive cell")
            return
        print(f"Step: {self._step_count}")
        # take the positions of all living cells
        alive_positions = []
        # lowest_position and highest_position exist to create the smallest board possible
        lowest_position = self._cells[0].position
        highest_position = self._cells[0].position
        for cell in self._cells:
            if cell.is_alive:
                alive_positions.append(cell.position)
                lowest_position = (min(lowest_position[0], cell.position[0]),
                                   min(lowest_position[1], cell.position[1]))
                highest_position = (max(highest_position[0], cell.position[0]),
                                    max(highest_position[1], cell.position[1]))

        print(f"Area is from {lowest_position} to {highest_position}")

        # actually drawing the board, if there is an cell on the x,y position print the alive symbol, if not print dead
        for x in range(lowest_position[0], highest_position[0] + 1):
            line = ""
            for y in range(lowest_position[1], highest_position[1] + 1):
                if (x, y) in alive_positions:
                    line += ALIVE
                else:
                    line += DEAD
            print(f"{line}\n")


# everything here is totally for test and practice reasons, this could be much simpler
def main():
    print("GAME 1")
    conway_game = ConwayGameOfLife([Cell((10, 10)), Cell((11, 11)), Cell((12, 10)), Cell((10, 12)), Cell((9, 9))])
    conway_game.game_start(2)
    while conway_game.still_playing():
        # input()
        conway_game.next_step()
    print()
    print("GAME 2")
    conway_game = ConwayGameOfLife([Cell((0, 0)), Cell((0, 1)), Cell((0, 2))])
    conway_game.game_start(5)
    while conway_game.still_playing():
        # input()
        conway_game.next_step()
    print()
    print("GAME 3")
    conway_game = ConwayGameOfLife([Cell((0, 0)), Cell((0, 1)), Cell((1, 0)), Cell((2, 2)), Cell((3, 2)), Cell((3, 1))])
    conway_game.game_start(5)
    while conway_game.still_playing():
        # input()
        conway_game.next_step()


if __name__ == "__main__":
    main()

# cool problem, i made it a little more complicate on purposed to see some python things that i never tested before,
# like notations, "privating" variable and functions, etc. Took me 30 minutes to do everything but the new cells,
# i still didnt like this solution, but the other i thought were getting errors. did all in 2 hours

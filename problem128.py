# Problem #128
#
# The Tower of Hanoi is a puzzle game with three rods and n disks, each a different size.
#
# All the disks start off on the first rod in a stack.
# They are ordered by size, with the largest disk on the bottom and the smallest one at the top.
#
# The goal of this puzzle is to move all the disks from the first rod to the last rod while following these rules:
#
#     You can only move one disk at a time.
#     A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
#     You cannot place a larger disk on top of a smaller disk.
#
# Write a function that prints out all the steps necessary to complete the Tower of Hanoi.
# You should assume that the rods are numbered, with the first rod being 1,
# the second (auxiliary) rod being 2, and the last (goal) rod being 3.
#
# For example, with n = 3, we can do this in 7 moves:
#
#     Move 1 to 3
#     Move 1 to 2
#     Move 3 to 2
#     Move 1 to 3
#     Move 2 to 1
#     Move 2 to 3
#     Move 1 to 3


# move a disk from one stack to the other
def move(from_stack, to_stack):
    print(f"Move from {from_stack} to {to_stack}")


def hanoi_solver(n, from_stack=1, intermediary_stack=2, to_stack=3):
    # if there is no disks, do nothing
    if not n:
        return
    # free the bigger disk by moving all the smaller disks to the intermediary stack
    hanoi_solver(n - 1, from_stack, to_stack, intermediary_stack)
    # move the bigger free disk to the end position
    move(from_stack, to_stack)
    # move all disks from the intermediary stack to the final stack
    hanoi_solver(n - 1, intermediary_stack, from_stack, to_stack)


print("Solve for 3")
hanoi_solver(3)
print()
print("Solve for 4")
hanoi_solver(4)

# I already watch this video https://www.youtube.com/watch?v=8lhxIOAfDss many times and code more than once this problem

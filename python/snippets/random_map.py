"""
Tried to make a random dungeon.
"""

from random import randrange


def get_grid(x, y, wall_prob=45):
    """Returns a 2d grid filled with True or False. The probability to be a wall is 45% by default"""

    grid = [[True if randrange(0, 100) < wall_prob else False for _ in range(y)]
            for __ in range(x)]
    # the borders are walls
    grid[0] = [True] * y
    grid[len(grid)-1] = [True] * y
    for n, line in enumerate(grid):
        grid[n][0] = True
        grid[n][len(grid[0])-1] = True
    return grid


def get_if_possible(grid, x, y):
    "Return True if it's a wall or an edge, and False if it's not"
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
        return True
    else:
        # return the asked case (True or False)
        return grid[x][y]


def count_walls(grid, x, y):
    "Return the number of walls around and in a case"
    neighboors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            neighboors.append(get_if_possible(grid, x+i, y+j))
    # return the sum of all the wall neighboors
    return sum(map(int, neighboors))



def iter_grid(grid, threshold=5):
    "threshold is the number of necessary neighboors to become a wall"
    newgrid = []
    for x in range(0, len(grid)):
        newline = []
        newgrid.append(newline)
        for y in range(0, len(grid[0])):
            if count_walls(grid, x, y) >= threshold:
                newline.append(True)
            else:
                newline.append(False)
    return newgrid


def gen_dungeon(x, y, iterations=5, wall_prob=45):
    "Return a complete dungeon, using the functions defined before."
    grid = get_grid(x, y, wall_prob)
    for x in range(iterations):
        grid = iter_grid(grid)
    return grid


"""
# Code used when testing. Output a formatted dungeon to a "grid_output.txt" file
iterations = 5
wall_prob = 45
grid = get_grid(40, 40, wall_prob)
for _ in range(iterations):
    grid = iter_grid(grid)

towrite = []
for i, line in enumerate(grid):
    newline = ["#" if cell else "-" for cell in grid[i]]
    towrite.append("".join(newline))
towrite = "\n".join(towrite) + "\n"

with open("grid_output.txt", "a") as f:
    f.write(str(iterations) + " iterations\n")
    f.write(str(wall_prob) + "% of walls initially\n")
    # for i, line in enumerate(grid):
    #    grid[i] = "".join(line)
    #f.write("\n".join(grid) + "\n")
    f.write(towrite)
# for line in grid:
#    print(line)
"""

if __name__ == "__main__":
    import os

    dungeon = gen_dungeon(100, 100)
    towrite = "\n".join(["".join(["#" if cell else "-" for cell in dungeon[i]]) for i in range(len(dungeon))])

    

    if os.path.exists("grid.txt"):
        with open("grid.txt", "a") as f:
            f.write("\n++++++++++++++\n")
    with open("grid.txt", "a") as f:
        f.write(towrite)

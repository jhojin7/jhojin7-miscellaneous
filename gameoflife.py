import os
import time

ALIVE = '@'
DEAD = '.'
EDGE = '+'
(WIDTH,HEIGHT) = (40,20)
# (WIDTH,HEIGHT) = os.get_terminal_size()


def init_grid(width,height):
    _grid = [['.' for _ in range(width)]\
        for _ in range(height)]

    for i in range(height):
        for j in range(width):
            _grid[i][j] = DEAD

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if i==0 or i==HEIGHT-1 or j==0 or j==WIDTH-1:
                _grid[i][j] = EDGE
    return _grid

def print_grid(_grid,height):
    for i in range(height):
        # print(_grid[i])
        print(' '.join(_grid[i]))
    print(f"{len(_grid[0])}x{len(_grid)}")

def next_state(_grid,x,y):
    # counts alive neighbors around the cell

    # neighboring_grid = [
    #     _grid[(i-1)%HEIGHT][(j-1)%WIDTH:(j+2)%WIDTH],
    #     _grid[i%WIDTH][(j-1)%WIDTH:(j+2)%WIDTH],
    #     _grid[(i+1)%HEIGHT][(j-1)%WIDTH:(j+2)%WIDTH]
    # ]
    # for x in neighboring_grid:
    #     neighbors += x.count(ALIVE)

    # for x in _grid[(i-1+HEIGHT)%HEIGHT:(i+2+HEIGHT)%HEIGHT]:
    #     y = x[(j-1+WIDTH)%WIDTH:(j+2+WIDTH)%WIDTH]
    #     neighbors += y.count(ALIVE)
    #     print((i,j),y,y.count(ALIVE))

    neighbors = 0
    for i in range(-1,2):
        for j in range(-1,2):
            # a = x+i if x+i > 0 and x+i <= HEIGHT else abs(x+i)%HEIGHT
            # b = y+j if y+j > 0 and y+j <= WIDTH else abs(y+j)%WIDTH
            # # a = (HEIGHT+x+i)%HEIGHT
            # # b = (WIDTH+y+j)%WIDTH
            a,b = x+i, y+j

            # if a < 0 or b < 0 or a >= HEIGHT or b >= WIDTH:
            #     return EDGE
            if _grid[a][b] == ALIVE and (i,j)!=(0,0):
                neighbors += 1
    # print((i,j),neighbors)
    
    if _grid[x][y] == EDGE:
        return EDGE

    if _grid[x][y] == ALIVE:
        if neighbors == 2 or neighbors == 3:
            return ALIVE
        else: return DEAD

    if _grid[x][y] == DEAD:
        if neighbors == 3:
            return ALIVE
        else: return DEAD
    
    else:
        return EDGE
    
    



def glider(_grid):
    
    _grid[3][2] = ALIVE
    _grid[3][3] = ALIVE
    _grid[3][4] = ALIVE
    _grid[2][3] = ALIVE
    _grid[4][3] = ALIVE

    # _grid[5][4] = ALIVE
    # _grid[5][5] = ALIVE
    # _grid[5][6] = ALIVE
    # _grid[4][5] = ALIVE
    # _grid[4][5] = ALIVE
    # _grid[6][5] = ALIVE


    # _grid[1][2] = ALIVE
    # _grid[2][3] = ALIVE
    # _grid[3][1] = ALIVE
    # _grid[3][2] = ALIVE
    # _grid[3][3] = ALIVE
    return _grid

if __name__=='__main__':
    os.system('clear||cls')
    print("=============")

    grid = init_grid(WIDTH, HEIGHT)
    next = init_grid(WIDTH, HEIGHT)

    # set grid
    grid = glider(grid)

    for _ in range(100000):
    # while input()==' ':
        time.sleep(0.6)
        os.system('clear||cls')
        print_grid(grid,HEIGHT)
        # set next state
        for i in range(1,HEIGHT-1):
            for j in range(1,WIDTH-1):
                next[i][j] = next_state(grid,i,j)

        grid[:] = next[:]
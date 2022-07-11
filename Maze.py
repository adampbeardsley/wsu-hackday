# Maze generator -- Randomized Prim Algorithm

## Imports
import random
import time
from colorama import init
from colorama import Fore, Back, Style
from pynput import keyboard

global pin
## Functions
def printMaze(maze):
    for i in range(0, height):
        for j in range(0, width):
            if (maze[i][j] == 'u'):
                print(Fore.WHITE + str(maze[i][j]), end=" ")
            elif (maze[i][j] == 'c'):
                print(Fore.GREEN + str(maze[i][j]), end=" ")
            elif (maze[i][j] =='s' or maze[i][j] =='f'):
                print(Fore.BLUE +str(maze[i][j]), end=" ")
            elif (maze[i][j] =='p'):
                print(Fore.YELLOW +str(maze[i][j]), end=" ")
            else:
                print(Fore.RED + str(maze[i][j]), end=" ")

        print('\n')


def printMazeDone(maze):
    for i in range(0, height):
        for j in range(0, width):
            print(Fore.YELLOW + str(maze[i][j]), end=" ")


        print('\n')


# Find number of surrounding cells
def surroundingCells(rand_wall):
    s_cells = 0
    if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
        s_cells +=1
    if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
        s_cells += 1

    return s_cells


## Main code
# Init variables
wall = 'w'
cell = 'c'
unvisited = 'u'
height = 10
width = 15
maze = []

# Initialize colorama
init()

# Denote all cells as unvisited
for i in range(0, height):
    line = []
    for j in range(0, width):
        line.append(unvisited)
    maze.append(line)

# Randomize starting point and set it a cell
starting_height = int(random.random()*height)
starting_width = int(random.random()*width)
if (starting_height == 0):
    starting_height += 1
if (starting_height == height-1):
    starting_height -= 1
if (starting_width == 0):
    starting_width += 1
if (starting_width == width-1):
    starting_width -= 1

# Mark it as cell and add surrounding walls to the list
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])

# Denote walls in maze
maze[starting_height-1][starting_width] = 'w'
maze[starting_height][starting_width - 1] = 'w'
maze[starting_height][starting_width + 1] = 'w'
maze[starting_height + 1][starting_width] = 'w'

while (walls):
    # Pick a random wall
    rand_wall = walls[int(random.random()*len(walls))-1]

    # Check if it is a left wall
    if (rand_wall[1] != 0):
        if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
            # Find the number of surrounding cells
            s_cells = surroundingCells(rand_wall)

            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                # Upper cell
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])


                # Bottom cell
                if (rand_wall[0] != height-1):
                    if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]+1, rand_wall[1]])

                # Leftmost cell
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                    if ([rand_wall[0], rand_wall[1]-1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]-1])
            

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Check if it is an upper wall
    if (rand_wall[0] != 0):
        if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

            s_cells = surroundingCells(rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                # Upper cell
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])

                # Leftmost cell
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                    if ([rand_wall[0], rand_wall[1]-1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]-1])

                # Rightmost cell
                if (rand_wall[1] != width-1):
                    if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                    if ([rand_wall[0], rand_wall[1]+1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]+1])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Check the bottom wall
    if (rand_wall[0] != height-1):
        if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

            s_cells = surroundingCells(rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                if (rand_wall[0] != height-1):
                    if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]+1, rand_wall[1]])
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]-1] = 'w'
                    if ([rand_wall[0], rand_wall[1]-1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]-1])
                if (rand_wall[1] != width-1):
                    if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                    if ([rand_wall[0], rand_wall[1]+1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]+1])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)


            continue

    # Check the right wall
    if (rand_wall[1] != width-1):
        if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

            s_cells = surroundingCells(rand_wall)
            if (s_cells < 2):
                # Denote the new path
                maze[rand_wall[0]][rand_wall[1]] = 'c'

                # Mark the new walls
                if (rand_wall[1] != width-1):
                    if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
                        maze[rand_wall[0]][rand_wall[1]+1] = 'w'
                    if ([rand_wall[0], rand_wall[1]+1] not in walls):
                        walls.append([rand_wall[0], rand_wall[1]+1])
                if (rand_wall[0] != height-1):
                    if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]+1][rand_wall[1]] = 'w'
                if ([rand_wall[0]+1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]+1, rand_wall[1]])
                if (rand_wall[0] != 0):	
                    if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
                        maze[rand_wall[0]-1][rand_wall[1]] = 'w'
                    if ([rand_wall[0]-1, rand_wall[1]] not in walls):
                        walls.append([rand_wall[0]-1, rand_wall[1]])

            # Delete wall
            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

            continue

    # Delete the wall from the list anyway
    for wall in walls:
        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
            walls.remove(wall)



# Mark the remaining unvisited cells as walls
for i in range(0, height):
    for j in range(0, width):
        if (maze[i][j] == 'u'):
            maze[i][j] = 'w'

# Set entrance and exit
for i in range(0, width):
    if (maze[1][i] == 'c'):
        maze[0][i] = 'f'
        break

for i in range(width-1, 0, -1):
    if (maze[height-2][i] == 'c'):
        maze[height-1][i] = 'p'
        pin = maze[height-1][i]
        break
    
# Print final maze
printMaze(maze)

#we will determine what turns it on 
on = True 


def on_press(key):
    done = False
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['up', 'down', 'left', 'right']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        print('Key pressed: ' + k)
        if(k == 'up'):
            # Mark the remaining unvisited cells as walls
            for i in range(0, height):
                for j in range(0, width):
                    if (maze[i][j] == 'p' and i > 0):
                        if(maze[i-1][j] == 'w'):
                            print("cannot move up")
                        else:
                            if(maze[i-1][j] == 'f'):
                                done = True
                            maze[i][j] = 'c'
                            maze[i-1][j] = 'p'
        if(k == 'down'):
             # Mark the remaining unvisited cells as walls
            for i in range(0, height):
                for j in range(0, width):
                    if (maze[i][j] == 'p' and i < height-1):
                        if(maze[i+1][j] == 'w'):
                            print("cannot move down")
                        else:
                            maze[i][j] = 'c'
                            maze[i+1][j] = 'p'
        
        if(k == 'left'):
             # Mark the remaining unvisited cells as walls
            for i in range(0, height):
                for j in range(0, width):
                    if (maze[i][j] == 'p' and j < width-1):
                        if(maze[i][j-1] == 'w'):
                            print("cannot move left")
                        else:
                            maze[i][j] = 'c'
                            maze[i][j-1] = 'p'
        
        if(k == 'right'):
          # Mark the remaining unvisited cells as walls
            for i in range(0, height):
                for j in range(0, width):
                    if (maze[i][j] == 'p' and j > 0):
                        if(maze[i][j+1] == 'w'):
                            print("cannot move right")
                        else:
                            maze[i][j] = 'c'
                            maze[i][j+1] = 'p'
        if(done):
            printMazeDone(maze)
        else: 
            # Print final maze
            printMaze(maze)
        return False  # stop listener; remove this if want more keys

while(on):
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join() 
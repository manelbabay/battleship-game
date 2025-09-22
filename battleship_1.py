# -----------------------------------------------------------------------------------------------------------------------------
#                                                     Importing the NumPy library
# -----------------------------------------------------------------------------------------------------------------------------
# We chose to import NumPy to handle our grid as a matrix to store the ships,
# and to generate random numbers for placing the computer's ships.

import numpy as np

# -----------------------------------------------------------------------------------------------------------------------------
#                                             Overview of the functions we will use
# -----------------------------------------------------------------------------------------------------------------------------

def initializeGrid(): 
    # This function initializes the computer's grid as a 10x10 matrix filled with zeros.
    grid = np.zeros((10,10))
    return grid

  
def displayGrid(grid):
    # This function displays a matrix as a grid with labels
    print(" ", np.arange(1,11,1))  # Display column names
    for i in range(10):
        print(chr(65+i), "|", end=' ')  # Display row letters (A to J)
        for j in range(10):
            if grid[i, j] == 10:
                print("*", end=' |')  # Water that has been hit
            elif -5 <= grid[i, j] < 0:
                print("+", end=' |')  # Ship that has been hit
            elif grid[i, j] <= -10:
                print("x", end=' |')  # Ship that has been sunk
            else:
                print(" ", end=' |')  # Unplayed cell
        print(" ")


def placeShips(grid, size):
    # This function places a ship of a given size randomly on the grid
    ship_placed = False
    
    while not ship_placed:
        i = np.random.randint(0, 10)  # Random row
        j = np.random.randint(0, 10)  # Random column
        orientation = np.random.randint(0, 2)  # 0: horizontal, 1: vertical

        if orientation == 0:  # Horizontal
            if j + size <= 10 and np.all(grid[i, j:j + size] == 0):
                grid[i, j:j + size] = size
                ship_placed = True
        else:  # Vertical
            if i + size <= 10 and np.all(grid[i:i + size, j] == 0):
                grid[i:i + size, j] = size
                ship_placed = True


def alreadyPlayed(i, j, grid):
    # This function checks if a cell has already been played
    if grid[i, j] < 0 or grid[i, j] == 10:
        return True
    return False


def play(grid, i, j, sunk_ships):
    # This function marks the played cell and checks if a ship has been hit or sunk
    ship_value = grid[i, j]
    if ship_value != 0:
        print("Hit!")
        grid[i, j] = -ship_value
        if ship_value not in grid:
            sunk_ships += 1
            for k in range(10):
                for l in range(10):
                    if grid[k, l] == -ship_value:
                        grid[k, l] *= 10  # Mark as sunk
            print("Sunk!")
    else:
        print("Miss.")
        grid[i, j] = 10  # Mark water
    return sunk_ships


def startGame():
    # Displays the intro message
    print("              ------------------------------------------------")
    print("              - Welcome to Battleship: Version 1 -")
    print("              ------------------------------------------------\n")
    print("\nYou will be playing against the computer. The rules are:")
    print("- The computer has placed its ships horizontally or vertically on the grid.")
    print("\nThere are five ships in total:")
    print("- 1 Aircraft Carrier (5 cells)\n- 1 Cruiser (4 cells)\n- 1 Destroyer (3 cells)\n- 1 Submarine (2 cells)\n- 1 Boat (1 cell)\n")
    print("At the end of the game, your accuracy will be shown.")
    print("\nYou are now ready to play. Good luck!\n")

# -----------------------------------------------------------------------------------------------------------------------------
#                                                      Main Program
# -----------------------------------------------------------------------------------------------------------------------------

computerGrid = initializeGrid()

# Place all 5 ships of increasing size
for ship_size in range(1, 6):
    placeShips(computerGrid, ship_size)
    
sunk_ships = 0
total_moves = 0

startGame()
displayGrid(computerGrid)

while sunk_ships != 5:
    print("Which cell do you want to play?")
    row_letter = input("Row (A-J): ")
    if len(row_letter) != 1:
        print("Error: Please enter only one character for the row (A to J).")
        row_letter = input("Row (A-J): ")  # Assuming the second attempt is correct
    row = ord(row_letter.upper()) - 65
    col = int(input("Column (1-10): ")) - 1
    
    if 0 <= row < 10 and 0 <= col < 10 and not alreadyPlayed(row, col, computerGrid):
        total_moves += 1
        sunk_ships = play(computerGrid, row, col, sunk_ships)
        displayGrid(computerGrid)
    else:
        print("Invalid coordinates! Please enter a letter from A to J for rows and a number from 1 to 10 for columns.")

print(f"Congratulations! You won in {total_moves} moves, giving you an accuracy of {15 * 100 / total_moves:.2f}%.")

if total_moves <= 50:
    print("Impressive! Try a harder challenge with a more advanced version.")
    print("Face the computer to find its ships before it destroys yours!")
else:
    print("Not bad! With a bit more practice, you'll improve your strategy even further.")

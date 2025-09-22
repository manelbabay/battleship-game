# -----------------------------------------------------------------------------------------------------------------------------
#                                                     Importing NumPy library
# -----------------------------------------------------------------------------------------------------------------------------
# We chose to import NumPy to manipulate our grid as a matrix to store our ships.
# Also to generate random numbers to place the computer's ships.
import numpy as np

# -----------------------------------------------------------------------------------------------------------------------------
#                                             Presentation of the various functions used
# -----------------------------------------------------------------------------------------------------------------------------

def initializeGrid():
    # This function initializes the computer's or player's grid
    # It creates a 10x10 matrix (size of the grid) filled with zeros.
    grid = np.zeros((10,10))
    return grid


def displayPlayerGrid(grid):
    # This function displays the player's grid, including their own ships.
    print(" ", np.arange(1, 11, 1))  # Display column numbers
    for i in range(10):
        print(chr(65+i), "|", end=' ')  # Display row letters (A-J)
        for j in range(10):
            if grid[i, j] == 5:
                print("A", end=' |')  # Aircraft Carrier
            elif grid[i, j] == 4:
                print("C", end=' |')  # Cruiser
            elif grid[i, j] == 3:
                print("D", end=' |')  # Destroyer
            elif grid[i, j] == 2:
                print("S", end=' |')  # Submarine
            elif grid[i, j] == 1:
                print("B", end=' |')  # Boat
            elif -5 <= grid[i, j] < 0:
                print("+", end=' |')  # Hit ship part
            elif grid[i, j] <= -10:
                print("x", end=' |')  # Sunk ship
            elif grid[i, j] == 10:
                print("*", end=' |')  # Missed shot
            else:
                print(" ", end=' |')
        print(" ")


def displayComputerGrid(grid):
    # This function displays the computer's grid (ships are hidden)
    print(" ", np.arange(1, 11, 1))
    for i in range(10):
        print(chr(65+i), "|", end=' ')
        for j in range(10):
            if grid[i, j] == 10:
                print("*", end=' |')  # Missed shot
            elif -5 <= grid[i, j] < 0:
                print("+", end=' |')  # Hit ship part
            elif grid[i, j] <= -10:
                print("x", end=' |')  # Sunk ship
            else:
                print(" ", end=' |')
        print(" ")


def placePlayerShip(grid, size):
    # Function that allows the player to place their ships manually
    ship_placed = False  
    while not ship_placed:
        row_letter = input("Row (A-J): ")
        if len(row_letter) != 1:
            print("Error: Please enter only one character for the row (A-J).")
            row_letter = input("Row (A-J): ")
        i = ord(row_letter.upper()) - 65
        j = int(input("Column (1-10): ")) - 1
        p = int(input("Horizontal (0) / Vertical (1): "))

        if p == 0:  # Horizontal
            if j + size <= 10 and np.all(grid[i, j:j + size] == 0):
                grid[i, j:j + size] = size
                ship_placed = True
        else:  # Vertical
            if i + size <= 10 and np.all(grid[i:i + size, j] == 0):
                grid[i:i + size, j] = size
                ship_placed = True


def placeComputerShip(grid, size):
    # Same as placePlayerShip, but random for the computer
    ship_placed = False
    while not ship_placed:
        i = np.random.randint(0, 10)
        j = np.random.randint(0, 10)
        p = np.random.randint(0, 2)

        if p == 0:  # Horizontal
            if j + size <= 10 and np.all(grid[i, j:j + size] == 0):
                grid[i, j:j + size] = size
                ship_placed = True
        else:  # Vertical
            if i + size <= 10 and np.all(grid[i:i + size, j] == 0):
                grid[i:i + size, j] = size
                ship_placed = True


def play(grid, i, j, ships_sunk):
    # Handles the logic when a shot is played on a grid
    value = grid[i, j]
    if value != 0:  # Ship was hit
        print("Hit!")
        grid[i, j] = -value
        if value not in grid:
            ships_sunk += 1
            for x in range(10):
                for y in range(10):
                    if grid[x, y] == -value:
                        grid[x, y] *= 10  # Mark as sunk
            print("Sunk!")
    else:
        print("Miss.")
        grid[i, j] = 10
    return ships_sunk


def alreadyPlayed(i, j, grid):
    # Checks if the cell has already been played
    return grid[i, j] < 0 or grid[i, j] == 10


def startGame():
    # Display the intro to the game
    print("              ------------------------------------------------")
    print("              - Welcome to Battleship: Version 2 -")
    print("              ------------------------------------------------\n")
    print("You will face off against the computer. The rules are:\n")
    print("- The computer has placed its ships randomly, horizontally or vertically.")
    print("- You can also place your ships horizontally or vertically.")
    print("- Just enter the row, column, and direction, and your ship will be placed.\n")
    print("There are five ships:\n")
    print("- 1 Aircraft Carrier (5 cells)")
    print("- 1 Cruiser (4 cells)")
    print("- 1 Destroyer (3 cells)")
    print("- 1 Submarine (2 cells)")
    print("- 1 Boat (1 cell)\n")
    print("Note: Ships cannot overlap!\n")
    print("At the end of the game, your score and hit rate will be shown.\n")
    print("You're ready to play, good luck!\n")


# -----------------------------------------------------------------------------------------------------------------------------
#                                                      Main Program
# -----------------------------------------------------------------------------------------------------------------------------

PlayerGrid = initializeGrid()
ComputerGrid = initializeGrid()

for i in range(1, 6):
    placeComputerShip(ComputerGrid, i)

startGame()
displayPlayerGrid(PlayerGrid)

for i in range(1, 6):
    print(f"Now place your ship of size {i}")
    placePlayerShip(PlayerGrid, i)
    displayPlayerGrid(PlayerGrid)

sunk_player = 0
sunk_computer = 0
shots = 0

print("Great! The grids are ready. The game can begin.")

while sunk_player != 5 and sunk_computer != 5:

    # COMPUTER'S TURN
    played = False
    while not played:
        i_comp = np.random.randint(0, 10)
        j_comp = np.random.randint(0, 10)
        if not alreadyPlayed(i_comp, j_comp, PlayerGrid):
            print("\nPlayer's Grid:")
            sunk_computer = play(PlayerGrid, i_comp, j_comp, sunk_computer)
            displayPlayerGrid(PlayerGrid)
            played = True

    # PLAYER'S TURN
    played = False
    while not played:
        print("\nComputer's Grid:")
        displayComputerGrid(ComputerGrid)
        print("Which cell would you like to shoot?")
        row_letter = input("Row (A-J): ")
        if len(row_letter) != 1:
            print("Error: Please enter only one character for the row (A-J).")
            row_letter = input("Row (A-J): ")
        i = ord(row_letter.upper()) - 65
        j = int(input("Column (1-10): ")) - 1
        if 0 <= i < 10 and 0 <= j < 10 and not alreadyPlayed(i, j, ComputerGrid):
            sunk_player = play(ComputerGrid, i, j, sunk_player)
            played = True
            displayComputerGrid(ComputerGrid)
        else:
            print("Invalid coordinates! Please enter valid values between A-J and 1-10.")

    shots += 1


# FINAL RESULTS
if sunk_player > sunk_computer:
    print("Congratulations! You won!")
    print(f"Score: {sunk_player} (You) - {sunk_computer} (Computer)")
    print(f"Your hit accuracy: {15 * 100 / shots:.2f}%")
    print("Great job! Maybe you're ready for an even more challenging version.")

elif sunk_player < sunk_computer:
    print("You lost! Try again, and maybe you'll have better luck.")
    print(f"Score: {sunk_computer} (Computer) - {sunk_player} (You)")
    print(f"Computer's hit accuracy: {15 * 100 / shots:.2f}%")

else:
    print("It's a tie! Try again to break the deadlock.")
    print(f"Score: {sunk_computer} (Computer) - {sunk_player} (You)")
    print(f"Hit accuracy: {15 * 100 / shots:.2f}%")

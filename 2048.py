import random

# Constants
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
# Initialize the grid
grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

# Add a random starting tile
grid[random.randint(0, 3)][random.randint(0, 3)] = 2

def print_grid():
  """Print the current state of the grid"""
  for row in grid:
    print(row)

def move(direction):
  """Move the tiles in the specified direction"""
  global grid
  move_counter = 0
  
  if direction == UP:

    def slideUp(col):
      nonlocal move_counter
      # Start at the top and work down
      current_row = 0
      # Move to first empty row
      while current_row < 4 and grid[current_row][col] != 0:
        current_row += 1
      # Slide tiles
      for row in range(4):
        # Skip empty tiles
        if grid[row][col] == 0:
          continue
        # Slide tile up as far as possible
        while current_row < row:
          move_counter += 1
          grid[current_row][col] = grid[row][col]
          grid[row][col] = 0
          current_row += 1

    # Move tiles up
    for col in range(4):
      slideUp(col)
      # Merge tiles up
      for row in range(1, 4):
        if grid[row][col] != 0 and grid[row][col] == grid[row-1][col]:
          move_counter += 1
          grid[row-1][col] *= 2
          grid[row][col] = 0
      slideUp(col)

  elif direction == RIGHT:

    def slideRight(row):
      nonlocal move_counter
      # Start at the right and work left
      current_col = 3
      # Move to first empty column
      while current_col >= 0 and grid[row][current_col] != 0:
        current_col -= 1
      for col in range(3, -1, -1):
        # Skip empty tiles
        if grid[row][col] == 0:
          continue
        # Slide tile right as far as possible
        while current_col > col:
          move_counter += 1
          grid[row][current_col] = grid[row][col]
          grid[row][col] = 0
          current_col -= 1

    # Move tiles right
    for row in range(4):
      slideRight(row)
      # Merge tiles right
      for col in range(2, -1, -1):
        if grid[row][col] != 0 and grid[row][col] == grid[row][col+1]:
          move_counter += 1
          grid[row][col+1] *= 2
          grid[row][col] = 0
      slideRight(row)
          
  elif direction == DOWN:

    def slideDown(col):
      nonlocal move_counter
      # Start at the bottom and work up
      current_row = 3
      # Move to first empty row
      while current_row >= 0 and grid[current_row][col] != 0:
        current_row -= 1
      for row in range(3, -1, -1):
        # Skip empty tiles
        if grid[row][col] == 0:
          continue
        # Slide tile down as far as possible
        while current_row > row:
          move_counter += 1
          grid[current_row][col] = grid[row][col]
          grid[row][col] = 0
          current_row -= 1

    # Move tiles down
    for col in range(4):
      slideDown(col)
      # Merge tiles down
      for row in range(2, -1, -1):
          if grid[row][col] != 0 and grid[row][col] == grid[row+1][col]:
              move_counter += 1
              grid[row+1][col] *= 2
              grid[row][col] = 0
      slideDown(col)

  elif direction == LEFT:

    def slideLeft(row):
      nonlocal move_counter
      # Start at the left and work right
      current_col = 0
      # move to first empty column
      while current_col < 4 and grid[row][current_col] != 0:
        current_col += 1
      for col in range(4):
        # Skip empty tiles
        if grid[row][col] == 0:
          continue
        # Slide tile left as far as possible
        while current_col < col:
          move_counter += 1
          grid[row][current_col] = grid[row][col]
          grid[row][col] = 0
          current_col += 1

    # Move tiles left
    for row in range(4):
      slideLeft(row)
      # Merge tiles
      for col in range(3):
        if grid[row][col] != 0 and grid[row][col] == grid[row][col+1]:
          move_counter += 1
          grid[row][col] *= 2
          grid[row][col+1] = 0
      slideLeft(row)

  return move_counter

def game_over():
  """Determine if the game is over"""
  global grid
  
  # Check if there are any empty tiles
  for row in range(4):
    for col in range(4):
      if grid[row][col] == 0:
        return False
  
  # Check if any tiles can be merged
  for row in range(4):
    for col in range(4):
      if (row > 0 and grid[row][col] == grid[row-1][col]) or (col > 0 and grid[row][col] == grid[row][col-1]):
        return False
  
  return True

# Main game loop
while True:
  print_grid()
  
  move_counter = 0
  # Get player input
  key = input("Enter a direction (up, right, down, left): ")
  if key == "up":
    move_counter = move(UP)
  elif key == "right":
    move_counter = move(RIGHT)
  elif key == "down":
    move_counter = move(DOWN)
  elif key == "left":
    move_counter = move(LEFT)
  
  # Check if game is over
  if game_over():
    print("Game over!")
    break
  
  # Add a random tile
  while move_counter > 0:
    row = random.randint(0, 3)
    col = random.randint(0, 3)
    if grid[row][col] == 0:
      grid[row][col] = 2
      break
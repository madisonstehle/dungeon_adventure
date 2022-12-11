import random
from Room import Room

class Dungeon:
  """
  Dungeon Class:

  A class containing all attributes and methods pertaining to the creation of and management of the Dungeon class
  Interacts frequently with the Room class.

  • Contains Methods:
    o __init__
    o build_maze
    o print_maze_by_coords
    o print_room_rows
    o traverse
    o is_valid_room
    o get_room
    o clear_room
    o clear_pillars
    o draw_room_by_coord
  """
  def __init__(self, row_count, col_count, test_mode=False):
    """
    constructor __init__(self, row_count, col_count) that creates a new Dungeon object
      Attributes:
        - test_mode: boolean
        - __maze: list
        - __rowCount: int
        - __colCount: int

      parameters: row_count, col_count
      return: None
    """
    self.test_mode = test_mode
    self.__maze = []
    self.__rowCount = row_count
    self.__colCount = col_count

    for r in range(0, self.__rowCount):
      self.__maze.append([Room() for c in range(0, self.__colCount)])

    self.build_maze()

  def build_maze(self):
    """
    build_maze(self) that builds the maze by setting entrances/exits, pillars, and ensures those aren't impassible
      parameters: None
      return: None
    """
    if self.test_mode and self.__colCount > 3:
      self.__maze[0][0].set_entrance()
      self.__maze[0][0].set_impassible(False)

      self.__maze[0][1].polymorphism = True
      self.__maze[0][1].set_impassible(False)

      self.__maze[0][2].abstraction = True
      self.__maze[0][2].set_impassible(False)

      self.__maze[0][3].inheritence = True
      self.__maze[0][3].set_impassible(False)

      self.__maze[0][4].encapsulation = True
      self.__maze[0][4].set_impassible(False)

      self.__maze[0][5].set_exit()
      self.__maze[0][5].set_impassible(False)

    elif self.test_mode and self.__colCount == 2:
      self.__maze[0][0].set_entrance()
      self.__maze[0][0].set_impassible(False)
      self.__maze[0][1].clear_room()
      self.__maze[0][1].pit = True

    elif self.test_mode and self.__colCount == 1:
      self.__maze[0][0].set_entrance()
      self.__maze[0][0].set_impassible(False)

    else:
      for row in range(0, self.__rowCount):
        for col in range(0, self.__colCount):
          number = random.randint(1, 100)
          if number > 80:  # % chance a room is impassable
            self.__maze[row][col].set_impassible(True)

      # set entrance and exit
      self.__maze[0][0].set_entrance()
      self.__maze[0][0].set_impassible(False)
      self.__maze[self.__rowCount - 1][self.__colCount - 1].set_exit()
      self.__maze[self.__rowCount - 1][self.__colCount - 1].set_impassible(False)

      # place pillars after entrance/exit
      for i in range(0, 4):
        row = random.randint(0, self.__rowCount - 2)
        col = random.randint(0, self.__colCount - 2)

        while self.__maze[row][col].get_entrance() or self.__maze[row][col].is_exit() or self.__maze[row][col].polymorphism or self.__maze[row][col].abstraction or self.__maze[row][col].inheritence or self.__maze[row][col].encapsulation:
          row = random.randint(0, self.__rowCount - 2)
          col = random.randint(0, self.__colCount - 2)

        if i == 0:
          self.__maze[row][col].polymorphism = True
        if i == 1:
          self.__maze[row][col].abstraction = True
        if i == 2:
          self.__maze[row][col].inheritence = True
        if i == 3:
          self.__maze[row][col].encapsulation = True

        self.__maze[row][col].set_impassible(False)

      for row in range(0, self.__rowCount):
        for col in range(0, self.__colCount):
          if self.__maze[row][col].can_enter():
            number = random.randint(1, 100)
            if self.__maze[row][col].get_health_chance() >= number:
              self.__maze[row][col].set_health(True)

  def print_maze_by_coords(self):
    """
    print_maze_by_coords(self) that interacts with the Rooms in the dungeon to print out a string representation of the maze
      parameters: None
      return: None
    """
    room_list = []
    x = 0
    y = 0
    for row in range(0, self.__rowCount):
      for col in range(0, self.__colCount):
        room_list.append(self.__maze[row][col].show_room_by_coords(self, y, x))
        y += 1
      self.print_room_rows(room_list)
      room_list = []
      x += 1
      y = 0

  def print_room_rows(self, room_list):
    """
    print_room_rows(self, room_list) that takes a list of string components to be printed in rows
      parameters: room_list
      return: None
    """
    split_list = []

    for room in room_list:
      if room is not None:
        split_list.append(room.split("\n"))

    for layer in range(3):
      for room_pieces in split_list:
        print(room_pieces[layer], end=" ")
      print("")

  def traverse(self, row, col):
    """
    traverse(self, row, col) that determines whether or not a given maze is traversable when starting at a particular row/col coordinate
      parameters: row, col
      return: boolean
    """
    found_exit = False
    if self.is_valid_room(row, col):
      self.__maze[row][col].set_visited(True)
      # check for exit
      if self.__maze[row][col].is_exit():
        return True
      # not at exit so try another room: south, east, north, west
      found_exit = self.traverse(row + 1, col)  # south
      if not found_exit:
        found_exit = self.traverse(row, col + 1)  # east
      if not found_exit:
        found_exit = self.traverse(row - 1, col)  # north
      if not found_exit:
        found_exit = self.traverse(row, col - 1)  # west

      # if we did not reach the exit from this room we need mark it as visited to
      # avoid going into the room again
      if not found_exit:
        self.__maze[row][col].set_visited(True)

    else:  # tried to move into a room that is not valid
      return False
    return found_exit

  def is_valid_room(self, row, col):
    """
    is_valid_room(self, row, col) determines whether or not a given room by coordinates is in bounds and can be entered
      parameters: row, col
      return: boolean
    """
    return 0 <= row < self.__rowCount and col >= 0 and col < self.__colCount and self.__maze[row][col].can_enter()

  def get_room(self, row, col):
    """
    get_room(self, row, col) gets a Room by coordinates
      parameters: row, col
      return: Room object
    """
    if 0 <= row < self.__rowCount and col >= 0 and col < self.__colCount:
      return self.__maze[row][col]

  def clear_room(self, row, col):
    """
    clear_room(self, row, col) gets a Room by coordinates and uses a clear function found in Room on that object
      parameters: row, col
      return: None
    """
    if 0 <= row < self.__rowCount and col >= 0 and col < self.__colCount:
      self.__maze[row][col].clear_room()

  def clear_pillars(self, row, col):
    """
    clear_pillars(self, row, col) gets a Room by coordinates and uses a clear function found in Room on that object
      parameters: row, col
      return: None
    """
    if 0 <= row < self.__rowCount and col >= 0 and col < self.__colCount:
      self.__maze[row][col].clear_pillars()

  def draw_room_by_coord(self, x, y):
    """
    draw_room_by_coord(self, x, y) gets a Room by coordinates and returns a string representation of that room
      parameters: x, y
      return: String
    """
    if 0 <= x < self.__rowCount and y >= 0 and y < self.__colCount:
      return self.__maze[x][y].show_room_by_coords(self, x, y)

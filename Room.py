import random

class Room:
    """
    Room Class:

    A class containing all attributes and methods pertaining to the creation of and management of the Room class
    Interacts frequently with the Dungeon class.

      • Contains Methods:
        o __init__
        o show_room_by_coords
        o get_health_chance
        o set_health
        o can_move_to
        o can_enter
        o is_exit
        o set_visited
        o set_entrance
        o get_entrance
        o set_impassible
        o set_exit
        o roll_for_content
        o clear_room
        o clear_pillars
        o get_room_content
    """
    def __init__(self):
        """
        constructor __init__(self) that creates a new Room object
          Attributes:
            - roll_content: int
            - __healthChance: int
            - healthPotion: boolean
            - visionPotion: boolean
            - multiPotion: boolean
            - pit: boolean
            - polymorphism: boolean
            - abstraction: boolean
            - encapsulation: boolean
            - inheritence: boolean
            - __exit: boolean
            - __impassable: boolean
            - __visited: boolean
            - __entrance: boolean

          parameters: name
          return: None
        """
        self.roll_content = random.randint(1, 9)
        self.__healthChance = random.randint(10, 50)

        self.healthPotion = False
        self.visionPotion = False
        self.multiPotion = False
        self.pit = False
        self.polymorphism = False
        self.abstraction = False
        self.encapsulation = False
        self.inheritence = False

        self.__exit = False
        self.__impassable = False
        self.__visited = False
        self.__entrance = False

        self.roll_for_content()

    def show_room_by_coords(self, dungeon, x, y):
        """
        show_room_by_coords(self, dungeon, x, y) that creates a room string that can be printed to represent the room

          parameters: dungeon, x, y
          return: String
        """
        can_move_north = dungeon.get_room(x, y - 1) is not None and dungeon.get_room(x, y - 1).can_move_to()
        can_move_south = dungeon.get_room(x, y + 1) is not None and dungeon.get_room(x, y + 1).can_move_to()
        can_move_west = dungeon.get_room(x - 1, y) is not None and dungeon.get_room(x - 1, y).can_move_to()
        can_move_east = dungeon.get_room(x + 1, y) is not None and dungeon.get_room(x + 1, y).can_move_to()

        room_content = self.get_room_content()
        room_str = ""

        if can_move_north:
            room_str += "* - *\n"
        else:
            room_str += "* * *\n"

        if can_move_east and can_move_west:
            room_str += f"| {room_content} |\n"
        elif not can_move_east and can_move_west:
            room_str += f"| {room_content} *\n"
        elif can_move_east and not can_move_west:
            room_str += f"* {room_content} |\n"
        else:
            room_str += f"* {room_content} *\n"

        if can_move_south:
            room_str += "* - *\n"
        else:
            room_str += "* * *\n"

        return room_str

    def get_health_chance(self):
        """
        get_health_chance(self) that returns the __healthChance attribute

          parameters: None
          return: int
        """
        return self.__healthChance

    def set_health(self, add_potion):
        """
        set_health(self, add_potion) that sets the value of the healthPotion attribute

          parameters: add_potion
          return: None
        """
        self.healthPotion = add_potion

    def can_move_to(self):
        """
        can_move_to(self) that returns the opposite of boolean value of __impassable attribute

          parameters: None
          return: boolean
        """
        return not self.__impassable

    def can_enter(self):
        """
        can_enter(self) that returns the opposite of boolean value of __impassable attribute and __visited

          parameters: None
          return: boolean
        """
        return not self.__impassable and not self.__visited

    def is_exit(self):
        """
        is_exit(self) that returns the boolean value of __exit

          parameters: None
          return: boolean
        """
        return self.__exit

    def set_visited(self, visited):
        """
        set_visited(self, visited) that sets the boolean value of __visited

          parameters: visited
          return: None
        """
        self.__visited = visited

    def set_entrance(self):
        """
        set_entrance(self) that sets the boolean value of __entrance to True

          parameters: None
          return: None
        """
        self.__entrance = True

    def get_entrance(self):
        """
        get_entrance(self) that gets the boolean value of __entrance

          parameters: None
          return: boolean
        """
        return self.__entrance

    def set_impassible(self, is_impassable):
        """
        set_impassible(self, is_impassable) that sets the boolean value of __impassable

          parameters: is_impassable
          return: None
        """
        self.__impassable = is_impassable

    def set_exit(self):
        """
        set_exit(self) that sets the boolean value of __exit to True

          parameters: None
          return: None
        """
        self.__exit = True

    def roll_for_content(self):
        """
        roll_for_content(self) that sets the boolean value of several attributes to determine what is in the room

          parameters: None
          return: None
        """
        if self.roll_content == 1:
            self.healthPotion = True
        if self.roll_content == 2:
            self.visionPotion = True
        if self.roll_content == 3:
            self.multiPotion = True
        if self.roll_content == 4:
            self.pit = True

    def clear_room(self):
        """
        clear_room(self) that sets the boolean value of several attributes to false

          parameters: None
          return: None
        """
        self.healthPotion = False
        self.visionPotion = False
        self.multiPotion = False

    def clear_pillars(self):
        """
        clear_pillars(self) that sets the boolean value of several attributes to false

          parameters: None
          return: None
        """
        self.polymorphism = False
        self.abstraction = False
        self.encapsulation = False
        self.inheritence = False

    def get_room_content(self):
        """
        get_room_content(self) that gets the attributes that are in the room and returns a string representation of the contents

          parameters: None
          return: String
        """
        if self.__entrance or self.__exit:
            self.clear_room()
            self.pit = False

        if self.polymorphism or self.encapsulation or self.inheritence or self.abstraction:
            self.clear_room()
            self.pit = False

        if self.healthPotion:
            return "H"
        if self.visionPotion:
            return "V"
        if self.multiPotion:
            return "M"
        if self.pit:
            return "X"
        if self.polymorphism:
            return "P"
        if self.encapsulation:
            return "E"
        if self.abstraction:
            return "A"
        if self.inheritence:
            return "I"
        if self.__entrance:
            return "i"
        if self.__exit:
            return "O"
        else:
            return " "  # empty room




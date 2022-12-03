class Room:
    """
    • Contains default constructor and all methods you deem necessary -- modular design is CRUCIAL
    • Contains the following items/behaviors
        o (Possibly a) Healing Potion - heals 5-15 hit points (this amount will be randomly generated -- you can modify the
        range)
        o (Possibly a) Pit - damage a pit can cause is from 1-20 hit points (this amount will be randomly generated - you can
        modify the range)
        o (Possibly an) Entrance - only one room will have an entrance and the room that contains the entrance will contain
        NOTHING else
        o (Possibly an) Exit - only one room will have an exit and the room that contains the exit will contain NOTHING
        else
        o (Possibly a) Pillar of OO - four pillars in game and they will never be in the same room
        o Doors - N, S, E, W
        o 10% possibility (this is a constant that you can modify) room will contain a healing potion, vision potion, and pit
        (each of these are independent of one another)
        o Vision Potion - can be used to allow user to see eight rooms surrounding current room as well as current room
        (location in maze may cause less than 8 to be displayed)

    Example: Room 1,1 might look like
    * - *
    | P |
    * - *
    Room 0,0 might look like
    * * *
    * E |
    * - *
    """

    def __init__(self):
        self.__healthPotion = False
        self.__visionPotion = False
        self.__pillar = "No pillar"
        self.__pit = False
        self.__exit = False
        self.__entrance = False
        self.__impassable = False
        self.__visited = False
        self.__healthChance = 50

    def __str__(self):
        """
        a _ _ str _ _ () method that builds a 2D Graphical representation of the room (NOTE: you may use any
        graphical components that you wish). The (command line) representation is as follows:
          o * - * will represent a north/south door (the - represents the door). If the room is on a boundary of the maze (upper
          or lower), then that will be represented with ***
          o East/west doors will be represented in a similar fashion with the door being the | character as opposed to a -.
          o In the center of the room you will display a letter that represents what the room contains. Here are the letters to use
          and what they represent:
              ▪ M - Multiple Items
              ▪ X - Pit
              ▪ i - Entrance (In)
              ▪ O - Exit (Out)
              ▪ V - Vision Potion
              ▪ H - Healing Potion
              ▪ <space> - Empty Room
              ▪ A, E, I, P - Pillars
        """
        item_count = 0
        if self.__healthPotion:
            item_count += 1
        if self.__visionPotion:
            item_count += 1

        if item_count > 1:
            return "M"

        # return "Health potion: " + str(self.__healthPotion) + "\n" \
        #        + "Vision potion: " + str(self.__visionPotion) + "\n" \
        #        + "Pillar: " + str(self.__pillar) + "\n" \
        #        + "Pit: " + str(self.__pit) + "\n" \
        #        + "Impassable: " + str(self.__impassable) + "\n" \
        #        + "Entrance: " + str(self.__entrance) + "\n" \
        #        + "Exit: " + str(self.__exit) + "\n\n"
        if self.__healthPotion:
            return "H"
        if self.__visionPotion:
            return "V"
        if self.__pit:
            return "X"
        if self.__pillar:
            # Just gonna do this for now, but will need to actually show the right pillar from the list
            return "P"
        if self.__entrance:
            return "I"
        if self.__exit:
            return "O"

        return " "

    def get_health_chance(self):
        return self.__healthChance

    def set_health(self, add_potion):
        self.__healthPotion = add_potion

    def can_move_to(self):
        return not self.__impassable

    def can_enter(self):
        return not self.__impassable and not self.__visited

    def is_exit(self):
        return self.__exit

    def set_visited(self, visited):
        self.__visited = visited

    def set_entrance(self):
        self.__entrance = True

    def set_impassible(self, is_impassable):
        self.__impassable = is_impassable

    def set_exit(self):
        self.__exit = True


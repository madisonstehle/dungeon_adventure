"""
Dungeon
• Creates/contains a maze of Rooms
    o The maze should be randomly generated
        ▪ You must incorporate an algorithm to ensure traversal of the maze from entrance to exit is possible once the
        maze has been generated. If the maze is not traversable, then generate a new one
    o The maze should have ‘dead ends’ (places that lead no further)
    o The type of data structure you use to represent your maze is up to you
        ▪ A list of lists has some advantages
        ▪ A linked list of linked lists has other advantages
        ▪ You could represent your maze via rooms that have references to other rooms (this would be much like a
        linked list structure but without all the basic linked list functionality which you do not need for this
        assignment)
• Places the Entrance, the Exit, and the Pillars. NOTES: the entrance and exit are empty rooms. The Pillars cannot be at
the entrance or the exit. No two Pillars may be in the same room.
• (Possibly) Maintains location of the Adventurer in the Dungeon
• Contains a _ _ str _ _ () method that builds a String containing information about the entire dungeon.
"""
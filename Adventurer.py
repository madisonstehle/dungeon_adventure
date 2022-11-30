"""
Adventurer
• Has a name
• Contains at least the following:
    o Hit Points - initially set to 75 - 100 upon creation (randomly generate - you can change the range)
    o The number of Healing Potions
    o The number of Vision Potions
    o The which Pillars found
• Ability to move in Dungeon (you might decide to place this behavior elsewhere)
• Increases or decreases the Hit Points accordingly
• Contains a _ _ str _ _ () method that builds a String containing:
    o Name
    o Hit Points
    o Total Healing Potions
    o Total Vision Potions
    o List of Pillars Pieces Found

NOTE: The Adventurer and the Dungeon will need to interact. When the Adventurer walks into a room if there is a potion in
the room, the Adventurer automatically picks up the potion. Likewise if there is a pit in the room, the Adventurer automatically
falls in the pit and takes a Hit Point loss. These changes obviously affect the room. For example, the Adventurer walks into a
room that contains a Healing Potion. The Adventurer will pick up the potion, changing the Adventurer's potion total, as well as
changing the room's potion total.
"""
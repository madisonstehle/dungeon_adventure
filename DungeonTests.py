from Adventurer import Adventurer
from Dungeon import Dungeon

import unittest

class DungeonTests(unittest.TestCase):
    def test_viable_dungeon(self):
        valid = False
        dungeon = None

        while not valid:
            dungeon = Dungeon(4, 4)

            if dungeon.traverse(0, 0):
                valid = True

        self.assertEqual(True, valid, "valid dungeon not created")

    def test_nonviable_dungeon(self):
        valid = True
        dungeon = None

        while valid:
            dungeon = Dungeon(4, 4)

            if not dungeon.traverse(0, 0):
                valid = False

        self.assertEqual(False, valid, "invalid dungeon not created")

    def test_losing(self):
        a = Adventurer("TestName")
        a.test_mode = True

        d = Dungeon(1, 2, True)

        north_room, south_room, west_room, east_room = a.available_rooms(d)

        a.move(north_room, south_room, west_room, east_room)

        self.assertEqual(a.name, 'TestName', 'a.name was not TestName')
        self.assertLessEqual(a.hit_points, 0, 'a.hit_points were not less than or equal to 0 after taking more damage than available hit points')
        self.assertEqual(False, a.alive, "adventurer.alive not false when player dies")

    def test_winning(self):
        a = Adventurer("TestName")
        a.test_mode = True

        d = Dungeon(1, 6, True)

        i = 0
        while i < 5:
            print(a.x, a.y)
            north_room, south_room, west_room, east_room = a.available_rooms(d)
            a.move(north_room, south_room, west_room, east_room)
            i += 1

        self.assertEqual(False, a.alive, "adventurer.alive not false when game ends")
        self.assertEqual("P", a.pillar_pieces_found[0], "adventurer doesn't have the P pillar before game ends")
        self.assertEqual("A", a.pillar_pieces_found[1], "adventurer doesn't have the A pillar before game ends")
        self.assertEqual("I", a.pillar_pieces_found[2], "adventurer doesn't have the I pillar before game ends")
        self.assertEqual("E", a.pillar_pieces_found[3], "adventurer doesn't have the E pillar before game ends")

    def test_healing_potion(self):
        a = Adventurer("TestName")
        a.test_mode = True
        a.hit_points = 100
        a.healing_potions = 2

        d = Dungeon(1, 1, True)
        north_room, south_room, west_room, east_room = a.available_rooms(d)
        a.move(north_room, south_room, west_room, east_room)

        self.assertGreater(a.hit_points, 100, "after taking a healing potion, adventurer's hit points were not increased")
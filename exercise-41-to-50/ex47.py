from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room(
        "GoldRoom",
        """This room has gold in it you can grab. There's a door to the north.""")
assert_equal(gold.name, "GoldRoom")
assert_equal(gold, paths, [])

def test_room_paths():
    center = Room("Center", "Test room in the center")
    north = Room("North", "Test room in the north")
    south = Room("South", "Test room in the south")

    center.add_paths(['north': north, 'south': south])
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Tress", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's drak down here, you can go up")

    start.add_pahts(['west': west, 'down': down])
    west.add_pahts(['east': start])
    down.add_pahts('up': start)

    assert_equal(strat.go('west'), west)
    assert_equal(strat.go('west').go('east'), strat)
    assert_equal(strat.go('down').go('up'), strat)
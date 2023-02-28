# This file is a class for a tile in the mines game

"""
Defines Tile class and constants that are used to simulate a tile in a mines game

Constants:
    * tile.BLANK = 0
    * tile.MINE = -1

Public objects:
    * Enum tile.State
    * Class tile.Tile
"""

from enum import Enum, auto

BLANK = 0
_BLANK_CHAR = ' ' # '\u25A1'
_COVERED = '\u25A8'
_FLAG = '\u2690'
_UNKNOWN = '?'
_MINE_CHAR = '\u2737'
MINE = -1


class State(Enum):
    """
This enum describes the state of the tile

Constants:
 * covered
 * flag
 * unknown
 * visible
    """
    covered = auto()
    flag = auto()
    unknown = auto()
    visible = auto()


class Tile:
    """
defines a Tile in a game of mines

self.is_blank(self) -> bool:     returns true if this tile has no number or mine
self.is_mine(self) -> bool:      returns true if this tile is a mine
self.get_value(self) -> int:     returns the value of the tile (1-8), (-1 for mine), (0 for blank)
self.set_value(self, v: int):    sets the value of the tile. Raises Exception if the tile value is not valid
    """

    def __init__(self):
        self._value = BLANK
        self.state = State.covered

    def is_blank(self) -> bool:
        return self._value == BLANK

    def is_mine(self) -> bool:
        return self._value == MINE

    def get_value(self) -> int:
        return self._value

    def set_value(self, v: int):
        if -1 <= v <= 8:
            self._value = v
        else:
            raise Exception("Value is not valid: v = " + str(v))

    def __str__(self):
        if self.state == State.covered:
            return _COVERED
        elif self.state == State.visible:
            if self.is_mine():
                return _MINE_CHAR
            if self._value == 0:
                return _BLANK_CHAR
            if 0 < self._value < 9:
                return str(self._value)
            else:
                raise Exception("Tile value is not valid")
        elif self.state == State.flag:
            return _FLAG
        elif self.state == State.unknown:
            return _UNKNOWN


"""
Documentation for this module:
Introduction:
This is a Python module that defines a Tile class and some constants which can be used to simulate a tile in a minesweeper game. The module provides a public State enumeration and a Tile class, which can be used to represent the state of a tile and perform operations on the tile.

Constants:
The module defines the following constants:

BLANK: An integer constant that represents a blank tile in the game.
_BLANK_CHAR: A string constant that represents the character to be displayed for a blank tile.
_COVERED: A string constant that represents the character to be displayed for a covered tile.
_FLAG: A string constant that represents the character to be displayed for a flagged tile.
_UNKNOWN: A string constant that represents the character to be displayed for a tile whose state is unknown.
_MINE_CHAR: A string constant that represents the character to be displayed for a mine tile.
MINE: An integer constant that represents a mine tile in the game.
Public objects:
The module provides the following public objects:

Enum tile.State: An enumeration that defines the state of a tile. It has four constants:
covered: A tile that is covered.
flag: A tile that is flagged.
unknown: A tile whose state is unknown.
visible: A tile that is visible.
Class tile.Tile: A class that defines a tile in the game. It has the following methods:
is_blank(self) -> bool: Returns True if the tile is blank.
is_mine(self) -> bool: Returns True if the tile is a mine.
get_value(self) -> int: Returns the value of the tile.
set_value(self, v: int): Sets the value of the tile. Raises an Exception if the value is not valid.
__str__(self): Returns a string representation of the tile based on its state.
Usage:
To use the module, you can import it and create instances of the Tile class to represent the tiles in your game. You can also use the State enumeration to represent the state of each tile. You can call the methods of the Tile class to get and set the value of the tile and check its type. You can also call the __str__ method to get a string representation of the tile based on its state.

Example usage:

```from minesweeper import Tile, State

# Create a tile and set its value to 5
tile = Tile()
tile.set_value(5)

# Print the value of the tile
print(tile.get_value())

# Print the string representation of the tile
print(str(tile))

# Set the state of the tile to 'flag'
tile.state = State.flag

# Print the string representation of the tile again
print(str(tile))
```
Output:

```
5
▨
⚑
```
"""
"""
The tile object in Wordle.

Tiles are essential components in any Wordle game. They provide players with
useful color-coded hints to increase their chances of guessing the hidden
word.
-------------------------------------------------------------------------------
  * `GREEN`  -- The character and its position are both correct.
  * `YELLOW` -- The character is correct but is in the wrong position.
  * `GRAY`   -- The character is not in the word at all.
  * `BLACK`  -- The character has not been used in a guess yet.
-------------------------------------------------------------------------------
Note that these color-codes serve to categorize the tile's accuracy and do not
necessarily imply visual representation in the game.

Author: Eggie
Version: 1.0.0
"""

__all__ = [
    'ColorCode', 'GREEN', 'YELLOW', 'GRAY', 'BLACK',
    'Tile'
]
__version__ = '1.0.0'


from typing import TypeAlias


ColorCode: TypeAlias = int
'A unique code representing a specific color. These codes are integer values.'

GREEN: ColorCode = 0
'The character and its position are both correct.'
YELLOW: ColorCode = 1
'The character is correct but is in the wrong position.'
GRAY: ColorCode = 2
'The character is not in the word at all.'
BLACK: ColorCode = 3
'The character has not been used in a guess yet.'


class Tile(object):
    """
    A `Tile` represents a character in a Wordle game, where each tile is
    assigned a color code that provides hints on the character's accuracy.
    ---------------------------------------------------------------------------
      * `GREEN`  -- The character and its position are both correct.
      * `YELLOW` -- The character is correct but is in the wrong position.
      * `GRAY`   -- The character is not in the word at all.
      * `BLACK`  -- The character has not been used in a guess yet.
    """

    def __init__(
        self,
        ch: str,
        color: ColorCode = BLACK
    ) -> None:
        """
        Initializes a tile object representing a character.

        :param ch: The character this tile represents.

        :param color: The color-code indicating the accuracy of the character
                      relative to the hidden word. Defaults to `BLACK`
                      indicating that the character has not been used yet.
        """
        self.ch = ch
        'The character this tile represents.'
        self.color = color
        'The color-code of this tile.'

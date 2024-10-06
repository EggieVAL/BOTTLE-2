"""
The tile object in Wordle.

Tiles are essential components in any Wordle game. They provide players with
useful color-coded hints to increase their chances of guessing the hidden
word.

Color-Codes
-----------
  * `GREEN`  -- The letter and its position are both correct.
  * `YELLOW` -- The letter is correct but is in the wrong position.
  * `GRAY`   -- The letter is not in the word at all.
  * `BLACK`  -- The letter has not been used in a guess yet.

Note that these color-codes serve to categorize the tile's status and do not
necessarily imply visual representation in the game.

Author: Eggie
Version: 1.0.0
"""

__all__ = [
    'GREEN', 'YELLOW', 'GRAY', 'BLACK',
    'Tile'
]
__version__ = '1.0.0'


from typing import TypeAlias


ColorCode: TypeAlias = int

GREEN: ColorCode = 0
'The letter and its position are both correct.'
YELLOW: ColorCode = 1
'The letter is correct but is in the wrong position.'
GRAY: ColorCode = 2
'The letter is not in the word at all.'
BLACK: ColorCode = 3
'The letter has not been used in a guess yet.'


class Tile(object):
    """
    A `Tile` represents a letter in a Wordle game, where each tile is assigned
    a color code that provides hints on the letter's accuracy.

    Color-Codes
    -----------
      * `GREEN`  -- The letter and its position are both correct.
      * `YELLOW` -- The letter is correct but is in the wrong position.
      * `GRAY`   -- The letter is not in the word at all.
      * `BLACK`  -- The letter has not been used in a guess yet.

    Example
    -------
      * Hidden Word: GAMER
      * Player's Guess: EARLY
      * Greens: {A}
      * Yellows: {E,R}
      * Grays: {L,Y}
    """

    version_added = '1.0.0'

    def __init__(
        self,
        letter: str,
        color: ColorCode = BLACK
    ) -> None:
        """
        Initializes a tile object representing a letter and its color-code.

        :param letter: The letter this tile represents.
        :param color:  The color code indicating the accuracy of the letter
                       relative to the hidden word. Defaults to `BLACK`
                       indicating that the letter has not been used yet.
        """
        raise NotImplementedError

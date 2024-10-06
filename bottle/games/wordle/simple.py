"""
A word puzzle-game called Wordle.

Wordle is a word puzzle-game where players attempt to guess a hidden word.
After each guess, the game provides feedback using color-coded hints:

Color-Codes
-----------
  * `GREEN`  -- The letter and its position are both correct.
  * `YELLOW` -- The letter is correct but is in the wrong position.
  * `GRAY`   -- The letter is not in the word at all.
  * `BLACK`  -- The letter has not been used in a guess yet.

The goal is to use these hints to deduce the hidden word using the least number
of attempts possible.

Author: Eggie
Version: 1.0.0
"""

__all__ = ['SimpleWordle']
__version__ = '1.0.0'


from .tile import *


class SimpleWordle(object):
    """
    A simple simulation of the Wordle puzzle-game.

    The objective of Wordle is to guess the hidden word in as few attempts as
    possible. After each guess, the player receives hints to help deduce the
    hidden word.

    In this simplified simulation, there are no restrictions on guesses, and
    the number of attempts is unlimited.
    """

    version_added = '1.0.0'

    def __init__(self, hidden_word: str) -> None:
        """
        Initializes a Wordle game simulator.

        This simulator supports a flexible Wordle-like game, with the only
        requirement being that the hidden word is valid. A valid word contains
        at least one character of any type.

        :param hidden_word: The word the player must guess to win.
        """
        raise NotImplementedError

    def validate(self, word: str) -> bool:
        """
        Validates the provided word.

        A word is considered valid if and only if the word is not empty. The
        word may include any type of character, including but not limited to
        alphabets, digits, emojis, and kanji.

        :param word: The word to validate.

        :return: `True` if the word is valid'; `False` otherwise.
        """
        raise NotImplementedError

    def attempt(self, word: str) -> <?>:
        """
        TODO: specification
        * Decide on...
            * returning a list[Tile]
            * returning a Hint object representing a list[Tile]

        Attempts a guess with the provided word.

        The `attempt()` method first validates the provided word, ensuring it
        is neither `None` nor empty. Any type of character is allowed in this
        simple Wordle simulation.

        After validation, the method generates a color-coded hint based on the
        player's guess by comparing each letter with the hidden word. The
        comparison results in one of the following color-codes:

        ------
          * `GREEN`  -- The letter and its position are both correct.
          * `YELLOW` -- The letter is correct but is in the wrong position.
          * `GRAY`   -- The letter is not in the word at all.
        ------

        Once all comparisons are made, the method returns the color-coded hint.

        :param word: The guess the player made.

        :return: <?>
        """
        raise NotImplementedError

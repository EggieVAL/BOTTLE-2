"""
A `Wordle` simulator with specific configurations.

This simulator follows the rules and game mechanics of the "New York Times"
Wordle. By default, the player has 6 attempts to guess the hidden word, all
words must contain only lower- or upper-case letters, and the word must be in
the English dictionary defined by "New York Times."

Author: Eggie
Version: 1.0.0
"""

__all__ = ['NYTWordle', 'dictionary']
__version__ = '1.0.0'


import string
from typing import TypeAlias

from bottle.wordle.errors import WordleError
from bottle.wordle.simple import Hint
from bottle.wordle.wordle import extract_dict, Wordle


DifficultyMode: TypeAlias = int
'Determines how difficult a "New York Times" Wordle game will be.'

NORMAL_MODE: DifficultyMode = 0
'The normal difficulty of a "New York Times" Wordle game.'
HARD_MODE: DifficultyMode = 1
'The hard difficulty of a "New York Times" Wordle game.'

dictionary = extract_dict('TODO: nyt-dict.txt')
'The English dictionary defined by "New York Times."'


class NYTWordle(Wordle):
    """
    A simulation of the "New York Times" Wordle.

    The objective of Wordle is to guess the hidden word in as few attempts as
    possible. After each guess, the player receives hints to help deduce the
    hidden word.

    In this version, there are two different modes that impose restrictions on
    guesses: normal mode and hard mode. In normal mode, the player must have
    attempts left to guess; the length of the guess must be the same as the
    length of the hidden word; the characters of each guess must be in the set
    of valid characters, if not empty; and the guess must be in the dictionary,
    if not empty.

    By default, the maximum number of attempts a player has is 6; the set of
    valid characters is the set of upper-case letters; and the dictionary is
    the English dictionary defined by "New York Times".

    In hard mode, the player must use any hints uncovered in addition to
    following the rules in normal mode. For example, if a green 'X' appears in
    the second character, then the player must include an 'X' in the second
    character going forward. If a yellow 'Y' appears in the third character,
    then the player must include a 'Y' somewhere in their guess.
    """

    def __init__(
        self,
        hidden_word: str,
        *,
        max_attempts: int = 6,
        valid_chars: set[str] = set(string.ascii_uppercase),
        dictionary: set[str] = dictionary
    ) -> None:
        """
        Initializes a "New York Times" Wordle game simulator.

        This simulator follows the rules and game mechanics of the "New York
        Times" Wordle. By default, the player has 6 attempts to guess the
        hidden word, all words must contain only upper-case letters, and the
        word must be in the English dictionary defined by "New York Times."

        :param hidden_word: The word the player must guess to win.

        :param max_attempts: The maximum number of attempts a player can make
                             to guess the hidden word. Defaults to 6.

        :param valid_chars: The game is restricted to these set of characters.
                            An empty set means all characters are valid.
                            Defaults to the set of upper-case letters.

        :param dictionary: A set of valid words a player can use as guesses.
                           An empty set means all strings are valid.
                           Defaults to the English dictionary defined by
                           "New York Times."

        :raises ValueError: If the provided hidden word does not pass the
                            `validate()` process.
        """
        raise NotImplementedError

    def change_difficulty(self, mode: DifficultyMode) -> bool:
        """
        Changes the difficulty of this game.

        The game's difficulty cannot be changed mid-game. That is, the player
        has already attempted a guess.

        :param mode: The difficulty mode to set.

        :return: `True` if the difficulty mode was successfully changed;
                 `False` otherwise.
        """
        raise NotImplementedError

    def unplayable(self, word: str) -> WordleError:
        """
        Determines if the provided word is unplayable in the game.

        A word is considered unplayable if the player has no more remaining
        attempts; the length of the guess does not equal to the length of the
        hidden word; at least one character the guess contains is not in the
        set of valid characters, if not empty; or the guess is not in the
        dictionary, if not empty.

        Additionally, if the difficulty is in hard mode, then the player must
        use all of the revealed hints. For example, if a green 'X' appears in
        the second character, then the player must include an 'X' in the second
        character going forward. If a yellow 'Y' appears in the third
        character, then the player must include a 'Y' somewhere in their guess.

        :param word: The word to determine if unplayable.

        :return: `True` if the word is unplayable; `False` otherwise.
                 Specifically, the method returns a type of `WordleError` using
                 an integer code.
        """
        raise NotImplementedError

    def attempt(self, guess: str) -> Hint:
        """
        Attempts to guess the hidden word with the provided guess.

        The `attempt()` method first ensures the provided guess is playable.
        For this simulation, a guess is playable if the player has remaining
        attempts left; the length of the guess is equal to the length of the
        hidden word; all the characters the guess contains are in the set of
        valid characters, if not empty; and the guess is in the dictionary, if
        not empty.

        Additionally, if the difficulty is in hard mode, then the player must
        use all of the revealed hints. For example, if a green 'X' appears in
        the second character, then the player must include an 'X' in the second
        character going forward. If a yellow 'Y' appears in the third
        character, then the player must include a 'Y' somewhere in their guess.

        If the guess is unplayable, then the method raises an error.

        Next, the method generates a color-coded hint based on the player's
        guess by comparing each character with the hidden word. The comparison
        results in one of the following color-codes:
        -----------------------------------------------------------------------
          * `GREEN`  -- The character and its position are both correct.
          * `YELLOW` -- The character is correct but is in the wrong position.
          * `GRAY`   -- The character is not in the word at all.
        -----------------------------------------------------------------------
        Once all comparisons are made, the method returns the color-coded hint.

        :param guess: The guess the player made.

        :raises ValueError: If the provided guess is not playable.

        :return: A color-coded hint in the form of a `Tile` list.
        """
        raise NotImplementedError

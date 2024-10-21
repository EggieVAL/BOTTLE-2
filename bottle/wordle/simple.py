"""
A word puzzle-game called Wordle.

Wordle is a word puzzle-game where players attempt to guess a hidden word.
After each guess, the game provides feedback using color-coded hints:
-------------------------------------------------------------------------------
  * `GREEN`  -- The character and its position are both correct.
  * `YELLOW` -- The character is correct but is in the wrong position.
  * `GRAY`   -- The character is not in the word at all.
  * `BLACK`  -- The character has not been used in a guess yet.
-------------------------------------------------------------------------------
The goal is to use these hints to deduce the hidden word using the least number
of attempts possible.

Author: Eggie
Version: 1.0.0
"""

__all__ = ['Hint', 'SimpleWordle']
__version__ = '1.0.0'


from bottle.wordle.errors import NoError, InvalidWordError, WordleError
from bottle.wordle.tile import GRAY, GREEN, YELLOW
from bottle.wordle.tile import Tile

from typing import TypeAlias


Hint: TypeAlias = list[Tile]
'A color-coded hint in the form of a `Tile` list.'


class SimpleWordle(object):
    """
    A simple simulation of the Wordle puzzle-game.

    The objective of Wordle is to guess the hidden word in as few attempts as
    possible. After each guess, the player receives hints to help deduce the
    hidden word.

    In this simplified simulation, there are almost zero restrictions on
    guesses, and the number of attempts a player can make is unlimited.
    """

    def __init__(self, hidden_word: str) -> None:
        """
        Initializes a simple Wordle game simulator.

        This simulator supports a flexible Wordle-like game, with the only
        requirement being that the hidden word is valid. A valid word contains
        at least one character of any type.

        :param hidden_word: The word the player must guess to win.

        :raises ValueError: If the provided hidden word does not pass the
                            `validate()` process.
        """
        if not self.validate(hidden_word):
            raise ValueError(f'invalid word "{hidden_word}"')

        self.hidden_word = hidden_word
        'The word the player must guess to win.'
        self.num_attempts = 0
        'The number of attempts the player has used.'
        self.has_won = False
        'If the player has guessed the hidden word.'
        self.guess_history: list[Hint] = []
        'All guesses the player has attempted.'

    def validate(self, word: str) -> bool:
        """
        Determines if the provided word is usable in the game.

        A word is considered usable if and only if the word is not empty. The
        word may include any type of character, including but not limited to
        alphabets, digits, emojis, and kanji.

        Note that even though this method validates a word to be usable, the
        word may not be playable. To check if the word is playable, see
        `unplayable()`.

        :param word: The word to validate.

        :return: `True` if the word is valid; `False` otherwise.
        """
        return len(word) != 0

    def unplayable(self, word: str) -> WordleError:
        """
        Determines if the provided word is unplayable in the game.

        A word is considered unplayable if and only if the word is not usable,
        which is determined by the `validate()` method.

        :param word: The word to determine if unplayable.

        :return: `True` if the word is unplayable; `False` otherwise.
                 Specifically, the method returns a type of `WordleError` using
                 an integer code.
        """
        if not self.validate(word):
            return InvalidWordError
        return NoError

    def _is_playable(self, guess: str) -> None:
        """
        Confirms if the guess can be played.

        Some Wordle variants have different restrictions imposed on player
        guesses. This method is meant to be overrided by those variants to
        allow them to decide playable words and how to handle unplayable words.

        :raises ValueError: If the provided guess is not playable.

        :param guess: The guess the player made.
        """
        if not (errno := self.unplayable(guess)):
            return

        errmsg = 'unknown error'
        if errno == InvalidWordError:
            errmsg = f'invalid guess "{guess}"'

        raise ValueError(errmsg)

    def algorithm(self, guess: str) -> Hint:
        """
        The Wordle algorithm to produce hints with the provided guess.

        -----------------------------------------------------------------------
          * `GREEN`  -- The character and its position are both correct.
          * `YELLOW` -- The character is correct but is in the wrong position.
          * `GRAY`   -- The character is not in the word at all.
        -----------------------------------------------------------------------

        :param guess: The guess the player made.

        :return: A color-coded hint in the form of a `Tile` list.
        """
        hint: Hint = [Tile(ch, GRAY) for ch in guess]
        hidden_map: dict[str, int] = {}

        min_length = min(len(guess), len(self.hidden_word))

        for i in range(min_length):
            ch = self.hidden_word[i]
            if guess[i] == ch:
                hint[i].color = GREEN
            else:
                hidden_map[ch] = hidden_map.get(ch, 0) + 1

        if len(hidden_map) == 0:
            self.has_won = True
        else:
            for i in range(len(guess)):
                if hint[i].color != GRAY:
                    continue
                ch = guess[i]
                if hidden_map.get(ch, 0) > 0:
                    hint[i].color = YELLOW
                    hidden_map[ch] -= 1

        return hint

    def attempt(self, guess: str) -> Hint:
        """
        Attempts to guess the hidden word with the provided guess.

        The `attempt()` method first ensures the provided guess is playable.
        For this simulation, any guess is playable as long as it's not empty.

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
        self._is_playable(guess)
        hint = self.algorithm(guess)
        self.guess_history.append(hint)
        self.num_attempts += 1
        return hint

    def reset(self, hidden_word: str) -> None:
        """
        Resets the game with a new hidden word.

        The `reset()` method reinitializes the simulation with a new word
        without needing to create a new simulation. This saves resources and
        avoids unnecessary object creation.

        Note that only some components of the game are reset:

        -----------------------------------------------------------------------
          * `num_attempts`
          * `has_won`
          * `guess_history`
        -----------------------------------------------------------------------

        :param hidden_word: The word the player must guess to win.

        :raises ValueError: If the provided hidden word does not pass the
                            `validate()` process.
        """
        if not self.validate(hidden_word):
            raise ValueError(f'invalid word "{hidden_word}"')

        self.hidden_word = hidden_word
        self.num_attempts = 0
        self.has_won = False
        self.guess_history.clear()

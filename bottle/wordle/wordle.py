"""
An advanced version of `SimpleWordle`.

Like `SimpleWordle`, the player attempts to guess a hidden word using few
attempts as possible. However, in this version, the player is constrained to a
limited number of guesses.

Moreover, the game must be played within a set of characters. Any words, both
hidden words and guesses, with characters that are not in this set will be
invalidated.

Guesses can be further restricted to a set of words called a dictionary. Any
hidden words and guesses that are not recognized by this dictionary will be
invalidated.

Author: Eggie
Version: 1.0.0
"""

__all__ = ['Wordle']
__version__ = '1.0.0'


from bottle.wordle.errors import (GuessLengthError, InvalidWordError,
                                  NoAttemptsError, NoError, WordleError)
from bottle.wordle.simple import Hint, SimpleWordle
from bottle.wordle.tile import BLACK


class Wordle(SimpleWordle):
    """
    A simulation of Wordle with rules.

    The objective of Wordle is to guess the hidden word in as few attempts as
    possible. After each guess, the player receives hints to help deduce the
    hidden word.

    In this version, there are a few restrictions on guesses: the player
    must have attempts left to guess; the length of the guess be the same as
    the length of the hidden word; the characters of each guess must be in the
    set of valid characters, if not empty; and the guess must be in the
    dictionary, if not empty.
    """

    def __init__(
        self,
        hidden_word: str,
        *,
        max_attempts: int,
        valid_chars: set[str] = set(),
        dictionary: set[str] = set()
    ) -> None:
        """
        Initializes a Wordle game simulator.

        This simulator has a set of rules, making the game more challenging and
        fun. These rules are imposed to restrict the player's guess, for
        example, a limited number of attempts.

        Before providing the hidden word, the valid characters, and the
        dictionary, note that the simulator will be case-sensitive.

        :param hidden_word: The word the player must guess to win.

        :param max_attempts: The maximum number of attempts a player can make
                             to guess the hidden word.

        :param valid_chars: The game is restricted to these set of characters.
                            An empty set means all characters are valid.
                            Defaults to an empty set.

        :param dictionary: A set of valid words a player can use as guesses.
                           An empty set means all strings are valid.
                           Defaults to an empty string.

        :raises ValueError: If the provided hidden word does not pass the
                            `validate()` process.
        """
        self.max_attempts = max_attempts
        'The maximum number of attempts a player can make to guess the word.'
        self.valid_chars = valid_chars
        'The game is restricted to these set of characters.'
        self.dictionary = dictionary
        'A set of valid words a player can use as guesses.'
        self.hints = {ch: BLACK for ch in valid_chars}
        'The hints revealed from all the attempts the player made.'

        super().__init__(hidden_word)

    def validate(self, word: str) -> bool:
        """
        Determines if the provided word is usable in the game.

        A word is considered usable if the word is not empty; the characters it
        contains must be in the set of valid characters, if not empty; and the
        word must be in the dictionary, if not empty.

        Note that even though this method validates a word to be usable, the
        word may not be playable. To check if the word is playable, see
        `unplayable()`.

        :param word: The word to validate.

        :return: `True` if the word is valid; `False` otherwise.
        """
        all_chars_valid = (not self.valid_chars
                           or all(ch in self.valid_chars for ch in word))

        in_dict = (not self.dictionary
                   or word in self.dictionary)

        return all_chars_valid and in_dict

    def unplayable(self, word: str) -> WordleError:
        """
        Determines if the provided word is unplayable in the game.

        A word is considered unplayable if the player has no more remaining
        attempts; the length of the guess does not equal to the length of the
        hidden word; at least one character the guess contains is not in the
        set of valid characters, if not empty; or the guess is not in the
        dictionary, if not empty.

        :param word: The word to determine if unplayable.

        :return: `True` if the word is unplayable; `False` otherwise.
                 Specifically, the method returns a type of `WordleError` using
                 an integer code.
        """
        if self.num_attempts == self.max_attempts:
            return NoAttemptsError
        if len(word) != len(self.hidden_word):
            return GuessLengthError
        if not self.validate(word):
            return InvalidWordError
        return NoError

    def _is_playable(self, guess: str) -> None:
        if not (errno := self.unplayable(guess)):
            return

        errmsg = 'unknown error'
        if errno == InvalidWordError:
            errmsg = f'invalid guess "{guess}"'
        elif errno == NoAttemptsError:
            errmsg = 'no attempts remaining'
        elif errno == GuessLengthError:
            len_diff = len(guess) - len(self.hidden_word)
            adjective = 'short' if len_diff < 0 else 'long'
            errmsg = 'guess is too ' + adjective

        raise ValueError(errmsg)

    def attempt(self, guess: str) -> Hint:
        """
        Attempts to guess the hidden word with the provided guess.

        The `attempt()` method first ensures the provided guess is playable.
        For this simulation, a guess is playable if the player has remaining
        attempts left; the length of the guess is equal to the length of the
        hidden word; all the characters the guess contains are in the set of
        valid characters, if not empty; and the guess is in the dictionary, if
        not empty.

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
        return super().attempt(guess)

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
          * `hints`
        -----------------------------------------------------------------------

        :param hidden_word: The word the player must guess to win.

        :raises ValueError: If the provided hidden word does not pass the
                            `validate()` process.
        """
        super().reset(hidden_word)

        for ch in self.hints.keys():
            self.hints[ch] = BLACK

    def suggestions(self, chars: str) -> list[str]:
        """
        Gives word suggestions for the provided list of characters.

        The `suggestions()` method picks out words from the dictionary using
        the provided list of characters. If the dictionary is empty, then no
        suggestions can be made.

        This method will take duplicate characters into consideration. That
        means if the list of characters contain two C's, then it will suggest
        words with two or more C's.

        :param chars: The list of characters a word must contain, in the form
                      of a string.

        :return: A list of suggested words for the provided list of characters.
        """
        raise NotImplementedError

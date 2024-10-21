"""
All types of errors a Wordle game can raise.

Author: Eggie
Version: 1.0.0
"""

__all__ = [
    'WordleError', 'NoError', 'InvalidWordError', 'NoAttemptsError',
    'GuessLengthError', 'UnusedHintError'
]
__version__ = '1.0.0'


from typing import TypeAlias


WordleError: TypeAlias = int
'A unique integer code representing specific Wordle errors.'

NoError: WordleError = 0
'No errors found.'
InvalidWordError: WordleError = 1
'Word is not usable or valid in the game.'
NoAttemptsError: WordleError = 2
'No attempts remaining to make guesses.'
GuessLengthError: WordleError = 3
'Different lengths of the guess and hidden word.'
UnusedHintError: WordleError = 4
'Player did not use a revealed hint in their guess.'

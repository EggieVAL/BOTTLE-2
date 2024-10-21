from bottle.wordle import GRAY, GREEN, YELLOW
from bottle.wordle import Hint
from bottle.wordle import Wordle


def print_hint(hint: Hint) -> None:
    green = '\x1b[38;2;0;165;80m'
    yellow = '\x1b[38;2;255;196;12m'
    gray = '\x1b[38;2;75;75;75m'
    reset = '\x1b[0m'

    string = ''
    for tile in hint:
        if tile.color == GREEN:
            string += green + tile.ch
        elif tile.color == YELLOW:
            string += yellow + tile.ch
        elif tile.color == GRAY:
            string += gray + tile.ch

    print(string + reset)


def playwordle(wordle: Wordle) -> None:
    while not wordle.has_won and wordle.num_attempts != wordle.max_attempts:
        guess = input('Enter your guess: ')
        try:
            wordle.attempt(guess)
            for hint in wordle.guess_history:
                print_hint(hint)
        except ValueError as e:
            print(e)

    print(f'The hidden word was "{wordle.hidden_word}"')


if __name__ == '__main__':
    wordle = Wordle('GAMER', max_attempts=6)
    playwordle(wordle)


import game
from game import Game

tic_tac = Game()

print(tic_tac.get_structure())

must_continue = True

close = ""

while must_continue:

    data = input(f"({tic_tac.current_player}) Enter a number from 1 to 9 to play : ")

    validation_code = tic_tac.validate_input(data)

    if validation_code == 0:
        results = tic_tac.play(data)

        if results == 0 and not tic_tac.value_structure.__contains__(" "):

            close = f"\n\nIt is a draw!!"
            break

        elif results == 0:

            close = f"\n\nCongratulations to player {tic_tac.current_player}, you won!!"
            break

    else:
        print(f"\n\n{game.CUSTOM_PLAY_ERRORS[validation_code]} \n\n")

    print(tic_tac.get_structure())

print(tic_tac.get_structure())
print(close)

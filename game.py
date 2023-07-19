
VALIDATING_STRUCTURE = {
    0: [[1, 2], [3, 6], [4, 8]],
    1: [[0, 2], [4, 7]],
    2: [[0, 1], [5, 8], [4, 6]],
    3: [[0, 6], [4, 5]],
    4: [[0, 8], [1, 7], [2, 6], [3, 5]],
    5: [[3, 4], [2, 8]],
    6: [[0, 3], [7, 8], [4, 2]],
    7: [[1, 4], [6, 8]],
    8: [[0, 4], [2, 5], [6, 7]]
}

CUSTOM_PLAY_ERRORS = {0: "Pass",
                      1: "Input cannot be empty",
                      2: "Input is out of range. Input must be any number from 1 to 9",
                      3: "Input must be a number ranging form 1 to 10 not including 10",
                      4: "There is already an input placed on the spot. Select a spot that is not occupied"}


class Game:

    def __init__(self):
        self.value_structure = [" ", " ", " ",
                                " ", " ", " ",
                                " ", " ", " "]

        self.player1 = "X"
        self.player2 = "O"

        self.current_player = self.player1

    def validate_input(self, data: str):

        try:

            data = int(data)

            if data < 1 or data > 9:
                return 2
            elif self.value_structure[data - 1] == " ":
                return 0
            else:
                return 4

        except ValueError:

            if data == "":
                return 1
            else:
                return 3

    def play(self, data):

        error_code = self.validate_input(data)

        data = int(data)

        if error_code == 0:

            data -= 1

            for array in VALIDATING_STRUCTURE[data]:

                if self.value_structure[array[0]] == self.current_player and self.value_structure[array[1]] == self.current_player:

                    self.value_structure[data] = self.current_player

                    return 0
        else:
            return 1

        self.value_structure[data] = self.current_player

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

        if self.value_structure.__contains__(" "):
            return 1
        else:
            return 0

    def get_structure(self):

        length = len(self.value_structure)

        structure = "\n"
        dashes = "-------------"

        skip = 2

        for i in range(0, length):

            structure += self.value_structure[i] + "  "

            if i == skip:
                structure += "\n" + dashes + "\n"
                skip += 3
            else:
                structure += "|" + "  "

        return structure.removesuffix(dashes + "\n")

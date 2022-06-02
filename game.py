# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import pip._vendor.requests
import string
import random


class Game:

    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
        print(self.grid)

    def random_grid(self):
        pass

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy()  # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        #return True
        return self.__check_dictionary(word)

    # Private method

    @staticmethod
    def __check_dictionary(word):
        response = pip._vendor.requests.get(
            f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']

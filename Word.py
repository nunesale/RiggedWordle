class Word:

    def __init__(self, letters, letter_data):
        # ordered list of letters in the word
        self.letters = letters

        # ordered list of "b" "y" "g" representing the colour of the cooresponding letter in the word
        self.letter_data = letter_data

    # return a tuple containing the letter at index in the word, and it's colour
    def get_data(self, index):
        return self.letters[index], self.letter_data[index]

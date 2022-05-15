from Word import Word


# count the number of yellows of letter in word, given data
def count_yellow(word, data, letter):
    count = 0
    for i in range(len(word)):
        if word[i] == letter and data[i] == "y":
            count += 1
    return count


# count the number of greens of letter in word, given data
def count_green(word, data, letter):
    count = 0
    for i in range(len(word)):
        if word[i] == letter and data[i] == "g":
            count += 1
    return count


# count the number of letter in word
def count_letters(word, letter):
    count = 0
    for character in word:
        if character == letter:
            count += 1
    return count


class GameState:

    def __init__(self, keyword):

        # the answer
        self.keyword = keyword

        # length of words in this game
        self.word_length = len(keyword)

        # ordered list of Word objects representing words the player has entered
        self.entered_words = []

        # number of previous words the player has entered
        self.num_entered_words = 0

        # ordered list of letter the player has typed in the current word
        self.entered_letters = []

        # number of letters the player has entered in the current word
        self.num_entered_letters = 0

        # add a letter to entered_letters, if possible

    def enter_letter(self, letter):
        if self.num_entered_letters < self.word_length:
            self.entered_letters.append(letter)
            self.num_entered_letters += 1

    # remove the latest letter from entered_letters, if possible
    def delete_letter(self):
        if self.num_entered_letters > 0:
            self.entered_letters.pop()
            self.num_entered_letters -= 1

    def submit(self):
        if self.num_entered_letters == self.word_length:
            letter_data = []
            for i in range(len(self.entered_letters)):
                if self.entered_letters[i] == self.keyword[i]:
                    letter_data.append("g")
                elif self.entered_letters[i] in self.keyword:
                    letter_data.append("y")
                else:
                    letter_data.append("b")
            for i in range(len(self.entered_letters)):
                if letter_data[i] == "y":
                    count_input = count_letters(self.entered_letters, self.entered_letters[i])
                    count_ans = count_letters(self.keyword, self.entered_letters[i])
                    if count_input > count_ans:
                        greens = count_green(self.entered_letters, letter_data, self.entered_letters[i])
                        yellows = count_yellow(self.entered_letters[:i], letter_data, self.entered_letters[i])
                        if greens + yellows >= count_ans:
                            letter_data[i] = "b"

            new_word = Word(self.entered_letters.copy(), letter_data.copy())
            self.entered_words.append(new_word)
            self.num_entered_words += 1

            self.entered_letters = []
            self.num_entered_letters = 0

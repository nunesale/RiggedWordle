import pygame

from GameState import GameState

alphabet = "abcdefghijklmnopqrstuvwxyz"

keyword = "place"

word_length = len(keyword)

white = (255, 255, 255)

display_width = 1200
display_height = 800

game_display = pygame.display.set_mode((display_width, display_height))

image_dict = {"  ": pygame.image.load('letters/blank.png')}

letter_width = image_dict["  "].get_width()
letter_height = image_dict["  "].get_height()

clock = pygame.time.Clock()

num_guesses = 6
letter_gap = 8

pygame.display.set_caption("Wordle (real)")


# draw an empty letter space at x,y
def draw_blank(x, y):
    game_display.blit(image_dict["  "], (x, y))


# draw a letter with the specified type (w, b, y, g) at x,y
def draw_letter(letter, type, x, y):
    game_display.blit(image_dict[letter + type], (x, y))


def game_loop(game):
    gameExit = False

    user_has_typed = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            elif event.type == pygame.KEYDOWN:
                if not user_has_typed:
                    user_has_typed = True
                if event.key == pygame.K_RETURN and game.num_entered_letters == word_length:
                    game.submit()
                elif event.key == pygame.K_BACKSPACE:
                    game.delete_letter()
                elif event.unicode.isalpha():
                    game.enter_letter(event.unicode)

        game_display.fill(white)

        x_offset = 0
        y_offset = 0

        # draw previous guesses
        for i in range(game.num_entered_words):
            for j in range(word_length):
                draw_letter(game.entered_words[i].letters[j], game.entered_words[i].letter_data[j],
                            word_entry_x_start + x_offset, word_entry_y_start + y_offset)
                x_offset += letter_width + letter_gap
            x_offset = 0
            y_offset += letter_height + letter_gap

        # draw current user input space
        for i in range(game.num_entered_letters):
            draw_letter(game.entered_letters[i], "w",
                        word_entry_x_start + x_offset, word_entry_y_start + y_offset)
            x_offset += letter_width + letter_gap

        for i in range(word_length - game.num_entered_letters):
            draw_blank(word_entry_x_start + x_offset, word_entry_y_start + y_offset)
            x_offset += letter_width + letter_gap

        x_offset = 0
        y_offset += letter_height + letter_gap

        # draw unused space
        for i in range(num_guesses - game.num_entered_words - 1):
            for j in range(word_length):
                draw_blank(word_entry_x_start + x_offset, word_entry_y_start + y_offset)
                x_offset += letter_width + letter_gap
            x_offset = 0
            y_offset += letter_height + letter_gap

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    pygame.init()

    pygame.event.set_blocked(None)
    pygame.event.set_allowed(pygame.KEYUP)
    pygame.event.set_allowed(pygame.KEYDOWN)
    pygame.event.set_allowed(pygame.QUIT)

    for alpha in alphabet:
        image_dict[alpha + "w"] = pygame.image.load("letters/" + alpha + "w.png")
        image_dict[alpha + "b"] = pygame.image.load("letters/" + alpha + "b.png")
        image_dict[alpha + "y"] = pygame.image.load("letters/" + alpha + "y.png")
        image_dict[alpha + "g"] = pygame.image.load("letters/" + alpha + "g.png")

    word_entry_length = ((letter_width + letter_gap) * word_length) - letter_gap
    word_entry_height = ((letter_height + letter_gap) * num_guesses) - letter_gap

    word_entry_x_start = (display_width // 2) - (word_entry_length // 2)
    word_entry_y_start = (display_height // 2) - (word_entry_height // 2)

    game = GameState(keyword)
    game_loop(game)

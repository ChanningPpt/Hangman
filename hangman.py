import random
from words import words
from hangman_visuals import welcome_display, hangman_stages

class Hangman:
    def __init__(self):
        self.word_list = words
        self.word = self.get_valid_word()
        self.guessed_word = ['_'] * len(self.word)
        self.guessed_letters = []
        self.lives = 6
        self.hangman_stages = hangman_stages

    def get_valid_word(self):
        word = random.choice(self.word_list)
        while '-' in word or ' ' in word:
            word = random.choice(self.word_list)
        return word.upper()

    def display_hangman(self):
        print(self.hangman_stages[6 - self.lives])

    def display_word(self):
        print("Current word: ", ' '.join(self.guessed_word))

    def check_guessed_letter(self, guessed_letter):
        if not guessed_letter.isalpha() or len(guessed_letter) != 1:
            print("Invalid input. Please try again.")
            return
        
        guessed_letter = guessed_letter.upper()

        if guessed_letter in self.guessed_letters:
            print("You have already guessed that letter. Please try again.")
            return

        self.guessed_letters.append(guessed_letter)

        if guessed_letter in self.word:
            for i in range(len(self.word)):
                if self.word[i].upper() == guessed_letter:
                    self.guessed_word[i] = guessed_letter
        else:
            self.lives -= 1
            print(f'Wrong guess! The letter "{guessed_letter}" is not in the word')

    def check_win(self):
        return ''.join(self.guessed_word).upper() == self.word

    def check_game_over(self):
        return self.lives == 0

    def reset_game(self):
        self.word = self.get_valid_word()
        self.guessed_word = ['_'] * len(self.word)
        self.guessed_letters = []
        self.lives = 6

    def play(self):
        while True:
            while not self.check_win() and not self.check_game_over():
                self.display_hangman()
                self.display_word()
                print(f'Guessed letters: {", ".join(self.guessed_letters)}')
                print(f'Lives remaining: {self.lives}')

                guessed_letter = input("Guess a letter: ")
                self.check_guessed_letter(guessed_letter)
            
            if self.check_win():
                print(f"\nCongratulations! You guessed the word: {self.word}")
            else:
                self.display_hangman()
                print(f"\nGame over! The word was: {self.word}")

            play_again = input("Would you like to play again? (yes/no): ").lower()
            if play_again == 'yes':
                self.reset_game()
            else:
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    print(welcome_display)
    game = Hangman()
    game.play()
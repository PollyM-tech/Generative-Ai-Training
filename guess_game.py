import random

class Game:
    def __init__(self, attempts):
        self.attempts = attempts
        
class GuessGame(Game):
    def __init__(self, attempts=10):
        super().__init__(attempts)
        self.correct_number = random.randint(1, 10)

    def play(self):
        while self.attempts > 0:
            guess = input("Enter your guess (1-10): ")
            if guess.isdigit():
                if self.process_guess(int(guess)):
                    print("🎉 Correct! You win!")
                    return
            else:
                print("Please enter a number.")

            self.attempts -= 1
            print(f"Attempts left: {self.attempts}")
        
        print("😢 Game over. You lost.")

    def process_guess(self, guess):
        if guess > self.correct_number:
            print("Too high!")
        elif guess < self.correct_number:
            print("Too low!")
        else:
            return True
        return False


game = GuessGame()
game.play()

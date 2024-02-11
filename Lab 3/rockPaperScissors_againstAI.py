import paho.mqtt.client as mqtt
import random

class RockPaperScissorsBot:
    def __init__(self):
        self.state = 'query_user'

    def run(self):
        while True:
            if self.state == 'query_user':
                user_action = input("Enter your choice (rock, paper, or scissors): ").lower()
                if user_action not in ['rock', 'paper', 'scissors']:
                    print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
                    continue
                self.state = 'generate_action'
            elif self.state == 'generate_action':
                bot_action = random.choice(['rock', 'paper', 'scissors'])
                self.state = 'display_results'
            elif self.state == 'display_results':
                print(f"Bot chose {bot_action}.")
                if user_action == bot_action:
                    print("It's a tie!")
                elif (user_action == 'rock' and bot_action == 'scissors') or \
                     (user_action == 'scissors' and bot_action == 'paper') or \
                     (user_action == 'paper' and bot_action == 'rock'):
                    print("You win!")
                else:
                    print("Bot wins!")
                self.state = 'standby'
            elif self.state == 'standby':
                self.state = 'query_user'

if __name__ == "__main__":
    game = RockPaperScissorsBot()
    game.run()



import random
import paho.mqtt.client as mqtt

class RockPaperScissorsBot:
    def __init__(self):
        self.state = 'query_user'
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect("mqtt.eclipse.org", 1883, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to MQTT broker with result code "+str(rc))
        client.subscribe("rps/user_action")

    def on_message(self, client, userdata, msg):
        user_action = msg.payload.decode()
        if user_action not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
            return
        self.state = 'generate_action'

    def run(self):
        while True:
            if self.state == 'generate_action':
                bot_action = random.choice(['rock', 'paper', 'scissors'])
                self.client.publish("rps/bot_action", bot_action)
                self.state = 'display_results'

    def stop(self):
        self.client.loop_stop()

if __name__ == "__main__":
    game = RockPaperScissorsBot()
    game.run()

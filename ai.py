from unittest import result
from player import Player
import random
from time import sleep

class Ai(Player):

    def __init__(self):
        super().__init__()

    def set_name(self):
       return random.choice(['Stuart', 'Weldon'])

    def choose_gesture(self):
        self.player_gesture = random.choice(self.gesture_list)
        sleep(1)
        print(
            f'{self.name} has picked {self.selected_guesture}')

from player import Player
import random
from time import sleep

class Ai(Player):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.score = 0

        self.ai_name_list = ['Stuart', 'Weldon']
        self.name = str(random.randint(0,1))
        print(f'You will be playing against {self.name[int(self.name)]}')

    def choose_gesture(self):
        gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.player_gesture = str(gesture_list[random.randint(0,4)])

        sleep(1)
        print(f'{self.name} has picked {gesture_list[int(self.choose_gesture)]}')

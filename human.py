from player import Player
import random
from time import sleep

class Human(Player):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.name = str(input('What is your gaming name? Please type your answer here: ' ))
        print('Welcome to the game,{self.name.str.input}!')

    def choose_gesture(self, player_gesture):
        print('')
        self.gesture_list = int(input(0,4))
        if self.gesture_list > 4:
            self.choose_gesture()
        gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        sleep(1)
        print(f'{self.name} has picked {gesture_list[int(self.gesture_list)]}')
        self.player_gesture = gesture_list[int(self.gesture_list)]

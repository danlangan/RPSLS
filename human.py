from player import Player
from utility import try_parse_int
from time import sleep

class Human(Player):

    def __init__(self):
        super().__init__()
        
    def set_name(self):
        username = input('What is your name?')
        print(f'Welcome to the game,{username}!')
        return username

    def choose_gesture(self):
        self.player_gesture = try_parse_int(print(f'''
        Select which gesture you would like to use: 
1) Rock
2) Paper
3) Scissors
4) Lizard
5) Spock
        '''))

        match self.player_gesture:
            case 1:
                self.selected_gesture = 'Rock'
            case 2:
                self.selected_gesture = 'Paper'
            case 3:
                self.selected_gesture = 'Scissors'
            case 4:
                self.selected_gesture = 'Lizard'
            case 5:
                self.selected_gesture = 'Spock'

        sleep(1)
        print(
            f'{self.name} has picked {self.selected_gesture}')
        
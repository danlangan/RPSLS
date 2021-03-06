from ai import Ai
from human import Human
from utility import try_parse_int
from time import sleep

print('Welcome to RPSLS! We are excited to get the game started!')

class Game:
    def __init__(self):
        self
        
    def print_options(self):
        print('Rock crushes Scissors')
        sleep(1)
        print('Scissors cuts Paper')
        sleep(1)
        print('Paper covers Rock')
        sleep(1)
        print('Rock crushes Lizard')
        sleep(1)
        print('Lizard poisons Spock')
        sleep(1)
        print('Spock smashes Scissors')
        sleep(1)
        print('Scissors decapitates Lizard')
        sleep(1)
        print('Lizard eats Paper')
        sleep(1)
        print('Paper disproves Spock')
        sleep(1)
        print('Spock vaporizes Rock')
        sleep(1)

    def choose_game_type(self):
        user_selection = try_parse_int(f'''
Select the type of game that you would like to play from the following options:

1) Single Player Game
2) Two Player Game
3) AI Bot War
''')

        if user_selection == 1:
            self.player_one = Human()
            self.player_two = Ai()

        elif user_selection == 2:
                self.player_one = Human()
                self.player_two = Human()

        elif user_selection == 3:
                self.player_one = Ai()
                self.player_two = Ai()

    def player_score(self):
        self.player_one.score
        self.player_two.score

    def player_move(self):
        self.game_score = print(f"{self.player_one.score} is {self.player_one.name}'s game score AND {self.player_two.score} is {self.player_two.name}'s game score.")
        self.print_options()
        self.player_one.choose_gesture()
        self.print_options()
        self.player_two.choose_gesture()
        self.player_one.player_gesture
        self.player_two.player_gesture
        self.compare_gestures()

    def choose_gestures(self):
        self.player_one.choose_gesture()
        self.player_two.choose_gesture()

    def compare_gestures(self):
        gesture_1 = self.player_one.selected_gesture
        gesture_2 = self.player_two.selected_gesture
        if gesture_1 == gesture_2:
            print("It's a tie!")
        elif gesture_1 == 'Rock':
            if gesture_2 == 'Scissors' or gesture_2 == 'Lizard':
                self.player_one.score_point()
            else:
                self.player_two.score_point()
        elif gesture_1 == 'Scissors':
            if gesture_2 == 'Paper' or gesture_2 == 'Lizard':
                self.player_one.score_point()
            else:
                self.player_two.score_point()
        elif gesture_1 == 'Paper':
            if gesture_2 == 'Rock' or gesture_2 == 'Spock':
                self.player_one.score_point()
            else:
                self.player_two.score_point()
        elif gesture_1 == 'Lizard':
            if gesture_2 == 'Paper' or gesture_2 == 'Spock':
                self.player_one.score_point()
            else:
                self.player_two.score_point()
        elif gesture_1 == 'Spock':
            if gesture_2 == 'Scissors' or gesture_2 == 'Rock':
                self.player_one.score_point()
            else:
                self.player_two.score_point()

    def declare_winner(self):

        if self.player_one.score == 3:
            print(f'{self.player_one.name} wins the game!')
        elif self.player_two.score == 3:
            print(f'{self.player_two.name} wins the game!')


    def run_game(self):
        self.choose_game_type()
        self.player_score()

        while self.player_one.score < 3 and self.player_two.score < 3:
            self.print_options()
            self.choose_gestures()
            self.compare_gestures()
        else:
            self.declare_winner()
from ai import Ai
from human import Human
from time import sleep

print('Welcome to RPSLS! We are excited to get the game started!')

class Game:
    def __init__(self):
        pass
        
    def print_options(self):
        print('Scissors cut paper')
        sleep(1)
        print('Paper cuts rock')
        sleep(1)
        print('Rock crushes lizard')
        sleep(1)
        print('Lizard poisons spock')
        sleep(1)
        print('Spock vaporizes rock')
        sleep(1)
        print('Rock crushes scissors')

    def player_score(self, player_one_score, player_two_score):
        self.player_one_score = 0
        self.player_two_score = 0
        
        int.input(print('How many players will be playing the game today? Select either one or two, and select 3 for a suprise!:' ))

    def players_in_game(self, player_one, player_two, active_players):
        self.active_players = int.input(print('How many players will be playing the game today? Choose between 0 and 2: '))
        while self.active_players <= 2:
            if self.active_players == 0:
                self.player_one = Ai()
                self.player_two = Ai()
            elif self.active_players == 1:
                self.player_one = Human()
                self.player_two = Ai()
            elif self.active_players == 2:
                self.player_one = Human()
                self.player_two = Human()
            else:
                self.active_players > 2
                print('You have made an incorrect choice, you will now witness two AI bots, Stuart and Weldon, duke it out. Enjoy!')
                self.player_one = Ai()
                self.player_two = Ai()

    def player_move(self):
        self.game_score = print(f'{self.player_one_score} is the score for player one and {self.player_two_score} is the score for player two')
        self.print_options()
        self.player_one.choose_gesture()
        self.print_options()
        self.player_two.choose_gesture()
        self.player_one.player_gesture
        self.player_two.player_gesture
        self.gesture_choices()

    def gesture_choices(self):
        self.player_one.player_gesture = int(input('Select 0 for Scissors, 1 for Paper, 2 for Rock, 3 for Lizard, and 4 for Spock. Which choice would you like to make? Enter your numnber here: '))
        self.player_two.player_gesture = int(input('Select 0 for Scissors, 1 for Paper, 2 for Rock, 3 for Lizard, and 4 for Spock. Which choice would you like to make? Enter your numnber here: '))

        if int(input(self.player_one.player_gesture)) == 0 and int(input(self.player_two.player_gesture)) == 2:
            print('Player two wins!')
            self.player_two_score += 1

        elif int(input(self.player_one.player_gesture)) == 2 and int(input(self.player_two.player_gesture)) == 0 or 3:
            print('Player one wins!')
            self.player_one_score += 1

        elif int(input(self.player_one.player_gesture)) == 1 and int(input(self.player_two.player_gesture)) == 0:
            print('Player two wins!')
            self.player_two_score += 1

        elif int(input(self.player_one.player_gesture)) == 0 and int(input(self.player_two.player_gesture)) == 1:
            print('Player one wins!')
            self.player_one_score += 1

        elif int(input(self.player_one.player_gesture)) == 3 and int(input(self.player_two.player_gesture)) == 4:
            print('Player one wins!')
            self.player_one_score += 1

        elif int(input(self.player_one.player_gesture)) == 4 and int(input(self.player_two.player_gesture)) == 2:
            print('Player one wins!')
            self.player_one_score += 1

        elif int(input(self.player_one.player_gesture)) == 0 or 3 and int(input(self.player_two.player_gesture)) == 2:
            print('Player two wins!')
            self.player_two_score += 1

        elif int(input(self.player_one.player_gesture)) == 0 and int(input(self.player_two.player_gesture)) == 1:
            print('Player one wins!')
            self.player_one_score += 1

        elif int(input(self.player_one.player_gesture)) == 4 and int(input(self.player_two.player_gesture)) == 3:
            print('Player two wins!')
            self.player_two_score += 1

        elif int(input(self.player_one.player_gesture)) == 2 and int(input(self.player_two.player_gesture)) == 4:
            print('Player two wins!')
            self.player_two_score += 1

        elif int(input(self.player_one.player_gesture)) == 1 and int(input(self.player_two.player_gesture)) == 2:
            print('Player one wins!')
            self.player_one_score += 1

        elif int(input(self.player_one.player_gesture)) == 2 and int(input(self.player_two.player_gesture)) == 1:
            print('Player two wins!')
            self.player_two_score += 1

     ## non scoring gesture choices are coming up next

        elif int(input(self.player_one.player_gesture)) == 0 and int(input(self.player_two.player_gesture)) == 3 or 4:
            print('No damage has been done, please select a new gesture and try again!')
            sleep(1)

        elif int(input(self.player_one.gesture_choices)) == 3 or 4 and int(input(self.player_two.gesture_choices)) == 0:
            print('No damage has been done, please select a new gesture and try again!')
            sleep(1)

        elif int(input(self.player_one.player_gesture)) == 0 or 1 and int(input(self.player_two.player_gesture)) == 3:
            print('No damage has been done, please select a new gesture and try again!')
            sleep(1)

        elif int(input(self.player_one.player_gesture)) == 3 and int(input(self.player_two.player_gesture)) == 0 or 1:
            print('No damage has been done, please select a new gesture and try again!')
            sleep(1)

        else: 
            int(input(self.player_one.player_gesture)) == int(input(self.player_two.player_gesture))
            print('Both players have made the same choice, choose again!')

    def run_game(self):
        self.players_in_game()
        self.player_score()
        while self.player_one_score < 2 and self.player_two_score < 2:
            self.player_move()
            self.gesture_choices()
        if self.player_one_score == 2 or self.player_two_score == 2:

            pass

        print('Welcome to RPSLS! We are excited to get the game started')
        


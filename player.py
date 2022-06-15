class Player:
    def __init__(self):
        self.name = self.set_name()
        self.score = 0

    def score_point(self):
        self.score += 1
        print(f'{self.name} wins!')

    def set_name(self):
        pass

    def choose_gesture(self):
        self.gesture_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        self.selected_guesture = ''
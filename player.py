class Player:
    def __init__(self):
        self.name = self.set_name()
        self.score = 0
        self.gesture_list = ['Rock','Paper','Scissors','Lizard','Spock']
        self.selected_gesture = ''

    def score_point(self):
        self.score += 1
        print(f'{self.name} wins this round!')

    def set_name(self):
        print(f'{self.name} is this players name!')
        pass

    def choose_gesture(self):
        pass

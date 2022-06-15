def try_parse_int(prompt):
    try:
        return int(input(prompt))
    except:
        return try_parse_int(prompt)

#self.ai_name_list = ['Stuart', 'Weldon']


#i = 1
#for gesture in gesture_list:
   # print(f'{i}) {gesture}')
   # i += 1

#user_input = try_parse_int('Choose your gesture: ') - 1

#print(gesture_list[user_input])


#def gesture_choices(self):
    #    self.player_one.player_gesture = int(input('Select 0 for Scissors, 1 for Paper, 2 for Rock, 3 for Lizard, and 4 for Spock. Which choice would you like to make? Enter your numnber here: '))
    #    self.player_two.player_gesture = int(input('Select 0 for Scissors, 1 for Paper, 2 for Rock, 3 for Lizard, and 4 for Spock. Which choice would you like to make? Enter your numnber here: '))

    #    if int(input(self.player_one.player_gesture)) == 0 and int(input(self.player_two.player_gesture)) == 2:
    #        print('Player two wins!')
    #        self.player_two_score += 1

    #    elif int(input(self.player_one.player_gesture)) == 2 and int(input(self.player_two.player_gesture)) == 0 or 3:
    #        print('Player one wins!')
    #        self.player_one_score += 1

    #    elif int(input(self.player_one.player_gesture)) == 1 and int(input(self.player_two.player_gesture)) == 0:
    #        print('Player two wins!')
    #        self.player_two_score += 1

    #    elif int(input(self.player_one.player_gesture)) == 0 and int(input(self.player_two.player_gesture)) == 1:
    #        print('Player one wins!')
    #        self.player_one_score += 1

    #    elif int(input(self.player_one.player_gesture)) == 3 and int(input(self.player_two.player_gesture)) == 4:
    #        print('Player one wins!')
    #        self.player_one_score += 1

    #    elif int(input(self.player_one.player_gesture)) == 4 and int(input(self.player_two.player_gesture)) == 2:
    #        print('Player one wins!')
    #        self.player_one_score += 1

    #    elif int(input(self.player_one.player_gesture)) == 0 or 3 and int(input(self.player_two.player_gesture)) == 2:
    #        print('Player two wins!')
    #        self.player_two_score += 1

    #    elif int(input(self.player_one.player_gesture)) == 0 and int(input(self.player_two.player_gesture)) == 1:
    #        print('Player one wins!')
    #        self.player_one_score += 1

    #    elif int(input(self.player_one.player_gesture)) == 4 and int(input(self.player_two.player_gesture)) == 3:
    #        print('Player two wins!')
    #        self.player_two_score += 1

    #    elif int(input(self.player_one.player_gesture)) == 2 and int(input(self.player_two.player_gesture)) == 4:
    #        print('Player two wins!')
    #        self.player_two_score += 1

    #    elif int(input(self.player_one.player_gesture)) == 1 and int(input(self.player_two.player_gesture)) == 2:
    #        print('Player one wins!')
    #        self.player_one_score += 1

    #    elif int(input(self.player_one.player_gesture)) == 2 and int(input(self.player_two.player_gesture)) == 1:
    #        print('Player two wins!')
    #        self.player_two_score += 1

     ## non scoring gesture choices are coming up next

    #    elif int(input(self.player_one.player_gesture)) == 0 and int(input(self.player_two.player_gesture)) == 3 or 4:
    #        print('No damage has been done, please select a new gesture and try again!')
    #        sleep(1)

    #    elif int(input(self.player_one.gesture_choices)) == 3 or 4 and int(input(self.player_two.gesture_choices)) == 0:
    #        print('No damage has been done, please select a new gesture and try again!')
    #        sleep(1)

    #    elif int(input(self.player_one.player_gesture)) == 0 or 1 and int(input(self.player_two.player_gesture)) == 3:
    #        print('No damage has been done, please select a new gesture and try again!')
    #        sleep(1)

    #    elif int(input(self.player_one.player_gesture)) == 3 and int(input(self.player_two.player_gesture)) == 0 or 1:
    #        print('No damage has been done, please select a new gesture and try again!')
   #         sleep(1)

     #   else: 
    #        int(input(self.player_one.player_gesture)) == int(input(self.player_two.player_gesture))
     #       print('Both players have made the same choice, choose again!')
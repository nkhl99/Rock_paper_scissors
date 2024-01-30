import random

the_game = {('r','r'):"tie", ('p','p'):"tie", ('s','s'):"tie",
            ('r','s'):"won", ('s','r'):"lost", ('r','p'):"lost",
            ('p','r'):"won", ('p','s'):"lost", ('s','p'):"won"}

no_of_rounds = ''
computer_input = ['r','p','s']
won = 0
lost = 0

while not no_of_rounds.strip().isdigit():
   print('---- Rock, Paper Scissors Game ----')
   no_of_rounds = input('How many rounds would you like to play? ')

   for my_game in range(int(no_of_rounds)):
      my_input = input('Rock, Paper or Sicssors [r/p/s]? ')

      random_computer_input = random.choice(computer_input)
      if (my_input,random_computer_input) in the_game:
         print('You: ',my_input,' | Computer:',random_computer_input)
         
         if my_input == random_computer_input:
            print('This round is a tie\n')
         elif the_game[(my_input,random_computer_input)] == 'won':
            won+=1
            print('You Won this round\n')
         elif the_game[(my_input,random_computer_input)] == 'lost':
            print('You Lost this round\n')
            lost+=1

   print(f'[Game Summary] Your Points: {won} | Computer points {lost}')
   
   if won > lost:
      print('You won.')
   elif lost > won:
      print('You Lost, Sorry')
   else:
      print('It was a tie.') 

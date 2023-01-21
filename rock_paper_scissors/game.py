rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
your_choice=input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.')
if your_choice != "0"  and your_choice != "1" and your_choice != "2":
  print('please play fair!!!')
else:
  your_choice_int=int(your_choice)
  variables=[rock, paper, scissors]
  pc_choice=(random.choice(variables))
  # pc_choice==scissors
  print(pc_choice, '\ncomputer chose')
  if pc_choice==rock and your_choice_int==0:
    print(rock, '\nit is a draw')
  if pc_choice==paper and your_choice_int==0:
    print(rock, '\nyou lost')
  if pc_choice==scissors and your_choice_int==0:
    print(rock,'\nyou win')
  if your_choice_int==1 and pc_choice==paper:
    print(paper, '\nit is a draw')
  if your_choice_int==1 and pc_choice==rock:
    print(paper, '\nyou win.')
  if your_choice_int==1 and pc_choice==scissors:
    print(paper, '\nyou lost')
  if your_choice_int==2 and pc_choice==scissors:
    print(scissors, '\nit is a draw')
  if your_choice_int==2 and pc_choice==paper:
    print(scissors, '\nyou win')
  if your_choice_int==2 and pc_choice==rock:
    print(scissors, '\nyou win')


l= int(input ('l'))
w= int(input ('w'))
sum=l*2+w*2
print (sum)
import random

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

choices=[rock,paper,scissors]
comp=random.randint(0,2)
user=int(input("pls enter ur choice between 0 to 2:"))
print(f"computer chose: {choices[comp]}")
print(f"u chose:{choices[user]}")

if user>=3 or user<0:
  print("pls enter a valid choice")

elif user==0 and comp==2:
  print("you won")
elif comp==0 and user==2:
  print("you lose")
elif comp>user:
  print("you lose")
elif comp==user:
  print("its a draw")
  


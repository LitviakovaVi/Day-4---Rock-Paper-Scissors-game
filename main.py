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

#Write your code below this line 👇
import random
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if your_choice == 0:
  print(f"Your choise is: {rock}")
elif your_choice == 1:
  print(f"Your choise is: {paper}")
elif your_choice == 2:
  print(f"Your choise is: {scissors}")

computer_choice = int(random.randint(0,2))
if computer_choice == 0:
  print(f"Computer choise is: {rock}")
elif computer_choice == 1:
  print(f"Computer choise is: {paper}")
elif computer_choice == 2:
  print(f"Computer choise is: {scissors}")


if your_choice >= 3 or your_choice < 0:
  print("You typed an invalid number!")
elif your_choice == computer_choice:
  print("Drow. Maybe try againe?")
elif your_choice == 0 and computer_choice == 2:
  print("Сongratulations! You win!")
elif computer_choice > your_choice: 
  print("Sorry, but you lost")
elif your_choice > computer_choice:
  print("Сongratulations! You win!")
elif computer_choice == 0 and your_choice == 2:
  print("Sorry, but you lost")

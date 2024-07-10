import random

entity_dict = {0: "Rock", 1: "Paper", 2: "Scissor"}
choice = int(input("Enter your choice 0,1,2 for rock,paper or scissor\n"))
comp_choice = random.choice(list(entity_dict.keys()))
print(f"Your choice {entity_dict[choice]}\tvs\tComputer's choice {entity_dict[comp_choice]}")

if (choice == comp_choice):
  print("\nDraw")

elif ((choice == 0 and comp_choice == 1) or (choice == 1 and comp_choice == 2)
      or (choice == 2 and comp_choice == 0)):
  print("\nYou lose")
elif ((choice == 0 and comp_choice == 2) or (choice == 1 and comp_choice == 0)
      or (choice == 2 and comp_choice == 1)):
  print("\nYou win")
else:
  print("\nInvalid Input")

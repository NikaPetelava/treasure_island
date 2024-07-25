print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to treasure island!")
print("your mission is to find treasure on island")

choice1 = input("You're on the crossroad. where do you want to go? type 'left' or 'right': \n")
if choice1 == 'left':
  print("Congrats! you passed the first level succesfully!")
  choice2=input("You've come to ocean seashores. There is an island far away the ocean. Type 'Wait' to wait for a boat. Type 'Swim' to swim across: \n")
  if choice2 == 'Wait' or choice2 == 'wait':
    print("Congrats! You passed the second level succesfully!")
    choice3 = input("You've arrived at the island. found a cave in which we found three doors.type 'first door', 'second door', 'third door'. Which one do you choose to open?: \n")
    if choice3 == 'first door':
      print("You fell into the lava. Game Over!")
    elif choice3 == "second door":
      print("You've eaten by a monster. Game Over!") 
    elif choice3 == "third door":
      print("Congrats, You win!")
  else:
    print("You've eaten by Shark. Game Over!") 
else:
  print("Oh no! You've fallen into a hole.")
# არჩევანი 2: მარცხენის არჩევით მივედით ზღვის სანაპიროსთან და შემდეგი არჩევანი გვაქვს გასაკეთებელი: დაველოდოთ გემს თუ გავცუროთ
# არჩევანი 3: მივედით კუნძულზე და დაგვხვდა გამოიქვაბული, რომელშიც დაგვხვდა სამი კარი თუ პირველ კარს გავაღებთ დაგვხვდება ცეცხლი, 
# თუ მეორე კარს გავაღებთ, იქნება გველები და თუ მესამეს გავაღებთ, ვიპოვით განძს

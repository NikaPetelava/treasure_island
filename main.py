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
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;               |
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

choice1 = input('''
    You're on the crossroad. where do you want to go?
    a. left
    b. right
    type the answer here: ''')
if choice1 == 'a':
  print("Congrats! you passed the first level succesfully!")
  print()
  choice2=input('''
    You've come to ocean seashores. There is an island far away the ocean what will you do?.
    a. swim by yourselves
    b. wait for the boat
    type the answer here: ''')
  if choice2 == 'b':
    print("Congrats! You passed the second level succesfully!")
    print()
    choice3 = input('''
    You've arrived at the island. found a cave in which we found three doors. Which one do you choose to open?: 
    a.first door
    b. second door
    c. third door
    type the answer here: ''')
    if choice3 == 'a':
      print("You fell into the lava. Game Over!")
    elif choice3 == "b":
      print("You've eaten by a monster. Game Over!") 
    elif choice3 == "c":
      print("Congrats, You win!")
  else:
    print("You've eaten by Shark. Game Over!") 
else:
  print("Oh no! You've fallen into a hole. Game Over")
# არჩევანი 2: მარცხენის არჩევით მივედით ზღვის სანაპიროსთან და შემდეგი არჩევანი გვაქვს გასაკეთებელი: დაველოდოთ გემს თუ გავცუროთ
# არჩევანი 3: მივედით კუნძულზე და დაგვხვდა გამოიქვაბული, რომელშიც დაგვხვდა სამი კარი თუ პირველ კარს გავაღებთ დაგვხვდება ცეცხლი, 
# თუ მეორე კარს გავაღებთ, იქნება გველები და თუ მესამეს გავაღებთ, ვიპოვით განძს
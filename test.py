
def shipwreck():
  choice = input("You stumble upon a shipwreck.You go in and find two doors. Type 'left' or 'right':\n").lower()
  if choice == 'right':
    print("You found the captain's log with a riddle.")
    print("The riddle says:")
    riddle = input("Its contents are really valuable So hopefully there are no locks That you will have to break through Once you dig up this buried box. Type your answer: \n").lower()
    while True:
      if riddle == "treasure":
        print("You a find Key!")
        break
      else:
        print("Incorrect. Try again!")
        riddle = input("Its contents are really valuable So hopefully there are no locks That you will have to break through Once you dig up this buried box. Your answer is: \n").lower()
  elif choice == "left":
    choice = input("You findd three doors. Type 'left', 'forward' or 'right': \n").lower()
    if choice == "left":
      print("Congratulations! You found the treasure! You Win!")
    elif choice == "forward":
      print("You get attacked by Bats")
      choice = input("What are you going to do? Type 'run' or 'fight': \n").lower()
      if choice == "run":
        print("You got eaten by Bats")
      elif choice == "fight":
        print("You killed Bats")
    else:
      print("You fall into a hole. Game Over.")

  else:
    print("Invalid Input") 

shipwreck()










  

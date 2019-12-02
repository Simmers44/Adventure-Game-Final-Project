import time


name = input("Welcome to Adventure Game! Please input your name: ")
print("Hello,", name, "let's begin. . .")


def display_intro():
  print(name,", you awake in an unfamiliar room with seemingly random objects strewn about the small room around you.")


def intro_choice():
  correct_choice = "check surroundings"
  while True:
    introchoice = input("What do you do?: ")
    if introchoice == correct_choice:
      print("There is a desk with many objects on it including an old desk top computer with a slightly open cabnet to its left.")
      time.sleep(2)
      print("Many papers are scattered on the desk, possibly covering other unseen objects.")
      time.sleep(2)
      print("Directly behind you is a closed and heavily secured locked door blocking your way out from behind.")
      time.sleep(2)
      print("On both the left and right walls are singular doors, they seem to be unlocked.")
      break
    else:
      print("That action could not be done. Please try again.")


def room1_choice1():
  correct1_choice1 = "check desk"
  correct1_choice2 = "check back door"
  correct1_choice3 = "check right door"
  correct1_choice4 = "check left door"
  while True:
    choice1 = input("Now, what do you do?: ")
    if choice1 == correct1_choice1:
      print("The desk is cluttered with mostly crumpled up pieces of paper and notes filled with what seems like nonsense.")
      time.sleep(2)
      print("After shuffling through the mess, you find a rusty pocket knife.")
      time.sleep(2)
      print("It is difficult to move but it is still sharp and may become useful")
      break
    elif choice1 == correct1_choice2:
      print("The door is very heavily secured and is unable to open.")
      time.sleep(2)
      print("You are not getting out this way. Try something else")
    elif choice1 == correct1_choice3:
      print("You approach the door on the right wall. The door is considerable large and may take some force to move it.")
      time.sleep(2)
      print("You push hard on it and it opens easier than you thought.")
      time.sleep(2)
      print("Your momentum makes you stumble and fall into another unfamiliar room.")
      break
      right_room1()
    elif choice1 == correct1_choice4:
      print("You approach the door on the left wall. It looks worse for wear and could almost be broken if pushed too hard.")
      time.sleep(2)
      print("You delicately push on the door but nothing happens.")
      time.sleep(2)
      print("You slowly increse pressure on the door but still nothing.")
      time.sleep(2)
      print("You grow impatient and put your shoulder into your efforts and bust through the door.")
      time.sleep(2)
      print("When looking back the door never actually opened, rather you broke right through the delapidated boards keeping it together.")
      time.sleep(2)
      print("You made it through, an exciting and dangerous way but you made it and as it seems, the door lead to another strange room.")
      break
    else:
      print("That action could not be done. Please try again.")


def right_room1():
  correctr_choice = "check surroundings"
  while True:
    choice2 = input("What will you do now?: ")
    if choice2 == correctr_choice:
      print("You are in another strange room but this one is set up a little differently")
      time.sleep(2)
      print("When looking around you see a bucket in the left corner and a singular door straight ahead.")
      time.sleep(2)
      print("Everything is very cleen in this room... very unusual.")
      break
    else:
      print("That action could not be done. Please try again.")


display_intro()
intro_choice()
room1_choice1()
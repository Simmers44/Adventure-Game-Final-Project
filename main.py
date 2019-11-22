# name (temporary variable name) will be used for the player's name throughout the entire code
name = input("Welcome to Adventure Game! Please input your name: ")
print("Hello,", name, "let's begin. . .")


# Room 1 Example/Early stages. Each room will have its own function specific to it and will be called when approaching/entering each room
print(name,", you awake in an unfamiliar room with seemingly random objects strewn about the small room around you. What do you do?")
choice = input()


# this choice will determine what the player will be doing at that time. At this point very little is possible here with only a few options available.
if choice == "check surroundings":
  print("There is a desk with many objects on it including an old desk top computer with a slightly open cabnet to its left. Many papers are scattered on the desk, possibly covering other unseen objects. Directly behind you is a closed and heavily secured locked door blocking your way out from behind. On both the left and right walls are singular doors, they seem to be unlocked")
  rm1_choice = input("what do you do?")
else:
  print("That action could not be done. Please try again")
  choice = input()


if rm1_choice == "check desk":
  print("The desk is cluttered with mostly crumpled up pieces of paper and notes filled with what seems like nonsense. After shuffling through the mess, you find a rusty pocket knife. It is difficult to move but it is still sharp and may become useful")
  
  knife_choice = input("will you take the knife?")
elif rm1_choice == "check the door behind me":
  print("The door is very heavily secured and is unable to open. You are not getting out this way. Try something else")
  
  rm1_choice = input("what do you do?")
elif rm1_choice == "check the right door":
  print("You approach the door on the right wall. The door is considerable large and may take some force to move it. You push hard on it and it opens easier than you thought. Your momentum makes you stumble and fall into another unfamiliar room.")
elif rm1-choice = "check the left door":
  print("You approach the door on the left wall. It looks worse for wear and could almost be broken if pushed too hard. You delicately puch on the door but nothing happens. You slowly increse pressure on the door but still nothing. You grow impatient and put your shoulder into your efforts and bust through the door. When looking back the door never actually opened, rather you broke right through the delapidated boards keeping it together. You made it through, an exciting and dangerous way but you made it. The door lead to another strange room.")
else:
  print("That action could not be done. Please try again")
 
  rm1_choice = input("what do you do?")
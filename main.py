# name (temporary variable name) will be used for the player's name throughout the entire code
name = input("Welcome to Adventure Game! Please input your name: ")
print("Hello,", name, "let's begin. . .")

# Room 1 Example/Early stages. Each room will have its own function specific to it and will be called when approaching/entering each room
print(name,", you awake in an unfamiliar room with seemingly random objects strewn about the small room around you. What do you do?")
choice = input()

# this choice will determine what the player will be doing at that time. At this point very little is possible here with only a few options available.
if choice == "check surroundings":
  print("There is a desk with many objects on it including an old desk top computer with a slightly open cabnet to its left. Many papers are scattered on the desk, possibly covering other unseem objects. Directly behind you is a closed and heavily secured locked door blocking your way out from behind. On both the left and right walls are singular doors, they seem to be unlocked")
  rm1_choice = input("what do you do?")
elif choice == "Check Surroundings":
  print("There is a desk with many objects on it including an old desk top computer with a slightly open cabnet to its left. Many papers are scattered on the desk, possibly covering other unseem objects. Directly behind you is a closed and heavily secured locked door blocking your way out from behind. On both the left and right walls are singular doors, they seem to be unlocked")
  rm1_choice = input("what do you do?")
elif choice == "Check surroundings":
  print("There is a desk with many objects on it including an old desk top computer with a slightly open cabnet to its left. Many papers are scattered on the desk, possibly covering other unseem objects. Directly behind you is a closed and heavily secured locked door blocking your way out from behind. On both the left and right walls are singular doors, they seem to be unlocked")
  rm1_choice = input("what do you do?")
else:
  print("That action could not be done. Please try again")
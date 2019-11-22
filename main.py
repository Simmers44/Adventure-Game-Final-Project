# name (temporary variable name) will be used for the player's name throughout the entire code
name = input("Welcome to Adventure Game! Please input your name: ")
print("Hello,", name, "let's begin. . .")

# the player class holds the health, weapon, and broad inventory for the character. There is also an add and remove item function that will directly link up to the players inventory. Also included is a damage function that will be used in later environments where the player may choose to encounter an enemy in battle.
class Player():
  def __init__(self, health, weapon):
    self.health = health
    self.weapon = weapon
    self.inventory = {}
  
  def add_item(self, item):
    if item in self.inventory:
      self.inventory[item] += 1
    else:
      self.inventory[item] = 1

  def remove_item(self, item):
    if item in self.inventory:
      self.inventory[item] -= 1
      if self.inventory[item] < 0:
        self.inventory[item] = 0
    else:
      print("Error: %s does not exist." % item)
    
    def damage(self, amount):
      self.health -= amount
      if self.health <= 0:
        print(name, "unfortunately, you have died. You did not escape. Try again. . . if you dare. . .")
        self.health = 0


class Weapon():
  def __init__(self, weapon_name, attack):
    self.weapon_name = weapon_name
    self.attack = attack


# player = Player(name, 100, Weapon(weapon_name, 0))


# Room 1 Example/Early stages. Each room will have its own function specific to it and will be called when approaching/entering each room
print(name,", you awake in an unfamiliar room with seemingly random objects strewn about the small room around you. What do you do?")
choice = input()


# this choice will determine what the player will be doing at that time. At this point very little is possible here with only a few options available. Note: all choices must be written in lower case in order for the action to be read and enacted correctly.
if choice == "check surroundings":
  print("There is a desk with many objects on it including an old desk top computer with a slightly open cabnet to its left. Many papers are scattered on the desk, possibly covering other unseen objects. Directly behind you is a closed and heavily secured locked door blocking your way out from behind. On both the left and right walls are singular doors, they seem to be unlocked.")
  rm1_choice = input("What do you do?: ")
else:
  print("That action could not be done. Please try again")
  choice = input()

# the first room choice will allow the player to check certain things in their surroundings such as the desk and the three seperate doors in the room. By checking the desk, the player is given the opportunity to find their first weapon that can be either picked up or left at the desk. That decision regarding the knife will have consequences ;ater. Two of the doors lead to new rooms, thus creating the first branching path of the game.
if rm1_choice == "check desk":
  print("The desk is cluttered with mostly crumpled up pieces of paper and notes filled with what seems like nonsense. After shuffling through the mess, you find a rusty pocket knife. It is difficult to move but it is still sharp and may become useful")
  
  knife_choice = input("Will you take the knife?: ")
elif rm1_choice == "check the door behind me":
  print("The door is very heavily secured and is unable to open. You are not getting out this way. Try something else")
  
  rm1_choice = input("What do you do?: ")
elif rm1_choice == "check the right door":
  print("You approach the door on the right wall. The door is considerable large and may take some force to move it. You push hard on it and it opens easier than you thought. Your momentum makes you stumble and fall into another unfamiliar room.")
elif rm1-choice == "check the left door":
  print("You approach the door on the left wall. It looks worse for wear and could almost be broken if pushed too hard. You delicately puch on the door but nothing happens. You slowly increse pressure on the door but still nothing. You grow impatient and put your shoulder into your efforts and bust through the door. When looking back the door never actually opened, rather you broke right through the delapidated boards keeping it together. You made it through, an exciting and dangerous way but you made it. The door lead to another strange room.")
else:
  print("That action could not be done. Please try again")
 
  rm1_choice = input("What do you do?: ")


if knife_choice == "yes":
  print("You stuggle to put away the blade of the knife but after some time you get it become loose again. The knife is useful now and may become useful in later situations. You place it in your back pocket and move on.")
  
  # player.append(Player(name, 100, Weapon("knife", 20)))
  # player.add_item("knife")
  rm1_choice = input("Now with the knife, what do you do?: ")
elif knife_choice == "no":
  print("You ponder the thought of taking the knife but ultimately choose to not take it. You place it back down on the desk, turning away. Out of sight, out of mind.")
  
  rm1_choice = input("Now without the knife, what do you do?: ")
else:
  print("That action could not be done. Please try again")
  knife_choice = ("Will you take the knife?: ")
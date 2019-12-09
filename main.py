import time


name = input("Welcome to The Doors Through the Unknown! Please input your name: ")
print("Hello,", name, "let's begin. . .")


def display_intro():
  print(name,", you awake in an unfamiliar room with seemingly random objects strewn about the small room around you.")
  intro_choice()


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
      room1_choice1()
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
      time.sleep(2)
      print("You think for a minute and end up taking the knife.")
      time.sleep(2)
      print("You struggle to close the knife but eventually accomplish your task")
      time.sleep(2)
      print("You put the knife in your pocket just in case you may need it in the future.")
    elif choice1 == correct1_choice2:
      print("The door is very heavily secured and is unable to open.")
      time.sleep(2)
      print("You are not getting out this way. Try something else")
    elif choice1 == correct1_choice3:
      print("You approach the door on the right wall. The door is considerably large and may take some force to move it.")
      time.sleep(2)
      print("You push hard on it and it opens easier than you thought.")
      time.sleep(2)
      print("Your momentum makes you stumble and fall into another unfamiliar room.")
      right_room1()
      break
    elif choice1 == correct1_choice4:
      print("You approach the door on the left wall. It looks worse for wear and could almost be broken if pushed too hard.")
      time.sleep(2)
      print("You delicately push on the door but nothing happens.")
      time.sleep(2)
      print("You slowly increase pressure on the door but still nothing.")
      time.sleep(2)
      print("You grow impatient and put your shoulder into your efforts and bust through the door.")
      time.sleep(2)
      print("When looking back the door never actually opened, rather you broke right through the delapidated boards keeping it together.")
      time.sleep(2)
      print("You made it through, an exciting and dangerous way but you made it and as it seems, the door lead to another strange room.")
      left_room1()
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
      right1_room1()
      break
    else:
      print("That action could not be done. Please try again.")


def left_room1():
  correctl_choice = "check surroundings"
  while True:
    choice3 = input("What will you do now?: ")
    if choice3 == correctl_choice:
      print("As you look around in this new room, you seem confused.")
      time.sleep(2)
      print("This new room is somehow more in disarray than the last one.")
      time.sleep(2)
      print("The entire room is covered in papers with strange symbols scrawled upon them as well as on the walls surrounding you.")
      time.sleep(2)
      print("Taking a further look around you see that there is an overflowing trash can in the middle of the room, full of unsightly items, emanating a horid stentch.")
      time.sleep(2)
      print("Taking your eyes away from the trash, you also see an old arm chair that is ripped to shreds blocking a singular door out of the room.")
      left1_room1()
      break
    else:
       print("That action could not be done. Please try again.")


def right1_room1():
  correctr_choice1 = "check bucket"
  correctr_choice2 = "check door"
  while True:
    rchoice1 = input("What are you going to do?: ")
    if rchoice1 == correctr_choice1:
      print("You are unsure why a bucket is in here but it must be important")
      time.sleep(2)
      print("You approach the lone bucket and look inside.")
      time.sleep(2)
      print("Its empty?!")
      time.sleep(2)
      print("You are utterly confused and frustrated so you kick the bucket across the room.")
      time.sleep(2)
      print("Now that the bucket is gone, you see a note on the ground reading, 'You are almost out, KEEP GOING!'")
    elif rchoice1 == correctr_choice2:
      print("You quickly stride over to the door ahead of you.")
      time.sleep(2)
      print("The door is incredibly tall with tons of ornate features on it.")
      time.sleep(2)
      print("The details are almost scary and demonic in nature but knowing that in order to escape you must keep moving forward, you advance through the door.")
      right_room2()
      break
    else:
      print("That action could not be done. Please try again.")


def left1_room1():
  correctl_choice1 = "check trash"
  correctl_choice2 = "check chair"
  correctl_choice3 = "check door"
  while True:
    lchoice1 = input("What are you going to do?: ")
    if lchoice1 == correctl_choice1:
      print("You incredibly slowly approach the rancid trash can.")
      time.sleep(2)
      print("You tell yourself it is not worth it and turn around and walk away.")
      time.sleep(2)
      print(". . .")
      time.sleep(2)
      print("You sigh and realize theres probably something important in the trash that might help you later so you turn back around and head back to the trash.")
      time.sleep(2)
      print("As you get closer the smell gets worse and worse.")
      time.sleep(2)
      print("You get to the trash and do not see anything useful right away so you begin to shuffle around in the unknown mush of disgust and utter filth.")
      time.sleep(2)
      print("After an uncalled for amount of time going through trash you find nothing and finaly throw up due to the horrible smells and texture of the trash itself.")
      time.sleep(2)
      print("You are so disappointed in yourself and happily move on.")
    elif lchoice1 == correctl_choice2:
      print("You approach the heavily torn chair.")
      time.sleep(2)
      print("Looking at the chair, you see many notes attached to it as well as a few notes inside the stuffing itself.")
      time.sleep(2)
      print("Most of the notes are scribbles or smeared with something you wish to forget about.")
      time.sleep(2)
      print("Of course, the last note you check is the one thats useful, with it reading, 'You are almost out, KEEP GOING!'")
    elif lchoice1 == correctl_choice3:
      print("You approach the door that is blocked by the chair.")
      time.sleep(2)
      print("You give a push to the chair but it breaks as you apply pressure.")
      time.sleep(2)
      print("Whatever, at least you can pass through the door now.")
      time.sleep(2)
      print("You turn the dirty handle and the door opens to yet another room.")
      left_room2()
      break
    else:
      print("That action could not be done. Please try again.")


def right_room2():
  correctr2_choice = "check surroundings"
  while True:
    rchoice4 = input("What will you do now?: ")
    if rchoice4 == correctr2_choice:
      print("This new room catches you off guard.")
      time.sleep(2)
      print("The room looks like a hotel room with all the common things that you would find in a hotel room; a bed, a desk with a T.V. on it and a bathroom.")
      time.sleep(2)
      print("Despite the conventioanal nature of this room, everything is red; the lights, the T.V. screen, all the objects are bathed in an ominous red glow.")
      time.sleep(2)
      print("Given a further look, there is no door leading out of it except for the door leading to the bathroom.")
      right2_room2()
      break
    else:
      print("That action could not be done. Please try again.")


def left_room2():
  correctl2_choice = "check surroundings"
  while True:
    lchoice2 = input("What will you do now?: ")
    if lchoice2 == correctl2_choice:
      print("You did not know how it could get any worse than it was in the last room but you are quickly proven wrong.")
      time.sleep(2)
      print("This new room is an incredibly destroyed bathroom, with sinks broken, urinals smashed, walls with huge holes in them, and doors thrown off their hinges.")
      time.sleep(2)
      print("You see water shooting out from broken sinks and toilets, new and used toilet paper strewn about everywhere, with feces smeared across the walls in the shape of foreign words and phrases.")
      time.sleep(2)
      print("There also does not seem to be any clear ways of getting out of this disgusting room either.")
      time.sleep(2)
      print("Thinking it could not have possibly gotten any worse, you notice that you are currently standing in a puddle and you are unsure if it is water or urine. . . and you choose never to find out for sure.")
      time.sleep(2)
      print("After further investigation you see that there is a singular, pristine, bright white toilet in the middle of all the mess.")
      left2_room2()
      break
    else:
      print("That action could not be done. Please try again.")


def right2_room2():
  correctr2_choice1 = "check bed"
  correctr2_choice2 = "check tv"
  correctr2_choice3 = "check lights"
  correctr2_choice4 = "check bathroom"
  while True:
    rchoice5 = input("What will you do?: ")
    if rchoice5 == correctr2_choice1:
      print("Despite the unnerving nature of the room, you approach the bed.")
      time.sleep(2)
      print("Nothing seems out of place and the bed even seems to be very comfortable.")
      time.sleep(2)
      print("All the stress has gotten to you so you decided to take the risk and take a quick power nap.")
      time.sleep(2)
      print(". . .")
      time.sleep(2)
      print(". . .")
      time.sleep(2)
      print(". . .")
      time.sleep(2)
      print("You awake forty-five minutes later, relatively well rested and suprised nothing bad happened to you while you were resting.")
    elif rchoice5 == correctr2_choice2:
      print("You walk over to the T.V. and see only red static.")
      time.sleep(2)
      print("You find the remote and find only one channel that works.")
      time.sleep(2)
      print("The only channel that seems to be working is a news channel that is from another country with a language that is completely foreign to you.")
      time.sleep(2)
      print("You turn the T.V. off and move on.")
    elif rchoice5 == correctr2_choice3:
      print("The lights are shrouding the room in a red hue.")
      time.sleep(2)
      print("The light switch does not turn off the lights of the lamps and even unplugging it does nothing.")
      time.sleep(2)
      print("Confused, you just move on.")
    elif rchoice5 == correctr2_choice4:
      print("You walk towards the bathroom door and open it.")
      time.sleep(2)
      print("Like expected, it appears to be a normal bathroom with everything covered in red lights.")
      time.sleep(2)
      print("With no better idea you decide to go to use the toilet.")
      time.sleep(2)
      print("Once you were done, you flushed the toilet and the wall next to you swings open to a long hallway.")
      right_hallway()
      break
    else:
      print("That action could not be done. Please try again.")


def left2_room2():
  correctl2_choice1 = "check puddle"
  correctl2_choice2 = "throw up"
  correctl2_choice3 = "check toilet"
  while True:
    lchoice3 = input("What will you do?: ")
    if lchoice3 == correctl2_choice1:
      print("You look down at the puddle you are standing in and wonder what exactly it is.")
      time.sleep(2)
      print("You begin to try and find out but smartly decide not to.")
      time.sleep(2)
      print("Do not want to think about that, moving on")
    elif lchoice3 == correctl2_choice2:
      print("The vile smell of the room and all the unsightly things around you upset your stomache.")
      time.sleep(2)
      print("You start to gag but hold yourself back.")
      time.sleep(2)
      print("But wait, everything is already disgusting around you, so you just let it all out.")
      time.sleep(2)
      print("After a solid three minutes of throwing up, you get your bearings straight, clean yourself off and move on.")
    elif lchoice3 == correctl2_choice3:
      print("You dodge all the gross piles of human waste and debris on your way to the unusually clean toilet.")
      time.sleep(2)
      print("As you finally approach the toilet, and unsuprisingly, it looks like a regular, everyday toilet.")
      time.sleep(2)
      print("Its a nice toilet, no fancy, extra features, just your average commercial toilet, however it is extraordinarily clean.")
      time.sleep(2)
      print("With a straight face, you flush the toilet hoping something might happen.")
      time.sleep(2)
      print("*FLUSH*")
      time.sleep(2)
      print(". . .")
      time.sleep(2)
      print("Nothing happened.")
      time.sleep(2)
      print(". . .")
      time.sleep(2)
      print("All of a sudden, after moments of complete silence and confusion, the ground beneath your feet falls out from under you without any signs of a warning!")
      time.sleep(2)
      print("After landing from that fall, you look up to see a staircase leading up to a long hallway.")
      left_hallway()
      break
    else:
      print("That action could not be done. Please try again.")


def right_hallway():
  correctrh_choice = "check surroundings"
  while True:
    rhallway = input("What will you do?: ")
    if rhallway == correctrh_choice:
      print("The hallway you find yourself in is incredibly long and pretty unnerving.")
      time.sleep(2)
      print("The walls around you are solid concrete with nothing on them.")
      time.sleep(2)
      print("The floor beneathe you is so smoothe you can almost see your reflection in it.")
      time.sleep(2)
      print("You eventually reach the end of this mesmerizing hallway where you encounter yet another note, face down between two doors, one leading right, one leading left.")
      break
    else:
      print("That action could not be done. Please try again.")


def left_hallway():
  correctlh_choice = "check surroundings"
  while True:
    lhallway = input("What will you do?: ")
    if lhallway == correctlh_choice:
      print("The hallway you find yourself in is incredibly long and pretty unnerving.")
      time.sleep(2)
      print("The walls around you are very worse for wear, cluttered with ripped and torn portrait paintings of deformed elites.")
      time.sleep(2)
      print("The portraits are extremely unsettling with strange features originating through generations of inbreeding.")
      time.sleep(2)
      print("You try to keep your eyes down but the floor is littered with fish bones, some with fresh meat still on it.")
      time.sleep(2)
      print("You just close your eyes and run straight forward until you smack into the wall at the end of the hallway.")
      time.sleep(2)
      print("After getting your bearings straight, you notice a note on the ground, face down between two doors, one leading right, one leading left.")
      break
    else:
      print("That action could not be done. Please try again.")


display_intro()
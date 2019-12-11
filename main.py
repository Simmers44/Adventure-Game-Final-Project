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
      right_hallway1()
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
      left_hallway1()
      break
    else:
      print("That action could not be done. Please try again.")


def right_hallway1():
  correctrh_choice1 = "check note"
  correctrh_choice2 = "check right door"
  correctrh_choice3 = "check left door"
  while True:
    rhallway1 = input("What should you do?: ")
    if rhallway1 == correctrh_choice1:
      print("You bend down and pick up the note.")
      time.sleep(2)
      print("Now standing back up, you flip over the note and begin to read it.")
      time.sleep(2)
      print("The note reads, 'You are only three rooms away from escaping,", name,"! You can do it... if you are lucky.'")
      time.sleep(2)
      print("You are shocked!")
      time.sleep(2)
      print("After reading this, tons of questions flood your brain.")
      time.sleep(2)
      print("How do they know your name?")
      time.sleep(2)
      print("Why do they know your name?")
      time.sleep(2)
      print("Who even are they?")
      time.sleep(2)
      print("Are they the ones that put you here?")
      time.sleep(2)
      print("This note angers you and knowing how close you are it causes an overflow of determination and you move on.")
    elif rhallway1 == correctrh_choice2:
      print("You turn to your right and face the door ahead of you.")
      time.sleep(2)
      print("You turn the handle and proceed through the door into yet another room, however this one concerns you.")
      r_right_room()
      break
    elif rhallway1 == correctrh_choice3:
      print("You turn to your left and face the door ahead of you.")
      time.sleep(2)
      print("You turn the handle and proceed through the door into yet another room, however this one actually comforts you.")
      l_right_room()
      break
    else:
      print("That action could not be done. Please try again.")


def left_hallway1():
  correctlh_choice1 = "check note"
  correctlh_choice2 = "check right door"
  correctlh_choice3 = "check left door"
  while True:
    lhallway1 = input("What should you do?: ")
    if lhallway1 == correctlh_choice1:
      print("You push away the fish corpses to fully see the note on the ground.")
      time.sleep(2)
      print("You bend down and pick up the note.")
      time.sleep(2)
      print("Now standing back up, you flip over the note and begin to read it.")
      time.sleep(2)
      print("The note reads, 'You are only three rooms away from escaping,", name,"! You can do it... if you are lucky.'")
      time.sleep(2)
      print("You are shocked!")
      time.sleep(2)
      print("After reading this, tons of questions flood your brain.")
      time.sleep(2)
      print("How do they know your name?")
      time.sleep(2)
      print("Why do they know your name?")
      time.sleep(2)
      print("Who even are they?")
      time.sleep(2)
      print("Are they the ones that put you here?")
      time.sleep(2)
      print("This note angers you and knowing how close you are it causes an overflow of determination and you move on.")
    elif lhallway1 == correctlh_choice2:
      print("You turn to your right and face the door ahead of you.")
      time.sleep(2)
      print("You turn the handle and proceed through the door into yet another room, and unsuprisingly, this next room is destroyed.")
      r_left_room()
      break
    elif lhallway1 == correctlh_choice3:
      print("You turn to your left and face the door ahead of you.")
      time.sleep(2)
      print("You turn the handle and proceed through the door into yet another room, and this one is the strangest one yet.")
      l_left_room()
      break
    else:
      print("That action could not be done. Please try again.")


def r_right_room():
  rcorrectr_choice = "check surroundings"
  while True:
    rightchoicer = input("What do you do?: ")
    if rightchoicer == rcorrectr_choice:
      print("As you step into this new room, you are concerned instantly by how recognizable it is.")
      time.sleep(2)
      print("You notice right away that this room looks like of your childhood bedroom.")
      time.sleep(2)
      print("The walls are covered in movie and band posters however, one poster seems to not be fully stuck to the wall.")
      time.sleep(2)
      print("Continuing to look around, you see your old toys everywhere.")
      time.sleep(2)
      print("There is a strange line of toys leading to your bed and it seems like someone, or something is laying under the covers.")
      r_right_room1()
      break
    else:
      print("That action could not be done. Please try again.")


def l_right_room():
  lcorrectr_choice = "check surroundings"
  while True:
    rightchoicel = input("What do you do?: ")
    if rightchoicel == lcorrectr_choice:
      print("You step through the doorway into a conforting environment.")
      time.sleep(2)
      print("The area around you appears to be a small park area with a pond in the middle.")
      time.sleep(2)
      print("The area is full of friendly wildlife and a park bench near the pond.")
      time.sleep(2)
      print("You are relieved to finally have a moment of peace in this strenuous adventure.")
      l_right_room1()
      break
    else:
      print("That action could not be done. Please try again.")


def r_left_room():
  rcorrectl_choice = "check surroundings"
  while True:
    leftchoicer = input("What do you do?: ")
    if leftchoicer == rcorrectl_choice:
      print("You step through the door on the right wall and see what can only be described as a disaster.")
      time.sleep(2)
      print("The area looks as though an explosion occured, leaving a large crater in the center of this rather large room.")
      time.sleep(2)
      print("Large symbols are drawn all over the walls in different shades of red and brown.")
      time.sleep(2)
      print("One can only assume what the symbols are drawn in.")
      time.sleep(2)
      print("You notice something strange lying in the crater and give a closer look.")
      time.sleep(2)
      print("You notice that in the center of the crater is a blown open safe covered in strange symbols and drawings in what looks like blood.")
      print("Across from you is a door with a ladder leading out of the crater to the door.")
      r_left_room1()
      break
    else:
      print("That action could not be done. Please try again.")


def l_left_room():
  lcorrectl_choice = "check surroundings"
  while True:
    leftchoicel = input("What do you do?: ")
    if leftchoicel == lcorrectl_choice:
      print("You advance through the left door into utter confusion.")
      time.sleep(2)
      print("For once, the room is not a mess and only contains a door on the right wall and a huge, singular object in the middle of the room.")
      time.sleep(2)
      print("The object in the room is a humongous pink teddy bear with a creepy smile stretching from ear to ear with pink and purple jewels for eyes.")
      time.sleep(2)
      print("The bear has to be at least sixty feet tall.")
      time.sleep(2)
      print("The creepiest part is that it is hunched over such that it is staring right at you as you are standing in the doorway.")
      l_left_room1()
      break
    else:
      print("That action could not be done. Please try again.")


def r_right_room1():
  rcorrectr_choice1 = "play"
  rcorrectr_choice2 = "check bed"
  rcorrectr_choice3 = "check poster"
  while True:
    rightchoicer1 = input("What will you do?: ")
    if rightchoicer1 == rcorrectr_choice1:
      print("You have a sudden uncontrollable urge to get down on the ground, pick up some toys and play!")
      time.sleep(2)
      print("You make a lot of noises while you are playing and it is quite adorable.")
      time.sleep(2)
      print("A few minutes of pure fun later, you stand up from the floor and move on.")
    elif rightchoicer1 == rcorrectr_choice2:
      print("You see the very clear line of toys leading to the bed and decide to follow it.")
      time.sleep(2)
      print("You slowly approach the bed, following the path of toys, keeping your eyes locked on the thing in your bed.")
      time.sleep(2)
      print("As you draw nearer, you become frightened to find what may be hiding under the blankets so you look for a weapon.")
      time.sleep(2)
      print("You reach for the pocket knife but you do not feel it.")
      time.sleep(2)
      print("You think to yourself and figure that it must have fallen out of your pocket earlier in your adventure.")
      time.sleep(2)
      print("You think fast and grab a toy lightsaber as your weapon... hey, it is better than nothing, may the force be with you.")
      time.sleep(2)
      print("You nervously step toward the bed, weapon in hand.")
      time.sleep(2)
      print("You slowly grip the blanket and rip it off while at the same time swinging the lightsaber down on the creature.")
      time.sleep(2)
      print("The blade hits with a distinct *SQUEEK*.")
      time.sleep(2)
      print("You are confused and look down to see a stuffed bear.")
      time.sleep(2)
      print("You are very embarassed, throwing the bear across the room, turning your back and moving on.")
    elif rightchoicer1 == rcorrectr_choice3:
      print("You notice that the poster is not fully attached to the wall and choose to investigate it.")
      time.sleep(2)
      print("You notice that the poster is covering something as you get closer to it.")
      time.sleep(2)
      print("You peel off the poster to see a hole large enough to crawl through.")
      time.sleep(2)
      print("The hole stretches into another room.")
      time.sleep(2)
      print("Knowing it is one step closer to getting out of here, you crawl in and advance in your travels.")
      r_right2_room()
      break
    else:
      print("That action could not be done. Please try again.")


def l_right_room1():
  lcorrectr_choice1 = "check pond"
  lcorrectr_choice2 = "check bench"
  while True:
    rightchoicel1 = input("What will you do?: ")
    if rightchoicel1 == lcorrectr_choice1:
      print("You calmly stroll through the peaceful area towards a small pond.")
      time.sleep(2)
      print("As you look around you take a sigh of relief while admiring the many small animals around you.")
      time.sleep(2)
      print("You look into the pond and see a variety of fish from al shapes and sizes as well as some small turtles.")
      time.sleep(2)
      print("This sight makes you smile but you realize that you must keep moving and decide to move on.")
    elif rightchoicel1 == lcorrectr_choice2:
      print("You can not find any signs of escape out of this room so you decide to take a break for a while.")
      time.sleep(2)
      print("You walk over to the park bench and sit down to think.")
      time.sleep(2)
      print("As you lean back in your seat, the whole bench leans back and sets a mechanism in motion that opens a passageway out of this room into yet another unfamiliar room.")
      l_right2_room()
      break
    else:
      print("That action could not be done. Please try again.")


def r_left_room1():
  rcorrectl_choice1 = "check safe"
  rcorrectl_choice2 = "check door"
  while True:
    leftchoicer1 = input("What will you do?: ")
    if leftchoicer1 == rcorrectl_choice1:
      print("You walk towards the edge of the crater, trying to find a safe way down to the bottom.")
      time.sleep(2)
      print("You are unsure about your decision but decide to keep going anyway.")
      time.sleep(2)
      print("Right after you start your careful descent, some unsolid ground beneathe you gives away.")
      time.sleep(2)
      print("You are sent barrelling down the decline, hitting the ground hard over and over again.")
      time.sleep(2)
      print("You tumble down for two minutes until settling down at the bottom.")
      time.sleep(2)
      print("The fall knocked the breath out from you so you struggle to breathe for a few seconds.")
      time.sleep(2)
      print("Finally catching your breath, you stand up and walk a couple feet to the cracked open safe.")
      time.sleep(2)
      print("You swing open the safe door frustrated and find nothing in it.")
      time.sleep(2)
      print("Angry that you hurt yourself for no reason you yell at the top of your lungs and kick the safe as hard as you could.")
      time.sleep(2)
      print("The safe does not move a single inch and your foot throbs in pain from the intense kick.")
      time.sleep(2)
      print("Ypu reel in pain for a while until you could stand and move on.")
    elif leftchoicer1 == rcorrectl_choice2:
      print("You walk over to the tall ladder leaning against the incredibly steep edge of the crater.")
      time.sleep(2)
      print("You grab the ladder about to climb but you are frozen in fear.")
      time.sleep(2)
      print("There is no way to brace the bottom of the ladder so you second guess your decision.")
      time.sleep(2)
      print("Realizing there is no other way out, you start to climb towards the door at the top.")
      time.sleep(2)
      print("Suprisingly, the climb is more stable as you thought.")
      time.sleep(2)
      print("As you get to the top the ladder begins to fall away from the edge of the crater.")
      time.sleep(2)
      print("You act quickly, spinning around to the other side of the falling ladder.")
      time.sleep(2)
      print("Now on the other side of the ladder, you leap to the edge of the crater, barely clinging on to the lip of it.")
      time.sleep(2)
      print("You eventually pull yourself up to the top, looking at the ladder as it crashes in pieces as it hits the ground.")
      time.sleep(2)
      print("You calm yourself down and walk through the door into another room.")
      r_left2_room()
      break
    else:
      print("That action could not be done. Please try again.")


def l_left_room1():
  lcorrectl_choice1 = "check bear"
  lcorrectl_choice2 = "check door"
  while True:
    leftchoicel1 = input("What will you do?: ")
    if leftchoicel1 == lcorrectl_choice1:
      print("You walk toward the giant bear, confused and frightened.")
      time.sleep(2)
      print("You are nervous that it is staring at you with that creepy smile.")
      time.sleep(2)
      print("You nudge the bear and nothing happens.")
      time.sleep(2)
      print("For once, you are relieve that nothing happened and happily move on from this creepy bear.")
    elif leftchoicel1 == lcorrectl_choice2:
      print("You walk past the bear towards the door.")
      time.sleep(2)
      print("Nothing happens to you, you just walk to the door with no trouble.")
      time.sleep(2)
      print("As you start to step through the door you look backward at the bear and notice that the bear is now turned towards you, staring back at you.")
      time.sleep(2)
      print("Extremely scared, you sprint through the door, slamming it behind you.")
      time.sleep(2)
      print("You once again find yourself in a new room.")
      l_left2_room()
      break
    else:
      print("That action could not be done. Please try again.")


def r_right2_room():
  rcorrectr2_choice = "check surroundings"
  while True:
    rightchoicer2 = input("What will you do now?: ")
    if rightchoicer2 == rcorrectr2_choice:
      print("You reach the end of the tunnel and fall out head first into the next room.")
      time.sleep(2)
      print("The hole in the wall is pretty high up and you land right on your head because the fall was so quick and so sudden that you were unable to brace your fall with your hands.")
      time.sleep(2)
      print("You land hard but your fall is easily absorbed by a very soft ground")
      time.sleep(2)
      print("You are thankful that it broke your fall and you give a better look around and you see that you are in a white padded room like those found in an insane asylum.")
      time.sleep(2)
      print("Everything is so bright that you feel like you might go insane.")
      time.sleep(2)
      print("Theres an empty straightjacket in the corner near a door that is thankfully, slightly open.")
      r_right2_room2()
      break
    else:
      print("That action could not be done. Please try again.")


def l_right2_room():
  lcorrectr2_choice = "check surroundings"
  while True:
    rightchoicel2 = input("What will you do now?: ")
    if rightchoicel2 == lcorrectr2_choice:
      print("As you look around this new room you get a sense of nervousness that overcomes you.")
      time.sleep(2)
      print("This room is set up as a pet store with many different sections for various different animals.")
      time.sleep(2)
      print("The problem is though, all of the cages and pens are completely empty.")
      time.sleep(2)
      print("The whole room is awkwardly silent, very strange for a pet store.")
      time.sleep(2)
      print("There seems to be a few cages and tanks that are open, one being a bird cage, one for a dog, and one for a snake.")
      time.sleep(2)
      print("It also looks like the only door out of this room is a maintenance door behind the counter.")
      l_right2_room2()
      break
    else:
      print("That action could not be done. Please try again.")


def r_left2_room():
  rcorrectl2_choice = "check surroundings"
  while True:
    leftchoicer2 = input("What will you do now?: ")
    if leftchoicer2 == rcorrectl2_choice:
      print("Now inside the next room, you are taken aback.")
      time.sleep(2)
      print("You are in a butcher shop!")
      time.sleep(2)
      print("There is blood everywhere with cuts of meat lining all the surfaces in the room.")
      time.sleep(2)
      print("Carcasses line the walls, and it gives you a disgusted feeling.")
      time.sleep(2)
      print("You also find a rusty door behind a large table at the back of the room.")
      time.sleep(2)
      print("All of a sudden you see one of the carcasses swaying and you hear some metal clanging sounds behind a curtain.")
      r_left2_room2()
      break
    else:
      print("That action could not be done. Please try again.")


def l_left2_room():
  lcorrectl2_choice = "check surroundings"
  while True:
    leftchoicel2 = input("What will you do now?: ")
    if leftchoicel2 == lcorrectl2_choice:
      print("Turning around and catching your breath, you begin to look around this new environment.")
      time.sleep(2)
      print("The walls of the room is lined with mirrors spanning from top to bottom.")
      time.sleep(2)
      print("The whole room is empty except for the mirrors and a single door straight ahead of you.")
      time.sleep(2)
      print("Once again, you are very puzzled by the room you are in.")
      l_left2_room2()
      break
    else:
      print("That action could not be done. Please try again.")


def r_right2_room2():
  rcorrectr2_choice1 = "check straightjacket"
  rcorrectr2_choice2 = "check door"
  while True:
    rightchoicer3 = input("What do you do?: ")
    if rightchoicer3 == rcorrectr2_choice1:
      print("You walk over to the straightjacket on the floor.")
      time.sleep(2)
      print("Every step you take squishes into the pads and you have touble keeping your balance.")
      time.sleep(2)
      print("After struggling walking over, you finally reach the jacket.")
      time.sleep(2)
      print("You realize that you have never actually seen a straight jacket in person before so you decide to take a closer look.")
      time.sleep(2)
      print("You pick up the jacket and admire the craftmanship.")
      time.sleep(2)
      print("As you are holding the jacket you spin it around to look at the back and you see that the places where the sleeves are held at the back is broken.")
      time.sleep(2)
      print("The amount of strength that it would take to break a straightjacket is insane, pun not intended.")
      time.sleep(2)
      print("Slightly shocked you drop the jacket back where you found it and move on.")
    elif rightchoicer3 == rcorrectr2_choice2:
      print("You carefully step over towards the door across the room.")
      time.sleep(2)
      print("Walking on the padded floor is still difficult but you manage to reach your destination.")
      time.sleep(2)
      print("You push the heavy door open and step through the doorway.")
      final_room()
      break
    else:
      print("That action could not be done. Please try again.")


def l_right2_room2():
  lcorrectr2_choice1 = "check bird cage"
  lcorrectr2_choice2 = "check dog cage"
  lcorrectr2_choice3 = "check snake tank"
  lcorrectr2_choice4 = "check door"
  while True:
    rightchoicel3 = input("What do you do?: ")
    if rightchoicel3 == lcorrectr2_choice1:
      print("You walk over to the open bird cage in the left side of the store.")
      time.sleep(2)
      print("Nothing seems wrong or broken, just open for some reason.")
      time.sleep(2)
      print("There also seems to have never even held a bird in it before.")
      time.sleep(2)
      print("You close the cage and move along.")
    elif rightchoicel3 == lcorrectr2_choice2:
      print("You decide to check the open dog cage.")
      time.sleep(2)
      print("The cage seems small, it was either for a small breed dog or a young puppy.")
      time.sleep(2)
      print("The tought of a dog reminds you of your dog back home and it makes you smile.")
      time.sleep(2)
      print("You gently close the door to the cage and move on.")
    elif rightchoicel3 == lcorrectr2_choice3:
      print("You go over to the snake tank and you cautious look inside.")
      time.sleep(2)
      print("You are scared of snakes so you close the top of the tank and move on.")
    elif rightchoicel3 == lcorrectr2_choice4:
      print("You walk around the ominous, empty store until you get to the front counter.")
      time.sleep(2)
      print("You see the door behind the counter so you head towards it.")
      time.sleep(2)
      print("Luckily, the door out was unlocked so you open it and step through the doorway.")
      final_room()
      break
    else:
      print("That action could not be done. Please try again.")


def r_left2_room2():
  rcorrectl2_choice1 = "check carcasses"
  rcorrectl2_choice2 = "check noise"
  rcorrectl2_choice3 = "check door"
  while True:
    leftchoicer3 = input("What do you do?: ")
    if leftchoicer3 == rcorrectl2_choice1:
      print("You head towards one of the walls with the carcasses hanging up.")
      time.sleep(2)
      print("You do not get too close because one was moving but you do not see anything that could have moved it.")
      time.sleep(2)
      print("You take a step back after finally getting the smell.")
      time.sleep(2)
      print("It smells horrible so you cover your nose and walk away.")
    elif leftchoicer3 == rcorrectl2_choice2:
      print("You follow the sounds of the clanging, walking as slowly and as quietly as possible.")
      time.sleep(2)
      print("You do not want to alert whatever it is making the noise that you are drawing closer.")
      time.sleep(2)
      print("You reach in your back pocket for your new pocket knife in order to protect yourslef.")
      time.sleep(2)
      print("You reach the curtain and the noises are louder than ever.")
      time.sleep(2)
      print("You are super nervous and adrenaline is pumping through you.")
      time.sleep(2)
      print("With the knife in hand, you silently grab the curtain abd swing it open!")
      time.sleep(2)
      print("You find that the thing making the noises was a large rat running through tons of pots, pans, and other cooking utensils.")
      time.sleep(2)
      print("The rat hisses at you and scurries away.")
      time.sleep(2)
      print("You are left speechless.")
      time.sleep(2)
      print("You close the pocket knife and move on.")
    elif leftchoicer3 == rcorrectl2_choice3:
      print("You approach the heavy door at the back of the shop.")
      time.sleep(2)
      print("The hinges are very rusty and require a lot of force to move it.")
      time.sleep(2)
      print("After some time, you eventually open the door wide enough to slip through.")
      final_room()
      break
    else:
      print("That action could not be done. Please try again.")


def l_left2_room2():
  lcorrectl2_choice1 = "check mirror"
  lcorrectl2_choice2 = "check door"
  while True:
    leftchoicel3 = input("What do you do?: ")
    if leftchoicel3 == lcorrectl2_choice1:
      print("You head towards one of the walls with the mirrors.")
      time.sleep(2)
      print("Of course all you see is your reflection.")
      time.sleep(2)
      print("You stand there for a moment just staring.")
      time.sleep(2)
      print("You get a grin on your face and start to flex and make funny faces.")
      time.sleep(2)
      print("You eventually get tired of this and decide to move on.")
    elif leftchoicel3 == lcorrectl2_choice2:
      print("You approach the door watching your reflection as you go along.")
      time.sleep(2)
      print("You reach the door and turn the handle.")
      time.sleep(2)
      print("You open the door, and not looking back.")
      final_room()
      break
    else:
      print("That action could not be done. Please try again.")


def final_room():
  correctf_choice = "check surroundings"
  while True:
    finalchoice1 = input("What are you going to do?: ")
    if finalchoice1 == correctf_choice:
      print("You find yourself in a long stretching hallway.")
      time.sleep(2)
      print("You can not possibly see the other end of this hallway and decide to venture down.")
      time.sleep(2)
      print("The walk is long and with no end in sight, you become weary with this whole strange adventure debacle.")
      time.sleep(2)
      print("You think back to what you went through to get to this point and you grow ever increasingly tired.")
      time.sleep(2)
      print("All you want to do is give up.")
      time.sleep(2)
      print("You want to just stop where you are, curl up in a ball, and cry.")
      time.sleep(2)
      print("All of the stress is finally getting to you and with this long walk all of the adrenaline has left your body.")
      time.sleep(2)
      print("It feels like you have been here for hours, possibly days.")
      time.sleep(2)
      print("You stop, still with no signs of the hallway ending, and just stand there.")
      time.sleep(2)
      print("Thinking.")
      time.sleep(2)
      print("Pondering.")
      time.sleep(2)
      print("Worrying.")
      time.sleep(2)
      print("But you make a fist, you furrow your brow, and keep going!")
      time.sleep(2)
      print("You think to yourself, believing that this has to be the end and you push on, harder and more determined than ever before!")
      time.sleep(2)
      print("The hallway stretches farther and farther, going up and down, left and right, seemingly in no particular reason.")
      time.sleep(2)
      print("As you press on, words start to appear on the walls.")
      time.sleep(2)
      print("'You are almost there!'")
      time.sleep(2)
      print("'Face your destiny!'")
      time.sleep(2)
      print("After what seemed like hours of running, you reach the end.")
      time.sleep(2)
      print("Now the only thing that stands in your way is a single door with the words, 'Game Warden' written on it.")
      time.sleep(2)
      print("Without hesitation, you swing the door open with an agressive might and charge in!")
      final_room1()
      break
    else:
      print("That action could not be done. Please try again.")


def final_room1():
  correctf_choice1 = "check surroundings"
  while True:
    finalchoice2 = input("What will you do?: ")
    if finalchoice2 == correctf_choice1:
      print("You are breathing heavily.")
      time.sleep(2)
      print("Everything has lead up to this moment.")
      time.sleep(2)
      print("The room is dark, mostly lit from countless computer monitors playing footage of you in the previous rooms.")
      time.sleep(2)
      print("There are some rooms you do not recognize without any footage of you in them.")
      time.sleep(2)
      print("You look behind you and see three other doors.")
      time.sleep(2)
      print("You think to yourself realizing that you could have possibly gotten to this point also by going different ways by making different decisions in the previous rooms.")
      time.sleep(2)
      print("You spin back around, once again examining the area around you.")
      time.sleep(2)
      print("There is a person sitting in a large swivel chair with their back to you with a spotlight shining on them.")
      time.sleep(2)
      print("The spotlight is the only direct source of light in the entire room.")
      time.sleep(2)
      print("You can almost see a large industrial door with a lit up red sign reading 'EXIT' partially obscured by the person in the chair.")
      time.sleep(2)
      print("This is your chance!")
      time.sleep(2)
      print("You can finally escape!")
      time.sleep(2)
      print("Your heart beats with an intense speed.")
      time.sleep(2)
      print("Without a second thought, you hustle to the door but a voice stops you in your tracks.")
      time.sleep(2)
      print("'Do you not want to know who put you here?'")
      time.sleep(2)
      print("'Who created all of this?'")
      time.sleep(2)
      print("You stop where you are.")
      time.sleep(2)
      print("The thought of finding out who did this to you intrigues you so you entertain them for the time being.")
      time.sleep(2)
      print("Now looking at the chair, you yell out, 'Who are you?!'")
      time.sleep(2)
      print("The chair spins around to face you and you are instantly shocked.")
      time.sleep(2)
      print("The person in the chair responds with a smile on their face, 'Well... I am you!'")
      time.sleep(2)
      print("You are stunned.")
      time.sleep(2)
      print("So many questions flow through you.")
      time.sleep(2)
      print("The Game Warden explains, 'I am you, but from the future.'")
      time.sleep(2)
      print("'In your future, my past, you create this experimental environment to find suitable subjects for your master plans.'")
      time.sleep(2)
      print("The Game Warden stands up, gesturing to the chair, 'Please, take a seat, the rightful place for you.'")
      time.sleep(2)
      print("'Accept your destiny and take your rightful place in your future as the infamous Game Warden!'")
      time.sleep(2)
      print("You do not know what to do.")
      time.sleep(2)
      print("You stand there and think about this final critical decision.")
      final_choice()
      break
    else:
      print("That action could not be done. Please try again.")


def final_choice():
  bad_ending = "stay"
  good_ending = "leave"
  while True:
    endingchoice = input("Will you stay or leave?: ")
    if endingchoice == bad_ending:
      print("You stand there completely frozen in shock and awe.")
      time.sleep(2)
      print("You think to yourself for a moment.")
      time.sleep(2)
      print("If this really is you from the future, you can not challenge destiny, let alone change it completely.")
      time.sleep(2)
      print("You have made your decision.")
      time.sleep(2)
      print("You silently walk towards the chair and face the future you.")
      time.sleep(2)
      print("Without breaking eye contact, you take a seat in the chair.")
      time.sleep(2)
      print("The future you revels in your decision yelling, 'Long live the Game Warden!'")
      time.sleep(2)
      print("You spin around, facing the monitors.")
      time.sleep(2)
      print("You look down to see a list of names of possible candidates for the master plan.")
      time.sleep(2)
      print("You decide to start the testing immediately.")
      time.sleep(2)
      print("You are now following your destiny.")
      time.sleep(2)
      print("You smile and wisper to yourself...")
      time.sleep(2)
      print("'Long live the Game Warden...'")
      credits()
      break
    elif endingchoice == good_ending:
      print("You stand there completely frozen in shock and awe.")
      time.sleep(2)
      print("You think to yourself for a moment.")
      time.sleep(2)
      print("If this really is you from the future, you can not challenge destiny, let alone change it completely.")
      time.sleep(2)
      print("You have made your decision.")
      time.sleep(2)
      print("You move your glance to the Game Warden and stare them in the eyes.")
      time.sleep(2)
      print("You throw a punch as hard as you possibly can and strike the Game Warden in the jaw.")
      time.sleep(2)
      print("While the Game Warden is reeling in pain, you run towards the door.")
      time.sleep(2)
      print("The door is locked!")
      time.sleep(2)
      print("You look around for a key but find nothing.")
      time.sleep(2)
      print("The Game Warden is starting to get up so you must hurry!")
      time.sleep(2)
      print("Continuing your frantic search you find a key pad.")
      time.sleep(2)
      print("You must input a code to unlock the door.")
      time.sleep(2)
      print("You try as many combinations of numbers as possible but nothing works.")
      time.sleep(2)
      print("After inputing so many incorrect codes, the panel locks you out from attempting any more options.")
      time.sleep(2)
      print("It is at this moment that the Game Warden fully stands up and starts angrily stumbling towards you.")
      time.sleep(2)
      print("You look at the panel and notice a failsafe where one could scan their haindprint in order to open the door.")
      time.sleep(2)
      print("The Game Warden is still dazed enough to not know what is fully going on but you must still hurry and think of something fast!")
      time.sleep(2)
      print("You say to yourself, 'Wait, if the Game Warden is actually me from the future, then my hand must work to open the door!'")
      time.sleep(2)
      print("You slam your hand onto the panel.")
      time.sleep(2)
      print("Here goes nothing!")
      time.sleep(2)
      print("The light on the panel shines green and the door unlocks!")
      time.sleep(2)
      print("You rush out of the door and slam it behind you, bracing the door with a large, heavy rock that was close by.")
      time.sleep(2)
      print("You can hear the banging and the furious yelling from the now trapped Game Warden still inside.")
      time.sleep(2)
      print("You do not want to stick around so you run off until you find safety.")
      time.sleep(2)
      print("You eventually reach a nearby town where you can lay low and find the authorities.")
      time.sleep(2)
      print("You are so excited to have finally escaped but this experiecnce is burned into your memory.")
      time.sleep(2)
      print("Was that really a future you?")
      time.sleep(2)
      print("Did someone code in your handprint to trick you into believing that the Game Warden is actually you from the future?")
      time.sleep(2)
      print("If that is really you in the future, did you seal destiny by leaving?")
      time.sleep(2)
      print("Are you destined to be the Game Warden?")
      time.sleep(2)
      print("All of these questions take over your mind but you stop them all with a simple statement.")
      time.sleep(2)
      print("'No...'")
      time.sleep(2)
      print("'Screw destiny...'")
      credits()
      break
    else:
      print("That action could not be done. Please try again.")


def credits():
  time.sleep(6)
  print("Thank you for playing The Doors Through the Unknown by Hunter Simmers!")
  time.sleep(2)
  print("Play again to find different paths and options as well as a different ending!")
  time.sleep(2)
  print("Can you find all of the differnt possibilities?")
  time.sleep(2)
  print("It is your destiny!")


display_intro()
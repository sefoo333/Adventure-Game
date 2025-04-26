# Seifeldeen Ali Mohamed Project

import time
import random

# to clear the text when he start the new game
import os

# monestars  
arr = ["dragon" , "dog" , "dinosaur" , "lizard"]

# game run if true the game will run if not the game will close
game_run = True


# choose random monestars
random = random.choice(arr)

# print massege with time
def print_pause(messege):
    print(messege)
    time.sleep(1.5)


# the function use for replay the game if he want the start will clear the old text and start the new game if not the game will close with goodbye massege
def replay():
    replay = ""
    while replay not in ["y","n"]:
     replay = input("Would to replay game again ? [y/n]").lower()
    if replay == "y":
     print_pause("Wooooahooooo , Let's Start The New Game 😀")
     os.system("cls")
     return True
    elif replay == "n":
     print("Okay See You later 😢")
     time.sleep(1)
     print("==========================")
     time.sleep(1)
     print("Game By : Seifeldeen Ali ❤️💻")
     time.sleep(1)
     print("==========================")
     return False



"""
 he will take the action , if he have a pistol ( weakest weapon) 
 the player will lose and if he have any weopens in store or cave (Shutgun - RPG - etc...) except pistol 
 the player will win with sign coins and score
"""
def attackWithWeapon():
     global score
     if weopen == "pistol":
      print_pause("You do your best...")
      print_pause("The pistol really can't hit him and runs out of ammo.")
      print_pause(f"The {random} killed you")
      print_pause("Game Over :D")
      print_pause("==========================")
      print_pause(f"Your Coins:{coins} \n your score:{score} => You Failed To Get A Full Score , Try Again \n you can do more again !")
      print_pause("==========================")
     else:
       score = score + 30
       print_pause(f"As the {random} moves to attack you you raise your You raise your {weopen} to aim at him.")
       print_pause(f"He shoots him and the {random} gets hit and falls from the force of the shot.")
       print_pause(f"The {random} escapes.")
       print_pause(f"You have rid the town of the {random}. You are victorious!")  
       print_pause("You Win :D")
       print_pause("==========================")
       if score == 180:
                  print(f"Your Coins:{coins} \n your score: {score} => wooahoo , You Are A complete The Score ! \n you are a great !")
       elif score < 180:
                              print(f"Your Coins:{coins} \n your score: {score} => You Can Do More For Full Score ! \n you are a great !")
       else:
        print_pause(f"Your Coins:{coins} \n your score:{score} => You are win but you Failed To Get A Full Score , Try Again \n You Can Do it !")
       print_pause("==========================")



# the function if he run from monster the score is missed and return to startGame 
def run():
    global score
    score = score - 20
    print("You run back into the field. Luckily, you don't seem to have been followed.")
    play()
    

# the player will open the door house and fight the monster , what will the player do? , run or fight the monester
def house():
        print_pause("You approach the door of the house")
        print_pause(f"You are about to knock when the door opens and out steps a {random}.")
        print_pause(f"Eep! This is the {random}'s house!")
        print_pause(f"The {random} finds you!")
        print_pause(f"You feel a bit under-prepared for this, what with only having a {weopen} gun")
        house_choose = ""
        while house_choose not in ["1" , "2"]:
             house_choose = input("Would you like to (1) shot Him or (2) run away?")
        if house_choose == "1":
            attackWithWeapon()
        elif house_choose == "2":
             run()
             



# the shop who you can buy your weopen for fight the monester
def shop():
    global shop_visited
    global weopen
    global coins
    global score
    if shop_visited is False:
         score = score + 50
    else:
     print_pause("Score Signed !")

    print_pause("You look and you are afraid of monsters")
    print_pause("Suddenly!, a gun store actually received")
    if shop_visited is False:
         print_pause("You Are Found The 50 coins :D , You Are luckiy ")    
         coins = coins + 50
         shop_visited = True
    print_pause("The Available Weopens is ")
    print_pause("=================")
    print_pause("1.pistol 🔫: 20 coins")
    print_pause("2.RPG 💣: 40 coins")
    print_pause("3.AK 🏹: 80 coins")
    print_pause("=================")

    print_pause("========")
    print_pause(f"your Coins: {coins}")
    print_pause("========")

    weopen_choose = input("Want To Buy ? 1,2,3 ,\n write any word if you want quit to this cave")
    if weopen_choose == "1" and coins >= 20:
        weopen = "pistol"
        print_pause(f"You Are Buy The Pistol Weopen , Current Weopen is {weopen}")
        print_pause("We Are Quit From This Cave !")
        coins = coins - 20
    elif weopen_choose == "2" and coins >= 40:
         weopen = "RPG"
         print_pause(f"You Are Buy The RPG Weopen , Current Weopen is {weopen}")
         print_pause("We Are Quit From This Cave !")
         coins = coins - 40
    elif weopen_choose == "3" and coins >= 80:
         weopen = "AK"
         print_pause(f"You Are Buy The AK Weopen , Current Weopen is {weopen}")
         print_pause("We Are Quit From This Cave !")
         coins = coins - 80
    else:
        print_pause("You do not have enough coins")
        print_pause("We Are Quit to this cave...")
        
    play()
        


# the cave you can take the coins and special weopen from score
def cave():
    global weopen
    global coins
    global cave_State
    global score
    if cave_State is False:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("You are found 30 coins !")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the A New Weopen!")
        print_pause(f"You discard your pistol and take the Shotgun with you.")
        print_pause("You walk back out to the field.")
        print_pause("")
        print_pause("Enter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        weopen = "shotgun"
        coins = coins + 30
        score = score + 100
        cave_State = True
    elif cave_State:
        print_pause("You Are Visited this cave , The Cave is Already empty")
        print_pause("but if you You want to continue the end of this way you can buy a more weopen with your coins")
        

    cave_choose = ""
    while cave_choose not in ["1","2"]:
     cave_choose = input("What would you like to do? \n (Please enter 1 [house] or 2 [continue to cave])")
    if cave_choose == "1":
            house()
    elif cave_choose == "2":
            shop()


# start The Game Function

def startGame():
    print("==================================\n==================================")
    print("Advensture Game 🔫 : By Seifeldeen Ali")
    print("==================================\n==================================")
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {random} is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(f"In your hand you hold your trusty (but not very effective) weapon")
    print("=================")


# the player can choose 1 or 2 for continue the game
def play():
    global wand
    global coins
    global cave_State
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave")
    print_pause("What would you like to do?")
    start = ""
    while start not in ["1","2"]:
      start = input("(Please enter 1 or 2.)")
    if start == "1":
        house()
    elif start == "2":
        cave()


# game controller , i use while loop if game_run true the game running if not the game end

while game_run:
    weopen = "pistol"
    oldwand = "cold"
    coins = 0
    score = 0
    cave_State = False
    shop_visited = False

    startGame()
    play()


# game run value
    game_run = replay();

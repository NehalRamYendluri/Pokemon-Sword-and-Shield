#imports
from art import *
import time, pickle, random
from replit import clear
import os, getkey
import sys

#functions
st = 0.03
fav = '\033[1;93m'
brown = "#8A3324"
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m"
black = "\033[0;30m"
cyan_back = "\033[0;46m"
purple_back = "\033[0;45m"
white_back = "\033[0;47m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
green_back = "\033[0;42m"
pink_back = "\033[0;41m"
grey_back = "\033[0;40m"
grey = '\033[38;4;236m'
bold = "\033[1m"
underline = '\033[4m'
italic = "\033[3m"
darken = "\033[2m" 
invisible = '\033[08m'
reverse = '\033[07m'
reset = '\033[0m'
grey = "\x1b[90m"


def sp(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(st)
    print()


def error():
    print("Enter a valid input")
    time.sleep(0.5)
    os.system("clear")


def clr():
    os.system('clear')


def any_key():
    print(Orange + '\n\n<NEXT>\t[Press any KEY to continue]' + White)
    getkey.getkey()


def welcome():
    tprint('                                  Pokemon')
    tprint('              Sword and Shield')
    any_key()
    time.sleep(0.3)
    clr()


def menu():
    print("\n\n\n                                                   |Play|")
    print("\n                                                   |Settings|")
    print(
        "\n                                                |Links of images|")
    print("\n                                                     |Quit|")
    sp("1.Play")
    sp("2.Settings")
    sp("3.Quit")
    sp("4.Links of all images")
    global option
    option = input(">>> ")
    if option == 1:
        clr()
        name()
    elif option == 2:
        clr()
        print("printing speed is 0.04")
        sp("Do you wanna change it?")
        option = input(">>>")
        if option == 'y':
            try:
                option = int(option)
                sp("set!")
            except:
                error()
                menu()
        elif option == 'n':
            clr()
            menu()
    elif option == 4:
      images()        

def images():
  clr()
  print("Mr.Rose - shorturl.at/rvxX7")
  print("Cufant - shorturl.at/rBIQZ")
  print("Leon - shorturl.at/dhBGK")
  print("Charizard - shorturl.at/rDGR2")
  print("Hop - shorturl.at/vCJS7")
  print("Wooloo - shorturl.at/HZ137")


def name():
    sp(fav + "Please select a name for your charecter" + White)
    option = input(">>>")
    global player_name
    player_name = option
    sp("Are you sure?(y/n)")
    option = input(">>> ")
    if option == "y":
        play()
    elif option == "n":
        clr()
        name()
    else:
        error()
        name()


def play():
    clr()
    sp(fav + "You wake up in the morning and take a shower." + White)
    any_key()
    clr()
    sp(fav +
       "Then you remeber its your big day. Today you turned 10 years old. That means you can be a pokemon trainer."
       + White)
    any_key()
    clr()
    sp(fav+"You get dressed and go downstairs.")
    sp(fav+"You see in the tv a man saying, Welcome and all!"
       )
    any_key()
    clr()
    sp(fav+"Welcome to the wonderful world of Pokémon!")
    sp("Our beloved Galar region is a wonderful place, with thriving nature..."
       )
    time.sleep(0.3)
    sp(fav+"beautiful cities, and many Pokémon with which we share our lives")
    any_key()
    clr()
    sp(fav+"Unknown: So as you know, our society is able to thrive...")
    any_key()
    clr()
    sp(fav+"*Throws a a pokeball to call cufant*")
    sp(fav+"thanks to help from these mysterious creatures we call - Pokémon")
    any_key()
    clr()
    sp(fav+"Rose: My name is Rose, and it is a pleasure to be here")
    any_key()
    clr()
    sp(fav+"Rose: Now turn your gaze to the Galar region's undefeated Champion.")
    sp("It's time for Champion Leon's exhibition match")
    any_key()
    clr()
    sp(fav+"*Leon walks into the stadium with his charizard*")
    sp("You turn off the T.V and")
    any_key()
    clr()
    sp(fav+"suddenly yout friend Hop comes into your house with his pokemon wooloo")
    sp("Hop: Hi, " + player_name + " is that your new T.V?")
    sp("Were you watching Leon's exhibition match?")
    any_key()
    clr()
    sp(fav+"Hop: Come with me, " + player_name + "he should be here any minute!")
    sp(fav+"Your mom walks in")
    any_key()
    clr()
    sp(fav+"Mum: Hop! Didn't expect to see you here today dear.\nIsn't this is the big day?")
    any_key()
    clr()
    play1()
def play1():
    print(fav+"What do you wanna do?")
    print(White+"1.Grab your dad's old bag to go to start the journey(main objective)")
    print("2.Look around the house")
    option = input(">>> ")
    if int(option) == 1:
      play2()
    elif option == 2:
      sp("Where do you wanna go?")
      print("1.Your room")
      print("2.Return")
    else:
      error()
      play1()
def play2():
  sp(fav+"You went to your dad's room and grabbed his old bag.")
  sp("You follow hop outside")
  any_key()
welcome()
menu()
name()


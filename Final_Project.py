# My text based game for my Final Project
# Kaden Seeger


name = input('What is your name: ')

def start2():
    print ('You go to him and he says', name, 'th..th..they took her' )
    print('he points where the scream came from')
    print ('do you go to the scream?')
    print('Yes(1)            No(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print(start1())
        else:
            print("")
            print('other path(2(1)')
    except ValueError:
        print("")
        print('Thats not an option')

def item1():
    print ('before you go to the scream there is a flashlight')
    print('do you take it?')
    print('Yes(1)            No(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print (start1())
        else:
            print("")
            print (start2())
    except ValueError:
        print("")
        print('Thats not an option')

def start1():
    print("As you travel towards the scream you see a old house that was not on any map you checked before you planed the trip")
    print ('when you get closer you see a dark figure running away from the house screaming YOUR NEXT')
    print ('do you go into the house or go where the dark figure went?')
    print ('House(1)            Dark figure(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print ('Next path(1(1)')
        else:
            print("")
            print ('other path(2(1)')
    except ValueError:
        print("")
        print('Thats not an option')

def start():
    print('You, your buddy and his girlfriend are camping in the woods when you get there it is pretty late so you decide to go to bed in the tent')
    print('')
    print("You wake up in the dark forest you see your friend bleeding out on the ground")
    print("You hear a blood curdling scream, do you go towards it or go to your friend?")
    print('Scream(1)            Friend(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print (start1())
        else:
            print("")
            print (start2())
    except ValueError:
        print("")
        print('Thats not an option')
        start2()


def welcome():
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print (start())
        else:
            print("")
            print (welcome())
    except ValueError:
        print("")
        print('Thats not an option')

print('Hello and welcome to my game where all of the options look like this, do you understand?: ')
print('Yes(1)            No(2)')
welcome()
print("")
# the welcome screen


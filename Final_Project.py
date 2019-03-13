# My text based game for my Final Project
# Kaden Seeger


name = input('What is your name: ')
def housekey():
    print('do you go upstairs or downstairs')
    print('upstairs(1)          downstairs(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print(upstairs())
        else:
            print("")
            print(downkey())
    except ValueError:
        print("")
        print('Thats not an option')

def ded(word, num):
    for i in range(num):
        print('')
        print(word)

def hut():
    for i in range(1):
        print('the door closes behind you once you get inside')
        print('you can barely make out the dark figure in the hut with you ')
        print('he tells you he didnt want to do this you should have just left when I killed your buddy ')
        print('he kills you with a rusty kitchen knife')
        ded('ded', 3)
        print('welcome back to my game do you wnat to play again?')
        print('yes(1)           no(2)')
        welcome()

def downstairs():
    print('when you get to the basement you see a big metal vault with blood stains on it')
    print('there is a keyhole in order to open it')
    print('do you look down here for the key or look upstairs?')
    print('look down here(1)            look upstairs(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print('option 1')
        else:
            print("")
            print(upstairs())
    except ValueError:
        print("")
        print('Thats not an option')

def upkeeplooking():
    print('when you look closer there is a chain with a key in it next to the chair ')
    print('you take it because it could be important')
    print('')
    print('you go down stairs')
    housekey()


def downkey():
    print ('now that you have the key you try to put the key in the hole')
    print('it opens')
    print('its your friends girlfriend')
    print('shes dead')
    print('you hear somthing behind you and you turn around and its the dark figure you can tell its an old man')
    print('he aproaches you, and stabs you')
    ded('ded', 3)
    print('welcome back to my game do you want to play again?')
    print('yes(1)           no(2)')
    welcome()


def upstairs():
    print('as you go upstairs you see a rocking chair still rocking back and forth like someone was just there but other')
    print('than that it looks like there is nobody up there anymore')
    print('do you go looking downstairs or do you keep looking up here')
    print('downstairs(1)            Keep looking(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print(downstairs())
        else:
            print("")
            print(upkeeplooking())
    except ValueError:
        print("")
        print('Thats not an option')

def house():
    print('when you go inside it looks like no one has been in there for ages, then there is loud bainging coming from the downstairs')
    print('but there is a blood trail leading upstairs')
    print('do you go upstairs or downstairs')
    print('upstairs(1)          downstairs(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print(upstairs())
        else:
            print("")
            print(downstairs())
    except ValueError:
        print("")
        print('Thats not an option')


def dark():
    print(
        'as go further in the the thick of the woods you start to see a hut that looks about the size of three people')
    print('the door opens as you stop to look at it about 10 feet away')
    print('do you go inside or run to the house?')
    print('inside(1)           run(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print(hut())
        else:
            print("")
            print(house())
    except ValueError:
        print("")
        print('Thats not an option')


def nobuddy():
    print('after a couple of seconds your buddy dies')
    print('you decide to go towards the scream because it could be his girlfriend')
    print('')
    start1()


def start2():
    print('You go to him and he says', name, 'th..th.they took her')
    print('he points where the scream came from')
    print('do you go to the scream?')
    print('Yes(1)            No(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print(start1())
        else:
            print("")
            print(nobuddy())
    except ValueError:
        print("")
        print('Thats not an option')


'''
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
        
        
waiting to figure out how to put this in my code
'''


def start1():
    print(
        "As you travel towards the scream you see a old house that was not on any map you checked before you planed the trip")
    print('when you get closer you see a dark figure running away from the house screaming YOUR NEXT')
    print('do you go into the house or go where the dark figure went?')
    print('House(1)            Dark figure(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print(house())
        else:
            print("")
            print(dark())
    except ValueError:
        print("")
        print('Thats not an option')


def start():
    print(
        'You, your buddy and his girlfriend are camping in the woods when you get there it is pretty late so you decide to go to bed in the tent')
    print('')
    print("You wake up in the dark forest you see your friend bleeding out on the ground")
    print("You hear a blood curdling scream, do you go towards it or go to your friend?")
    print('Scream(1)            Friend(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print(start1())
        else:
            print("")
            print(start2())
    except ValueError:
        print("")
        print('Thats not an option')
        start2()


def welcome():
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print(start())
        else:
            print("")
            print(welcome())
    except ValueError:
        print("")
        print('Thats not an option')


print('Hello and welcome to my game where all of the options look like this, do you understand?: ')
print('Yes(1)            No(2)')
welcome()
print("")
# the welcome screen




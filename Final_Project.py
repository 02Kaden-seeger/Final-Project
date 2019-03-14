'''
# My text based game for my Final Project
# Kaden Seeger
3.14.19
'''
name = input('What is your name: ')
# This will be used later
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
# When you have the key it aks you if you are going to upstairs or downstairs

def ded(word, num):
    while True:
        for i in range(num):
            print('')
            print(word)
        break
# The Dead screen

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
# When you go in the hut he kills you

def yesdog2():

    print('you shake the dog again')
    print('he wakes up')
    print('he bites you because you woke him up')
    print('')
    ded('ded', 3)
    print ('welcome back to my game do you wnat to play again?')
    print('yes(1)           no(2)')
    welcome()
# after you shake the dog twice it kills you

def yesdog():
    print('you shake the dog once')
    print('he doesnt move')
    print('do you shake him again?')
    print('yes(1)           no(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print(yesdog2())
        else:
            print("")
            print(nodog())
    except ValueError:
        print("")
        print('Thats not an option')
# You shake the dog and he doesnt move so you can try again

def nodog():
    print('there is nothing here maybe there is somthing upstairs')
    print('do you want to go upstair or try and wake up the dog?')
    print('upstairs(1)          wake the dog(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print(upstairs())
        else:
            print("")
            print(yesdog())
    except ValueError:
        print("")
        print('Thats not an option')
# if you say no to the dog you have the option to wake him upi agian
    
    
    

def lookdown():
    print('When you look around some more you see a hall way')
    print('you go through the hall way you see a mangy dog')
    print('he has a collar, his name is Atticus')
    print('he isnt moving')
    print('')
    print('he might be dead')
    print('do you try to wake up the dog?')
    print ('yes(1)          no(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print(yesdog())
        else:
            print("")
            print(nodog())
    except ValueError:
        print("")
        print('Thats not an option')
# When look around downstairs and you find a dog


def downstairs():
    print('when you get to the basement you see a big metal vault with blood stains on it')
    print('there is a keyhole in order to open it')
    print('do you look down here for the key or look upstairs?')
    print('look down here(1)            look upstairs(2)')
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print(lookdown())
        else:
            print("")
            print(upstairs())
    except ValueError:
        print("")
        print('Thats not an option')
# Before you get the key and you go downstairs

def upkeeplooking():
    print('when you look closer there is a chain with a key in it next to the chair ')
    print('you take it because it could be important')
    print('')
    print('you go down stairs')
    housekey()
# This is the way to get the key upstairs

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
# after you have the key and go downstairs


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
# The upstairs

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
# When you go inside the house


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
# the decision to go to the house or the dark figure


def nobuddy():
    print('after a couple of seconds your buddy dies')
    print('you decide to go towards the scream because it could be his girlfriend')
    print('')
    start1()
# If you decide to say no for going towards the scream to your friend


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
#If you go to the friend

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
# When you go to the scream


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
# the begining


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

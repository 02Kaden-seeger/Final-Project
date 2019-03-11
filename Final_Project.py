# My text based game for my Final Project
# Kaden Seeger

Name = input('What is your name: ')

def pathbloodcurdalscreamyes():
    print("As you travel towards the scream you see a old house that was not on any map you checked before you  ")
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
    print("You are in a dark forest, the last thing you remember is you planning a trip in the forest with your buddy and his girlfriend.")
    print(" You hear a blood curdling scream, do you go towards it ?")
    print('Yes(1)            No(2)')
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


# My text based game for my Final Project
# Kaden Seeger

Name = input('What is your name: ')
def welcome():
    try:
        choice = int(input('Your Answer: '))
        if choice < 1.1:
            print("")
            print ('Next path(1)')
        else:
            print("")
            print ('other path(2)')
    except ValueError:
        print("")
        print('Thats not an option')

print('Hello and welcome to my game where all of the options look like this, do you understand?: ')
print('Yes(1)            No(2)')
welcome()
print("")
# the welcome screen
# template for "Guess the number" mini-project
import random
import simplegui
import math
number_low = 0
number_high = 100
secret_number = 0
n_guesses = 0 
# input will come from buttons and an input field

# all output for the game will be printed in the console
print 'New game start!' 
print "Please, select between ranges: [0 - 100) and [0 - 1000)!"     

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global number_low 
    global number_high
    global secret_number 
    secret_number = random.randrange(number_low, number_high)
    print

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global n_guesses, number_high
    number_high = 100
    n_guesses =  int(math.ceil(math.log(100,2)))
    print
    print "Start guessing a number in the range [0,100)"
    print "You have ", n_guesses , " guesses for this game:" 
    new_game() 
   

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global n_guesses , number_high
    number_high = 1000
    n_guesses =  int(math.ceil(math.log(1000,2)))
    print
    print "Start guessing a number in the range [0,1000)"
    print "You have", n_guesses , "guesses for this game:" 
    new_game()
   
   
    
def input_guess(guess):
    
    global n_guesses
    global secret_number 
    global number_high
    print "You guessed: ",guess
    n_guesses = n_guesses - 1
    if(n_guesses == 0) :
        print "Sorry, you have no more guesses!!"
        frame.stop()
        return
    print "You have " , n_guesses , " guesses remaining;"
    print 
    if int(guess) == secret_number :
        print "Correct! Congratulations!"
        frame.stop() 
    elif int(guess) < secret_number :
        print "Higher!"
    else: 
        print "Lower!"
              
# create frame

frame = simplegui.create_frame("Input Fields", 300, 200)
# register event handlers for control elements and start frame

frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Guess:", input_guess, 200)
# call new_game 

frame.start()
new_game()
# always remember to check your completed program against the grading rubric
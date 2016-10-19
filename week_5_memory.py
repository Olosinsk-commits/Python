# implementation of card game - Memory
import simplegui
import random

pos = [15, 60]
list1 = range(0, 8)
list2 = range(0, 8)
cards = list1+list2
exposed = False
count = 0

# helper function to initialize globals
def new_game():
    global cards, state, count, exposed 
    count = 0
    exposed = [False]*16
    random.shuffle(cards)
    state = 0
    label.set_text("Moves = 0")  
    print cards 

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, count, cards, card1, card2
    
    i = pos[0]//50
    if exposed[i]== False: exposed[i]=True
    else:
        pass
    
    if state == 0:
        state = 1
        card1 = i
        exposed[card1] = True 
        count += 1

    elif state == 1:
        state = 2
        card2 = i
        exposed[card2] = True

    elif state == 2:
        if cards[card1] != cards[card2]:
            exposed[card1] = False
            exposed[card2] = False
            exposed[i] = True
            state = 1
            card1 = i
            if exposed[card1] == True:
                count +=1
            else:
                pass

        else:
            exposed[card1] = True
            exposed[card2] = True
            state = 1
            card1 = i
            if exposed[i]== True:
                count += 1

    label.set_text("Moves = " + str(count)) 
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global pos, exposed, cards    
    for card_index in range(len(cards)):    
        if exposed[card_index]==True:
            canvas.draw_text(str(cards[card_index]), (pos[0]+card_index*50, pos[1]), 50, "White")
        else:
            canvas.draw_polygon([[(card_index*50)+0, 0], [(card_index*50)+50, 0], [(card_index*50)+50, 100], [(card_index*50)+0, 100]], 4, "Black", "green")
     
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

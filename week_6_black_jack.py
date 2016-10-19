# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []	# create Hand object

    def __str__(self):
        s='Hand contains: '  
        for tmp in self.cards:  
            s+=str(tmp)+' '  
        return s   # return a string representation of a hand
                
    def add_card(self, card):
        self.cards.append(card) # add a card object to a hand        
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust  
        value=0 # compute the value of the hand, see Blackjack video  
        num_ace=0  
        if len(self.cards)==0:  
            return value  
        for index in range(0,len(self.cards)):  
            tmp=self.cards[index].get_rank()  
            value+=VALUES[tmp]  
            if tmp=='A':num_ace+=1  
        if (num_ace>0)and(value+10<=21):value+=10  
        return value 

   
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):# create a Deck object
        self.cards=[]   # create a Deck object  
        for tmp1 in SUITS:  
            for tmp2 in RANKS:  
                card=Card(tmp1,tmp2)  
                self.cards.append(card)  

    def shuffle(self): # use random.shuffle()
        random.shuffle(self.cards) # shuffle the deck 
        
          

    def deal_card(self):
        tmp=self.cards.pop()  # deal a card object from the deck
        #print str(tmp)  
        return tmp
        
    
    def __str__(self):
        s='Deck contains '  # return a string representing the deck  
        if len(self.cards)==0:  
            return s  
        for tmp in self.cards:  
            s+=str(tmp)+' '  
        return s  # return a string representing the deck
            



#define event handlers for buttons
def deal():
    global outcome, in_play

    # your code goes here
    
    in_play = True

def hit():
    # replace with your code below
    global in_play,score,outcome  
    if in_play:  
        tmp=deck.deal_card()  
        player.add_card(tmp)  
        if player.get_value()>21:  
            outcome = "You have busted"  
            in_play=False  
            score-=1  
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():  # replace with your code below  
    global score,outcome,in_play  
    if not in_play:return  
    if player.get_value()>21:    
        outcome = "You have busted! New deal?"  
        score-=1  
    else:  
        while(dealer.get_value()<17):  
            tmp=deck.deal_card()  
            dealer.add_card(tmp)  
    if dealer.get_value()>21:  
        outcome = "dealer have busted! New deal?"  
        score+=1  
    else:  
        if player.get_value()>dealer.get_value():  
            outcome = 'You win! New deal?'  
            score+=1  
        else:  
            score-=1  
            outcome = 'You loose! New deal?'  
              
    in_play=False 	# replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
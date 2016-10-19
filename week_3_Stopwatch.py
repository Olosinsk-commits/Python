# template for "Stopwatch: The Game"

import simplegui
import time

# define global variables
counter = 0
t = 0
x = 0
y = 0
last_stop = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global counter
    a = counter // 600
    b = ((counter//100)%6)
    c = (counter//10)%10
    d = counter%10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global x
    global y
    global last_stop
    timer.stop()
    if counter != last_stop:
        x += 1
        last_stop = counter
        if counter%10 == 0:
                y += 1
    
    
def reset():
    global counter
    global x
    global y
    global last_stop
    timer.stop()
    counter = 0
    y = 0
    x = 0
    last_stop = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global counter
    counter += 1
    return counter


# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), (100, 100), 40, "Orange")
    canvas.draw_text((str(y) + "/" + str(x)), (230, 179), 30, "green")
    

# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)



# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)
button1 = frame.add_button('Start', start, 100)
button2 = frame.add_button('Stop', stop, 100)
button2 = frame.add_button('Reset', reset, 100)
# start frame

frame.start()
#timer.start()
# Please remember to review the grading rubric

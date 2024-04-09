import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# DONE: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (4 pts)
#
#   Now, create a frame called frm_a that has a width of 100 and height of 100.
#
#   Use the bind() method to bind that frame to both a left mouse click and a
#   right mouse click. You will need to bind frm_a twice.
#
#   You will see this in the resources for Session 21, but the event pattern
#   for left click is "<Button-1>" and the event pattern for right click is
#   "<Button-3>".
#
#   When the user presses the left mouse button, the program should print
#   "Left". Similarly, when the user presses the right mouse button, it should
#   print "Right".
#
#   To accomplish this, you will need two event handlers, one for the left
#   mouse click and one for the right mouse click.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
#
###############################################################################

window = tk.Tk()
window.title("window")

frm_a = tk.Frame(master=window, height=100, width=100)

def handle_right(event):
    print("right")

def handle_left(event):
    print("left")

window.bind("<Button-1>", handle_left)
window.bind("<Button-3>", handle_right)

window.mainloop()
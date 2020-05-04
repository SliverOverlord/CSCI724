#GUI code goes here.
from tkinter import *

# Function declairations ------------------

def load_map():
    print("map loaded")

def save_map():
    #saves a map
    print("save map")
    
def select_image():
    print ("select_image")

# End of function declairations -----------

#hello from rajan

#Welcome to the project


#main_window
main_window = Tk()
main_window.title("Fire and Weather Hazard Detection and Warning System")

#set main_windos size
main_window.geometry("1000x1000+30+30")

# Top frame
top_frame = Frame(main_window)
top_frame.pack(side = TOP)

heading = Label(main_window, text = "Fire and Weather Hazard Detection and Warning System", fg = "blue")
heading.pack()

# Map frame
map_frame = Frame(main_window)
map_frame.pack(side = LEFT)

n = Label(map_frame, text = "N", fg = "silver")
n.pack(side = TOP)

e = Label(map_frame, text = "E", fg = "silver")
e.pack(side = LEFT)

w = Label(map_frame, text = "W", fg = "silver")
w.pack(side = BOTTOM)

s = Label(map_frame, text = "S", fg = "silver")
s.pack(side = TOP)

# Left frame
left_frame = Frame(main_window)
left_frame.pack(side = RIGHT)

# Button to select an image
image_button = Button( left_frame, text = "Select an image", fg = "red", command = select_image)

# Bottom frame
bottom_frame = Frame(main_window)
bottom_frame.pack(side = BOTTOM)


# Load map
load_map()


# Main loop
main_window.mainloop()


from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO 

RPi.GPIO.setmode(RPi.GPIO .BCM)

## hardware
yellow_led = LED(11)
green_led = LED(9)
red_led = LED(14)

# creates tk object
win = Tk()
win.title("RPi GUI")
# configure font used is GUI
gui_font = tkinter.font.Font(family = "Arial", size = 12, weight = "bold")

# GUI layout
left_frame = Frame(win)
right_frame = Frame(win)
mid_frame = Frame(win)
left_frame.pack(side = LEFT)
right_frame.pack(side = RIGHT)
mid_frame.pack(side = RIGHT)

## definitions for widgets
# assign variable to capture button variables
rad = tkinter.StringVar()
# set to nothing first to make radio buttons look active
rad.set("0")

## event functions
def toggle_led():
    # turn all off first so only one stays on after radio button is clicked
    yellow_led.off()
    red_led.off()
    green_led.off()
    # get value from radiobutton functions
    value = rad.get()
    # depending on value passed through, the coressponding LED will light up
    if value == "red_led": red_led.on() 
    if value == "yellow_led": yellow_led.on() 
    if value == "green_led": green_led.on()

# Function to cleanly close the GUI
def close():
    RPi.GPIO.cleanup()
    win.destroy()

# Set up labels
label = Label(left_frame)
label.pack()
label.config(text = "Click button to change LED")

### BUTTONS ###

#RED RADIO BUTTON
redLED = Radiobutton(left_frame, text = "Red", variable=rad, value = "red_led", command = toggle_led)
redLED.pack()
# YELLOW RADIO BUTTON
yellowLed = Radiobutton(left_frame, text = "Yellow", variable=rad, value = "yellow_led", command = toggle_led)
yellowLed.pack()
# GREEN RADIO BUTTON
greenLed = Radiobutton(left_frame, text = "Green", variable=rad, value = "green_led", command = toggle_led)
greenLed.pack()

# EXIT BUTTON
exit_button = Button(win, text = "X", font = gui_font, command = close, bg = 'red', height = 1, width = 2)
exit_button.pack(side = BOTTOM)

win.protocol("WM_DELETE_WINDOW", close) # attatch to close function and exit cleanly

win.mainloop() # keep GUI running 

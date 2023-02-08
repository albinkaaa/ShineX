from sense_hat import SenseHat
import time

"""

  Sense HAT Sensors Display
  
  Select Temperature, Pressure, or Humidity  with the Joystick
  to visualize the current sensor values on the LED.
  
  Note: Requires sense_hat 2.2.0 or later

"""

def show_S():
  sense.show_letter("S", back_colour = black)
  time.sleep(.75)

def show_H():
  sense.show_letter("H", back_colour = black)
  time.sleep(.75)

def show_I():
  sense.show_letter("I", back_colour = black)
  time.sleep(.75)
  
def show_N():
   sense.show_letter("N", back_colour = black)
   time.sleep(.75)
  
def show_E():
   sense.show_letter("E", back_colour = black)
   time.sleep(.75)
  
def show_X():
  sense.show_letter("X", back_colour = black)
  time.sleep(.75)
  
def update_screen(mode, show_letter = False):
  if mode == "temp":
    if show_letter:
      show_S()
    temp = sense.temp
    temp_value = temp / 2.5 + 16
    
def butterfly_logo():
    B = black
    O = orange
    P = pink
    W = white
    logo = [
    W, W, W, W, W, W, W, W, 
    W, W, B, W, B, W, W, W,
    O, O, W, B, W, O, O, W, 
    O, P, O, B, O, P, O, W,
    O, O, P, B, P, O, O, W,
    W, W, P, B, P, W, W, W,
    W, W, W, B, W, W, W, W,
    W, W, W, W, W, W, W, W,
    ]
    return logo
    

####
# Intro Animation
####
def Intro_Animation():
    show_S()
    show_H()
    show_I()
    show_N()
    show_E()
    show_X()

    update_screen("temp")

    index = 0
    sensors = ["temp", "pressure", "humidity"]

    s = SenseHat()
    s.low_light = True

    images = [ butterfly_logo, butterfly_logo]

    s.set_pixels(images[count % len(images)]())
    time.sleep(2.75)


sense = SenseHat()

white = (255,255,255)
black = (0, 0, 0)
pink = (255, 0, 255)
orange = (255, 153, 0)

count = round(3*3600/(6*0.75+2.75))
while count >0: 
    Intro_Animation()
    count -= 1
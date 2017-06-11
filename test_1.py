#########
# firstTry.py
# This program is part of the online PS-Drone-API-tutorial on www.playsheep.de/drone.
# It shows how to do basic movements with a Parrot AR.Drone 2.0 using the PS-Drone-API.
# Dependencies: a POSIX OS, PS-Drone-API 2.0 beta or higher.
# (w) J. Philipp de Graaff, www.playsheep.de, 2014
##########
# LICENCE:
#   Artistic License 2.0 as seen on http://opensource.org/licenses/artistic-license-2.0 (retrieved December 2014)
#   Visit www.playsheep.de/drone or see the PS-Drone-API-documentation for an abstract from the Artistic License 2.0.
###########

import pygame
import time
import ps_drone                # Imports the PS-Drone-API
from gpiozero import Button
from signal import pause

drone = ps_drone.Drone()       # Initializes the PS-Drone-API
drone.startup()

########### Take Off #################
def Take_off():
    print("Flying")
    print ("off")
             
    drone.takeoff()                # Drone starts
    time.sleep(7)                  # Gives the drone time to start
    #drone.land()                   # Drone lands'''

########### Land #################
def Land():
    print("Land")
    print ("off")
             
    drone.land()                   # Drone lands'''


############## Forward ##################
def Forward():
    print ("Forward")

    drone.moveForward()            # Drone flies forward...
    time.sleep(1)
    drone.stop()                   # Drone stops...
    time.sleep(1)


############## Backward ##################
def Backward():
    print ("Backward")

    drone.moveBackward()            # Drone flies forward...
    time.sleep(1)
    drone.stop()                   # Drone stops...
    time.sleep(1)

####### move right ######
def Right():
    print ("Move Right")
    drone.moveRight()
    time.sleep(1)
    drone.stop()


### move left ######
def Left():
    print ("Move Left")
    drone.moveLeft()
    time.sleep(1)
    drone.stop()

#### Fly up #####
def Up():
    print ("Up")
    drone.moveUp()
    time.sleep(2)
    drone.stop()


### Fly Down ####
def Down():
    print ("Down")
    drone.moveDown()
    time.sleep(2)
    drone.stop()

### Turn Left ###
def Turn_Left():
    print ("turn left")
    drone.turnLeft()
    time.sleep(1)
    drone.stop()

### Turn_Right ###
def Turn_Right():
    print ("Turn Right")
    drone.turnRight()
    time.sleep(1)
    drone.stop()

########## Buttons ##############
button1 = Button(2) #takeoff
button2 = Button(17) #land

######### Finger Two ##########
button3 = Button(22) #forward
button4 = Button(23) #backwards

### Finger One ###
button1a = Button(14) #left
button1b = Button(15) #right

### Finger Three ###
button3a = Button(8) #Up
button3b =  Button(7) #Down

### Finger Four ####
button9 = Button(5) #Turn_Left
button10 = Button(12) #Turn_Right

########## CONTROLS ###############
button1.when_pressed = Take_off
button2.when_pressed = Land

button3.when_pressed = Forward
button4.when_pressed = Backward

button1a.when_pressed = Right
button1b.when_pressed = Left

button3a.when_pressed = Up
button3b.when_pressed = Down

button9.when_pressed = Turn_Left
button10.when_pressed = Turn_Right

pause()



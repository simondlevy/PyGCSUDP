#!/usr/bin/env python
'''
udptx.py - Fly with Open Pilot GCS through an R/C transmitter connected via cable

Requires: PyGame, PyQuadStick

'''

# Choose your controller ======================================================

#from quadstick.axial.game.logitech import ExtremePro3D as Controller
#from quadstick.axial.game.sony import PS3 as Controller
#from quadstick.axial.rc.spektrum import DX8 as Controller
from quadstick.axial.rc.frsky import Taranis as Controller
#from quadstick.keyboard import Keyboard as Controller

from gcsudp import GCSUDP

DELAY_SEC   = 0.1
ZERO_THRESH = 0.01

from time import sleep

def negone(val):
    return val < -(1-ZERO_THRESH)

def posone(val):
    return val > (1-ZERO_THRESH)

if __name__ == '__main__':

    # Initiate UDP connnection
    gcsudp = GCSUDP()

    # Initiate controller
    controller = Controller(hidden=True)

    # Make sure throttle is in lowest position
    print('Please turn off switches and go throttle down, yaw right to start')
    moved_up = False
    while True:

        # Poll controller throttle
        ((_,_,yaw,throttle),switches) = controller.poll()

        # Never gets all the way to 1.0
        if (not any(switches)) and negone(throttle) and posone(yaw):
            break

    print('Ready... To quit, go throttle down, yaw left')

    # Start a-loopin'!
    while True:

        # Get sticks, switches
        ((pitch,roll,yaw,throttle),(althold,poshold,autopilot)) = controller.poll()

        # Set GCS UDP, reversing roll and adjusting throttle to [0,1]
        gcsudp.set(pitch, yaw, -roll, throttle / 2 + 0.5)

        # Quit on throttle down, yaw left
        if negone(throttle) and negone(yaw):
            break

        # Chill a spell
        sleep(DELAY_SEC)

    # Close UDP connection
    gcsudp.close()

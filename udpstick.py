#!/usr/bin/env python
'''
udpstick.py - Fly with Open Pilot GCS through a Logitech Extreme 3D Pro joystick.

Requires: PyGame

'''

DELAY_SEC = 0.1

import sys
import pygame
import time

from gcsudp import GCSUDP

# Initiate UDP connnection
gcsudp = GCSUDP()

# Intitiate PyGame
pygame.display.init()
pygame.joystick.init()
js = pygame.joystick.Joystick(0)
js.init()

# Make sure throttle is in lowest position
print('Please move the throttle all the way up and back to start')
moved_up = False
while True:

    # Get next PyGame event
    pygame.event.pump()

    axis3 = js.get_axis(3)

    if axis3 < 0:
        moved_up = True

    # Never gets all the way to 1.0
    if moved_up and (axis3 > 0.9999):
        break

print('Ready... To quit, throttle down and click trigger & side button simultaneously')

# Start a-loopin'!
while True:

    # Get next PyGame event
    pygame.event.pump()

    # Get pitch, yaw, roll
    pitch  = js.get_axis(1)
    yaw   = js.get_axis(2)
    roll = js.get_axis(0)

    # Special handling for throttle
    throttle = -js.get_axis(3) / 2 + 0.5

    if throttle < 1e-4:
        throttle = 0

    # Set GCS UDP
    gcsudp.set(pitch, yaw, roll, throttle)

    time.sleep(DELAY_SEC)

    # Quit when till trigger & thumb button pressed simultaneously with throttle off
    if (throttle == 0) and js.get_button(0) and js.get_button(1):
        break

# Close UDP connection
gcsudp.close()

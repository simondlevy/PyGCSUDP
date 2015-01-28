#!/usr/bin/env python
'''
udpstick.py - Fly with Open Pilot GCS through a Logitech Extreme 3D Pro joystick.

Requires: PyGame

Copyright (C) 2014 Simon D. Levy
This code is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU Lesser General Public License
along with this code. If not, see <http://www.gnu.org/licenses/>.
'''

DELAY_SEC = 0.1

# Set these for each OS (Windows 7 values shown here)
PITCH_AXIS      = 1
YAW_AXIS        = 0
ROLL_AXIS       = 3
THROTTLE_AXIS   = 2

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

    throttle = js.get_axis(THROTTLE_AXIS)

    if throttle < 0:
        moved_up = True

    # Never gets all the way to 1.0
    if moved_up and (throttle > 0.9999):
        break

print('Ready... To quit, throttle down and click trigger & side button simultaneously')

# Start a-loopin'!
while True:

    # Get next PyGame event
    pygame.event.pump()

    # Get pitch, yaw, roll
    pitch  = -js.get_axis(PITCH_AXIS)
    yaw   = js.get_axis(YAW_AXIS)
    roll = js.get_axis(ROLL_AXIS)

    # Special handling for throttle
    throttle = -js.get_axis(THROTTLE_AXIS) / 2 + 0.5

    if throttle < 1e-4:
        throttle = 0

    # Set GCS UDP
    print('%+3.3f %+3.3f %+3.3f %+3.3f' % (pitch, roll, yaw, throttle))
    gcsudp.set(pitch, yaw, roll, throttle)

    time.sleep(DELAY_SEC)

    # Quit when till trigger & thumb button pressed simultaneously with throttle off
    if (throttle == 0) and js.get_button(0) and js.get_button(1):
        break

# Close UDP connection
gcsudp.close()

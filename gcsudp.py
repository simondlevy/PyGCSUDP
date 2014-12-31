'''
gcsudp.py  Python API for the Open Pilot Ground Control Station's UDP / Hardware-In-The-Loop control

Copyright (C) 2014 Kevin Finisterre and Simon D. Levy

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
import socket
import struct

class GCSUDP(object):

    def __init__(self, host='localhost', port=2323):
        '''
        Establishes a UDP connection to the Ground Control Station (GCS) on a specified host
        (default localhost) and port (default 2322).
        
        You should first configure GCS for UDP as shown here: 
        '''

        self.sock = socket.socket( socket.AF_INET,socket.SOCK_DGRAM )
        self.host = host
        self.port = port

    def close(self):
        '''
        Closes the UPD connection.
        '''

        self.sock.close()

    def set(self, pitch, yaw, roll, throttle):
        '''
        Sets pitch, yaw, roll, and throttle.  Use values in [-1,+1] for pitch, roll, yaw; in [0,1] for throttle.
        '''

        data = [42, pitch, yaw, roll, throttle, 36]
        send = struct.pack("!dddddd", *data)
        self.sock.sendto(send,(self.host, self.port))



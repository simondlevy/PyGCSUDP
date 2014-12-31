import socket
import struct

class GCSUDP(object):

    def __init__(self, host='localhost', port=2323):

        self.sock = socket.socket( socket.AF_INET,socket.SOCK_DGRAM )
        self.host = host
        self.port = port

    def close(self):

        self.sock.close()

    def set(self, pitch, yaw, roll, throttle):

        data = [42, pitch, yaw, roll, throttle, 36]
        send = struct.pack("!dddddd", *data)
        self.sock.sendto(send,(self.host, self.port))



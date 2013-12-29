import socket

MAX_UDP_SIZE = 4096

class UdpLinkImpl:
    def __init__(self, local, remote):
        self.recv_callback = lambda x: None
        self.local = local
        self.remote = remote
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.local)

    def send(self, data):
        self.sock.sendto(data, self.remote)

    def get_fd(self):
        return self.sock

    def recv(self):
        data, addr = self.sock.recvfrom(MAX_UDP_SIZE)
        self.recv_callback(data)
import socket
import time
import threading


def print_client_request():
    for client in client_list:
        if client.clientsocket is None:
            client_list.remove(client)
        elif client.timestamp_request is not None:
            print(client)


class client_thread(threading.Thread):
    """docstring for client_thread"""

    def __init__(self, ip, port, clientsocket):
        super(client_thread, self).__init__()
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        self.name = self.clientsocket.recv(255).decode()
        print('Nouveau client: {}\t{}'.format(self.name, self.ip))

        self.timestamp_request = None
        self.msg = None

    def run(self):
        while True:
            msg = self.clientsocket.recv(255).decode()
            if msg == 'exit':
                self.clientsocket.close()
                print('Disconnecting {}\t{}'.format(self.ip, self.name))
                self.clientsocket = None
                break
            if self.timestamp_request is None:
                self.timestamp_request = time.time()
            self.msg = msg
            print_client_request()

    def delta_tmstp(self):
        if self.timestamp_request is not None:
            struc_time = time.gmtime(time.time() - self.timestamp_request)
            delta = time.strftime("%H:%M:%S", struc_time)
            return delta
        else:
            return 'XX:XX:XX'

    def __repr__(self):
        return '{}\t{}\t{}\t{}'.format(self.delta_tmstp(),
                                       self.ip,
                                       self.name,
                                       self.msg)


port_ecoute = 5000
socket_ecoute = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_ecoute.bind(('', port_ecoute))

client_list = []

while True:
    socket_ecoute.listen()
    client, adress = socket_ecoute.accept()
    client_object = client_thread(ip=adress[0],
                                  port=adress[1],
                                  clientsocket=client)
    client_object.start()
    client_list.append(client_object)

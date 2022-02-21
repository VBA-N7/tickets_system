import socket
import re


class client(object):
    """docstring for client"""

    def __init__(self, IP, port, name=None):
        super(client, self).__init__()
        self.server_IP = IP
        self.server_port = port
        self.connexion = None
        self.name = name
        self.connect()

    def connect(self):
        self.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connexion.settimeout(5)  # timeout 5s
        try:
            print('Trying to connect to {}'.format(self.server_IP))
            self.connexion.connect((self.server_IP, self.server_port))
        except socket.timeout:
            print('Unable to connect to the server')
            self.connexion = None
        else:
            print("Connection on {}".format(self.server_port))
            self.connexion.send(self.name.encode())

    def close_connexion(self):
        print('Closing {} / {} connexion'.format(self.server_IP,
                                                 self.server_port))
        self.connexion.close()
        self.connexion = None

    def send_request(self):
        request = input('Entrez un message pour envoyer une requete: ')
        self.connexion.send(request.encode())
        if request.find('exit') != -1:
            self.close_connexion()


print('Launching client script')

# hote = "localhost"
# hote = "192.168.1.17"
# port = 5000
# name = 'Vincent'

while True:
    hote = input("Entrez l'adresse IP du serveur (XXX.XXX.XXX.XXX): ")
    if re.search('^([0-9]{1,3}[.]){3}([0-9]{1,3}){1}$', hote) is None:
        print("Mauvais format d'IP")
        continue
    break

while True:
    port = input('Entrez le port de connexion du serveur: ')
    if re.search('^[0-9]{1,5}$', port) is None:
        print('Mauvais format de port')
        continue
    port = int(port)
    break

while True:
    name = input('Entrez un nom de groupe (single word 15 letters max without whitespace and number): ')
    if re.search('^[a-zA-Z]{1,15}$', name) is None:
        print('Mauvais format de nom')
        continue
    break


my_client = client(IP=hote, port=port, name=name)

if my_client.connexion is not None:
    while my_client.connexion is not None:
        my_client.send_request()

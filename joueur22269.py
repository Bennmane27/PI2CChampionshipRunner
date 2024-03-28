import socket

def connect_to_server():
    # Créer un socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Adresse du serveur
    server_address = ("localhost", 3000)

    # Connexion au serveur
    s.connect(server_address)

    print("Connecté au serveur sur le port 3000")

connect_to_server()
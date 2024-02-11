import socket
import os


class Server:
    """ This is a class for defining the server
    Attributes
    ----------

    Inheritance: None

    Methods:
        connection -> Establishes a connection for the server
        receive_data -> Receives data from the client in real time.

    """

    def __init__(self, ip, port):
        """ A constructor for the server
        :param ip -> The ip address of the server
        :param port -> The port of the server

        """
        self.ip = ip
        self.port = port

    def connection(self):
        """ This establishes a connection to the server"""
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_server.bind((self.ip, self.port))
        socket_server.listen()
        conn, address = socket_server.accept()
        return conn, address

    def receive_data(self, conn):
        """ This receives data from the client in real time.
        :param conn-> Client connection

        """
        data = conn.recv(1024)
        return data


if __name__ == "__main__":
    ip = os.environ["SERVER_IP"]
    port = int(os.environ["SERVER_PORT"])
    server_class = Server(ip, port)
    conn, _ = server_class.connection()
    while True:
        data = server_class.receive_data(conn)
        if not data:
            break
        print(data.decode())
        conn.sendall(data)

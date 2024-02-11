import socket
import os


class Client:
    """ This client connects to the server and sends messages to it
    :param ip -> The ip address of the server
    :param port -> The port of the server

    """
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def connect_to_server(self):
        """
        This method connects to the server using Internet protocol and TCP
        Returns a socket connection as output
        """
        socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_client.connect((self.ip, self.port))
        return socket_client

    def send_data(self, conn, message: str):
        """
        This method sends messages to the server in real time.
        It uses an input to request for a message.
        You can terminate this connection by typing bye

        :param conn -> The client connection established
        in self.connect_to_server()

        :param message: str -> The message you want to send
        to the server
        """
        to_bytes = message.encode()
        conn.sendall(to_bytes)
        data = conn.recv(1024)
        return data


if __name__ == "__main__":
    ip = os.environ["SERVER_IP"]
    port = int(os.environ["SERVER_PORT"])
    client_class = Client(ip, port)
    conn = client_class.connect_to_server()
    while True:
        to_send = input(("What are you sending"
                         "...(Enter a value or press bye) to end\n"))
        if to_send.lower() != "bye":
            data = client_class.send_data(conn, to_send)
            if not data:
                break
        else:
            break

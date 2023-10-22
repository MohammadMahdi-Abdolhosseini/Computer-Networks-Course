# Mohammad Mahdi Abdolhosseini
# std.num: 810 198 434
# Computer Network: Computer Assignment

import socket
import threading

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.username = None
        self.client_socket = None

    def start(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print("Connected to the server!")

        self.username = input("Choose username: ")
        self.client_socket.sendall(self.username.encode())

        client_thread = threading.Thread(target=self.receive_messages)
        client_thread.start()

        self.join_group('General')

        while True:
            message = input()
            if message:
                self.send_message(message)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                print(message)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def send_message(self, message):
        self.client_socket.sendall(message.encode())

    def join_group(self, group_name):
        self.send_message(f"join {group_name}")

    def leave_group(self, group_name):
        self.send_message(f"leave {group_name}")

    def create_group(self, group_name):
        self.send_message(f"create {group_name}")

    def send_public_message(self, group_name, message):
        self.send_message(f"public {group_name} {message}")

    def send_private_message(self, receiver, message):
        self.send_message(f"private {receiver} {message}")

    def exit_program(self):
        self.send_message("exit")
        self.client_socket.close()
        exit()


if __name__ == '__main__':
    client = Client('127.0.0.1', 9000)
    client.start()

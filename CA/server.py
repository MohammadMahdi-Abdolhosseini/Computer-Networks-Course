# Mohammad Mahdi Abdolhosseini
# std.num: 810 198 434
# Computer Network: Computer Assignment

import socket
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.clients = []
        self.groups = {'General': []}

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server is listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connected with {client_address[0]}:{client_address[1]}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        client_username = client_socket.recv(1024).decode()
        self.clients.append((client_username, client_socket))
        self.send_message(client_socket, f'You are {client_username}')


        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    self.handle_message(client_username, message)
                else:
                    self.remove_client(client_username)
                    break
            except Exception as e:
                print(f"Error handling client: {e}")
                self.remove_client(client_username)
                break

    def handle_message(self, sender, message):
        if message.startswith('create'):
            group_name = message.split()[1]
            self.groups[group_name] = []
            self.send_message_to_group('General', f"New group chat with name '{group_name}' has created")

        elif message.startswith('join'):
            group_name = message.split()[1]
            if group_name in self.groups:
                self.groups[group_name].append(sender)
                self.send_message_to_group(group_name, f"{sender} joined the '{group_name}'")
            else:
                self.send_message_to_client(sender, f"Group '{group_name}' does not exist")

        elif message.startswith('leave'):
            group_name = message.split()[1]
            if group_name in self.groups and sender in self.groups[group_name]:
                self.groups[group_name].remove(sender)
                self.send_message_to_group(group_name, f"{sender} left the '{group_name}'")
            else:
                self.send_message_to_client(sender, f"You are not a member of the '{group_name}'")

        elif message == 'groups':
            group_list = '\n'.join(self.groups.keys())
            self.send_message_to_client(sender, f"Available groups:\n{group_list}")

        elif message == 'users':
            user_list = '\n'.join([username for username, _ in self.clients])
            self.send_message_to_client(sender, f"Online users:\n{user_list}")

        elif message.startswith('public'):
            group_name, content = message.split(maxsplit=2)[1:]
            if group_name in self.groups and sender in self.groups[group_name]:
                self.send_message_to_group(group_name, f"In '{group_name}', {sender} : {content}")
            else:
                self.send_message_to_client(sender, f"You are not a member of group '{group_name}'")

        elif message.startswith('private'):
            _, receiver, content = message.split(maxsplit=2)
            self.send_private_message(sender, receiver, content)

        elif message == 'exit':
            self.remove_client(sender)

    def send_message(self, client_socket, message):
        client_socket.sendall(message.encode())

    def send_message_to_client(self, client_username, message):
        for username, client_socket in self.clients:
            if username == client_username:
                self.send_message(client_socket, message)

    def send_message_to_group(self, group_name, message):
        for username, client_socket in self.clients:
            if username in self.groups[group_name]:
                self.send_message(client_socket, message)

    def send_private_message(self, sender, receiver, content):
        for username, client_socket in self.clients:
            if username == receiver:
                self.send_message(client_socket, f"Private message from {sender} : {content}")

    def remove_client(self, client_username):
        for username, client_socket in self.clients:
            if username == client_username:
                self.clients.remove((username, client_socket))
                client_socket.close()
                print(f"{client_username} has disconnected.")
                self.send_message_to_group('General', f"{client_username} has left group chat 'General'")
                break


if __name__ == '__main__':
    server = Server('127.0.0.1', 9000)
    server.start()

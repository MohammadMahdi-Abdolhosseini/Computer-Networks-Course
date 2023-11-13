# Computer-Networks-Course
Computer networks course projects

# Final Project: Chatroom with Socket Programming

A simple chatroom implementation using Python with socket programming. This project allows users to connect to a server, join different groups, and chat in public or private.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Commands](#commands)
- [Example](#example)

## Features

- Public chat in groups
- Private messaging between users
- Group creation, joining, and leaving
- List available groups and online users
- Handling multiple clients concurrently using threading.
- Easy-to-use command-line interface

## Usage

1. Run the server:

   ```bash
   python server.py
   ```

   The server will be running on `127.0.0.1:9000` by default.

2. Open multiple terminals and run clients:

   ```bash
   python client.py
   ```

   Choose a username when prompted.

3. Start chatting!

## Commands

- `create [group-name]`: Create a new group.
- `join [group-name]`: Join an existing group.
- `leave [group-name]`: Leave a group.
- `groups`: List all available groups.
- `users`: List online users.
- `public [group-name] [message]`: Send a public message to a group.
- `private [user-name] [message]`: Send a private message to a specific user.
- `exit`: Exit the chatroom.

## Example

### Server

```bash
python server.py
Server is listening on 127.0.0.1:9000
Connected with ('127.0.0.1', 54546)
Connected with ('127.0.0.1', 54436)
Connected with ('127.0.0.1', 37842)
```

### Client 1

```bash
python client.py
Choose username: Jim
Connected to the server!
You joined the room 'General'
George joined the room 'General'
Michael joined the room 'General'
join G1
You have joined in group chat 'G1' successfully!
Michael has joined in group chat 'G1'
public G1 Hey Michael, What's up?
In group G1, Michael : Not much!
George has joined in group chat 'G1'
leave G1
You have left group chat 'G1' successfully!
exit
```

### Client 2

```bash
python client.py
Choose username: George
Connected to the server!
You joined the room 'General'
Michael joined the room 'General'
users
online users:
Jim
George
Michael
private Michael Could you help me join a group chat?
Private message from Michael : sure
groups
available groups:
General
G1
join G1
You have joined in group chat 'G1' successfully!
Jim has left group chat 'G1'
```

### Client 3

```bash
python client.py
Choose username: Michael
Connected to the server!
You joined the room 'General'
create G1
New group chat with name 'G1' has created successfully!
join G1
You have joined in group chat 'G1' successfully!
Private message from George : Could you help me join a group chat?
private George sure
In group G1, Jim : Hey Michael, What's up?
public G1 Not much!
George has joined in group chat 'G1'
Jim has left group chat 'G1'
```

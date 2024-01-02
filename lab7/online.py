class User:
    def __init__(self, name):
        self.name = name
        self.messages = []

    def send_message(self, recipient, message):
        new_message = {"sender": self.name, "recipient": recipient.name, "message": message}
        recipient.receive_message(new_message)
        self.messages.append(new_message)

    def receive_message(self, message):
        self.messages.append(message)


class MessagingSystem:
    def __init__(self):
        self.users = []

    def register_user(self, user):
        self.users.append(user)

    def get_all_messages(self, user):
        return user.messages
    
# Instantiate MessagingSystem
messaging_system = MessagingSystem()

# Create users
luffy = User("Monkey D. Luffy")
zoro = User("Roronoa Zoro")
nami = User("Nami")

# Register users in the messaging system
messaging_system.register_user(luffy)
messaging_system.register_user(zoro)
messaging_system.register_user(nami)

# Users send messages to each other
luffy.send_message(zoro, "Hey Zoro, let's go on an adventure!")
zoro.send_message(luffy, "Sure, Captain! I'm ready.")

nami.send_message(luffy, "Luffy, don't forget to bring money for navigation charts.")
luffy.send_message(nami, "Got it, Nami! We'll gather treasures on our way!")

# Users view their messages
print(f"{luffy.name}'s Messages:")
for message in messaging_system.get_all_messages(luffy):
    print(f"{message['sender']} to {message['recipient']}: {message['message']}")

print(f"\n{zoro.name}'s Messages:")
for message in messaging_system.get_all_messages(zoro):
    print(f"{message['sender']} to {message['recipient']}: {message['message']}")

print(f"\n{nami.name}'s Messages:")
for message in messaging_system.get_all_messages(nami):
    print(f"{message['sender']} to {message['recipient']} : {message['message']}")


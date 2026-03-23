class MessageBus:

    def __init__(self):
        self.messages = []

    def send(self, sender, receiver, content):
        msg = {
            "from": sender,
            "to": receiver,
            "content": content
        }
        self.messages.append(msg)
        return msg

    def get_messages_for(self, receiver):
        return [m for m in self.messages if m["to"] == receiver]

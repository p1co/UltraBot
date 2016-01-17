def main(t, t1, client):
        client.send_message(t.channel, "Hello, world!")
def help(message, args, client):
        client.send_message(message.channel,"A nerdier ping. Usage: !hello")

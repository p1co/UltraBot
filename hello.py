def main(t, t1, client):
        client.send_message(t.channel, "Hello, world!")
def help(message, args, client):
        print("A nerdier ping. Usage: !hello")

def main(t, t1, client):
        client.send_message(t.channel, "A help command will go here one day!")
def help(message, args, client):
        client.send_message(message.channel,"so meta. Usage: !help [command]")

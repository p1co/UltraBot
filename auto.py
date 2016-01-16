def main(t, client):
        str = t.content
        if "should of" in str.lower():
            client.send_message(t.channel, "You mean SHOULD HAVE")
            return True
        elif "would of" in str.lower():
            client.send_message(t.channel, "You mean WOULD HAVE")
            return True
        elif "could of" in str.lower():
            client.send_message(t.channel, "You mean COULD HAVE")
            return True
        elif "definately" in str.lower() or "definetly" in str.lower():
            client.send_message(t.channel, "You mean DEFINITELY")
            return True
        elif " ur " in str.lower():
            client.send_message(t.channel, "You mean YOUR/YOU'RE")
            return True
        elif " u " in str.lower():
            client.send_message(t.channel, "You mean YOU")
            return True
        elif "u wot" in str.lower() or "fight me" in str.lower() or "fite me" in str.lower():
            client.send_message(t.channel, "(╯°□°)╯︵ ┻━┻")
            client.send_message(t.channel, "DON'T PICK ON MY FRIENDS")
            client.send_message(t.channel, "You've made a very powerful enemy")
            return True

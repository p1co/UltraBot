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
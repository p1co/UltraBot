#This module named 'auto' will always be loaded as the auto module, which means that any text that isn't a command will be run through the main function within this module.
#You can edit this file to include a custom function, meaning that you can do something when someone says a specific phrase.

def main(t, client):
        str = t.content
        if "should of" in str.lower():
            client.send_message(t.channel, "You mean SHOULD HAVE")
            return True
        elif "would of" in str.lower():
            client.send_message(t.channel, "You mean WOULD HAVE")
            return True
        elif "doot doot" in str.lower():
            client.send_message(t.channel, "thank mr skeltal")
            return True
        elif "could of" in str.lower():
            client.send_message(t.channel, "You mean COULD HAVE")
            return True
        elif "definately" in str.lower() or "definatly" in str.lower() or "definantly" in str.lower() or "definetly" in str.lower() or "definently" in str.lower() or "defiantly" in str.lower():
            client.send_message(t.channel, "You mean DEFINITELY")
            return True
        elif " ur " in str.lower():
            client.send_message(t.channel, "You mean YOUR/YOU'RE")
            return True
        elif " u " in str.lower():
            client.send_message(t.channel, "You mean YOU")
            return True
        elif "me and" in str.lower() or "me &" in str.lower():
            client.send_message(t.channel, "You mean AND I")
            return True
        elif "and me" in str.lower() or "& me" in str.lower():
            client.send_message(t.channel, "You mean AND I")
            return True
        elif "u wot" in str.lower() or "fight me" in str.lower() or "fite me" in str.lower():
            client.send_message(t.channel, "(╯°□°)╯︵ ┻━┻")
            client.send_message(t.channel, "DON'T PICK ON MY FRIENDS")
            client.send_message(t.channel, "You've made a very powerful enemy")
            return True
        elif "yolo" in str.lower():
            client.send_message(t.channel, "No. Just no.")
        elif "sp00ky" in str.lower():
            client.send_message(t.channel, "https://www.youtube.com/watch?v=q6-ZGAGcJrk")

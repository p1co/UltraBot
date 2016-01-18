#Salt-generating module for the bot.

import random
SaltLinks = [
    "http://vignette4.wikia.nocookie.net/gfaqssb/images/0/03/PJSalt.jpg/revision/latest?cb=20151213112803",
    "http://img1.ak.crunchyroll.com/i/spire4/1f6f0dc88ec848aa2ff3d0e8354ad8db1412410883_full.jpg",
    "http://ingredientsnetwork.com/wp-content/uploads/2015/09/too_much_salt_360.jpg",
    "http://www.seasaltsuperstore.com/Userfiles/Replacement-Pics/shutterstock_70709578.jpg-Sea-salt-mounds.jpg",
]

maxNum = len(SaltLinks) - 1

def main(message, comms, client):
    if (len(comms) == 1):
        ranNum = random.randint(0, maxNum)
        client.send_message(message.channel, SaltLinks[ranNum])
    else:
        if int(comms[1]) <= maxNum + 1:
            client.send_message(message.channel, SaltLinks[int(comms[1]) - 1])

def help(message, comms, client):
    client.send_message(message.channel, "For use when someone's being a little bitch. Usage: !salt")

import dischord

detils = open("login.txt", "r")
login = detils.read().split(",")
detils.close()

client= dischord.Client()
client.login(detils[0], detils[1])

def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


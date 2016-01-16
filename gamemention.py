import discord

client = discord.Client()
client.login("james@hurcomb.net", "ALongerPassword")

def listContains(listMain, test):
    for a in listMain:
        if a.name.lower() == test:
            return True


class newCommands:
    def mention(message, args):
        members = client.get_all_members()
        users = []
        toMessage = "Mentioning all members in GTA: "
        for member in members:
            print(member.name)
            if listContains(member.roles, args[1].lower()):
                toMessage = toMessage + " " + member.mention()
        client.send_message(message.channel, toMessage)
    def hello(t, t1):
        client.send_message(t.channel, "Hello, world!")
    def lenny(t, t1):
        client.send_message(t.channel, "( ͡° ͜ʖ ͡°)")



commands_main = newCommands()

@client.event
def on_message(message):
    if message.content.startswith("!"):
        messCont = message.content[1:]
        commTbl = messCont.split(" ")
        try:
            toCall = getattr(newCommands, commTbl[0])
            toCall(message, commTbl)
        except AttributeError:
            print("Something's gone wrong. It could be that the command didn't exist, or the command errored.")

@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run()
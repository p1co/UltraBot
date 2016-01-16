import discord

detils = open("login.txt", "r")
logins = detils.read().split(",")
detils.close()

client= discord.Client()
client.login(logins[0], logins[1])

if not client.is_logged_in:
    print("Failed to login")
    exit(1)

print("Starting...")

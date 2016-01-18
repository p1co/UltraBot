# UltraBot

A bot that patrols the server for any custom commands being called. If such a command is called, then it will carry out a custom function. Fucntions can include calling all members with a specified role, posting a weird image macro, or just saying hi,

# Installation

- Install the [Discord python API](https://github.com/Rapptz/discord.py)
- Enter your bot's Discord credentials into the login.txt in the form (username@example.com, pass)
- Run main.py

# I want to make a module!

Cool! Here's an example module to get you started below:
```
# Hello module
async def main(message, args, client):
  await client.send_message(message.channel, "Hello, " + message.author.mention)
async def help(message, args, client):
  await client.send_message(message.channel, "A command that says hello to people.")
```

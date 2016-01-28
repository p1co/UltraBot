# UltraBot

A bot that responds to custom commands, certain phrases and keywords and possibly more in the future. Some useful functions include:

- An easily useable way to add custom commands, with 'modules'. If you wish to make such a module, scroll down for an example.
- A built-in debug function to run custom modules and see where they might be erroring.

[Here's the wiki!](https://github.com/elephantLocator/UltraBot/wiki)

# Installation

- Make sure you are running python 3.5
- Install the [Discord python API (async branch)](https://github.com/Rapptz/discord.py)
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

Please note that there are 'special' modules defined by default, which perform special actions and are not used in the standard module way. These are, as of current:
- auto.py
- debug.py

If you have any problems with the bot, make an issue or message us.

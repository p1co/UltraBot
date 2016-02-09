#This module named 'auto' will always be loaded as the auto module, which means that any text that isn't a command will be run through the main function within this module.
#You can edit this file to include a custom function, meaning that you can do something when someone says a specific phrase.

async def main(t, client, autoMods):

    cont = t.content
    for modName in autoMods:
        if modName.lower() in cont.lower():

            if (type(autoMods[modName]) is list):
                for i2 in range(0, len(autoMods[modName])):
                    await client.send_message(t.channel, autoMods[modName][i2])
                break

            elif (type(autoMods[modName]) is str):
                await client.send_message(t.channel, autoMods[modName])
                break

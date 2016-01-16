discord = require 'discord.init'

myClient = discord.Client:new()

-- For the love of god, don't store the password in a GitHub repo.
if myClient:login('email', 'password') then

    print('Logged in!')

    local serverList = myClient:getServerList()
    print('First Server Name: ' .. serverList[1].name)

    -- First Server Name: Y[e]

    local channelList = myClient:getChannelList(serverList[1].id)
    print('First Channel Name: ' .. channelList[1].name)

    -- First Channel Name: general

    myClient:sendMessage('I can send messages!', channelList[1].id)

    -- # general: VideahBot: I can send messages!

end
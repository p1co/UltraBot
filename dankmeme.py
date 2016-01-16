import random

memes = [
	"http://i2.kym-cdn.com/photos/images/facebook/000/875/509/533.jpg",
	"http://vignette3.wikia.nocookie.net/dank-memes/images/1/19/When_ur_a_fag_019.JPG/revision/latest?cb=20150323032531",
	"http://cdn.meme.am/instances/500x/60609861.jpg",
	"http://i2.kym-cdn.com/photos/images/facebook/000/913/033/134.jpg",
	"http://img.memecdn.com/jet-fuel-cant-melt-dank-memes_o_5137411.jpg",
	"http://dankmaymays.com/dank.jpg",
	"http://i1.kym-cdn.com/photos/images/original/001/026/966/a17.png",
	"https://stephentmorris.files.wordpress.com/2016/01/oldermeme.jpg",
	"http://s.quickmeme.com/img/c9/c9c9573e46b3fb7bd6003c62958f4e9bbe9b305801c1e14dff0ab955172c0f74.jpg",
	"https://bacontoday.com/wp-content/uploads/2013/06/vpq.jpg",
	"http://i.imgur.com/aTDVeFX.jpg",
	"http://i.imgur.com/SwIsGcW.jpg",
]

def main(message, args, client):
	maxNum = len(memes) - 1
	rand = random.randint(0, maxNum)
	client.send_message(message.channel, memes[rand])
def help(message, args, client):
        client.send_message(message.channel,"Inserts a dank meme picked by @Screw Jenny. Not as dank as he thinks. Usage: !dankmeme")

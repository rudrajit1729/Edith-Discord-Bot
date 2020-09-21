import discord
import random
import requests
import asyncio

def read_token():
	with open("token.txt", "r") as f:
		lines = f.readlines()
		return lines[0].strip()

token = read_token()
CODE = "No Code Given"
SERVER = "No Server Selected"

client = discord.Client()

@client.event
async def on_member_join(member):
	for channel in member.server.channels:
		if str(channel) == "chit_chat":
			await client.send_message("Hi {}, Welcome to the server, Have Fun!".format(member.mention))


@client.event
async def on_message(message):
	global CODE, SERVER
	id = client.get_guild(755720234685562900)
	channels = ["chit_chat", "timing-and-code", "rules"]
	query = message.content
	query = query.lower()
	valid_users = ["username#id"]

	if message.channel: # in channels and str(message.author) in valid_users:

		if "hi edith" in query or "hello edith" in query or "is anyone there?" in query:
			greetBack = ["Hello","Good to see you again"]
			msg = 'Hello {0.author.mention}'.format(message)
			# await message.channel.send(random.choice(greetBack))
			await message.channel.send("{0} {1.author.mention}!".format(random.choice(greetBack), message))

		if "what\'s up" in query or 'how are you' in query:
			greetBack = ['Just doing my thing!', 'I am fine!', 'Existing!!!', 'I am nice and full of energy']
			await message.channel.send(random.choice(greetBack))

		if "!code:" in query:
			CODE = query[1:].upper()
		if "!server:" in query:
			SERVER = query[1:].upper()

		if "!help" in query:
			embed = discord.Embed(title = "Bot Manual", description="Edith-v1.0.1 Created By - @rudrajit1729")
			embed.add_field(name="!code:", value = "Lets you store room code")
			embed.add_field(name="!server:", value = "Lets you store room server")
			embed.add_field(name="_play", value="Mention song name/link when in voice channel to play")
			embed.add_field(name="_stop", value="Stops music")
			embed.add_field(name="_help", value="Manual for music bot")

			embed.add_field(name="any other text", value="chat with the bot")
			await message.channel.send(content = None, embed = embed)

		if ("code" in query or "among us" in query) and "!code:" not in query:
			embed = discord.Embed(title = "Join", description="Room Code: Among Us")
			embed.add_field(name=CODE, value = SERVER)
			await message.channel.send(content = None, embed = embed)

		if "edith" in query and "joke" in query:
			res = requests.get('https://icanhazdadjoke.com/', headers={"Accept": "application/json"})
			if res.status_code == requests.codes.ok:
				await message.channel.send(str(res.json()['joke']))
			else:
				await message.channel.send('Human your life is a joke in itself!!!')

		elif "edith" in query and "news" in query:
			my_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=9113b9445d8c4e399c473f41890d6126"
			my_open_bbc_page = requests.get(my_url).json()
			my_article = my_open_bbc_page["articles"]
			res = []
			for ar in my_article:
				res.append(ar["title"])
			await message.channel.send("Here is the top ten headlines from BBC world.")
			for i in range(len(res)):
				await message.channel.send("{}. {}".format(i+1, res[i]))

		elif "users" in query:
			await message.channel.send("No. of members: {}".format(id.member_count))

client.run(token)
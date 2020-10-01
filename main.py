import discord
from glob import glob
from commands import loader

bot = discord.Client()

options = {
	"owners": [194137531695104000],
	"prefix": ['!'],
	"disabled_commands": []
}

mods = loader.loader()

async def on_ready():
	print("Bot started!")

async def on_message(msg):
	if not msg.content[:1] in options.prefix: return
	args = msg.content.split(" ")
	cmd = args[0][1:]
	del args[0]
	try:
		mods[cmd]
		info = mods[cmd][0]
		if not cmd in options["disabled_commands"]:
			if info["ownerOnly"] == False:
				if info["guildOnly"] == True and msg.channel.type != 'private':
					mods[cmd][1](bot, msg, args)
			elif msg.author.id in options["owners"]:
				if info["guildOnly"] == True and msg.channel.type != 'private':
					mods[cmd][1](bot, msg, args)
	except:
		print('a')
from random import randint
import discord

class Game():
	def getMoji(which):
		if which == 'player':
			return '😳'
		elif which == 'crate':
			return '🟫'
		elif which == 'desti':
			return '🟫'
		elif which == 'bg':
			return '⬛'
		elif which == 'wall':
			return '🟪'
	def getJSON():
		with open("..games.json", "r") as f:
			return json.loads(f.read())
	def newPos(player):
		for i in ['player','crate','desti']:
			json = Game.getJSON()
			json[player][i]["pos"] = [randint(0,9), randint(0,6)]
		with open('..games.json', 'w') as f:
			f.write(json)
	def embedBuilder(title, description, footer, color):
		embed=Embed(title=title, description=description, color=int("0x{}".format(color)))
		embed.set_footer(text=footer)
		return embed
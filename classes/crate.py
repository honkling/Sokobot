from desti.Desti import getPos
from game.Game import getJSON

class Crate():
	def getPos(player):
		f = getJSON()
		try:
			f[player]["crate"]["pos"]
			return f[player]["crate"]["pos"]
		except:
			return -1
	def move(player, direction):
		dir = int(direction.replace('y', '1').replace('x', '0'))
		which = -1 if '-' in direction else 1
		pos = Crate.getPos(player)
		pos[dir] += which
		tile = getTileFromPos(pos)
		if tile == "wall":
			return "Unable to move"
		json = getJSON()
		json[player]["crate"]["pos"][dir] += which
		with open("..games.json", "w") as f:
			f.write(json)
		return json
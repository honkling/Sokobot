from board.Boardimport getTileFromPos
from game.Game import getJSON, win
from crate.Crate import move
from desti.Desti import getPos

class Player():
	def getPos(player):
		f = getJSON()
		try:
			f[player]["player"]["pos"]
			return f[player]["player"]["pos"]
		except:
			return -1
	def move(player, direction):
		dir = int(direction.replace('y', '1').replace('x', '0'))
		which = -1 if '-' in direction else 1
		pos = Player.getPos(player)
		pos[dir] += which
		tile = getTileFromPos(pos)
		if tile == "wall":
			return "Unable to move"
		elif tile == "crate":
			newpos = move(player, direction)
			if newpos == getPos(player):
				win(player)
		json = getJSON()
		json[player]["player"]["pos"][dir] += which
		with open("..games.json", "w") as f:
			f.write(json)
		return json
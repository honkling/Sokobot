from game.Game import getJSON

class Desti():
	def getPos(player):
		json = getJSON()
		try:
			json[player]["desti"]["pos"]
			return json[player]["desti"]["pos"]
		except:
			return -1
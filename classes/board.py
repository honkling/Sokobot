from game.Game import getJSON, getMoji

class Board():
	def generateBoard(player):
		board = []
		json = getJSON()
		player = json[player]["player"]["pos"]
		crate = json[player]["crate"]["pos"]
		desti = json[player]["destination"]["pos"]
		for i in range(0, 10):
			str = '⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛'
			for o in [player, crate, desti]:
				if o[1] == i:
					str = getMoji('player').join([str[:o[0]], str[o[0]+1:]])
			if player or crate == desti:
				a = getMoji('player') if player == desti else getMoji('crate')
				str = str.replace(getMoji('desti'), a)
			board += ''.join([getMoji('wall'), str, getMoji('wall')])
		return '\n'.join(board)

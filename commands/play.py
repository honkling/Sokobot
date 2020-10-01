import discord
from glob import glob

from game.Game import embedBuilder

class Play():
	def info():
		return {
			"name": "play",
			"description": "Play Sokoban!",
			"aliases": ["start"],
			"ownerOnly": False,
			"guildOnly": True
		}
	def cmd(bot, msg, args):
		embed = embedBuilder("Welcome to Sokoban!", "**HOW TO PLAY**\nReact to this message with :yes: to start the game, then you can react with arrow keys to control your character! Your goal is to push the crate to it's destination!\n\nPLAYER = :flushed:\nCRATE = :brown_square:\nDESTINATION = :x:", "Requested by {}#{}".format(msg.author.name, msg.author.tag), "3df907")
		msg.channel.send(embed)

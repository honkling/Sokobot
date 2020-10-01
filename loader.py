from glob import glob

cmds = {}

class Loader():
	def loader():
		cmds = {}
		for i in glob("commands/*"):
			if i != '__pycache__':
				a = __import__(i.replace('/', '.').replace('.py', ''))
				info = a.info()
				cmds[info["name"]] = [info, a.run]
		return cmds
	def check(name):
		cmds = Loader.loader()
		for i in cmds():
			if name in cmds[i]["info"]["aliases"]:
				return cmds[i]
		return False
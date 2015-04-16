
class Dungeon:

	def __init__(self, filename):
		with open(filename, "r") as in_file:
			lines = in_file.read().splitlines()
			self.dungeon_map = []
			for line in lines:
				self.dungeon_map.append(list(line))

	def print_map(self):
		for line in self.dungeon_map:
			print (''.join(line))
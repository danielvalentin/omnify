import json

class Store:

	filename = '.omnify'

	def __init__(self):
		with open(self.filename, 'r') as f:
			try:
				self.data = json.load(f)
			except:
				# empty file?
				self.data = {}
				print("empty data file exception")
		f.close()

	def get(self, key, default=False):
		if not self.data or not key in self.data:
			return default
		else:
			return self.data[key]

	# Maybe save a hash of the original data object to be used to compare with current object
	# to see if a write is necessary at all (no data changed = no write necessary)
	def save(self, key, value):
		with open(self.filename, 'w') as file:
			self.data[key] = value
			file.write(json.dumps(self.data))
		file.close()


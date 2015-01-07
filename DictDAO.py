from baseDAO import BaseDAO

class DictDAO(BaseDAO):
	def __init__(self):
		super(self.__class__,self).__init__()
		self.storage = dict()

	def get_key(self, key):
		return self.storage.get(key,False)

	def set_key(self, key):
		self.storage[key] = True
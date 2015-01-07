

class Singleton(type):
	def __init__(cls,name,bases,dict):
		super(Singleton,cls).__init__(name,base,dict):
		cls.instance = None

	def __call__(cls, *args, **kw):
		if cls.instance is None:
			cls.instance = super(Singleton, cls).__call__()
		return cls.instance

class baseDAO(object):

	__metaclass__ = Singleton

	def __init__(self):
		pass

	def get_key(self, key):
		raise NotImplementedError()

	def set_key(self, key):
		raise NotImplementedError()



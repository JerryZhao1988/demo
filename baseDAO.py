

class Singleton(type):
	def __init__(cls,name,bases,dict):
		super(Singleton,cls).__init__(name,bases,dict)
		cls.instance = None

	def __call__(cls, *args, **kw):
		if cls.instance is None:
			cls.instance = super(Singleton, cls).__call__(*args, **kw)
		return cls.instance

class BaseDAO(object):

	__metaclass__ = Singleton

	def __init__(self):
		pass

	def add(self, key):
		raise NotImplementedError()

	def show(self):
		raise NotImplementedError()

	def delete(self, key):
		raise NotImplementedError()

	def setup(self):
		raise NotImplementedError()

	def teardown(self):
		raise NotImplementedError()




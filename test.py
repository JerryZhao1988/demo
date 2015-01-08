import unittest
from baseDAO import BaseDAO
from DbDAO import DbDAO
from sax import Test
from index import Index

class BaseDAOTest(unittest.TestCase):

	def test_add(self):
		dao = BaseDAO()
		self.assertRaises(NotImplementedError,dao.add,"123")



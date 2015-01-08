import unittest
from baseDAO import BaseDAO
from DbDAO import DbDAO
from sax import Test
from index import Index
import sqlite3
import mock

class BaseDAOTest(unittest.TestCase):

	def test_add(self):
		dao = BaseDAO()
		self.assertRaises(NotImplementedError,dao.add,"123")

	def test_show(self):
		dao = BaseDAO()
		self.assertRaises(NotImplementedError,dao.show)

	def test_delete(self):
		dao = BaseDAO()
		self.assertRaises(NotImplementedError,dao.delete,"123")

	def test_setup(self):
		dao = BaseDAO()
		self.assertRaises(NotImplementedError,dao.setup)

	def test_teardown(self):
		dao = BaseDAO()
		self.assertRaises(NotImplementedError,dao.teardown)

class DbDAOTest(unittest.TestCase):

	def test_singleton(self):
		dao_1 = DbDAO("test.db")
		dao_2 = DbDAO("test.db")
		self.assertEqual(id(dao_1),id(dao_2))

	def test_setup(self):
		dao = DbDAO("test.db")
		self.assertEqual(type(dao.setup()),sqlite3.Connection)


if __name__ == '__main__':
	unittest.main()



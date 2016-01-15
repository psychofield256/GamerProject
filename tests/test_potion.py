#-*-coding:utf-8-*-

from required.classes import Potion
import unittest

class PotionTest(unittest.TestCase):
	"""tests of the Potion class"""
	def test_init(self):
		"""tests the init function"""
		p = Potion(1)
		self.assertIsInstance(p.lore, str)
		self.assertIsInstance(p.__str__(), str)

unittest.main()

# -*-coding:utf-8-*-

#tests.py
#Written by Cheikhrouhou Yacine while learning how to use unittest

import random
import unittest

class RandomTest(unittest.TestCase):
	"""Test Case utilisé pour tester les fonction du module 'random'."""

	def setUp(self):
		"""Creer une liste vierge de 0 à 9.
		Fonction lancée avant chaque test"""
		self.liste = list(range(10))
	def test_choice(self):
		"""Test le fonctionnement de la fonction 'random.choice'."""
		elt = random.choice(self.liste)
		#vérifie que elt est dans liste
		self.assertIn(elt, self.liste)
	def test_shuffle(self):
		"""test le fonctionnement de la fonction 'random.shuffle'."""
		random.shuffle(self.liste)
		self.liste.sort()
		self.assertEqual(self.liste, list(range(10)))
	def test_sample(self):
		"""test le fonctionnement de la fonction 'random.sample'."""
		k = 10
		l2 = random.sample(self.liste, k)
		for element in l2:
			self.assertIn(element, self.liste)
			with self.assertRaises(ValueError):
				random.sample(self.liste, 20)



#unittest.main()
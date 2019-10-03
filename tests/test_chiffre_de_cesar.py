import unittest
from  chiffre_de_cesar import chiffrage
from  chiffre_de_cesar import dechiffrage

class TestChiffreDeCesarFunctions(unittest.TestCase):

    def test_chiffrage(self):
        self.assertEqual(chiffrage('$'), ',')
        self.assertEqual(chiffrage('?'), 'G')
        self.assertEqual(chiffrage('5'), '=')
        self.assertEqual(chiffrage('W'), '_')

    def test_dechiffrage(self):
        self.assertEqual(dechiffrage('~'), 'v')
        self.assertEqual(dechiffrage('-'), '%')
        self.assertEqual(dechiffrage('<'), '4')
        




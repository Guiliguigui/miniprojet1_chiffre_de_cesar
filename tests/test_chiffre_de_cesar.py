import unittest
from  chiffre_de_cesar import chiffrage
from  chiffre_de_cesar import dechiffrage
from  chiffre_de_cesar import decoupage

class TestChiffreDeCesarFunctions(unittest.TestCase):

    def test_chiffrage(self):
        self.assertEqual(chiffrage(['t','e','s','t',]), "|m{|")
        self.assertEqual(chiffrage(['l',']','k','l',]), "test")

    def test_dechiffrage(self):
        self.assertEqual(dechiffrage(['t','e','s','t',]), "l]kl")
        self.assertEqual(dechiffrage(['|','m','{','|',]), "test")

    def test_decoupage(self):
        self.assertEqual(decoupage("test"),['t','e','s','t',])
        self.assertEqual(decoupage(82),['8','2',])
        




import unittest
from  chiffre_de_cesar import chiffrage
from  chiffre_de_cesar import dechiffrage
from  chiffre_de_cesar import decoupage
from  chiffre_de_cesar import chiffrage_circulaire
from  chiffre_de_cesar import dechiffrage_circulaire

class TestChiffreDeCesarFunctions(unittest.TestCase):

    def test_chiffrage(self):
        self.assertEqual(chiffrage(['t','e','s','t',],8), "|m{|")
        self.assertEqual(chiffrage(['l',']','k','l',],8), "test")

    def test_dechiffrage(self):
        self.assertEqual(dechiffrage(['t','e','s','t',],8), "l]kl")
        self.assertEqual(dechiffrage(['|','m','{','|',],8), "test")

    def test_decoupage(self):
        self.assertEqual(decoupage("test"),['t','e','s','t',])
        self.assertEqual(decoupage(82),['8','2',])

    def test_chiffrage_circulaire(self):
        self.assertEqual(chiffrage_circulaire(['z','a','b','c',],3),"cdef")
        self.assertEqual(chiffrage_circulaire(['Z','A','B','c',],3),"CDEf")


    def test_dechiffrage_circulaire(self):
        self.assertEqual(dechiffrage_circulaire(['d','E','f','C',],3),"aBcZ")
        




import unittest
from src.Logica.Conjunto import Conjunto


class TestConjunto( unittest.TestCase ):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

import unittest
from src.reservas import reserva_valida

class TestReservas(unittest.TestCase):
    def test_limites(self):
        for horas, esperado in [(0, False), (1, True), (4, True), (5, False)]:
            with self.subTest(horas=horas):
                self.assertEqual(reserva_valida(horas), esperado)
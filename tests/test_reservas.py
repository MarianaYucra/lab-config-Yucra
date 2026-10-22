import unittest
from src.reservas import reserva_valida

class TestReservas(unittest.TestCase):
    def test_limites(self):
        for horas, esperado in [(-1, False), (0, False), (1, True), (2, True),
                                (3, False), (1.5, False), (True, False), (2.0, False)]:
            with self.subTest(horas=horas):
                self.assertEqual(reserva_valida(horas), esperado)
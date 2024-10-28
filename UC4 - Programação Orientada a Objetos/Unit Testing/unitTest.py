import unittest

# Função que vamos testar
def soma(a, b):
    return a + b

# Classe de teste
class TestSoma(unittest.TestCase):

    # Método de teste
    def test_soma_positivos(self):
        self.assertEqual(soma(2, 3), 5)  # Verifica se 2 + 3 é igual a 5

    def test_soma_negativos(self):
        self.assertEqual(soma(-2, -3), -5)  # Verifica se -2 + -3 é igual a -5

    def test_soma_zero(self):
        self.assertEqual(soma(0, 0), 0)  # Verifica se 0 + 0 é igual a 0

# Executa os testes
if __name__ == '__main__':
    unittest.main()

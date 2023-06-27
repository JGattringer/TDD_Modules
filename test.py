import pytest
from funcoes_exercicio.funcoes import multiplo

class TesteFuncao:
    def setup(self):
        pass

    def testeMultiplo_5(self):
        resultado = multiplo(50)
        assert resultado == 'Fizz'

    def testeMultiplo_7(self):
        resultado = multiplo(49)
        assert resultado == 'Buzz'

    def testeMultiplo_5_7(self):
        resultado = multiplo(70)
        assert resultado == 'FizzBuzz'

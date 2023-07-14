"""
Module of test for the function multiple from funcoes module
"""
from funcoes import multiplo


class TesteFuncao:
    """Functions created to test the program with pytest,
    need to import and execute the test in this file
    """
    def setup(self):
        pass

    def testem_multiplo_5(self):
        """Test if the number is multiple of 5"""
        resultado = multiplo(50)
        assert resultado == 'Fizz'

    def teste_multiplo_7(self):
        """Test if the number is multiple of 7"""
        resultado = multiplo(49)
        assert resultado == 'Buzz'

    def teste_multiplo_5_7(self):
        """Test if the number is multiple of 5 and 7 at the same time"""
        resultado = multiplo(70)
        assert resultado == 'FizzBuzz'

'''
    Programa: Teste Teorema de Bhaskara utilizando modularização
    Autor: José Wesley Feitosa Oliveira
    Concluída em: 11/2019
    Breve descricao:
    Exemplo de código com a utilização de testes automatizados para verificação de erros,
    foram utilizadas três maneiras de fazer a automatização dos testes, cada uma buscando
    reduzir o número de respetições da antetior.
'''

import Bhaskara
import pytest

''' Primeira cadeia de testes utilizando a definiçao de uma variável 'b' que
    recebe o valores calculados na classe Bhaskara'''
'''
class TestBhaskara:

    def test_uma_raiz(self):
        b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(1, 0, 0) == (1, 0)

    def test_duas_raizes(self):
        b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)

    def test_zero_raizes(self):
        b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(10, 10, 10) == 0

    def test_raiz_negativa(self):
        b = Bhaskara.Bhaskara()
        assert b.calcula_raizes(10, 20, 10) == (1, -1)
'''

''' Segunda cadeia de testes utilizando o fixture e a definiçao de um método 'b' que
    não recebe parametros e retorna a chamada de Bhaskara, esse método é
    passado como parâmetro nos métodos de teste, desse modo não é necessário
    criar uma variável 'b' em cada função de teste. '''
'''
class TestBhaskara:

    @pytest.fixture
    def b(self):
        return Bhaskara.Bhaskara()
    
    def test_uma_raiz(self, b):
        assert b.calcula_raizes(1, 0, 0) == (1, 0)

    def test_duas_raizes(self, b):
        assert b.calcula_raizes(1, -5, 6) == (2, 3, 2)

    def test_zero_raizes(self, b):
        assert b.calcula_raizes(10, 10, 10) == 0

    def test_raiz_negativa(self, b):
        assert b.calcula_raizes(10, 20, 10) == (1, -1)

'''
''' Terceira cadeia de testes utilizando o parametrize e a definiçao de métodos para os testes
    recebendo como parâmetros os termos a, b e c, além da quantidade de raízes
    e os seus respectivos valores, o assert está chamando do método 'calcula_raizes'. Podemos
    ver nesse exemplo que o uso do parametrize não foi muito eficiente, visto que o método
    'calcula_raizes' pode retornar quantidades diferentes de raízes, o que gerou a criação
    de várias funções test.'''
'''
class TestBhaskara:

    @pytest.mark.parametrize("a, b, c, qtd_raizes, raiz1, raiz2", [(1, -5, 6, 2, 3, 2)])
    def test_duas_raizes(self, a, b, c, qtd_raizes, raiz1, raiz2):
        x = Bhaskara.Bhaskara()
        assert x.calcula_raizes(a, b, c) == (qtd_raizes, raiz1, raiz2)
        
    @pytest.mark.parametrize("a, b, c, qtd_raizes, raiz1", [
        (1, 0, 0, 1, 0),
        (10, 20, 10, 1, -1)
        ])
    def test_uma_raiz(self, a, b, c, qtd_raizes, raiz1):
        x = Bhaskara.Bhaskara()
        assert x.calcula_raizes(a, b, c) == (qtd_raizes, raiz1)
        
    @pytest.mark.parametrize("a, b, c, qtd_raizes",[(10, 10, 10, 0)])
    def test_zero_raizes(self, a, b, c, qtd_raizes):
        x = Bhaskara.Bhaskara()
        assert x.calcula_raizes(a, b, c) == (qtd_raizes)
'''



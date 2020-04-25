'''
    Programa: Testes da classe Triangulo utilizando modularização
    Autor: José Wesley Feitosa Oliveira
    Concluída em: 04/2020
    Breve descricao:
    Exemplo de código com a utilização de testes automatizados para verificação de erros,
    foram utilizadas três maneiras de fazer a automatização dos testes, cada uma buscando
    reduzir o número de respetições da antetior.
'''

import Triangulo
import pytest

''' Primeira cadeia de testes utilizando a definiçao de uma variável 'p' que
    recebe o perímetro do triângulo e uma variável 't' que recebe o tipo do
    triângulo'''
'''
class TestTriangulo:

    def test_nao_existe(self):
        p = Triangulo.Triangulo()
        assert p.perimetro(5, 0, -2) == ("Triangulo não existe")

    def test_perimetro(self):
        p = Triangulo.Triangulo()
        assert p.perimetro(15, 15, 5) == (35)

    def test_equilatero(self):
        t = Triangulo.Triangulo()
        assert t.tipo_lado(5, 5, 5) == ("equilátero")

    def test_isosceles(self):
        t = Triangulo.Triangulo()
        assert t.tipo_lado(15, 15, 10) == ("isósceles")

    def test_escaleno(self):
        t = Triangulo.Triangulo()
        assert t.tipo_lado(5, 15, 10) == ("escaleno")
'''
''' Segunda cadeia de testes utilizando o fixture e a definiçao de dois métodos
    'p' (para o perímetro) e 't' (para o tipo do triângulo), ambas não recebem
    parametros e retornam a chamada de Triangulo, esses métodos são passados
    como parâmetros nos métodos de teste, desse modo não é necessário criar uma
    variável dentro de cada método de teste.'''
'''
class TestTriangulo:

    @pytest.fixture
    def p(self):
        return Triangulo.Triangulo()

    def test_nao_existe(self, p):
        assert p.perimetro(5, 0, -2) == ("Triangulo não existe")

    def test_perimetro(self, p):
        assert p.perimetro(15, 15, 5) == (35)

    @pytest.fixture
    def t(self):
        return Triangulo.Triangulo()

    def test_equilatero(self, t):
        assert t.tipo_lado(5, 5, 5) == ("equilátero")

    def test_isosceles(self, t):
        assert t.tipo_lado(15, 15, 10) == ("isósceles")

    def test_escaleno(self, t):
        assert t.tipo_lado(5, 15, 10) == ("escaleno")
'''

''' Terceira cadeia de testes utilizando o parametrize e a definiçao de métodos
    para os testes recebendo como parâmetros os termos a, b e c, além do
    perímetro_calculado ou tipo_triangulo, a depender do teste. O código de
    testes ficou mais limpo e com menos repetições.'''
'''
class TestTriangulo:

    @pytest.mark.parametrize("a, b, c, perimetro", [
        (5, 0, -2, "Triangulo não existe"),
        (15, 15, 5, 35)
        ])
    def test_perimetro(self, a, b, c, perimetro):
        p = Triangulo.Triangulo()
        assert p.perimetro(a, b, c) == (perimetro)
        
    @pytest.mark.parametrize("a, b, c, tipo", [
        (5, 5, 5, "equilátero"),
        (15, 15, 10, "isósceles"),
        (5, 15, 10, "escaleno")
        ])
    def test_tipo_lado(self, a, b, c, tipo):
        t = Triangulo.Triangulo()
        assert t.tipo_lado(a, b, c) == (tipo)
''' 

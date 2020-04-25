'''
    Programa: Cálculo de perímetro e classificação de triângulos
    Autor: José Wesley Feitosa Oliveira
    Concluída em: 11/2019
    Breve descricao:
    Código simples para cálculo de perímetro e classificação de triângulos.
    A classe Triangulo foi criada para deixar o código mais limpo e as funções
    perimetro e tipo_lado foram passadas como métodos da classe.
'''
class Triangulo:
    
    def perimetro(self, a, b, c):

        if a <= 0 or b <= 0 or c <= 0:
             return "Triangulo não existe"
        else:       
            perimetro = a + b + c
            return perimetro

    def tipo_lado(self, a, b, c):

        if a == b and a == c and b == c:
            tipo = "equilátero"
        elif a != b and a != c and b != c:
            tipo = "escaleno"
        else:
            tipo = "isósceles"

        return tipo
        
    def main(self):

        a_digitado = float(input("entre com o primeiro lado: "))
        b_digitado = float(input("entre com o segundo lado: "))
        c_digitado = float(input("entre com o terceiro lado: "))
        print("O perímetro é" ,self.perimetro(a_digitado, b_digitado, c_digitado), "e o triângulo é", self.tipo_lado(a_digitado, b_digitado, c_digitado))

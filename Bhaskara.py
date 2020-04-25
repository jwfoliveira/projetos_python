'''
    Programa: Aplicação do Teorema de Bhaskara
    Autor: José Wesley Feitosa Oliveira
    Concluída em: 11/2019
    Breve descricao:
    Código simples para aplicação do Teorema de Bhaskara, foi utilizado a
    estrutura condicional if para o cálculo das raízes. Classe Bhaskara foi
    criada para deixar o código mais organizado e as funções para cálculo foram
    passadas como métodos dessa classe.
'''

import math

class Bhaskara:

    def delta(self, a, b, c):
        return b**2 -4*a*c

    def calcula_raizes(self, a, b, c):
        d = self.delta(a, b, c)

        if d < 0:
                return 0
        elif d == 0:
                raiz = -b /(2*a)
                return 1, raiz
        else:
                raiz1 = (-b + math.sqrt(d))/(2*a)
                raiz2 = (-b - math.sqrt(d))/(2*a)
                return 2, raiz1, raiz2 

    def main(self):

        a_digitado = float(input("entre com o termo a: "))
        b_digitado = float(input("entre com o termo b: "))
        c_digitado = float(input("entre com o termo c: "))
        print(self.calcula_raizes(a_digitado, b_digitado, c_digitado))
    

                

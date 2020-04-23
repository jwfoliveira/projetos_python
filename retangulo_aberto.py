'''
    Programa: Usuário escolhe largura e altura e o programa gera um retângulo aberto com as dimensões descritas
    Autor: José Wesley Feitosa Oliveira
    Concluída em: 11/2019
    Breve descricao:
        O programa recebe como entradas dois números inteiros correspondentes à largura e à altura de um retângulo, respectivamente. O programa 
        imprimi uma cadeia de caracteres que represente o retângulo informado com caracteres '#' na saída, contudo o '#' estará apenas formando
        o retângulo e não ocupando o interior do polígono.
'''

largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
aux_larg = largura
aux_alt = altura

''' Estruturas de While's encadeados para que seja possível formar o retângulo, a cada linha formada a iteração reduz uma unidade da altura '''

while altura == aux_alt or altura == 1:
    while largura > 0:
        print("#",end = "")
        largura = largura - 1
    largura = aux_larg
    print()
    altura = altura - 1

    while altura > aux_alt-1 or altura > 1:
        if largura == aux_larg:
            print("#",end="")
            largura = largura - 1
        else:
            while largura > aux_larg-1 or largura>1:
                print(" ",end="")
                largura = largura - 1
            largura = aux_larg
            print("#")
            altura = altura - 1
        

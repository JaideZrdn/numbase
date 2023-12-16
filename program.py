from base import Numero

if __name__ == '__main__':

    valor = str(input('Digite o número à ser convertido: '))
    baseori = (input('Qual é a base desse número? '))
    if not baseori:
        baseori = 10
    numeroori = Numero(valor, int(baseori))
    basedest = (input('Para qual base você deseja alterar o número? '))
    if not basedest:
        basedest = 10

    numerofin = numeroori.mudabase(int(basedest))
    print(f"\nSeu número era {numeroori}\n\nConvertido foi para {numerofin}")

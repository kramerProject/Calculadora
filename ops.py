from time import sleep
from calculadora import ops


def titulo(msg):

    global tam
    tam=len(msg)+4
    print('*'*tam)
    print(f'{msg.center(tam)}')
    print('*' * tam)
    return ""



def menu():

    titulo('BEM-VINDO Á KRAMCULATOR')
    opcoes=['Soma','Subtraçāo','Multiplicaçāo','Divisāo','Sair']

    c=1
    for item  in opcoes:
        print(f'  \033[34m{c:<1} - [{item}]\033[m')
        c+=1
    print('*'*tam)

def leiaint():

    while True:
        try:
            op=int(input('Selecione a operaçāo desejada: '))
        except ValueError:
            print('\033[33mErro: Digite um número válido\033[m')
        else:
            if op > 5 or op <1:
                print('\033[33mErro: Digite um número de acordo om as opçoes do menu.\033[m')
            else:
                break
    return op


def soma():

    n1=int(input('Digite o primeiro número: '))
    n2=int(input('Digite o segundo número: '))
    print('Calculando.....')
    sleep(1)
    s=n1+n2
    return titulo(f'O resultado da soma entre {n1} e {n2} é {s}.')


def sub():
    n1=int(input('Digite o primeiro número: '))
    n2=int(input('Digite o segundo número: '))
    print('Calculando.....')
    sleep(1)
    s=n1-n2
    return titulo(f'O resultado da subtraçāo entre {n1} e {n2} é {s}.')


def mult():
    n1=int(input('Digite o primeiro número: '))
    n2=int(input('Digite o segundo número: '))
    print('Calculando.....')
    sleep(1)
    s=n1*n2
    return titulo(f'O resultado da multiplicaçāo entre {n1} e {n2} é {s}.')


def div():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print('Calculando.....')
    sleep(1)
    s = n1 / n2
    return titulo(f'O resultado da divisāo entre {n1} e {n2} é {s}.')



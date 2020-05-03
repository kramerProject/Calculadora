from calculadora import ops
from time import sleep

while True:
    ops.menu()
    opcao=ops.leiaint()
    if opcao == 1:
        resultado=ops.soma()
    elif opcao == 2:
        resultado=ops.sub()
    elif opcao == 3:
        resultado=ops.mult()
    elif opcao == 4:
        resultado=ops.div()
    elif opcao==5:
        break
    print(resultado,end='')
    sleep(1)
    continuar=str(input('Deseja continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print(ops.titulo('Volte Sempre! '))
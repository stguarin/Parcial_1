#Santiago Guarin Alfaro 1031646221
#programa para sacar el cuadrado de un numero que no sea negativo
#se solicita el numero para potenciar y se pasa de str a int
num = int(input('Digite un numero para convertirlo en su cuadrado: '))
#se establece un filto pra numeros positivos
if num>= 0:
    #se usa un f str para ordenar el resultado y potenciarlo al cuadrado
    print(f'el numero {num} al cuadrado es {num**2}')
#se informa al susuario que el numero digitado no es positivo
else:
    print('digite un numero mayor a 0 para conseguir su cuadrado')
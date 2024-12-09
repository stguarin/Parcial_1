#Santiago Guarin Alfaro 1031646221
#n/2 si es par, 3n+1 si es impar
#se establece la variable que se usara para inicar el bucle
n= -1
#se establece una segunda variable que servira como contador para que el mucle se repita las veces que sea necesario
x= 0
#se inicia el bucle 
while n!=1:
    #es establece el primer filtro para saber si un numero es negativo o positivo
    if n> 0:
        #se establece un segundo bucle para determinar si es par comparando el resultado de una division entrea entre 2 con una divicion convencional entre 2 
        if n//2 == n/2:
            #el numero se divide en 2 y se impreime su resultado
            n= n/2
            print(int(n))
        else:
            #el numero se multiplica por 3,se le suma 1 y se imprime su resultado
            n= (3*n)+1
            print(int(n))
    # en caso de que sea negativo se imprimira un aviso al respecto y se volvera solicitar el numero
    else:
        #se usa un contador para determinar que sea la primera vez que el usuario solicita un numero, en la proxima vez se imprimira el mensaje alertando el negativo
        if x!=0:
            print('El numero digitado no es mayor a 0')
            x= x+1
        #se solicita el numero por primera vez en esta parte del bucle 
        n = int(input('Digite un numero mayor a 0: '))

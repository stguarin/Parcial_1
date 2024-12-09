#Santiago Guarin Alfaro 1031646221
# aumentar la poblacion un 2% para el pais A y un 3% para el pais B
#se establecen las constantes que se usaran a lo largo del programa como lo es el año, la poblacion inicial y la tasa de cresimiento anual
año = 2022
pob_A = 25000000
pob_B = 18900000
inc_A = 0.02
inc_B= 0.03
#se establece un bucle que se rompera en el momento en el que la poblacion B alcanze a la poblacion A 
while pob_A>pob_B:
    print(f'el año es {año}')
    print(f'la poblacion del pais A es de: {pob_A}')
    print(f'la poblacion del pais B es de: {pob_B}')
    pob_A = pob_A + (pob_A*inc_A)
    pob_B = pob_B + (pob_B*inc_B)
    año = año + 1
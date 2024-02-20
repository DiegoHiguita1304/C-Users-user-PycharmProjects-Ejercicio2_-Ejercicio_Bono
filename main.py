#Variables globales
total_estrato_1 = 0
total_estrato_2 = 0
total_sin_hijos = 0
total_hasta_dos_hijos = 0
total_tres_o_mas_hijos = 0
total_sin_hijos_bono = 0
total_hasta_dos_hijos_bono = 0
total_tres_o_mas_hijos_bono = 0
total_bonos_pagados = 0


def calcular_bono_ayuda(estrato, num_hijos):
    bono = 0

    if estrato == 1:
        if num_hijos == 0:
            bono = 20000
        elif num_hijos <= 2:
            bono = 25000
        else:
            bono = 30000
    elif estrato == 2:
        if num_hijos == 0:
            bono = 16500
        elif num_hijos <= 2:
            bono = 21500
        else:
            bono = 26500

    return bono


def proceso_entrega_bonos():
    global total_estrato_1, total_estrato_2, total_sin_hijos, total_hasta_dos_hijos, total_tres_o_mas_hijos
    global total_sin_hijos_bono, total_hasta_dos_hijos_bono, total_tres_o_mas_hijos_bono, total_bonos_pagados

    while True:
        print("------------------------------------------------------")
        desea_ingresar = int(input("Desea ingresar Datos 1.Si  2.No: "))
        if desea_ingresar == 2:
            break
        estrato = int(input("Ingrese el estrato al que pertenece (1 o 2): "))
        num_hijos = int(input("Ingrese el número de hijos: "))
        print("------------------------------------------------------")

        bono = calcular_bono_ayuda(estrato, num_hijos)
        if bono is not None:
            total_bonos_pagados += bono
        else:
            print("No se pudo calcular el bono para el estrato y número de hijos ingresados.")
            print("------------------------------------------------------")

        if estrato == 1:
            total_estrato_1 += 1
            if num_hijos == 0:
                total_sin_hijos += 1
                total_sin_hijos_bono += bono
            elif num_hijos <= 2:
                total_hasta_dos_hijos += 1
                total_hasta_dos_hijos_bono += bono
            else:
                total_tres_o_mas_hijos += 1
                total_tres_o_mas_hijos_bono += bono
        elif estrato == 2:
            total_estrato_2 += 1
            if num_hijos == 0:
                total_sin_hijos += 1
                total_sin_hijos_bono += bono
            elif num_hijos <= 2:
                total_hasta_dos_hijos += 1
                total_hasta_dos_hijos_bono += bono
            else:
                total_tres_o_mas_hijos += 1
                total_tres_o_mas_hijos_bono += bono

    #Resultados
    print(f"------------------------------------------------------")
    print(f"Cantidad de personas del estrato 1:  {total_estrato_1}")
    print(f"Cantidad de personas del estrato 2: {total_estrato_2}")
    print(f"Total de dinero entregado al estrato 1: {total_estrato_1}")
    print(f"Total de dinero entregado al estrato 2: {total_estrato_2}")
    print(f"Cantidad de personas que no tienen hijos: {total_sin_hijos}")
    print(f"Cantidad de personas que tienen hasta 2 hijos: {total_hasta_dos_hijos}")
    print(f"Cantidad de personas que tienen 3 o más hijos: {total_tres_o_mas_hijos}")
    print(f"Total de dinero entregado a los beneficiarios que no tienen hijos: {total_sin_hijos_bono}")
    print(f"Total de dinero entregado a los beneficiarios que tienen hasta 2 hijos: {total_hasta_dos_hijos_bono}")
    print(f"Total de dinero entregado a los beneficiarios que tienen 3 o más hijos: {total_tres_o_mas_hijos_bono}")
    print(f"Total pagado por los bonos: {total_bonos_pagados}")
    print(f"------------------------------------------------------")



if __name__ == '__main__':
    proceso_entrega_bonos()

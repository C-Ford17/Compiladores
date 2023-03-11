def es_expresion_numerica(cadena):

    alfabeto = {'numeros': ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'),
                'signos': ('+', '-'),
                'exp': ('e', 'E'),
                'punto': '.'}

    tabla = {
        0: {'signos': 1, 'numeros': 2, 'punto': 3},
        1: {'numeros': 2, 'punto': 2},
        2: {'numeros': 2, 'punto': 3, 'exp': 5},
        3: {'numeros': 4},
        4: {'numeros': 4, 'exp': 5},
        5: {'numeros': 5, 'signos': 6},
        6: {'numeros': 6}
    }

    estado_actual = 0
    
    for simbolo in cadena:
        esta = False
        for clave, valores in alfabeto.items():
            if simbolo in valores:
                if clave in tabla[estado_actual]:
                    esta = True
                    estado_actual = tabla[estado_actual][clave]
        if esta == False:
            return False
    return True


print(es_expresion_numerica('+213.e-32'))

def es_numero_romano(cadena):
    # alfabeto
    simbolos = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    
    # tabla de transiciones
    tabla = {
        0: {'I': 1, 'V': 5, 'X': 6, 'L': 9, 'C': 11, 'D': 14, 'M':16},
        1: {'I': 3, 'V':4, 'X':4},
        2: {'I':3},
        3: {'I':4},
        4: {},
        5: {'I':2},
        6: {'I':1,'X':7,'V':5, 'L':8, 'C':8},
        7: {'I':1,'X':8, 'V':5},
        8: {'I':1, 'V':5},
        9: {'I':1,'X':10,'V':5},
        10:{'I':1,'X':7,'V':5},
        11:{'I':1,'X':6,'V':5,'L':9,'C':12, 'D':13, 'M':13},
        12:{'I':1,'X':6,'V':5,'L':9,'C':13},
        13:{'I':1,'X':6,'V':5,'L':9},
        14:{'I':1,'X':6,'V':5,'L':9,'C':15},
        15:{'C':12},
        16:{'I':1,'X':6,'V':5,'L':9,'C':15, 'D':14, 'M':17},
        17:{'I':1,'X':6,'V':5,'L':9,'C':15,'D':14,'M':18},
        18:{'I':1,'X':6,'V':5,'L':9,'C':19,'D':14},
        19:{'C':12,'M':13}
    }
    
    estado_actual =0
    
    for simbolo in cadena:
        
        if simbolo not in simbolos:
            return False
        
        if simbolo in tabla[estado_actual]:
            estado_actual=tabla[estado_actual][simbolo]
            
        else:
            return False
        
    return True

print(es_numero_romano('MMMCMXCIX')) # True

from grammar_parser import leer_gramatica, obtener_simbolos
from first_follow import calcular_first, calcular_follow
from ll1_parser import es_ll1, analizar_cadena_ll1, construir_tabla_ll1
from slr1_parser import es_slr1, analizar_cadena_slr1, construir_tabla_slr1
from utils import imprimir_conjuntos

def main():
    producciones, simbolo_inicial = leer_gramatica("ejemplo_entrada.txt")
    no_terminales, terminales = obtener_simbolos(producciones)

    
    first = calcular_first(producciones)
    follow = calcular_follow(producciones, simbolo_inicial, first)

    
    imprimir_conjuntos(first, "First")
    imprimir_conjuntos(follow, "Follow")

    es_ll1_gramatica = es_ll1(producciones, first, follow)
    es_slr1_gramatica = es_slr1(producciones, first, follow)

    
    tabla_ll1 = construir_tabla_ll1(producciones, first, follow) if es_ll1_gramatica else None
    tabla_slr1 = construir_tabla_slr1(producciones) if es_slr1_gramatica else None

    
    if es_ll1_gramatica and es_slr1_gramatica:
        print("Seleccionar un analizador (T: para LL(1), B: para SLR(1), Q: salir):")
        while True:
            opcion = input().strip().upper()
            if opcion == 'T':
                print("Usando el analizador LL(1) . Ingresar cadenas para analizar (para salir, dejar linea en blanco):")
                while True:
                    cadena = input().strip()
                    if cadena == "":
                        break
                    resultado = analizar_cadena_ll1(cadena, tabla_ll1, simbolo_inicial)
                    print("si" if resultado else "no")
                print("Seleccionar un analizador (T: para LL(1), B: para SLR(1), Q: salir):")
            elif opcion == 'B':
                print("Usando el analizador SLR(1) . Ingresar cadenas para analizar (para salir, dejar linea en blanco):")
                while True:
                    cadena = input().strip()
                    if cadena == "":
                        break
                    resultado = analizar_cadena_slr1(cadena, tabla_slr1, simbolo_inicial)
                    print("si" if resultado else "no")
                print("Seleccionar un analizador (T: para LL(1), B: para SLR(1), Q: salir):")
            elif opcion == 'Q':
                break
            else:
                print("opcion no válida. Seleccionar T, B, o Q.")

    # Caso 2: La gramática es LL(1), pero no SLR(1)
    elif es_ll1_gramatica:
        print("La gramática es LL(1). Ingresar cadenas para analizar (para salir, dejar linea en blanco):")
        while True:
            cadena = input().strip()
            if cadena == "":
                break
            resultado = analizar_cadena_ll1(cadena, tabla_ll1, simbolo_inicial)
            print("si" if resultado else "no")

    # Caso 3: La gramática es SLR(1), pero no LL(1)
    elif es_slr1_gramatica:
        print("La gramática es SLR(1). Ingresar cadenas para analizar (para salir, dejar linea en blanco):")
        while True:
            cadena = input().strip()
            if cadena == "":
                break
            resultado = analizar_cadena_slr1(cadena, tabla_slr1, simbolo_inicial)
            print("si" if resultado else "no")

    
    else:
        print("La gramatica no es ni LL(1) ni SLR(1).")

if __name__ == "__main__":
    main()
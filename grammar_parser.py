def leer_gramatica(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.read().splitlines()

    n = int(lineas[0])  
    producciones = {}

    for i in range(1, n + 1):
        izquierda, derecha = lineas[i].split("->")
        izquierda = izquierda.strip()
        alternativas = derecha.strip().split()
        lista_alternativas = []
        for alt in alternativas:
            regla = list(alt.strip().replace(" ", ""))
            lista_alternativas.append(regla)
        producciones[izquierda] = lista_alternativas

    simbolo_inicial = 'S'  
    return producciones, simbolo_inicial


def obtener_simbolos(producciones):
    no_terminales = set(producciones.keys())
    terminales = set()

    for alternativas in producciones.values():
        for alternativa in alternativas:
            for simbolo in alternativa:
                if simbolo.islower() or simbolo in {'$', 'e'}:  
                    terminales.add(simbolo)

    return no_terminales, terminales
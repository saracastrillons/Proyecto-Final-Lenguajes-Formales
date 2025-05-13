def imprimir_conjuntos(conjuntos, nombre):
    print(f"{nombre} sets:")
    for simbolo, conjunto in conjuntos.items():
        print(f"{simbolo}: {sorted(conjunto)}")
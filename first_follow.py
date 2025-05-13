def calcular_first(producciones):
    first = {no_terminal: set() for no_terminal in producciones}

    def obtener_first(simbolo):
        if simbolo.islower() or simbolo == 'e':  
            return {simbolo}
        if simbolo not in producciones:  
            return set()
        resultado = set()
        for alternativa in producciones[simbolo]:
            for s in alternativa:
                resultado |= obtener_first(s)
                if 'e' not in obtener_first(s):
                    break
            else:
                resultado.add('e')
        return resultado

    for no_terminal in producciones:
        first[no_terminal] = obtener_first(no_terminal)
    return first


def calcular_follow(producciones, simbolo_inicial, first):
    follow = {no_terminal: set() for no_terminal in producciones}
    follow[simbolo_inicial].add('$')  

    while True:
        cambios = False
        for no_terminal, alternativas in producciones.items():
            for alternativa in alternativas:
                for i, simbolo in enumerate(alternativa):
                    if simbolo.isupper():  
                        siguientes = set()
                        for s in alternativa[i + 1:]:
                            if s in first:  
                                siguientes |= first[s] - {'e'}
                            else:  
                                siguientes.add(s)
                                break
                            if 'e' not in first[s]:
                                break
                        else:
                            siguientes |= follow[no_terminal]
                        if not siguientes.issubset(follow[simbolo]):
                            follow[simbolo] |= siguientes
                            cambios = True
        if not cambios:
            break
    return follow
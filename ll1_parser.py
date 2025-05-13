def es_ll1(producciones, first, follow):
    for no_terminal, alternativas in producciones.items():
        conjuntos = []
        for alternativa in alternativas:
            conjunto = set()
            for simbolo in alternativa:
                if simbolo.islower() or simbolo == 'e':  
                    conjunto.add(simbolo)
                    break
                else:  
                    conjunto |= first[simbolo]
                    if 'e' not in first[simbolo]:
                        break
            else:
                conjunto |= follow[no_terminal]
            if any(conjunto & c for c in conjuntos):
                return False
            conjuntos.append(conjunto)
    return True


def construir_tabla_ll1(producciones, first, follow):
    tabla = {}
    for no_terminal, alternativas in producciones.items():
        for alternativa in alternativas:
            conjunto = set()
            for simbolo in alternativa:
                if simbolo.islower() or simbolo == 'e':  
                    conjunto.add(simbolo)
                    break
                else:  
                    conjunto |= first[simbolo]
                    if 'e' not in first[simbolo]:
                        break
            else:
                conjunto |= follow[no_terminal]
            for terminal in conjunto:
                if terminal != 'e':
                    if (no_terminal, terminal) in tabla:
                        raise ValueError(f"Conflicto en la tabla LL(1) para ({no_terminal}, {terminal})")
                    tabla[(no_terminal, terminal)] = alternativa
    return tabla

def analizar_cadena_ll1(cadena, tabla_ll1, simbolo_inicial):
    pila = [simbolo_inicial, '$']
    entrada = list(cadena) + ['$']

    while pila:
        tope = pila.pop()
        simbolo = entrada[0]

        if tope == simbolo == '$':
            return True
        elif tope.islower() or tope == '$':
            if tope == simbolo:
                entrada.pop(0)
            else:
                return False
        elif (tope, simbolo) in tabla_ll1:
            produccion = tabla_ll1[(tope, simbolo)]
            if produccion != ['e']:
                pila.extend(reversed(produccion))
        else:
            return False
    return False
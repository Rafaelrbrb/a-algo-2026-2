import heapq

# Grafo representando as distâncias entre os polos tecnológicos
grafo = {
    'A': [('B', 4), ('C', 4)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 5), ('E', 6)],
    'D': [('B', 5), ('C', 5), ('E', 3), ('F', 4)],
    'E': [('C', 6), ('D', 3), ('F', 2)],
    'F': [('D', 4), ('E', 2)]
}


def prim(grafo, inicio):
    visitados = set()
    fila_prioridade = []
    arvore_minima = []
    custo_total = 0

    # Adiciona o nó inicial
    visitados.add(inicio)

    # Coloca as arestas do nó inicial na fila
    for vizinho, peso in grafo[inicio]:
        heapq.heappush(fila_prioridade, (peso, inicio, vizinho))

    while fila_prioridade:
        peso, origem, destino = heapq.heappop(fila_prioridade)

        # Ignora se já foi visitado
        if destino in visitados:
            continue

        # Marca como visitado
        visitados.add(destino)

        # Adiciona na árvore mínima
        arvore_minima.append((origem, destino, peso))
        custo_total += peso

        # Adiciona novas conexões
        for vizinho, novo_peso in grafo[destino]:
            if vizinho not in visitados:
                heapq.heappush(
                    fila_prioridade,
                    (novo_peso, destino, vizinho)
                )

    return arvore_minima, custo_total


# Executando o algoritmo
rota, total = prim(grafo, 'A')

# Exibindo resultados
print("Rotas dos cabos instalados:\n")

for origem, destino, peso in rota:
    print(f"{origem} --> {destino} : {peso} Km")

print(f"\nQuantidade total mínima de cabos: {total} Km")
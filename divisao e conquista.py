def conta_elementos(vetor):
    # Caso base: se o vetor estiver vazio, retorne 0
    if len(vetor) == 0:
        return 0
    # Caso base: se o vetor contém apenas um elemento, retorne 1
    elif len(vetor) == 1:
        return 1
    else:
        # Divida o vetor ao meio
        meio = len(vetor) // 2
        # Conquiste: conte os elementos na primeira metade e na segunda metade
        return conta_elementos(vetor[:meio]) + conta_elementos(vetor[meio:])

# Testando a função
vetor = [1, 2, 3, 4, 5]
print(conta_elementos(vetor))  # Deve imprimir 5

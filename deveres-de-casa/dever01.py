class Paciente:
    def __init__(self, nome, dor):
        self.nome = nome
        self.dor = dor

    def __str__(self):
        return f"{self.nome} (Dor: {self.dor})"


class MaxHeap:
    def __init__(self):
        self.heap = []

    # Índices
    def pai(self, i):
        return (i - 1) // 2

    def esquerda(self, i):
        return 2 * i + 1

    def direita(self, i):
        return 2 * i + 2

    # Inserir paciente
    def inserir(self, paciente):
        self.heap.append(paciente)
        self.subir(len(self.heap) - 1)

    # Ajustar para cima
    def subir(self, i):
        while i > 0 and self.heap[self.pai(i)].dor < self.heap[i].dor:
            self.heap[i], self.heap[self.pai(i)] = (
                self.heap[self.pai(i)],
                self.heap[i],
            )
            i = self.pai(i)

    # Ajustar para baixo
    def descer(self, i):
        maior = i
        esq = self.esquerda(i)
        dir = self.direita(i)

        if esq < len(self.heap) and self.heap[esq].dor > self.heap[maior].dor:
            maior = esq

        if dir < len(self.heap) and self.heap[dir].dor > self.heap[maior].dor:
            maior = dir

        if maior != i:
            self.heap[i], self.heap[maior] = self.heap[maior], self.heap[i]
            self.descer(maior)

    # Remover paciente com maior prioridade
    def atender_paciente(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        raiz = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.descer(0)

        return raiz

    # Alterar prioridade (Increase/Decrease Key)
    def alterar_prioridade(self, nome, nova_dor):
        for i in range(len(self.heap)):
            if self.heap[i].nome == nome:
                dor_antiga = self.heap[i].dor
                self.heap[i].dor = nova_dor

                # Se aumentou a dor -> sobe no heap
                if nova_dor > dor_antiga:
                    self.subir(i)

                # Se diminuiu a dor -> desce no heap
                else:
                    self.descer(i)

                print(f"Prioridade de {nome} alterada para {nova_dor}")
                return

        print("Paciente não encontrado.")

    # Mostrar heap
    def mostrar_fila(self):
        print("\nFila de Prioridade:")
        for paciente in self.heap:
            print(paciente)


# ==========================
# Programa principal
# ==========================

fila = MaxHeap()

n = int(input("Quantidade de pacientes: "))

for _ in range(n):
    nome = input("Nome do paciente: ")
    dor = int(input("Nível de dor (1-10): "))

    fila.inserir(Paciente(nome, dor))

fila.mostrar_fila()

# Alterar prioridade
print("\n=== Alterar Prioridade ===")
nome = input("Nome do paciente: ")
nova_dor = int(input("Novo nível de dor: "))

fila.alterar_prioridade(nome, nova_dor)

fila.mostrar_fila()

# Atendimento
print("\n=== Ordem de Atendimento ===")
while len(fila.heap) > 0:
    paciente = fila.atender_paciente()
    print(f"Atendendo: {paciente}")

"""
Inserção no Heap: O(log n)
Remoção do maior elemento: O(log n)
Alterar prioridade (Increase/Decrease Key):
Buscar o paciente: O(n)
Reorganizar o heap: O(log n)
"""
class Node:
    """Classe que representa cada nó da lista encadeada."""

    def __init__(self, data):
        self.data = data  # Armazena o valor do nó
        self.next = None  # Referência para o próximo nó (inicialmente nulo)


class LinkedList:
    """Classe que representa a lista encadeada simples."""

    def __init__(self):
        self.head = None  # A lista começa vazia (cabeça é None)

    def is_empty(self):
        """Verifica se a lista está vazia."""
        return self.head is None

    def insert_beginning(self, value):
        """Insere um elemento no início da lista."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, value):
        """Insere um elemento no final da lista."""
        new_node = Node(value)

        if self.is_empty():
            self.head = new_node
            return

        current = self.head
        # Percorre até encontrar o último nó
        while current.next:
            current = current.next

        current.next = new_node

    def remove(self, value):
        """Remove a primeira ocorrência do elemento na lista."""
        if self.is_empty():
            print("A lista está vazia. Nada para remover.")
            return False

        # Caso especial: o valor a ser removido está no primeiro nó (head)
        if self.head.data == value:
            self.head = self.head.next
            return True

        current = self.head
        # Percorre a lista verificando o próximo nó
        while current.next:
            if current.next.data == value:
                # Pula o nó que contém o valor, removendo-o da cadeia
                current.next = current.next.next
                return True
            current = current.next

        print(f"Valor {value} não encontrado na lista.")
        return False

    def search(self, value):
        """Procura um elemento na lista e retorna True se encontrado, caso contrário retorna False."""
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def print_list(self):
        """
        Imprime os elementos da lista encadeada em um formato legível.
        Se a lista estiver vazia, imprime "Lista Vazia".
        Caso contrário, percorre a lista, coleta os dados de cada nó
        e imprime os elementos no formato: "dado1 -> dado2 -> ... -> None"."""
        if self.is_empty():
            print("Lista Vazia")
            return

        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next

        print(" -> ".join(elements) + " -> None")

    def size(self):
        """Retorna o tamanho atual da lista (quantidade de nós)."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


minha_lista = LinkedList()

# Inserindo elementos
minha_lista.insert_end(10)
minha_lista.insert_end(20)
minha_lista.insert_beginning(5)
minha_lista.insert_end(30)

# Imprimindo a lista
print("Lista atual:")
minha_lista.print_list()

# Verificando o tamanho
print(f"Tamanho da lista: {minha_lista.size()}")

# Buscando elementos
print(f"O número 20 está na lista? {minha_lista.search(20)}")
print(f"O número 50 está na lista? {minha_lista.search(50)}")

# Removendo um elemento do meio e outro do início
minha_lista.remove(20)
minha_lista.remove(5)

# Imprimindo após remoções
print("\nLista após remoções:")
minha_lista.print_list()
print(f"Novo tamanho da lista: {minha_lista.size()}")

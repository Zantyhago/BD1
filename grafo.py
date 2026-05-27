class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, origen, destino, peso):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen].append((destino, peso))
            #self.vertices[destino].append(origen)

    def obtener_vertices(self):
            return list(self.vertices.keys())
    
    def obtener_aristas(self):
        aristas = []
        for vertice, adyacentes in self.vertices.items():
            for adyacente, peso in adyacentes:
                aristas.append((vertice, adyacente, peso))
        return aristas

# Ejemplo de uso
grafo = Grafo()

# Agregar vértices al grafo
grafo.agregar_vertice("1")
grafo.agregar_vertice("2")
grafo.agregar_vertice("3")
grafo.agregar_vertice("4")
grafo.agregar_vertice("5")
grafo.agregar_vertice("6")
grafo.agregar_vertice("7")
grafo.agregar_vertice("8")
grafo.agregar_vertice("9")
grafo.agregar_vertice("10")
grafo.agregar_vertice("11")
grafo.agregar_vertice("12")
grafo.agregar_vertice("13")
grafo.agregar_vertice("14")

# Agregar aristas al grafo
grafo.agregar_arista("3", "4", "C")
grafo.agregar_arista("1", "4", "C")
grafo.agregar_arista("2", "5", "C")
grafo.agregar_arista("1", "6", "C")
grafo.agregar_arista("3", "6", "C")
grafo.agregar_arista("4", "7", "C")
grafo.agregar_arista("1", "7", "R")
grafo.agregar_arista("5", "8", "C")
grafo.agregar_arista("2", "8", "R")
grafo.agregar_arista("5", "9", "C")
grafo.agregar_arista("2", "9", "R")
grafo.agregar_arista("4", "10", "C")
grafo.agregar_arista("1", "10", "R")
grafo.agregar_arista("7", "11", "C")
grafo.agregar_arista("8", "11", "C")
grafo.agregar_arista("4", "11", "R")
grafo.agregar_arista("7", "12", "C")
grafo.agregar_arista("4", "12", "R")
grafo.agregar_arista("9", "13", "C")
grafo.agregar_arista("5", "13", "R")
grafo.agregar_arista("4", "14", "C")
grafo.agregar_arista("3", "14", "R")

# Obtener todos los vértices del grafo
vertices = grafo.obtener_vertices()
print("Vértices:", vertices)

# Obtener todas las aristas del grafo
aristas = grafo.obtener_aristas()
print("Aristas:")
for arista in aristas:
    print(arista)
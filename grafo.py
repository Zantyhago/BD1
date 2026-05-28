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

#Ejecución
grafo = Grafo()

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

grafo.agregar_arista("3", "4", "cursada")
grafo.agregar_arista("1", "4", "rendida")
grafo.agregar_arista("2", "5", "cursada")
grafo.agregar_arista("1", "6", "cursada")
grafo.agregar_arista("3", "6", "cursada")
grafo.agregar_arista("4", "7", "cursada")
grafo.agregar_arista("1", "7", "rendida")
grafo.agregar_arista("5", "8", "cursada")
grafo.agregar_arista("2", "8", "rendida")
grafo.agregar_arista("5", "9", "cursada")
grafo.agregar_arista("2", "9", "rendida")
grafo.agregar_arista("4", "10", "cursada")
grafo.agregar_arista("1", "10", "rendida")
grafo.agregar_arista("7", "11", "cursada")
grafo.agregar_arista("8", "11", "cursada")
grafo.agregar_arista("4", "11", "rendida")
grafo.agregar_arista("7", "12", "cursada")
grafo.agregar_arista("4", "12", "rendida")
grafo.agregar_arista("9", "13", "cursada")
grafo.agregar_arista("5", "13", "rendida")
grafo.agregar_arista("4", "14", "cursada")
grafo.agregar_arista("3", "14", "rendida")

print("\nCuatrimestre 1:\n1: AyRP. 2: M. Básica. 3: EyFC.\nCuatrimestre 2:\n4: Prog. Proc. 5: Álgebra Lineal. 6: SO.\nCuatrimestre 3:\n7: POO. 8: Teo. de la Comp. 9: AM I. 10: Ing. de Sist.\nCuatrimestre 4:\n11: EDA. 12: Prog. Web. 13: AM II. 14: Inglés I\n\n")
vertices = grafo.obtener_vertices()
print("Vértices:", vertices)

aristas = grafo.obtener_aristas()
print("\nAristas:")
for arista in aristas:
    txtArco = str(arista)
    txtArco.strip()
    cadena = txtArco.split(",")
    materia1 = cadena[0].replace("(","")
    materia1 = materia1.replace("[","")
    materia1 = materia1.replace("'","")
    materia2 = cadena[1].replace("'","")
    peso = cadena[2].replace(")","")
    peso = peso.replace("'","")
    print(f"{materia2} necesita {materia1} {peso} para cursar.")
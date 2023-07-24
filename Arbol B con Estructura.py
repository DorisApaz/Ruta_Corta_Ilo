class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijo_izquierdo = None
        self.hijo_derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.hijo_izquierdo is None:
                nodo_actual.hijo_izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.hijo_izquierdo)
        else:
            if nodo_actual.hijo_derecho is None:
                nodo_actual.hijo_derecho = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.hijo_derecho)

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(valor, nodo_actual.hijo_izquierdo)
        else:
            return self._buscar_recursivo(valor, nodo_actual.hijo_derecho)

    def recorrido_inorden(self):
        self._recorrido_inorden_recursivo(self.raiz)

    def _recorrido_inorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._recorrido_inorden_recursivo(nodo_actual.hijo_izquierdo)
            print(nodo_actual.valor)
            self._recorrido_inorden_recursivo(nodo_actual.hijo_derecho)

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(200)
arbol.insertar(376)
arbol.insertar(736)
arbol.insertar(234)
arbol.insertar(422)


arbol.recorrido_inorden()  # Imprime: 200 234 376 422 736

nodo_encontrado = arbol.buscar(376)
if nodo_encontrado:
    print("El nodo con valor 376 fue encontrado.")
else:
    print("El nodo con valor 376  no fue encontrado.")

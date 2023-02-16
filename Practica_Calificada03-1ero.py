class ListaEnlazada:
    class Nodo:
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None

    def __init__(self):
        self.primero = None
        self.tamanio = 0
    
    def agregar(self, valor):
        nodo = self.Nodo(valor)
        if self.tamanio == 0:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.siguiente != None:
                actual = actual.siguiente
            actual.siguiente = nodo
        
        self.tamanio += 1

    def agregar_Final(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.size += 1

    def eliminarInicio(self):
        if len(self) == 0:
            pass
        elif self.primero.siguiente == None:
            self.primero = None
        else:
            self.primero = self.primero.siguiente
    
    def eliminar(self, valor):
        if self.tamanio == 0:
            return False
        elif valor == self.primero.dato:
            self.primero = self.primero.siguiente
            
        else:
            actual = self.primero
            try:
                while actual.siguiente.dato != valor:
                    actual = actual.siguiente
                
                nodoBorrar = actual.siguiente
                actual.siguiente = nodoBorrar.siguiente
                
            except AttributeError:
                return False
        
        self.tamanio -= 1          
    
    def __len__(self):
        return self.tamanio
    
    def __str__(self):
        cadena = ''
        actual = self.primero
        while actual != None:
            cadena += str(actual.dato)
            cadena += ' ⟶  '
            actual = actual.siguiente
        cadena += 'None'
        
        return cadena

class Producto():
    def __init__(self):
        self.nombre = None

def lista_Compras():
    lista_Compras = listaSimple.ListaEnlazada()
    def menu():
        print('''
        ---Lista de Compra---
        1. Agregar producto 
        2. Eliminar primer producto
        3. Mostrar productos
        4. Fin
        ''')
        val = input('Opcion: ')
        return val

    def agregarProducto(producto):
        lista_Compras.agregar(producto)

    def eliminarPrimerProducto():
        lista_Compras.eliminarInicio()
    
    def mostrarListaProducto():
        cont = 0
        cadena = ''
        lista = lista_Compras
        actual = lista.primero

        while actual != None:
            cadena += f'Producto {cont + 1}: {actual.dato.nombre}'
            cadena += '\n'
            actual = actual.siguiente
            cont += 1
        if cont == 0:
            cadena += 'No hay productos para mostrar'

        return cadena

    # _main_

    while True:
        val = menu()
        if val == '1':
            producto = Producto()
            nombre = input("Ingrese nombre de producto: ")
            producto.nombre = nombre
            agregarProducto(producto)

        elif val == '2':
            eliminarPrimerProducto()

        elif val == '3':
            cadena = mostrarListaProducto()
            print(cadena)

        elif val == '4':
            break

        else:
            print('Ingrese una opción correcta')
            pass

if __name__ == "__main__":
    lista_Compras()
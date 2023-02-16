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

    def agregar_inicio(self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.anterior = None
            self.primero = aux
        self.size += 1

    def eliminar_final(self):
        if self.vacia():
            print("Lista Vacía")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size -= 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -= 1
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
    def recorrer_fin_inicio(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.anterior

def historialTareas():
    historialTareas = listaSimple.ListaEnlazada()
    def menu():
        print('''
        --- Historial de tarea ---
        1. Agregar tarea 
        2. Eliminar tarea
        3. Mostrar tarea
        4. Fin
        ''')
        val = input('Opcion: ')
        return val

    def agregarTarea(tarea):
        historialTareas.agregarInicio(tarea)

    def eliminarTarea(tarea):
        historialTareas.eliminar(tarea)
    
    def mostrarTareas():
        cont = 0
        cadena = ''
        lista = historialTareas
        actual = lista.primero

        while actual != None:
            cadena +=  f'Tarea {cont + 1}: {actual.dato}'
            cadena += '\n'
            actual = actual.siguiente
            cont += 1
        if cont == 0:
            cadena += 'No hay tareas para mostrar'

        return cadena

    # __main__

    ultTarea = ''
    while True:
        val = menu()
        if val == '1':
            tarea = input("Ingrese una tarea: ")
            agregarTarea(tarea)
            ultTarea = tarea

        elif val == '2':
            eliminarTarea(ultTarea)

        elif val == '3':
            cadena = mostrarTareas()
            print(cadena)

        elif val == '4':
            break

        else:
            print('Ingrese la opción correcta!')
            pass

if __name__ == "__main__":
    historialTareas()

#-------------------------------------------------------------------------------------
#                       PROGRAMACION ORIENTADA A OBJETOS
#--------------------------------------------------------------------------------------
# La función del codigo es gestionar una lista de tareas pendietes permitiendo:
# 1. Agregar
# 2. Marcar como completada
# 3. Mostrar
# 4. Eliminar tareas
#-----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
#Importación del modulo time para usar la funcion sleep
#------------------------------------------------------------------------------------
import time
#-----------------------------------------------------------------------------------

#------------------------------------------------------------------------------------
#Impresion de un banner como titulo 
#-------------------------------------------------------------------------------------
banner="""╔═╗╔═╗╔═╗╔╦╗╔═╗╦═╗  ╔╦╗╔═╗  ╔╦╗╔═╗╦═╗╔═╗╔═╗╔═╗
║ ╦║╣ ╚═╗ ║ ║ ║╠╦╝   ║║║╣    ║ ╠═╣╠╦╝║╣ ╠═╣╚═╗
╚═╝╚═╝╚═╝ ╩ ╚═╝╩╚═  ═╩╝╚═╝   ╩ ╩ ╩╩╚═╚═╝╩ ╩╚═╝  """

print(banner)
#----------------------------------------------------------------------------

#-------------------------------------------------------------------------------------
# Definición de una función para una animación de carga
#--------------------------------------------------------------------------------------
def loading ():
         # Define una lista de caracteres que representarán los distintos estados de la animación
        signs = ["|", "/", "-", "\\"]
        # Inicia un bucle que se ejecutará 40 veces para controlar la duración de la animación
        for i in range(40):
                # Imprime en la misma línea el símbolo correspondiente al estado actual de la animación
                ## Selecciona el símbolo mediante el operador de módulo
                print(signs[i%4].format(i%4), end='\r')
                 # Tiempo de espera para crear el efecto de animación
                time.sleep(0.1)
#-----------------------------------------------------------------------------------------------------


#Para que se de lugar a la función del codigo se siguen los siguientes pasos:

#-----------------------------------------------------------------------------------------------
# 1. Definición de la clase 'Tarea' y caracteristicas de ella como su nombre o estado
#-----------------------------------------------------------------------------------------------
class Tarea:
    """Clase que representa una tarea con un nombre y un estado: pendiente o completada."""
    # 1.1. Función para definir la clase 'Tarea' en función de las variables del nombre y el estado
    def __init__(self, nombre):
        #Inicia el nombre de la tarea
        self.nombre = nombre
        #Inicia el estado de la tarea como pendiente
        self.completada = False

   # 1.2. Función para marcar la tarea como completada
    def marcar_completada(self):
        """Marca la tarea como completada."""
        # Cambia el estado de la tarea a completada
        self.completada = True

    # 1.3. Función para representar la tarea como una cadena de texto
    def __str__(self):
        """Devuelve una representación en cadena de la tarea, indicando si está completada o pendiente."""
         # Determina el estado de la tarea
        estado = 'Completada' if self.completada else 'Pendiente'
        # Devuelve el nombre de la tarea y su estado
        return f'{self.nombre} - {estado}'
#-----------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# 2. Definición de la clase 'ListaTareas'
#-------------------------------------------------------------------------------
class ListaTareas:
    """Clase que gestiona una lista de tareas."""

    # 2.1. Función para definir la clase 'ListaTareas'
    def __init__(self):
        # Inicializa una lista vacía de tareas
        self.tareas = []  

    # 2.2. Función para agregar una nueva tarea a la lista
    def agregar_tarea(self, nombre):
        """Agrega una nueva tarea a la lista de tareas."""
        # Crea una nueva instancia de la clase 'Tarea'
        tarea = Tarea(nombre)
        # Agrega la tarea a la lista de tareas
        self.tareas.append(tarea)
        # Llama a la función para iniciar la animación de carga
        loading()
        # Imprime un mensaje confirmando que la tarea fue agregada
        print(f'Tarea "{nombre}" agregada.')

    # 2.3. Función para marcar una tarea como completada por su índice
    def marcar_completada(self, indice):
        """Marca una tarea como completada dado su índice en la lista."""
        try:
            # Intenta marcar la tarea en el índice dado como completada
            self.tareas[indice].marcar_completada()  
            # Llama a la función para iniciar la animación de carga
            loading()
            # Imprime un mensaje confirmando que la tarea fue marcada como completada
            print(f'Tarea "{self.tareas[indice].nombre}" marcada como completada.')
        except IndexError:
            # Imprime un mensaje de error si el índice no es válido
            print("Error: El índice proporcionado no es válido.")

    # 2.4. Función para mostrar todas las tareas con su estado
    def mostrar_tareas(self):
        """Muestra todas las tareas con su estado."""
        if not self.tareas:
             # Imprime un mensaje si no hay tareas en la lista
            print("No hay tareas en la lista.")
        else:
            # Recorre la lista de tareas con un índice que empieza en 1
            for i, tarea in enumerate(self.tareas, start=1):
                # Imprime cada tarea con su índice
                print(f'{i}. {tarea}')

    # 2.5. Función para eliminar una tarea de la lista por su índice
    def eliminar_tarea(self, indice):
        """Elimina una tarea de la lista dado su índice."""
        try:
            # Intenta eliminar la tarea en el índice dado
            tarea_eliminada = self.tareas.pop(indice) 
            # Imprime un mensaje confirmando que la tarea fue eliminada
            print(f'Tarea "{tarea_eliminada.nombre}" eliminada.')
        except IndexError:
            # Imprime un mensaje de error si el índice no es válido
            print("Error: El índice proporcionado no es válido.")
#------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------
# 3. Función principal que ejecuta el gestor de tareas
#-------------------------------------------------------------------------------------------------
def main():
    # Crea una nueva instancia de 'ListaTareas'
    lista_tareas = ListaTareas()  

    # 3.1. Bucle infinito para el menú interactivo
    while True:
        print("\n Bienvenido al gestor de tareas. Las tareas disponibles son las siguientes:")  # Imprime el título del menú
        print("1. Agregar tarea")  # Opción para agregar una tarea
        print("2. Marcar tarea como completada")  # Opción para marcar una tarea como completada
        print("3. Mostrar todas las tareas")  # Opción para mostrar todas las tareas
        print("4. Eliminar tarea")  # Opción para eliminar una tarea
        print("5. Salir")  # Opción para salir del programa

        # Solicita al usuario que seleccione una opción:
        opcion = input("Seleccione una opción: ")
        
        # Llama a la función para iniciar la animación de carga
        loading()
        
        # 3.1.1. Si la opción es '1':
        if opcion == '1':
            #Primero, solicita el nombre de la tarea
            nombre_tarea = input("Ingrese el nombre de la tarea: ")
            # Agrega la tarea a la lista
            lista_tareas.agregar_tarea(nombre_tarea)

        # 3.1.2. Si la opción es '2'
        elif opcion == '2':
            try:
                # Solicita el índice de la tarea a marcar como completada
                indice_tarea = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
                # Marca la tarea como completada
                lista_tareas.marcar_completada(indice_tarea)
            except ValueError:
                # Imprime un mensaje de error si la entrada no es un número válido
                print("Error: Ingrese un número válido.")

        # 3.1.3. Si la opción es '3'
        elif opcion == '3':
            # Muestra todas las tareas
            lista_tareas.mostrar_tareas()  

         # 3.1.4. Si la opción es '4'
        elif opcion == '4':
            try:
                # Solicita el índice de la tarea a eliminar
                indice_tarea = int(input("Ingrese el número de la tarea a eliminar: ")) - 1  
                # Elimina la tarea de la lista
                lista_tareas.eliminar_tarea(indice_tarea)
            except ValueError:
                # Imprime un mensaje de error si la entrada no es un número válido
                print("Error: Ingrese un número válido.") 
        
        # 3.1.5. Si la opción es '5'
        elif opcion == '5':
            # Imprime un mensaje de salida
            print("Saliendo del gestor de tareas.")
            # Llama a la función para iniciar la animación de carga
            loading()
            # Rompe el bucle para salir del programa
            break
        # Imprime un mensaje de error si la opción solicitada no es válida
        else:
            print("Opción no válida, por favor seleccione una opción del 1 al 5.") 

# Ejecuta la función principal si el archivo se ejecuta como un script
if __name__ == "__main__":
    main()
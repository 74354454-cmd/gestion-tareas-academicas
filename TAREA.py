import datetime

class Tarea:
    """Clase que representa una tarea académica siguiendo Clean Code."""
    
    def __init__(self, titulo, fecha_limite, prioridad):
        self.titulo = titulo
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.completada = False

    def __str__(self):
        estado = "✅" if self.completada else "⏳"
        return f"[{estado}] {self.titulo} - Vence: {self.fecha_limite} (Prioridad: {self.prioridad})"

class GestorTareas:
    """Clase encargada de la lógica de negocio y manejo de datos."""
    
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, fecha_str, prioridad):
        """Implementa manejo de excepciones para robustez."""
        try:
            # Validación de fecha
            fecha_valida = datetime.datetime.strptime(fecha_str, '%Y-%m-%d').date()
            
            # Validación de prioridad
            prioridad_int = int(prioridad)
            if not (1 <= prioridad_int <= 5):
                raise ValueError("La prioridad debe estar entre 1 y 5.")

            nueva_tarea = Tarea(titulo, fecha_valida, prioridad_int)
            self.tareas.append(nueva_tarea)
            print("✔️ Tarea agregada con éxito.")
            
        except ValueError as e:
            print(f"❌ Error de validación: {e}")
        except Exception as e:
            print(f"❌ Ocurrió un error inesperado: {e}")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
            return
        
        print("\n--- LISTA DE TAREAS ACADÉMICAS ---")
        for i, tarea in enumerate(self.tareas, 1):
            print(f"{i}. {tarea}")

def menu():
    gestor = GestorTareas()
    
    while True:
        print("\n1. Agregar Tarea\n2. Ver Tareas\n3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Nombre de la tarea: ")
            fecha = input("Fecha límite (AAAA-MM-DD): ")
            prioridad = input("Prioridad (1-5): ")
            gestor.agregar_tarea(titulo, fecha, prioridad)
        elif opcion == "2":
            gestor.mostrar_tareas()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
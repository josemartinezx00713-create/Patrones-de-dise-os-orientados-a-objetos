"""
PATRÓN CREACIONAL: SINGLETON (Instancia Única)

Explicación Detallada:
El patrón Singleton garantiza que una clase tenga únicamente UNA instancia en todo el ciclo de vida del programa.
Para lograr esto, 'secuestramos' el método de creación nativo de la clase (en Python es __new__) para que:
1. Revise si ya hay una instancia guardada.
2. Si NO la hay, permita crearla y la guarde.
3. Si SÍ la hay, aborte la creación y simplemente devuelva la que ya estaba guardada.

¿Cuándo usarlo? Cuando debes tener control total y centralizado sobre un recurso, como la conexión a 
una Base de Datos, el manejo de configuraciones de una aplicación (como este ejemplo) o un sistema de Logs.
"""

class RegistroUnico:
    # Atributo estático a nivel de clase donde guardaremos la única instancia permitida.
    # Comienza en None porque al inicio aún no existe nada.
    _instancia = None

    # __new__ se ejecuta ANTES que __init__. Es el verdadero constructor en Python.
    def __new__(cls):
        # Paso 1: Verificamos si _instancia sigue siendo None (es la primera vez que se llama)
        if cls._instancia is None:
            # Paso 2: Usamos super().__new__(cls) para crear verdaderamente el objeto en memoria
            cls._instancia = super().__new__(cls)
            # Inicializamos nuestro estado interno solo esta primera vez (ej: la lista de mensajes vacía)
            cls._instancia.mensajes = []
            print("[✓] Se ha creado la instancia del Registro por primera y ÚNICA vez en la memoria.")
        
        # Paso 3: Retornamos la instancia. 
        # Si no era None, se saltó el 'if' y directamente retorna la vieja instancia.
        return cls._instancia

    def agregar_mensaje(self, mensaje):
        # Este método es normal de la instancia, añade datos a la lista centralizada.
        self.mensajes.append(mensaje)


# --- DEMOSTRACIÓN ---
print("Empezamos el programa, varios sistemas intentarán crear su propio registro...\n")

# Punto A: Digamos que el "Sistema de Interfaz" pide el registro
print("-> Sistema de Interfaz pide una instancia:")
registro_a = RegistroUnico()
registro_a.agregar_mensaje("Error visual en la ventana principal.")

# Punto B: Digamos que el "Sistema de Red" también pide crear un registro
print("\n-> Sistema de Red pide otra instancia (supuestamente nueva):")
registro_b = RegistroUnico()
registro_b.agregar_mensaje("Advertencia de caída de red.")

# Verificación de que el patrón funciona:
# 'is' en Python verifica si físicamente apuntan al mismo espacio de memoria RAM
son_iguales = (registro_a is registro_b)

print(f"\n¿Son registro_a y registro_b exactamente el mismo objeto en memoria? -> {son_iguales}")

print("\nAl ver los mensajes en la segunda variable, veremos también los de la primera (porque es el mismo objeto):")
for msg in registro_b.mensajes:
    print(f" - {msg}")

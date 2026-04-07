"""
PATRÓN CREACIONAL: PROTOTYPE (Prototipo)

Explicación Detallada:
Crear objetos grandes desde cero ('new') en programación puede retrasar severamente al sistema porque
tendría que calcular variables, conectarse a bases de datos cada vez, generar lógicas o cargar 
texturas inmensas todas las veces.

El Patrón Prototipo te salva creando el Objeto "Pesado" UNA SOLA VEZ. Una vez que lo tienes "en caché",
simplemente le pides al objeto que se "Clone a sí mismo".
La máquina tarda milisegundos en clonar bytes en memoria (Ctrl+C, Ctrl+V), muchísimo menos que arrancar de cero.

¿Cuándo usarlo? Al instanciar muchos objetos que tienen la mayor parte de su información repetida.
(Generación masiva de enemigos iguales, clonación de figuras gráficas).
"""

# La librería copy se encarga nativamente de clonar objetos en memoria profunda
import copy

# ===============================
# OBJETO COSTOSO DE CREAR (El Elemento a clonar)
# ===============================
class FormaGeometrica:
    def __init__(self, nombre, color, tamaño, textura_compleja):
        # Imagina que recibir todo esto de una base de datos cuesta muchos segundos
        self.nombre = nombre
        self.color = color
        self.tamaño = tamaño
        self.textura_compleja = textura_compleja 
        
        # Simulamos que esto fue muy laborioso
        print(f"[*] (CARGANDO... Llenando memoria...) Se ha creado laboriosamente una forma desde CERO: '{self.nombre}'")

    # MÉTODO CLAVE DEL PROTOTYPE
    def clonar(self):
        # La instrucción copy.deepcopy copia estructuralmente el objeto a un espacio RAM nuevo sin llamar al __init__
        print(f"[>] Clonación inmediata de '{self.nombre}' invocada...")
        return copy.deepcopy(self)

    def mostrar_info(self, nombre_variable):
        print(f"[{nombre_variable}] Soy {self.nombre} de color {self.color}, tamaño {self.tamaño} y llevo Textura {self.textura_compleja}% cargada.")


# --- DEMOSTRACIÓN ---
print("=== Inicio del Editor de Dibujo ===\n")

# 1. El usuario arrastra un Círculo a la pantalla. Hay que crearlo desde cero con esfuerzo (Es el Prototipo)
circulo_rojo_original = FormaGeometrica("Círculo Perfecto", "Rojo Sangre", "Grande", "100")
print()

# 2. El usuario dice "Quiero 3 círculos idénticos".
print("El usuario presiona Ctrl+V varias veces para copiar el círculo original.")

# En lugar de crearlos desde 0 (volviendo a simular que tarda), los CLONAMOS en milisegundos.
clon_1 = circulo_rojo_original.clonar()
clon_2 = circulo_rojo_original.clonar()
clon_3 = circulo_rojo_original.clonar()

# 3. Y aunque los hemos clonado, siguen siendo objetos INDEPENDIENTES. 
# Puedo alterar uno de ellos sin destruir a los demas.
clon_3.color = "Azul Zafiro" # Modificamos el clon 3 independientemente

print("\nResultados en Pantalla después de las clonaciones:\n")
circulo_rojo_original.mostrar_info("Original")
clon_1.mostrar_info("Clon 1")
clon_2.mostrar_info("Clon 2")
clon_3.mostrar_info("Clon 3") # Este será azul zafiro, manteniendo la misma textura del original

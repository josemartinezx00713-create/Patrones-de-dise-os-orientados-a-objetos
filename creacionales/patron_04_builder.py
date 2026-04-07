"""
PATRÓN CREACIONAL: BUILDER (Constructor)

Explicación Detallada:
El Builder resuelve el problema del "Constructor Telescópico" gigantesco.
Imagina si tienes un documento que puede tener Título, Autor, Fotos, Videos y Links.
Si usas un __init__ tendrías esto: "Documento('Título', 'Autor', True, False, False)". Lleno de Trues y Falses confusos.

El Builder externaliza el proceso. Te permite construir el objeto POCO A POCO utilizando una clase dedicada
solo a armarlo. Retornar 'self' en cada método es un truco llamado 'Fluent Interface' que permite 
encadenar llamadas como 'armar().ponerA().ponerB()'.

¿Cuándo usarlo? Para objetos complejos que tienen muchos detalles opcionales al crearse (PCs a medida, Hamburguesas modulares,
documentos complejos).
"""

# ===============================
# 1. EL OBJETO COMPLEJO
# ===============================
# Esta clase no sabe cómo es construida por el usuario, solo tiene variables normales.
class Hamburguesa:
    def __init__(self):
        # Datos opcionales por pieza de comida
        self.pan = None
        self.carne = None
        self.queso = False
        self.lechuga = False
        self.salsa = None

    def mostrar(self):
        # Mostramos una representación visual bonita
        detalles = f"Pan: {self.pan} | Carne: {self.carne} "
        if self.queso: detalles += "| Queso Añadido "
        if self.lechuga: detalles += "| Lechuga Fresca "
        if self.salsa: detalles += f"| Salsa: {self.salsa} "
        print(detalles)


# ===============================
# 2. EL BUILDER (El cocinero / El constructor)
# ===============================
# Aquí está la magia. El usuario usará el Builder en lugar de a la Hamburguesa directo.
class HamburguesaBuilder:
    def __init__(self):
        # Comienza con una hamburguesa vacía
        self._hamburguesa = Hamburguesa()

    # Cada método arma una pequeña parte del objeto complejo
    def poner_pan(self, tipo_pan):
        self._hamburguesa.pan = tipo_pan
        # --- RETURN SELF ---
        # Al regresar 'self' (la instancia del constructor), quien nos llamó
        # puede ponerle un punto al final e invocar otro comando sin escribir la variable.
        return self  

    def poner_carne(self, tipo_carne):
        self._hamburguesa.carne = tipo_carne
        return self

    def añadir_queso(self):
        self._hamburguesa.queso = True
        return self

    def añadir_lechuga(self):
        self._hamburguesa.lechuga = True
        return self
        
    def añadir_salsa(self, tipo_salsa):
        self._hamburguesa.salsa = tipo_salsa
        return self

    def obtener_resultado(self):
        # Cuando termina devuelve el objeto complejo finalmente armado
        return self._hamburguesa


# --- DEMOSTRACIÓN ---
print("=== RECIBIENDO ÓRDENES DE CLIENTES ===\n")

print("Preparando una HAMBURGUESA DOBLE CON TODO ENCADENADO:\n")
# Observa cómo se "encadenan" los métodos porque todos retornan el mismo objeto Builder
mi_burger = (HamburguesaBuilder()
             .poner_pan("Sésamo tostado")
             .poner_carne("Doble Res Wagyu")
             .añadir_queso()
             .añadir_lechuga()
             .añadir_salsa("BBQ")
             .obtener_resultado()) # Al final pedimos el resultado para guardarlo en la variable
mi_burger.mostrar()


print("\nPreparando una HAMBURGUESA SENCILLA POR PASOS (Técnica clásica):\n")
# Esto es sin encadenar. A veces no puedes encadenar si el usuario lo hace en momentos y pantallas diferentes
constructor2 = HamburguesaBuilder()

constructor2.poner_pan("Pan Blanco Clásico")
constructor2.poner_carne("Pollo Frito")
# Este cliente no quiso ni queso, ni lechuga, ni salsa

# Obtenemos finalmente la hamburguesa
sencilla = constructor2.obtener_resultado()
sencilla.mostrar()

"""
PATRÓN ESTRUCTURAL: DECORATOR (Decorador)

Explicación Detallada:
Es una manera muy inteligente de agregar nuevas responsabilidades u opciones ("extras") a un objeto existente, pero 
DURANTE EL TIEMPO DE EJECUCIÓN DEL PROGRAMA, es decir, ¡sin modificar la clase original y sin crear subclases monstruosas!

Si no usaramos patron Decorator, tendríamos un caos de subclases: CafeConAzucarLecheYVainilla(), CafeSoloConVainilla()...
Con este patrón, creas tu objeto base (Ej. CafeSolo) puro y pequeño, y luego lo envuelves dentro de la decoración (Ej. Leche), 
y luego dentro de otra (Ej. Canela), como las famosas Muñecas Matryoshka rusas. Al final tú interactúas con la muñeca exterior, pero
ella llama a las más pequeñas en cascada hasta la del centro.

¿Cuándo usarlo? Cuando quieras añadir "complementos apilables" (como plugins a un editor, extras a la comida, coberturas a un escudo
en un videojuego) y de una manera flexible sin herencia pesada.
"""

from abc import ABC, abstractmethod

# ===============================
# 1. EL COMPONENTE CENTRAL BASE
# ===============================
class Bebida(ABC):
    @abstractmethod
    def obtener_nombre(self): pass
    
    @abstractmethod
    def obtener_precio(self): pass

# Este es la matryoshka chiquita, el objeto nuclear en el centro de todas las envolturas.
class CafeSolo(Bebida):
    def obtener_nombre(self):
        return "Taza de Café Negro Clásico"

    def obtener_precio(self):
        return 1.50 # Cuesta 1.50 dolares


# ===============================
# 2. EL DECORADOR ENVOLVENTE (BASE)
# ===============================
class DecoradorBebida(Bebida):
    # La parte mágica del patrón Decorator es recibir al componente base DURANTE la creación
    def __init__(self, bebida_interior: Bebida):
        # Nos lo guardamos en la panza para que se procese después
        self._bebida_interior = bebida_interior


# ===============================
# 3. LOS EXTRAS INDIVIDUALES CONCRETOS (Los decoradores funcionales)
# ===============================
class DecoradorEspumaLeche(DecoradorBebida):
    def obtener_nombre(self):
        # A lo que sea que estuviera devuelto antes, ponle el agregado
        return self._bebida_interior.obtener_nombre() + " [con Espuma Leche]"
    
    def obtener_precio(self):
        # Obtiene el precio del bloque completo que hay dentro y le suma su propio costo (+0.50)
        return self._bebida_interior.obtener_precio() + 0.50

class DecoradorChispaChocolate(DecoradorBebida):
    def obtener_nombre(self):
        return self._bebida_interior.obtener_nombre() + " [con Extra de Chispas]"

    def obtener_precio(self):
        return self._bebida_interior.obtener_precio() + 0.70


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN DECORATOR ===\n")

print("\n--- Cliente A pide un Café Normal y barato ---")
vaso_cliente_a = CafeSolo()
print(f"La bebida resultante es: {vaso_cliente_a.obtener_nombre()}")
print(f"Costo final: ${vaso_cliente_a.obtener_precio():.2f}")


print("\n--- Cliente B pide la bebida más grande de Starbucks ---")
# Empieza con la pequeña muñeca rusa
vaso_cliente_b = CafeSolo()

# Lo empezamos a envolver
vaso_cliente_b = DecoradorEspumaLeche(vaso_cliente_b)
vaso_cliente_b = DecoradorEspumaLeche(vaso_cliente_b) # Oh si, doble porción de leche. El patrón funciona perfecto apilándolo.
vaso_cliente_b = DecoradorChispaChocolate(vaso_cliente_b)

# Al pedir el nombre desde afuera, pasará las barreras transparentemente y construirá todo "on as-needed basis"
print(f"La bebida hiper-apilada es: {vaso_cliente_b.obtener_nombre()}")
print(f"Costo extra cobrado: ${vaso_cliente_b.obtener_precio():.2f}")

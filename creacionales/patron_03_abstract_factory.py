"""
PATRÓN CREACIONAL: ABSTRACT FACTORY (Fábrica Abstracta)

Explicación Detallada:
Imagina al Abstract Factory como "una fábrica de fábricas".
Problema a resolver: Tienes "Familias" de productos (Muebles victorianos vs Muebles modernos). 
Un 'Sillón Victoriano' solo debe combinarse con una 'Mesa Victoriana'.
Si los mezclas creas inconsistencias graves (un crash en UI o un diseño espantoso en muebles).

La Fábrica Abstracta define una interfaz genérica de la cual derivan fábricas específicas (TemaOscuro o TemaClaro).
Esto garantiza 100% que los objetos generados desde una de esas fábricas específicas SIEMPRE van a combinar entre sí.

¿Cuándo usarlo? Sistemas multiplataforma (UI para Windows y MacOS al mismo tiempo), Temas estéticos, etc.
"""

from abc import ABC, abstractmethod

# ===============================
# 1. INTERFACES DE LOS PRODUCTOS
# ===============================
# Todo tipo de tema tendrá un Botón y un Fondo
class Boton(ABC):
    @abstractmethod
    def click(self): pass

class Fondo(ABC):
    @abstractmethod
    def dibujar(self): pass


# ===============================
# 2. PRODUCTOS CONCRETOS (FAMILIA 1: Oscuro)
# ===============================
# Ambas piezas son exclusivamente para modo oscuro
class BotonOscuro(Boton):
    def click(self): print("🔘 [Dark-UI] Clicaste un botón con bordes negros y fondo oscuro.")

class FondoOscuro(Fondo):
    def dibujar(self): print("⬛ [Dark-UI] Pintando un fondo color gris muy oscuro, cuidando la vista.")

# ===============================
# 3. PRODUCTOS CONCRETOS (FAMILIA 2: Claro)
# ===============================
# Ambas piezas exclusivas de la versión clara
class BotonClaro(Boton):
    def click(self): print("⚪ [Light-UI] Clicaste un botón blanquecino con sombra suave.")

class FondoClaro(Fondo):
    def dibujar(self): print("⬜ [Light-UI] Pintando el fondo de un color blanco cegador clásico.")



# ===============================
# 4. LA FÁBRICA ABSTRACTA (Plantilla de Fábricas)
# ===============================
# Solo dice QUÉ SE DEBE FABRICAR, pero no dice cómo. Toda familia debe tener estos métodos.
class FabricaTema(ABC):
    @abstractmethod
    def crear_boton(self) -> Boton: pass
    
    @abstractmethod
    def crear_fondo(self) -> Fondo: pass


# ===============================
# 5. LAS FÁBRICAS CONCRETAS
# ===============================
# Esta es La Fabrica del Tema Oscuro. Solo va a botar componentes Oscuros. Es imposible que devuelva uno claro.
class TemaOscuro(FabricaTema):
    def crear_boton(self): return BotonOscuro()
    def crear_fondo(self): return FondoOscuro()

# Esta es La Fabrica del Tema Claro. Solo bota componentes Claros.
class TemaClaro(FabricaTema):
    def crear_boton(self): return BotonClaro()
    def crear_fondo(self): return FondoClaro()


# --- DEMOSTRACIÓN ---
# La función aplicar_tema no tiene idea de qué le vamos a mandar (si será Oscuro o Claro).
# Ella solo recibe una "Fábrica" cualquiera y sabe que al pedirle fondo y botón, ESTOS VAN A COMBINAR PERFECTO.
def aplicar_tema(fabrica: FabricaTema):
    fondo_actual = fabrica.crear_fondo()
    boton_actual = fabrica.crear_boton()
    
    print("-> Dibujando los elementos obtenidos de la fábrica:")
    fondo_actual.dibujar()
    boton_actual.click()

print("--- El sistema acaba de arrancar en TEMA OSCURO ---")
# Le pasamos la fábrica en modo oscuro, con total seguridad de compatibilidad
una_fabrica_oscura = TemaOscuro()
aplicar_tema(una_fabrica_oscura)

print("\n--- El usuario cambia manualmente en Ajustes a TEMA CLARO ---")
# Le pasamos la otra fábrica y reconstruye todo.
una_fabrica_clara = TemaClaro()
aplicar_tema(una_fabrica_clara)

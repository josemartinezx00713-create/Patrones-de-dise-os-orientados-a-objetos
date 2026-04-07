"""
PATRÓN ESTRUCTURAL: COMPOSITE (Patrón Compuesto)

Explicación Detallada:
Útil cuando debes manipular "Estructuras de Árbol", donde un elemento contiene más elementos similares a él 
y esos a su vez contienen aún más. Por ejemplo: El Sistema de Archivos de tu Computadora.
Una Carpeta tiene Archivos u otras Carpetas adentro.

El problema es que si tuvieras que preguntar todo el tiempo: "¿Eres archivo o eres carpeta? Ah, 
si eres carpeta métete dentro y revisa", el código sería espantoso (puros For-Loops anidados infinitos).
El patrón *Composite* arregla esto haciendo que los objetos hijos simples (Archivo) y 
los englobadores complejos (Carpeta) COMPARTAN LA MISMA INTERFAZ general (ComponenteSistema). 

Al compartirla, puedes llamar a `.mostrar()` en la C:\ principal, y la cascada lo resolverá hermosamente.

¿Cuándo usarlo? Diagramas de directorios, Menús UI anidados, organigramas corporativos complejos (Ceo->Managers->Empleados).
"""

from abc import ABC, abstractmethod

# ===============================
# 1. LA INTERFAZ COMPARTIDA (La Base)
# ===============================
# Tanto los Archivos solitarios como las Carpetas GIGANTES deberán implementar esto.
class ComponenteSistema(ABC):
    @abstractmethod
    def mostrar(self, tabulacion=0):
        # Recibe un nivel de tabulación solo para que se miren bonitos los espacios al imprimir
        pass

# ===============================
# 2. EL ELEMENTO HOJA "LEAF" (Elementos últimos de la cadena, NO contienen hijos)
# ===============================
class Archivo(ComponenteSistema):
    def __init__(self, nombre, tamaño_mb):
        self.nombre = nombre
        self.tamaño_mb = tamaño_mb

    def mostrar(self, tabulacion=0):
        # Calcula los espacios en blanco necesarios
        espacios = "  " * tabulacion
        # El archivo individual no tiene que complicarse, simplemente se imprime a sí mismo y termina ahí.
        print(f"{espacios}📄 [Arch] {self.nombre} - {self.tamaño_mb}MB")


# ===============================
# 3. EL COMPUESTO O ENGLOBADOR (Elementos que SÍ tienen Listas de hijos)
# ===============================
class Carpeta(ComponenteSistema):
    def __init__(self, nombre_carpeta):
        self.nombre = nombre_carpeta
        # Una lista para mantener rastreo de Archivos y *también Carpetas* hijas
        self._hijos = []

    def agregar_hijo(self, componente: ComponenteSistema):
        self._hijos.append(componente)

    def mostrar(self, tabulacion=0):
        espacios = "  " * tabulacion
        # Primero se imprime a sí misma como recipiente
        print(f"{espacios}📁 [Carpeta] {self.nombre}")
        
        # ACTO CLAVE DEL PATRÓN COMPOSITE:
        # Aquí delega la magia llamando al propio comando mostrar() sobre todos sus hijitos.
        # Por herencia recursiva, si el hijito es carpeta, repetirá la delegación. Si es archivo solo frenará.
        for hijo in self._hijos:
            # Los manda a ejecutarse sumando 1 al espacio de margen visual
            hijo.mostrar(tabulacion + 1)


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN COMPOSITE ===\n")

print("Se crearon archivos sueltos en memoria.")
doc_tesis = Archivo("Tesis_Final.pdf", 4)
doc_CV = Archivo("Curriculum.docx", 1)
meme_gato = Archivo("gato.jpg", 3)

# Armamos el arbol jerarquicamente
carpeta_uni = Carpeta("Documentos Universitarios")
carpeta_uni.agregar_hijo(doc_tesis)

carpeta_personal = Carpeta("Archivos Personales")
carpeta_personal.agregar_hijo(doc_CV)
carpeta_personal.agregar_hijo(meme_gato)
# Las carpetas pueden ir DENTRO de las carpetas perfectamente gracias a la Interfaz común!
carpeta_personal.agregar_hijo(carpeta_uni)

disco_C = Carpeta("Disco Duro Local C:\\")
# Metemos las carpetas en el disco principal junto con un programa suelto
disco_C.agregar_hijo(carpeta_personal)
disco_C.agregar_hijo(Archivo("python.exe", 25))

print("\nImprimiendo la estructura (¡Desde un solo punto llamamos a TODOS!)\n")
# Llamamos al padre principal y el patrón Composite hace el resto mágicamente:
disco_C.mostrar()

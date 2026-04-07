"""
PATRÓN DE COMPORTAMIENTO: STRATEGY (Estrategia Reemplazable)

Explicación Detallada:
Extrae algoritmos, y los mete en sus propias Clases para volverlos reemplazables "al vuelo".
Problema a la vista: Un algoritmo de "Filtro de colores en Photosohp" tiene 9 modos distintos.
(Blanco-negro, Negativo, UltraSaturación, etc).
Si tuvieras un gigantesco "If modo == 1: ... else If Modo == 2 ... " te quedará un archivo Python 
tan grande (10k líneas) que no se podrá leer y romperá todo Solid Princples.

Strategy hace que crees una clase `FiltroBlancoNegro`, y otra clase separada `FiltroUltraSaturado`.
En el Main, en tu Software en tiempo vivo, tu Inyectas la clase seleccionada por el usuario (o IA)
a la ranura cerebral. Tu software usará ciegamente la "Estrategia Activa" y si luego seleccionan otra,
desmontas y reemplazas como un casette de Atari Retro del viejo console.

¿Cuándo usarlo? Sistemas de cobro y pagos (Paypal, TCD, Cripto). Routing apps para Maps (Pie, Autos, Avión). Sort lists (Bubble, QuickSort).
"""

from abc import ABC, abstractmethod


# ===============================
# 1. LA INTERFAZ DE ESTRATEGIA MATRÍZ (LA RANURA CENTRAL DEL HARDWARE)
# ===============================
# El cartucho del Nintendo que calzara perfecto con las clavijas.  Cualquier ruta se calcula.
class ClavijaInterfazEstrategiaRuteoGPS(ABC):
    @abstractmethod
    def computar_y_crear_trayectoria(self, p_origen_coord: str, p_fin_destino: str):
        pass


# ===============================
# 2. LAS ESTRATEGIAS REEMPLAZABLES INDIVIDUALES (LOS CARTUCHOS)
# ===============================
# Cartucho amarillo: Autos pesados y rapidos
class AlgoritmoBypassPeajesCamionetas(ClavijaInterfazEstrategiaRuteoGPS):
    def computar_y_crear_trayectoria(self, p_origen_coord: str, p_fin_destino: str):
         return f"[🏎️ GPS COCHE] -> Computando ruta a base de Límites 120kmh. Autopistas y bypass conectando ({p_origen_coord}) hasta ({p_fin_destino}). Tiempo 40min."

# Cartucho Verde ecologico: A pedales.
class AlgoritmoSeguroBicicletas(ClavijaInterfazEstrategiaRuteoGPS):
     def computar_y_crear_trayectoria(self, p_origen_coord: str, p_fin_destino: str):
         return f"[🚲 GPS BICI] -> Calibrando trayectos seguros de ciclovías iluminadas evadiendo colosos motorizados entre ({p_origen_coord}) hasta ({p_fin_destino}). Cuidado baches de lluvia."

# Cartucho blanco aburrido: Gente con tenis.
class AlgoritmoApieUrbanoBasico(ClavijaInterfazEstrategiaRuteoGPS):
     def computar_y_crear_trayectoria(self, p_origen_coord: str, p_fin_destino: str):
         return f"[🚶 GPS PEATÓN] -> Trazando ruta cortísima entre callejones atajos raros invisibles al tránsito desde ({p_origen_coord}) hacia ({p_fin_destino}). Calorías estimadas quemadas 900kcal xd."


# ===============================
# 3. EL SISTEMA MATRÍZ QUE CAMBIA Y MUTA SU PROPIO CEREBRO (App del Usuario)
# ===============================
# La Maquinorra madre genérica central sin dependencias crudas duras a nadie.
class PhoneGoogleMapsSistemaApp:
    def __init__(self):
        # Inicia preconfiguradon su cerebro a algo por defecto standard y popular.
        self._ranura_de_memoria_estrategia = AlgoritmoBypassPeajesCamionetas()
        
    def clikear_el_intercambiar_modo_motor(self, el_nuevo_estrategia_cartucho: ClavijaInterfazEstrategiaRuteoGPS):
        print("\n [¡Hardware Swapping Live] Removiendo la estrategia anterior y encajando chips de rutado nuevos en la App! 💽...")
        self._ranura_de_memoria_estrategia = el_nuevo_estrategia_cartucho

    def invocar_accion_principal(self, lugar_a, lugar_z):
        # Invierte la cadena lógica en total locura. El llama ciego!
        texto_resultado_inmenso = self._ranura_de_memoria_estrategia.computar_y_crear_trayectoria(lugar_a, lugar_z)
        print(texto_resultado_inmenso)


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN STRATEGY ===\n")

print("Se enciende la app de GPS global de la humanidad de celular Apple.")
dispositivo_terminal = PhoneGoogleMapsSistemaApp()


print("1. Salimos de la casa hacia la gran ciudad central:")
dispositivo_terminal.invocar_accion_principal("Suburbio Nro 91A", "La Gran Plaza Central") # Lo usa por defecto en coche rapido


print("\n2. Oh, resulta ser un día hermoso de verano en Holanda. Saquemos la bicicleta mejor! [Cambio de estrategia]")
# Le pasamos UNA CLASE COMPLETA DISTINTA de estrategia viva como puntero intercambiable de memoria!
dispositivo_terminal.clikear_el_intercambiar_modo_motor( AlgoritmoSeguroBicicletas() )
dispositivo_terminal.invocar_accion_principal("Suburbio Nro 91A", "La Gran Plaza Central") 


print("\n3. Rayos, la rueda se me pinchó en pleno centro histórico. Tendré que irme caminando trágicamente hacia la terminal de buses...")
dispositivo_terminal.clikear_el_intercambiar_modo_motor( AlgoritmoApieUrbanoBasico() )
dispositivo_terminal.invocar_accion_principal("Calle Caos Peatonal", "Terminal de Autobus 4") 

"""
PATRÓN DE COMPORTAMIENTO: VISITOR (Visitante Invasor)

Explicación Detallada:
Es de extremada utiildad cuando tu código ya esta compilaodo, terminado , tus Jefes no te dejan
editar el nucleo del programa ("Ya no toques Fruta ni Libro ehhhh!! Romperas todo!") pero justo
ahí llega el Gobierno e impone algo letal: "Impuestos Regionales Variables Dinámicos según Geopolítica".

Si tocaras la clase Libro e hicieras `imprimir_calculo(self, configGeoPolitica_obj)` llenarías el pobre 
Libro tonto con código geopolítico mega gordo inyectando acoplamientos del demonio.

El VISITOR crea una clase ajena total que "visita y pasa rapidito a tocar el hombro" por los distintos objetos extraños que andan
circulando en una coleccion gigante. "Hola libro, dame tus datos te aplico los cobros yo solito (Sin modificarlo)... Hola fruta...!"
El secreto oscuro detrás del código es el famoso `DOUBLE DISPATCH` (Doble Envío):
El arreglo le pasa el visitante al Libro. Y el Libro inmediatamente le avienta SU MISMO CUERPO por los oidos al puente del Visitante. 
Así se auto-desencadena sin condicionales if tontos del humano.

¿Cuándo usarlo? Sistemas Legacy donde no puedes andar modificando 50 clases nativas originales 
para inyectar algorítmica foránea externa nueva contable exportadora analítica XML.
"""

from abc import ABC, abstractmethod

# ===============================
# 1. LA MASA LÓGICA ACTUANTE EXTERNA EXTRANJERA (EL VISITANTE Y SUS IMPLEMENTACIONES LOCAS)
# ===============================
class InterfaceVisitanteInspector(ABC):
    # Por obligacion y ley de la geometria, tiene que tener Un método Expositivo para cada raza diferente en el ecosistema 
    @abstractmethod
    def inspeccionar_calculosT_sobre_Libro(self, target_libro_cuerpo): pass

    @abstractmethod
    def inspeccionar_calculosT_sobre_Frutitas(self, target_fruta_cuerpo): pass


# Esta es una sola Variante (El impuesto Latino de hoy... mañana alguien inventa el impuesto IVA Europa).
class CalculoIVAExportadorJSON_VisitanteLATAM(InterfaceVisitanteInspector):
    
    # La logica y contabilidad no toca el libro, se ejecuta en la RAM del propio Inspector ajeno ajeno
    def inspeccionar_calculosT_sobre_Libro(self, target_libro_cuerpo):
        # Aca el impuesto es risorio (Fomento lectura), solo toma logicas
        impacto_precio = target_libro_cuerpo.dolares_netos_precio_base * 1.05 
        print(f"   🧾 [INSPECTOR VISITANTE GUBERNAMENTAL LATAM] -> Vio Volumen Literario con coste {target_libro_cuerpo.dolares_netos_precio_base}USD... Aplicando Ley 9.04 de Fomento! Total Sale: ${impacto_precio:0.2f}")
        return impacto_precio

    def inspeccionar_calculosT_sobre_Frutitas(self, target_fruta_cuerpo):
        impacto_precio = target_fruta_cuerpo.dolares_netos_precio_base * 1.50 # Impuestos mega salvajes a agricultura extranjera imaginario
        print(f"   🧾 [INSPECTOR VISITANTE GUBERNAMENTAL LATAM] -> Vio Fruta Organica a {target_fruta_cuerpo.dolares_netos_precio_base}USD. Aplicamos tarifazo 50% extra fronterizo brutal.  Total Sale: ${impacto_precio:0.2f}")
        return impacto_precio


# ===============================
# 2. LOS COMPONENTES CAMELLO DEL REINO TRABAJADOR OPRIMIDO (Elementos del Arbol Estructural de tu App)
# ===============================
class NodoArbolMercaderiasElementos(ABC):
    
    # LA REGLA AUREA INDESTRUCTIBE: DEBEN ABRIR LA MENTE EN SU CUERPO PARA QUE EL PARASITO EXTRANJERO PUEDA PASAR EN LA RED (Accept Method).
    @abstractmethod
    def aceptar_inspector_extranjero(self, el_paracaidista_inspector_puntero: InterfaceVisitanteInspector):
         pass

class LibroDeFilosofiaAlemanaGorda(NodoArbolMercaderiasElementos):
    def __init__(self, const_precio_dolares):
        self.dolares_netos_precio_base = const_precio_dolares
        
    def aceptar_inspector_extranjero(self, el_paracaidista_inspector_puntero: InterfaceVisitanteInspector):
        # DOUBLE DISPATCH MISTICO!! => Se recibe la instancia, y el propio Libro LLAMA A ESE INSPECTOR EN MANDANDOLE SU PROPIA CARNE MUNDANA COMO CARNADA Y PUNTERO 'SELF'.
        return el_paracaidista_inspector_puntero.inspeccionar_calculosT_sobre_Libro(self)


class FrutaManzanilExtremaDelBosque(NodoArbolMercaderiasElementos):
     def __init__(self, const_precio_dolares):
         self.dolares_netos_precio_base = const_precio_dolares

     def aceptar_inspector_extranjero(self, el_paracaidista_inspector_puntero: InterfaceVisitanteInspector):
        # Auto-engarzamiento re-cursivo inverso en el inspector delegador para Frutitas logic base method overload.
        return el_paracaidista_inspector_puntero.inspeccionar_calculosT_sobre_Frutitas(self)


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN EXTRACTIVO DEL VISITOR ===\n")

print("Se escanea una boleta brutal de compra gigantesca de elementos sin relaciones intrinsecas lógicas comunes mas que venta:")
array_cinta_cajeros_magnetica = [
    LibroDeFilosofiaAlemanaGorda(precio_dolares= 12.0),
    FrutaManzanilExtremaDelBosque(precio_dolares= 4.50),
    FrutaManzanilExtremaDelBosque(precio_dolares= 1.10),
    LibroDeFilosofiaAlemanaGorda(precio_dolares= 98.40)
]

print("   (La cinta del cajero esta corriendo de a pocos en el for general)...")
cajero_suma_acumuladora_total = 0

# Se instancia al inspector politico fiscal extraniio
inspector_sunat = CalculoIVAExportadorJSON_VisitanteLATAM()

for item_random_actual_de_array in array_cinta_cajeros_magnetica:
    # Se impone al item que acepte tragar la instancia del inspector
    cajero_suma_acumuladora_total += item_random_actual_de_array.aceptar_inspector_extranjero(inspector_sunat)

print(f"\n >>> La suma universal sacada por el inspector del Gobierno dio:   $ {cajero_suma_acumuladora_total:0.2f} USD")

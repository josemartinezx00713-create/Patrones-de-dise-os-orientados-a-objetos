"""
PATRÓN DE COMPORTAMIENTO: TEMPLATE METHOD (Método de Plantilla Sagrada)

Explicación Detallada:
El Template Method nos soluciona el horripilante mal del "Código Duplicado".
Imagina un analizador de información. 
La clase "PDF_Miner" hace: Abrir_fichero() -> Leer_Formato_PDF() -> Extraer_TXT() -> Guardar_Result_Bin().
La clase "TXT_Miner" hace: Abrir_fichero() -> Leer_Formato_TXT() -> ExtraerTXT() -> Guardar_Result_Bin().

Ambos repiten "AbrirFichero", "ExtraerTXT", "GuardarResultBin". Si hay 20 clases, tienes 20 veces ese algoritmo repetido.
¡Si hay un Bug, tendrás que arreglar las 20 clases o te echarán al fuego!
El Método Pantilla crea esa "Carcasa del Flujo Total De Los Datos" en la Clase PADRE Abstracta (El esqueleto).
Luego le dice tajantemente a las subclases Hijos: "Nadie toca mis algoritmos de inicio y fin, uds solo implementen 
la peculiaridad exacta diferencial".

¿Cuándo usarlo? Ciclos de empaquetados e imports empresariales, Frameworks webs, Fabricación de flujos de bebidas 
(todas hierven pero tiran hierbas diferentes del molde).
"""

from abc import ABC, abstractmethod


# ===============================
# 1. LA CLASE ABSOLUTA (EL ESQUELETO Y GESTOR DEL MOLDE DE PLATINO)
# ===============================
class AbstractaRecetadoraPlantillerDeBebidas(ABC):
    
    # ---- ¡ESTE ES EL TEMPLATE METHOD REAL OFICIAL! ---- 
    # Es el "Pipeline" O "Embudos". Rige la ley de CÓMO y CUÁNDO deben acontecer los pasos.
    # EN LENGUAJES ESTRICTOS (Java/C#) SE DECLARA COMO "final" PARA Q NADIE NUNCA LO SOBRE ESCRIBA CON HACKS! En Python usamos convenciones y respeto civilizado.
    def preparar_secuencialmente_infusion(self):
        print("[>] Iniciando Pipeline de la Receta Absoluta Creadora de Brebaje Sagrado..")
        self.accion_hervir_liquido_termodinamica()  # Base (Comun)
        self.accion_insertar_hojas_sabor() # Magia Especial de cada quien
        self.accion_derramar_en_la_taza() # Base (Comun)
        self.accion_aplicar_condimentos_extras() # Magia Especial de cada quien
        print("[✓] Pipeline FInalizado. Bebida terminada en bandeja metálica reluciente y humeante.\n")

    # METODOS DE CÓDIGO COMÚN, BASES GENÉRICAS (No hace falta que mis hijos se maten en re-escribir como hervir agua 100 veces por siempre).
    def accion_hervir_liquido_termodinamica(self):
         print("   |- [COMUN GENERIC BASE METHOD]  Poniendo olla a presion electrica y calentando moleculas de H2O a 100 ºC")

    def accion_derramar_en_la_taza(self):
         print("   |- [COMUN GENERIC BASE METHOD]  Destapando pistero y derramando el elemento caliente a taza blanca de ceramica")

    # METODOS FALTANTES EXCLUSIVOS DE LOS HIJOS REBELDES INCOMPLETOS: (Hook Abstractos)
    @abstractmethod
    def accion_insertar_hojas_sabor(self): pass

    @abstractmethod
    def accion_aplicar_condimentos_extras(self): pass


# ===============================
# 2. LOS EXPANSORES CONCRETOS HIJOS (Rellenadores de hoyos huecos de platino)
# ===============================
class InfusionHacedorCafe(AbstractaRecetadoraPlantillerDeBebidas):
    def accion_insertar_hojas_sabor(self):
        print("   |+ [MODIFICACION HIJO LOCAL] Exprimiendo 10KG del mejor grano de la sabana colombiana a presion titanica 2.0 bar espresso machine.")

    def accion_aplicar_condimentos_extras(self):
        print("   |+ [MODIFICACION HIJO LOCAL] Rociando azúcar rubio con un trazo fino de espuma leche cortita.")


class InfusionHijoTeLimonSuave(AbstractaRecetadoraPlantillerDeBebidas):
     def accion_insertar_hojas_sabor(self):
         print("   |+ [MODIFICACION HIJO TE LOCAL] Ahogando una misera bolsita porosa filtrante Lipton dentro de las profundidades del vacio ciego del liquido negro.")

     def accion_aplicar_condimentos_extras(self):
         print("   |+ [MODIFICACION HIJO TE LOCAL] Cortando 1/4 rodaja de limón al fallo con mucho ácido y sin endulcorante artificial.")


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN METODO PLANTILLA ===\n")

print("Se acerca un programador estresado e hipercinético al sistema y da grito de CAFE URGENTE.")
productor_de_dioses_cafe = InfusionHacedorCafe()

# Se invoca AL MOLDE GENERAL unicamente: No hay if else a mano humana de si es cafe pon algo q no sea cafe q explota etc etc. 
# El flujo dictará a la eternidad lo que debe acontecerle al objeto per se.
productor_de_dioses_cafe.preparar_secuencialmente_infusion()

print("-" * 55)

print("\nSe acerca el Gerente corporativo con mal de estomago gastritis aguda de estrés financiero. (Pide su Te)")
brebajeizador_de_tes_gerenciales = InfusionHijoTeLimonSuave()
brebajeizador_de_tes_gerenciales.preparar_secuencialmente_infusion()

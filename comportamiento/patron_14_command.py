"""
PATRÓN DE COMPORTAMIENTO: COMMAND (Comando)

Explicación Detallada:
El Command toma una "Petición" cruda, la saca de su entorno físico normal, y la envuelve/encapsula dándole vida propia 
dentro de su propio OBJETO independiente de todo.

¿Para qué hacer esto? Piénsalo:
Si apagas un foco en la pared usando los dedos.. el cuarto se obscurece, pero la electricidad hizo eso y nadie se acuerda de nada.
Pero si apagas un foco con una "Clase Encapsulada Clic()" que tiene las librerías "ejecutar()" y "deshacer()"... 
¡El control central puede ir guardando todos esos clicks en un Array Gigante de historial y luego irlos ejecutando en reversa usando Deshacer() o deshacer()!
Esa es la técnica milagrosa secreta usada para que Word, Photoshop o tu navegador web tengan el clásico CTRL+Z y CTRL+Y (Historiales).

¿Cuándo usarlo? Sistemas con menús de acciones muy complejas, botones UI de aplicaciones que requieren Deshacer/Rehacer. Programaciones de colas batch para 
cuando el Internet conecte todo se dispare de golpe al mismo tiempo.
"""

from abc import ABC, abstractmethod

# ===============================
# 1. PLANTILLA COMÚN DEL SOLDADO OBEDIENTE
# ===============================
# A un comando no le importa QUÉ demonios le vas a pedir hacer (matar alguien, borrar texto... solo pide métodos Execute/Undo).
class InterfazComando(ABC):
    @abstractmethod
    def accionar(self): pass

    @abstractmethod
    def ejecutar_inversa(self): pass


# ===============================
# 2. OBJETO DE IMPACTO O "RECEPTOR" (A quien el comando le va a hacer daño)
# ===============================
class DocumentoTextoVirtual:
    def __init__(self):
        self._str_contenido = "Querido Diario... Hoy fui al parque."
        
    def añadir_por_posicion(self, frase_extra):
        self._str_contenido += frase_extra
        
    def decapitar_letras(self, contador):
        # Slice en Python avanzado para recortar la parte trasera de una cadena. Lo contrario exacto a Sumar cadenas al fondo.
        self._str_contenido = self._str_contenido[:-contador]

    def gritar_estado(self):
        print(f"   [PAPIRO ACTUAL] ---> '{self._str_contenido}'")


# ===============================
# 3. LOS COMANDOS ACTIVOS CONCRETOS (Clases dedicadas EXCLUSIVAMENTE a guardar tu instrucción)
# ===============================
class EscribirLetrasCommand(InterfazComando):
    def __init__(self, target_a_daniar: DocumentoTextoVirtual, string_para_poner: str):
        self.doc_target = target_a_daniar
        self.tinta = string_para_poner

    def accionar(self):
        # Adelante marcha
        self.doc_target.añadir_por_posicion(self.tinta)

    def ejecutar_inversa(self):
        # Atrás retroceso reverso anulatorio místico.
        self.doc_target.decapitar_letras(len(self.tinta))


# ===============================
# 4. EL CEREBELO O "INVOKER" HISTORIAL MÁGICO (Registra todo lo acontecido)
# ===============================
class MotorDeDeshacerMisterioso:
    def __init__(self):
        # Array cronológico del CTRL Z
        self._comandos_stack = []

    def pulsar_boton_creador(self, paquete_comando_pre_armado: InterfazComando):
        # Primero que lo mande hacer y vea si no rompió la PC
        paquete_comando_pre_armado.accionar()
        # Si sobrevive, mételo a la cola para poder deshacerlo a futuro
        self._comandos_stack.append(paquete_comando_pre_armado)

    def simular_tecla_ctrl_z(self):
        # Saca el último comando enviado y dispárale su anulación
        if len(self._comandos_stack) > 0:
            comando_muerto = self._comandos_stack.pop() # .pop borra de array sacando el ultimo en entrar
            comando_muerto.ejecutar_inversa()
        else:
            print("No hay nada que el CTRL Z pueda salvarte ahora...")

# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN COMMAND ===\n")

tu_diario = DocumentoTextoVirtual()
historializador_del_programa = MotorDeDeshacerMisterioso()

tu_diario.gritar_estado()

# Escribes cosas en el teclado
print("\n[Usuario teclea más frases]:")
cm_1 = EscribirLetrasCommand(tu_diario, " Y conocí a la chava mas linda de mi vida.")
historializador_del_programa.pulsar_boton_creador(cm_1)
tu_diario.gritar_estado()

cm_2 = EscribirLetrasCommand(tu_diario, " Le hablé y me ignoró miserablemente. El perrito me mordió.")
historializador_del_programa.pulsar_boton_creador(cm_2)
tu_diario.gritar_estado()

print("\n--- ¡AL CHICO LE DIO ANSIEDAD Y BORRA SUS TEXTOS APRETANDO CTRL Z FURIOSAMENTE! ---\n")
historializador_del_programa.simular_tecla_ctrl_z()
tu_diario.gritar_estado()

print("Una vez más CTRL Z!")
historializador_del_programa.simular_tecla_ctrl_z()
tu_diario.gritar_estado() # Volvió a la pureza del querido diario.

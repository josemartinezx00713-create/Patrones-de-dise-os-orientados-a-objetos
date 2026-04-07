"""
PATRÓN DE COMPORTAMIENTO: MEMENTO (El Recuerdo Inviolable)

Explicación Detallada:
Si tú estás creando tu videojuego o procesador de textos como Word, llega el doloroso instante
en donde el jefe te dice: "Hay que implementar un botón para Deshacer (Undo) ó Cargar Partida Antigua".
Mucha gente entra a las tripas, extrae el "player.vida" y el "player.monedas" usando setters/getters
y se lo guarda cruda y torpemente en un Array del Sistema principal. ¡Eso rompe masivamente el pilar de la Encapsulacion de Clases!

La solución mágica y elegante es el Patrón Memento.
Compuesto por 3 entes:
1. Originador (El Player. Solo él sabe crear y revivir a partir de sus copias secretas pasadas)
2. Memento (La foto de la vieja vida, un objeto encapsulado y bloqueado sin ningun método exterior invocable. Ni siquiera el sistema puede husmear dentro de él propiamente).
3. Caretaker-Conserje (El Archivero Inutil. El motor del juego general guardará la variable Memento, pero solo es capaz de darsela de nuevo al Player sin inspeccionarle su información y encriptaciones internas!).

¿Cuándo usarlo? Sistemas de Undo/Redo y Autoguardados y Quicksaves de Estado de Máquina Total.
"""

# ===============================
# 1. EL MEMENTO INAMOVIBLE (Snapshot / Caja Fuerte Cerrada)
# ===============================
class CofreStatus_MementoPartida:
    # Estos variables no se exponen con getters ni setters de manipulación exterior.
    # El caretaker no interactúa jamás con ésto. Se quedan selladas al vacio en esta instancia memoria.
    def __init__(self, stage_nivel, barras_salud):
        self._nivel_congelado = stage_nivel
        self._salud_congelada = barras_salud


# ===============================
# 2. EL ORIGINADOR MADRE (El personaje del Usuario Principal que posee sus datos propios)
# ===============================
class PlayerPrincipal:
    def __init__(self):
        self.mis_vidas = 100
        self.etapa_mazmorra = 1

    def recibir_daño(self):
        self.mis_vidas -= 45
        print(f"🗡️ ¡Daño critico detectado! Vidas penden de un hilo: {self.mis_vidas}")

    def caminar_proximo_nivel(self):
        self.etapa_mazmorra += 1
        print(f"🌟 Avanzas al area {self.etapa_mazmorra} y cruzas tu destino.")

    def pintar_en_GUI_pantalla(self):
        print(f"[UI] Level-{self.etapa_mazmorra}     Health[====_ {self.mis_vidas} _====]")


    # ---- PARTE MÁGICA 1 DEL PATRÓN (MÁQUINA EXPULSADORA DE SAVESTATES) ----
    def expulsar_quick_save(self) -> CofreStatus_MementoPartida:
        print("[Engine Físico:] Extrayendo snapshot y fabricando Memento Criptográfico...")
        # Instancia al memento privado y lo expulsa como burbuja.
        return CofreStatus_MementoPartida(self.etapa_mazmorra, self.mis_vidas)


    # ---- PARTE MÁGICA 2 DEL PATRÓN (LA INYECCIÓN DEL SAVESTATE A LAS VENAS MADRINA) ----
    def chupar_quicksave_retroceso(self, inyectadora_memento: CofreStatus_MementoPartida):
        print("\n[Engine Físico:] Volviendo atras el reloj biológico universal en 5, 4, 3...")
        # Desempaqueta y se recubre con estos variables sagrados que vienen del pasado
        self.etapa_mazmorra = inyectadora_memento._nivel_congelado
        self.mis_vidas = inyectadora_memento._salud_congelada


# ===============================
# 3. EL CARETAKER INEFICIENTE / CONSERJE (El sistema principal, o la consola)
# ===============================
# Es como un estante de biblioteca de CDs tristes. Él los cuida pero no puede introducirse al disco.
class EngineDelJuegoDeConserje:
    def __init__(self):
        self.archivos_slot_guardado = []

    def save_presionado(self, objeto_memento_opaco):
        self.archivos_slot_guardado.append(objeto_memento_opaco)

    def load_presionado(self):
        if self.archivos_slot_guardado:
            return self.archivos_slot_guardado[-1]
        return None

# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN MEMENTO ===\n")

# Se corre ejecutable
usuario_xbox = PlayerPrincipal()
consola = EngineDelJuegoDeConserje()

usuario_xbox.pintar_en_GUI_pantalla()

usuario_xbox.caminar_proximo_nivel()
usuario_xbox.caminar_proximo_nivel()
print("¡El jugador está antes de abrirle la última puerta maldita del Jefe a Nivel 3!\n")

print("SUDANDO EL CHICO PRESIONA 'GUARDAR ARCHIVO' EN LA ESQUINA DEL TV:")
# Pasamos la burbuja al archivero ciego que no sabe manipular variables
consola.save_presionado(usuario_xbox.expulsar_quick_save())

print("\n--- LA PUERTA SE ABRE... EL JEFE DISPARA LÁSER DESTRUCTIVO ---")
usuario_xbox.recibir_daño()
usuario_xbox.recibir_daño() # La salud va por debajo
usuario_xbox.pintar_en_GUI_pantalla()

print("\nEl jugador antes del último deceso le da 'QUICK LOAD'")
# Saca la burbuja sellada y se lo transfuende puramente al cuerpo original del usuario madrea.
burbuja = consola.load_presionado()
usuario_xbox.chupar_quicksave_retroceso(burbuja)

print("\nHAS SOBREVIVIDO, TODO ES AHORA PAZ Y FELICIAD DEL VIAJE TEMPORAL.")
usuario_xbox.pintar_en_GUI_pantalla()

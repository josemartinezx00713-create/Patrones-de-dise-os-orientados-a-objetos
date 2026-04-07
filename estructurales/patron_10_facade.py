"""
PATRÓN ESTRUCTURAL: FACADE (Fachada)

Explicación Detallada:
El mundo informático está lleno de cosas brutalmente complejas hechas de 50 partes. 
La Fachada es proveer un solo "Controlador Inteligente" o "Panel frontal" que junte y simplifique 
el acceso a toda esa complejidad para el cliente final inexperto (el sistema exterior).

Piénsalo como cuando llamas por teléfono a pedir una Pizza. La recepcionista del local es tu "Fachada".
Tú solo dices "Quiero la de pepperoni". No tienes que ir personalmente a hablar con el hornero, luego buscar al
repartidor de masas y finalmente ir al cajero del negocio para cobrarte.

¿Cuándo usarlo? Cuando tengas muchas clases complejas colaborando juntas y necesites crear una 
clase simple "coordinadora" que exponga botones fáciles (métodos) de una sola cara para los desarrolladores.
"""

# ===============================
# LAS LIBRERÍAS DE TRÁNSITO Y EL SUBSISTEMA (Lo muy técnico y complejo detrás de escena)
# ===============================
# Imagina que este es el complejo e incomprensible sistema de luces y hardware de tu casa domótica.
class HardwareIluminacion:
    def bajar_intensidad(self, porciento): print(f"[HARDWARE INTENNO] 💡 Intensidad diodo luz -> bajada a {porciento}%.")
    def apagar_completamente(self): print(f"[HARDWARE INTENNO] 💡 Circuito lámpara DESCONECTADO (Apagado completo).")

class HardwareAltavoces:
    def configurar_surround_hdmi(self): print("[HARDWARE INTENNO] 🔊 Protocolo Sonido HDMI ARC Activo.")
    def fijar_salida_db(self, decibeles): print(f"[HARDWARE INTENNO] 🔊 Limitando decibeles a: {decibeles}dB.")

class ProyectorMaestro:
    def encender_laser(self): print("[HARDWARE INTENNO] 📽️ Calentando proyector...")
    def ajustar_lente(self, px, py): print(f"[HARDWARE INTENNO] 📽️ Modos Pan Tilt de Proyector seteados a: x:{px} y:{py}.")

# ===============================
# LA FACHADA "FACADE"
# ===============================
# Conecta todas las piezas feas juntas y muestra botones agradables hacia el usuario común.
class AsistenteDomoticoFachada:
    def __init__(self):
        # La fachada inicializa los fierros pesados una sola vez y los sostiene.
        self.iluminacion = HardwareIluminacion()
        self.audio = HardwareAltavoces()
        self.video = ProyectorMaestro()

    def activar_rutina_noche_cine(self):
        print("\n[Asistente IA] Empezando la rutina de cine para el humano...")
        # El usuario hace clic en el celular y la IA (la fachada) se encarga del dolor de cabeza interno:
        self.iluminacion.bajar_intensidad(10)
        self.audio.configurar_surround_hdmi()
        self.audio.fijar_salida_db(80)
        self.video.encender_laser()
        self.video.ajustar_lente(1920, 1080)
        print("[Asistente IA] Sala VIP de cine cargada exitosamente.")

    def dormir_la_casa(self):
        print("\n[Asistente IA] Rutina general de bloqueo y suspension del hardware...")
        self.iluminacion.apagar_completamente()
        self.audio.fijar_salida_db(0)
        # Apagamos el proyector de forma brusca para ahorrar luz (ejemplo)


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN FACADE ===\n")

# Todo el cliente común de tu software (interfaz frontend celular_app) usará solo "AsistenteDomotico"
celular_app = AsistenteDomoticoFachada()

print("Pulsaste el gran botón único de tu interfaz en el dispositivo móvil: 'Ver Película'")
celular_app.activar_rutina_noche_cine()

print("\nTerminó la noche de cine, pulsaste el botón gris: 'Todo Off'")
celular_app.dormir_la_casa()

"""
PATRÓN ESTRUCTURAL: BRIDGE (Puente)

Explicación Detallada:
El Bridge (Puente) nos evita un dolor de cabeza llamado "Explosión de Clases".
Imagina que construyes un "Control Remoto para Televisores".
Luego te piden "Control Remoto para Radio". Creas otra clase.
Luego te piden que haya controles básicos y avanzados.
Tendrías que crear: 
- ControlBasicoTele, ControlAvanzadoTele, ControlBasicoRadio, ControlAvanzadoRadio (¡4 clases!).
Y si agregas Aire Acondicionado, se multiplica el problema.

El Bridge soluciona esto separando la cosa en 2 pilares independientes:
Pilar 1: La Interfaz de Usuario (El 'Control Remoto')
Pilar 2: La Implementación (El 'Dispositivo' como TV, Radio)
Luego unes ambos pilares dándole a cada Control una referencia al Dispositivo. 
Así ambos pueden evolucionar sin obligarte a crear 100 clases mezcladas.

¿Cuándo usarlo? Cuando preveas que las funciones (interfaces) y quienes las ejecutan (plataformas/dispositivos) 
crecerán de manera paralela e independiente.
"""

from abc import ABC, abstractmethod

# ===============================
# PILAR 1: LA IMPLEMENTACIÓN (Los Dispositivos físicos)
# ===============================
class Dispositivo(ABC):
    @abstractmethod
    def encender(self): pass
    
    @abstractmethod
    def apagar(self): pass

# Dispositivos concretos independientes...
class Television(Dispositivo):
    def encender(self): print("📺 [TELEVISIÓN] Encendida y mostrando canal 1.")
    def apagar(self): print("📺 [TELEVISIÓN] Apagada. Pantalla en negro.")

class Radio(Dispositivo):
    def encender(self): print("📻 [RADIO] Encendida, sintonizando FM.")
    def apagar(self): print("📻 [RADIO] Apagada por completo.")


# ===============================
# PILAR 2: LA ABSTRACCIÓN (Los controles remotos o GUIs)
# ===============================
class ControlRemoto:
    # EL "PUENTE" AQUÍ ESTÁ EN LA VARIABLE 'dispositivo'
    # Recibe una interfaz general sin importarle de qué aparato se trate exactamente
    def __init__(self, dispositivo: Dispositivo):
        self._dispositivo = dispositivo

    def boton_rojo(self):
        print("\n-> [Control Genérico] El humano pulsó el Botón Rojo de Encendido.")
        # Simplemente delega el trabajo real al dispositivo conectado
        self._dispositivo.encender()

# Podemos extender el control sin tocar la Tele ni la Radio!
class ControlRemotoAvanzado(ControlRemoto):
    def boton_silenciar(self):
        print("-> [Control Avanzado] El humano pulsó MUTE.")
        # Imaginemos que apagarlo fungirá como silenciado por ahora
        print("(Cortando el fluido de ruido del aparato...)")


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN BRIDGE ===\n")

# Compramos equipos independientes
mi_tele = Television()
mi_radio = Radio()

# Compramos controles universales y los 'vinculamos' usando el puente (pasándole la variable)
control_para_tele = ControlRemoto(mi_tele)
control_para_radio = ControlRemotoAvanzado(mi_radio)

print("Usuario usando la TV:")
control_para_tele.boton_rojo()

print("\nUsuario usando la Radio:")
control_para_radio.boton_rojo()
control_para_radio.boton_silenciar() 
# Funciona maravillosamente y nos ahorramos decenas de herencias cruzadas.

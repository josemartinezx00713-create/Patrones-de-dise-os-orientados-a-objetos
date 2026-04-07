"""
PATRÓN DE COMPORTAMIENTO: STATE (Máquina de Estados)

Explicación Detallada:
El patrón State se utiliza para que un objeto cambie *violentamente su comportamiento* interno completo en memoria
en el momento en que su "Estado Psicológico" interno se ve modificado.

Imagina un documento Word que está programador gigantesco. Si tiene un booleano (bool_borrador = True)...
Las letras no se publican, no se ve a la nube, y no se pasa corrector... todo tu código de acciones estará 
minado con inmundicios antiestéticos estatementos 'if bool_borrador else bool_final if bool_enrevision...'.

Con State Pattern cada ESTADO de las cosas es una sola Clase totalmente propia inyectada dentro de tu objeto.
El 'Documento' nunca ejecuta nada él mismo. A él si publicas le delega un pase ciego:
self.estado_actualizando_enRAM.publicar_si_se_puede().
En RAM los estados se sustituyen: "Borrador() -> Publicado() -> Cerrado()". 
Es un Automata celular o "State Machine" nativa y purista total.

¿Cuándo usarlo? Sistemas que atraviesan transformaciones cíclicas lógicas de fases duras (Semáforos (Rojo, Amarillo), 
Pedidos Ecommerce (Empaquetando, RepartidorVía, Recepcionado) y Personajes de FPS Videojuegos (Vivo, Congelado, PoisonVenenoso).
"""

from abc import ABC, abstractmethod

# ===============================
# 1. LA INTERFAZ DE ESTADO COMUN 
# ===============================
# Todos los estados imaginables deben tener métodos unificados. Si eres Mario Bro y te atacan... no importa si te pisa un alien
# o si te dan un balazo... El Estado reaccionará segun tu status en este instante.
class EstadoInternoAbsPersonaje(ABC):
    @abstractmethod
    def accionar_danho_recibido(self, puntero_personaje_origen):
        # AQUI LA MAGIA FASCINANTE ES: Retornaremos CUAL ES EL ESTADO NUESTRO A FUTURO de acuerdo a esta accion.
        pass


# ===============================
# 2. LOS ESTADOS PSICOLÓGICOS ESPECÍFICOS Y COMPLETAMENTE DISTINTOS LÓGICAMENTE (Las máquinas secundarias).
# ===============================
class PildoraEstadoChiquitito(EstadoInternoAbsPersonaje):
    def accionar_danho_recibido(self, puntero_personaje_origen):
        # Escenario trágico de muertes directas si te tocan.
        print("  🍄 ¡Mario Enanito no aguanta un golpe! El monstruo gomba lo pisotea cruelmente.")
        print("  ☠️ Suena música fúnebre retro de Mario. ¡Haz muerto perdiste todas tus almas y moneditas!")
        return PildoraEstadoFallecidoCadaver() # Inyecta que te conviertas en este estado oscuro.

class PildoraEstadoSuperPoderosoHongoRed(EstadoInternoAbsPersonaje):
    def accionar_danho_recibido(self, puntero_personaje_origen):
        print("  🌟 Super Mario fue quemado un poquito por la planta piraña fuego...")
        print("  🔻 Mario Brilla sin morir, se reduce drásticamente su tamaño y poder y continúa en el nivel luchando.")
        return PildoraEstadoChiquitito() # Solo reduce a nivel anterior.

class PildoraEstadoFallecidoCadaver(EstadoInternoAbsPersonaje):
    def accionar_danho_recibido(self, puntero_personaje_origen):
        print("  👻 Error. El fontanero ya está fuera del plano de los vivos e incorpoces... no lo golpees en el piso inútilmente.")
        # Se lo devuelve tal y como era y perpetua el daño irreparable del estado actual oscuro
        return self


# ===============================
# 3. EL HOST O CONTEXTO EXTERNO PRINCIPAL ("EL MACHO" O EN ESTE CASO EL MARIO)
# ===============================
# Para el mundo real y tu cerebro el que pelea es MarioX, el ni se inmuta a reaccionar if s else ifs.. el delega como Dios en el fondo la cosa.
class EnteMarioMundoAvanzado:
    def __init__(self):
        # Mario Inicia la vida de su codigo universal con este Estado primigenio obligatorio. 
        # Inyecta a su vena local una instancia virgen local.
        self._maquina_estado_de_flujo = PildoraEstadoChiquitito()

    def tragar_hongo_recolector(self):
         print("\n🍄->🌟 Mario golpea la piedra interrogación dorada y salta devorando un Super Hongo de Crecimiento...")
         # Sobreescribimos al viejo y debil Enanito, y clavamos en la vena el estado duro por memoria bruta de la nada.
         self._maquina_estado_de_flujo = PildoraEstadoSuperPoderosoHongoRed()

    def es_atacado(self):
        print("\n💥 (Una tortuga veloz voladora colisiona con el hitbox X del fontanero de pronto!!)")
        # Llama a tu estado presente en nanosegundos el cual decidirá si sobrevives o si haces game_over
        self._maquina_estado_de_flujo = self._maquina_estado_de_flujo.accionar_danho_recibido(self)

# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN STATE MACHINE ===\n")

print("=> El Jugador_A carga 'Nivel-1'. Es novato.")
victima = EnteMarioMundoAvanzado()

victima.es_atacado() # Recibira un estado PildoraFallecido
victima.es_atacado() # Para ver que ya nada ocurre x que era finiquitado el código del sistema.


print("\n----------------\n")
print("=> El Jugador_VIP_Experto carga 'Nivel 1'. Es muy veloz y salta cajas y usa el patrón state a su máxima expresión.")
profresional = EnteMarioMundoAvanzado()

profresional.tragar_hongo_recolector() # Alteró su interioridad atómica.
profresional.es_atacado() # El algoritmo del delegador le dirá que NO murio.
profresional.es_atacado() # Ahora este segundo choque x las tortugas, SÍ lo mandara a su cadaver estado en cadena fatídica de events

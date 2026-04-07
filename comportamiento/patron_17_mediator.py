"""
PATRÓN DE COMPORTAMIENTO: MEDIATOR (Mediador)

Explicación Detallada:
Soluciona un sistema infernal que se denomina en la ingeniería de Sistemas "El Caos Spaguetti Multidireccional".
Este infierno inicia cuando la Clase A tiene que hablarle y actualizar a las Clases B, C, D, E.
Al mismo tiempo, la Clase D tiene que hablarle y disparar eventos a las Clases A, F y C.

Con el Mediator, NINGUNA clase puede mirarse a la cara mutuamente. Cortas todos sus nexos directos.
Colocas una "Gran Torre De Comunicaciones Central" en el medio de la red de Clases y obligas a que si A 
quiere avisarle a C, primero pase por el filtro y las antenas de transmisión del Mediator Central.

Ejemplo en la vida Real:
Hub de domótica WiFi, un Chatroom general de Discord/WhatsApp CentralGroup, y por supuesto la torre de control de aeropuertos de jets.
"""

from abc import ABC, abstractmethod

# ===============================
# 1. LA INTERFAZ CENTRAL MEDIADORA (Dictadura de las Comunicaciones de la empresa)
# ===============================
class MediadorGeneralInteractivo(ABC):
    @abstractmethod
    def comunicar_evento_critico(self, dict_msg_str: str, quien_inició_el_paquete_red):
        pass


# ===============================
# 2. EL CENTRO SERVIDOR CONCRETO (La Torre)
# ===============================
class ChatRoomServerMediador(MediadorGeneralInteractivo):
    def __init__(self):
        # Esta torre guarda registro y punteros en RAM de todos los objetos en el sistema actual vivos.
        self.usuarios_conectados = []

    def hacer_login_registro(self, nuevo_user):
        self.usuarios_conectados.append(nuevo_user)

    # La única forma en que los usuarios reciben mensajes directos si no son ellosismos que lo lanzaron:
    def comunicar_evento_critico(self, paquete_str, remitente_original):
        for usuario_terminal in self.usuarios_conectados:
            # "Broadcasteamos" la señal a todos el resto en la lista negra que no sean el propio tipo escribiendo eso.
            if usuario_terminal != remitente_original:
                usuario_terminal.buzon_correo_recibir_notificacion(paquete_str)


# ===============================
# 3. COMPONENTE CLIENTE DE TERMINAL (Nunca conocerá a otros Clientes directos, todo lo enruta la Torre al medio local)
# ===============================
class UsuarioCelularApp:
    def __init__(self, username_tag, IP_Mediador_Sever: ChatRoomServerMediador):
        self.username = username_tag
        self._servidor_mediador_ligado = IP_Mediador_Sever # Componente vital. Lo forzamos en constructor obligatorio para evitar bypass locales.
        self._servidor_mediador_ligado.hacer_login_registro(self)

    def evento_teclado_send(self, str_teclado):
        print(f"📱 📤 [{self.username}] aprieta ENTER y manda mensaje por antenas 4G al SERVER CENTRAL: '{str_teclado}'")
        # El server sabrá qe hacer. 
        self._servidor_mediador_ligado.comunicar_evento_critico(f"El usuario {self.username} dice ---> {str_teclado}", self)

    def buzon_correo_recibir_notificacion(self, red_str_recibido):
        # Este disparador solo el mediador es capaz de invocarselo silencioso
        print(f"      📳 📥 (Ring...) IP_Cel_Pantalla_APP_{self.username} acaba de descargar una alerta de Chat entrante: {red_str_recibido}")


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN MEDIATOR ===\n")

print("1. Arrancando DataCenter y Base de Comunicaciones de San Francisco.\n")
discord_server = ChatRoomServerMediador()

user_1 = UsuarioCelularApp("xXReyGamerXx", discord_server)
user_2 = UsuarioCelularApp("ChicaVlog", discord_server)
user_3 = UsuarioCelularApp("Moderador_Discord", discord_server)

print("--- INICIANDO LLUVIA DE DATOS EN EL CANAL CENTRALIZADO --- \n")

user_1.evento_teclado_send("Cual es la guia del server o algo, ando perdido.")
print("-" * 55)

user_3.evento_teclado_send("Ban a todos x ser inactivos :v")

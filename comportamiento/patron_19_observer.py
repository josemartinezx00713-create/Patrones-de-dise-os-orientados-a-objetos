"""
PATRÓN DE COMPORTAMIENTO: OBSERVER (Observador)

Explicación Detallada:
También famosamente conocido en toda la industria universal como "Patron PUBLISHER - SUBSCRIBER".
Maneja toda la dependencia de Uno(Canal Youtuber) -a- Muchos(Fanáticos).

Si tienes un objeto Sensacional (Una noticia, una acción de Amazon en bolsa cambiando a 120USD)...
Y muchísimos terminales que deben "recibir y mostrarla en verde en pantalla si subió".
Tendrías a miles de terminales consultando como tontos cada literal milisegundo mediante un "while(True): ¿Y Ya subió? ¿Y YA subió? ...".
Eso quema los anchos de banda a limites estratosféricos y sobrecarga por peticiones polling absurdas.

El milagro Observer erradica esas miles de consultas: Nadie hace nada excepto quedarse callados escuchando.
Es el propio Centro (Publisher / Youytuber) que cuando cambia o sube video.. itera velozmente su arrray maestro de punteros "suscriptores",
y dispara un método push "Oigan todos mis hijos, subí video. Aqui lo pasé en el argumento string method()!".  
Bum. 0 lag, infinita eficiencia escalable.

¿Cuándo usarlo? Sistemas basados en EVENTOS o REACTIVIDAD extrema (Como React frameworks). Mailing, Avisos e Notificaciones móviles.
"""

# ===============================
# 1. LA INTERFAZ PUBLICA PARA QUE TE CAIGA LA PLATA (El Observador Pasivo / Oculto)
# ===============================
class InterfazSuscriptorOcultoBase:
    def despertar_por_notificacion(self, data_cruda_enviada_del_cielo): pass


# ===============================
# 2. EL CENTRO PUBLICADOR CREADOR NOTICIERO MÁXIMO
# ===============================
class CanalServidorYouTubeBlogger:
    def __init__(self, nombre_estetico):
        self.canal_alias_id = nombre_estetico
        # Puntero maestro sagrado. Todas las IPs de quienes quieren info iran acá.
        self._lista_emails_listeners = []

    def hacer_suscripcion_listener(self, instancia_obj_oyente: InterfazSuscriptorOcultoBase):
        self._lista_emails_listeners.append(instancia_obj_oyente)
        print(f"      [BDD CANAL]: Nuevo puntero cliente registrado bajo campanita.")

    def expulsar_desuscripcion(self, viejo_oyente):
        self._lista_emails_listeners.remove(viejo_oyente)
        print(f"      [BDD CANAL]: Eliminación de array list_emails ejecutada local.")

    # ------ ESTE ES EL METODO NUCLEAR ------
    def notificar_a_todo_array_del_mundo_conectado(self, enlace_al_video):
        # Manda el broadcast push inmediato a toda la raza
        for seguidor_vivo_for in self._lista_emails_listeners:
             seguidor_vivo_for.despertar_por_notificacion(enlace_al_video)


    # El accionador para el Youtuber Humano:
    def postear_y_subir_vid(self, titulo_y_tags):
        print(f"\n+++=======================+++")
        print(f"  El Dueño Youtuber del canal ({self.canal_alias_id}) está subiendo video ahora: {titulo_y_tags}")
        print(f"+++=======================+++\n")
        
        # Invoca a alertar automàticamente al finalizar barra de carga
        self.notificar_a_todo_array_del_mundo_conectado(titulo_y_tags)


# ===============================
# 3. LOS CLIENTES APLICACIÓN CONCRETOS
# ===============================
# Entidad de baja estirpe que implementa religiosamente el comando de interface.
class AppMovilFanCliente(InterfazSuscriptorOcultoBase):
    def __init__(self, alias_del_cliente):
         self.alias_personaje = alias_del_cliente

    def despertar_por_notificacion(self, data_cruda_enviada_del_cielo):
        # Se despierta el thread e ilumina pantalla.
        print(f"  🔔 [Notificación Banner a {self.alias_personaje}]: Has recibido un clip nuevo!: '{data_cruda_enviada_del_cielo}'")


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN OBSERVER ===\n")

# Se crea un canal
canal_linuxers_master = CanalServidorYouTubeBlogger("LinusTechAndCoffee44")

# Humanos clientes instancian sus teléfonos en sus pueblitos remotos.
juan_latam = AppMovilFanCliente("Juan")
maria_europa = AppMovilFanCliente("María")
ana_latina = AppMovilFanCliente("Ana")

# Se atan silenciosamente a la matrix base madre
canal_linuxers_master.hacer_suscripcion_listener(juan_latam)
canal_linuxers_master.hacer_suscripcion_listener(maria_europa)

# Sube evento -> (Dispara a Juan y Maria solamente q ue se registraron al array en tiempo exacto del push de la variable)
canal_linuxers_master.postear_y_subir_vid("¿Cómo Instalar ArchLinux en una tostadora 2026? [TUTORIAL FACIL]")

# Eventos asincronos del mundo real. María ya le cansan estas cosas muy técnicas, quita su campanita.
# Pero Ana se mete
canal_linuxers_master.expulsar_desuscripcion(maria_europa)
canal_linuxers_master.hacer_suscripcion_listener(ana_latina)

# Sube otro Video. De toda la gente, esta vez el For-Loop dispara alertas para dar los print al Array compuesto de [Juan, Ana]:
canal_linuxers_master.postear_y_subir_vid("TOP 10 Motivos por el que programar en C++ da dolores musculares y cefaleas severas.")

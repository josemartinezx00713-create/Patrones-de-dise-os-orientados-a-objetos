"""
PATRÓN CREACIONAL: FACTORY METHOD (Método Fábrica)

Explicación Detallada:
El patrón Método Fábrica nos soluciona el problema de tener "clases acopladas". 
En programación, acoplado significa que el sistema principal conoce de memoria a las clases exactas (ej. Email, SMS).
Si luego quieres agregar Telegram, tendrías que modificar el código central.

Con Factory Method, creamos una Interfaz general ('Notificacion') y hacemos que una Fábrica tome las decisiones.
Nosotros solo le pedimos a la Fábrica "Dame algo tipo SMS" y ella nos devuelve un objeto listo para usar que
cumple con la Interfaz universal.

¿Cuándo usarlo? Cuando no sabes de antemano las clases exactas y dependencias de los objetos que tu 
código debe trabajar; dejas que las subclases o la fábrica decidan.
"""

from abc import ABC, abstractmethod

# --- 1. PRODUCTO (Interfaz Base) ---
# Esta es la regla. Cualquier tipo de notificación tiene que tener un método 'enviar'.
class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass

# --- 2. PRODUCTOS CONCRETOS ---
# Estas clases implementan la interfaz base, pero cada una hace la acción a su manera.
class NotificacionEmail(Notificacion):
    def enviar(self, mensaje):
        # Aquí iría el código complejo para conectar a un servidor SMTP
        print(f"📧 EMAIL enviado mediante SMTP. Cuerpo del mensaje: {mensaje}")

class NotificacionSMS(Notificacion):
    def enviar(self, mensaje):
        # Aquí iría el código complejo para conectar a una red móvil (Twilio, etc.)
        print(f"📱 SMS enviado por telefonía. Texto: {mensaje}")

# --- 3. LA FÁBRICA (El Creador) ---
# Esta clase aísla el proceso doloroso de creación. 
class FabricaNotificaciones:
    
    # Este es el MÉTODO FÁBRICA como tal.
    def crear_notificacion(self, tipo) -> Notificacion:
        # Aquí la fábrica toma las decisiones de qué objeto concreto inflar y preparar
        if tipo == "email":
            return NotificacionEmail() # Crea el email
        elif tipo == "sms":
            return NotificacionSMS()   # Crea el SMS
        else:
            # Si le pedimos un formato inventado, lanza error
            raise ValueError(f"El formato '{tipo}' no está soportado todavía.")

# --- DEMOSTRACIÓN ---
print("Iniciando nuestro sistema de envío masivo...\n")

# Solo creamos la fábrica, no creamos ningún Mensaje aún
fabrica = FabricaNotificaciones()

# El cliente le dice a la fábrica: "Necesito un Email"
noto_email = fabrica.crear_notificacion("email")
# El cliente ni siquiera sabe cómo se construyó internamente NotificacionEmail
noto_email.enviar("Tu compra ha sido confirmada.")

print()

# El cliente ahora le pide un SMS a la fábrica
noto_sms = fabrica.crear_notificacion("sms")
noto_sms.enviar("Código de verificación: 9876.")

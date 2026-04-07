"""
PATRÓN ESTRUCTURAL: PROXY (Representante / Sustituto)

Explicación Detallada:
El patrón Proxy funciona creando una clase intermediaria (El Proxy) que tiene EXACTAMENTE
la misma interfaz/métodos que la clase Real original de alta importancia que deseas esconder.

Como tienen los mismos nombres de métodos (Implementan a la InterfazBase), tú le pasas el Proxy a un cliente exterior
(a una app móvil, a un usuario) en lugar del objeto Real Directo.
El cliente envía comandos ciegamente creyendo que habla con el Servidor Verdadero, pero en el medio
el Proxy los frena y puede realizar acciones "Middleware" críticas como:
1. Control de accesos (Verificar credenciales Bancarias antes de dejar hacer retirar_dinero).
2. Autenticación, Cacheo, o Inicializaciones lentas en Base de Datos (Si el servidor tarda, el Proxy manda un eskeleto de carga)

¿Cuándo usarlo? Pasarelas de pagos, Conexión a Servicios Web RESTful (creando Proxys lentos y Proxys cacheados súper rapidos locales), 
Sistemas de autenticación pesados.
"""

from abc import ABC, abstractmethod

# ===============================
# 1. LA INTERFAZ COMÚN (El Contrato Central)
# ===============================
# Aquí atamos las manos de la cuenta Real y del Fake-Proxy. Tienen que verse matemáticamente igualitos por fuera.
class InterfaceBancariaBase(ABC):
    @abstractmethod
    def ejecutar_transaccion_a_cuenta(self, numero_cuenta_destino: str, dolares_monto: int):
        pass


# ===============================
# 2. EL SERVIDOR REAL (La clase sensible de Back-end crítico inmodificable)
# ===============================
# Esta clase asume ciegamente que si recibe una petición de retiro, TODO ESTÁ BIEN Y LA EJECUTA (No hace chequeos de fraude).
class ModuloBancarioInterno(InterfaceBancariaBase):
    def __init__(self):
        self.fondos_reserva = 1000000

    def ejecutar_transaccion_a_cuenta(self, numero_cuenta_destino: str, dolares_monto: int):
        self.fondos_reserva -= dolares_monto
        print(f"💰 [SERVIDOR BANCARIO CENTRAL] Enviando ${dolares_monto} a la cuenta {numero_cuenta_destino}. (Nuevos fondos caja fuerte: ${self.fondos_reserva})")


# ===============================
# 3. EL GUARDAESPALDAS (Proxy Proxy) 
# ===============================
class ProxySeguridadAppMovil(InterfaceBancariaBase):
    # En su estómago esconde a la clase original frágil
    def __init__(self, servidor_interno: ModuloBancarioInterno):
        self._servidor_interno = servidor_interno
        self.token_secreto_valido = "8899"

    def filtro_autenticacion(self, intento_token):
        # Esta es la lógica extra y de validación pre-filtro que da razón de existir al patrón
        print("[PROXY INTERMEDIO] Verificando tokens SSL y Credenciales locales...")
        return intento_token == self.token_secreto_valido

    # Sobrecarga con un parámetro extra local pero cumple la misión global de despachar transacciones si hay éxito.
    def ejecutar_transaccion_a_cuenta(self, numero_cuenta_destino: str, dolares_monto: int, prueba_token: str):
        # Primero filtra...
        if self.filtro_autenticacion(prueba_token):
            print("[PROXY INTERMEDIO] Token correcto. Derivando la llamada transparente hacia la Mainframe Original...")
            # Aquí desvía el control tranquilamente hacia el núcleo sin que hayan cambiado nombres ni comportamientos en él
            self._servidor_interno.ejecutar_transaccion_a_cuenta(numero_cuenta_destino, dolares_monto)
        else:
            print("[PROXY INTERMEDIO] 🚨 ALERTA ROJA 🚨. ¡Token de sesión Invalido! Operación paralizada, el sistema banco-interno fue salvado.")


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN PROXY ===\n")

# Se levanta en los deep backends inaccesibles un servidor central
server_real = ModuloBancarioInterno()

# A la app móvil del cliente en su bolsillo, en el frontend solo le llega el "Proxy", su pasarela intermedia
aplicacion_ios = ProxySeguridadAppMovil(server_real)

print("--- Intento Hacker Ruso ---")
print("Robando datos por POST al API y tratando de mandar dinero a Suiza")
# Usan una contraseña inventada
aplicacion_ios.ejecutar_transaccion_a_cuenta("CUENTA_BANK_SUSTO999", 50000, prueba_token="0000")

print("\n--- Intento Legítimo Usuario de la APP ---")
print("El usuario usa su lector biométrico del dedo, el cual envía el token criptográfico perfecto.")
aplicacion_ios.ejecutar_transaccion_a_cuenta("CUENTA_TIENDA_ROPA101", 15, prueba_token="8899")

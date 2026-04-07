"""
PATRÓN ESTRUCTURAL: ADAPTER (Adaptador)

Explicación Detallada:
Literalmente es como un adaptador de corriente en la vida real. Si viajas a otro país y tu enchufe 
no entra en la pared, no cambias toda la instalación eléctrica del país (sería como intentar modificar
el código del sistema ajeno), y tampoco rompes tu enchufe. Compras un adaptador que va en medio.

En código: Tenemos un sistema existente que espera llamar al método `encender_con_conector_plano()`.
Del otro lado conseguimos un código de terceros muy útil (MotorEuropeo) que arranca con `arrancar_con_enchufe_redondo()`.
El Patrón Adaptador envuelve al código de terceros, expone hacia afuera la firma que espera nuestro sistema, y
por debajo lo traduce/redirecciona a la forma en que lo entiende el código de terceros.

¿Cuándo usarlo? Cuando deseas usar una clase existente pero su interfaz (sus nombres de métodos) no concuerda
con lo que necesita tu programa. Muy común al integrar librerías viejas o de terceros.
"""

# ===============================
# 1. EL CÓDIGO INCOMPATIBLE (Lo que queremos usar, pero no entrelaza)
# ===============================
# Supongamos que esta clase vino en una librería externa y NO PODEMOS MODIFICARLA
class MotorEuropeo:
    def arrancar_con_enchufe_redondo(self):
        print("Trr trr trr... [Motor Europeo girando y en marcha]")


# ===============================
# 2. NUESTRO CÓDIGO OBJETIVO (Lo que nuestro sistema "sabe" usar)
# ===============================
# Esto es lo que todos nuestros demás sistemas esperan que exista
class MotorAmericano:
    def encender_con_conector_plano(self):
        pass


# ===============================
# 3. EL ADAPTADOR (El puente traductor)
# ===============================
# Hereda o implementa la clase que NUESTRO SISTEMA espera (MotorAmericano)
class AdaptadorMotor(MotorAmericano):
    
    def __init__(self, motor_europeo: MotorEuropeo):
        # En su interior, recibe la clase que "no encaja" y se guarda una copia secreta de ella.
        self._motor_incompatible = motor_europeo

    # Implementamos el método EXACTO que el sistema esperaba que tuviéramos
    def encender_con_conector_plano(self):
        print("[⚡ Adapatador Eléctrico] Convirtiendo señal plana americana a la forma redonda europea...")
        # Aquí está la traducción: por debajo de la mesa llamamos al método que el motor europeo sí entiende
        self._motor_incompatible.arrancar_con_enchufe_redondo()


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN ADAPTER ===\n")

# Compramos un motor europeo de alta eficiencia
motor_aleman = MotorEuropeo()

print("-> Intento directo: Mi casa intenta usar el motor europeo...")
print("[Error Mental]: Mi casa solo sabe hacer `.encender_con_conector_plano()` pero el motor no tiene ese método!\n")

print("-> Intento con ADAPTADOR: Enchufo el motor europeo en el Adaptador...")
# Envolvemos el problema en nuestra solución conectora
motor_listo_para_usar = AdaptadorMotor(motor_aleman)

# Ahora mi casa felizmente le llama como ella sabe hacerlo.
# El adaptador escucha eso, y silenciosamente le avisa al motor alemán como a él le gusta que se lo digan.
motor_listo_para_usar.encender_con_conector_plano()

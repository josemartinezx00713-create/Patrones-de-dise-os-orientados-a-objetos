"""
PATRÓN DE COMPORTAMIENTO: CHAIN OF RESPONSIBILITY (Cadena de Responsabilidad)

Explicación Detallada:
Literalmente es como pasar una papa caliente que va de mano en mano hasta que alguien finalmente
puede manejarla o es el último de la fila.
Creas muchas clases distintas ("Los Manejadores") que se referencian unas a las otras en cadena sucesiva infinita.
Cuando un mensaje o solicitud entra por el extremo más bajo y débil de la cadena, el objeto A (Eslabón inferior) piensa:
"¿Yo puedo con este problema?" 
Si la respuesta es SÍ: Lo procesa y destruye la solicitud, finalizándolo ahí.
Si la respuesta es NO: No se complica la vida, lo pasa hacia su propiedad 'self.sucesor', que es el objeto
inmediatamente superior en la pirámide de la cadena de mando operativa, y así ad-infinitum.

¿Cuándo usarlo? Eventos de interfaces graficas (El botón Click->Ventana->Pantalla->Windows UI), o sistemas de Callcenters, 
Autorizaciones de escalamiento corporativo (Comprar Bolígrafo=Gerente Menor->Comprar Yate=CEO Director General).
"""

from abc import ABC, abstractmethod

# ===============================
# 1. PLANTILLA PARA CUALQUIER NIVEL (El Link de Contacto / Eslabón)
# ===============================
class ManejadorSoporte(ABC):
    # El corazón del sistema "Siguiente Elemento". Todo empleado conoce a su jefe o superior dictado.
    def __init__(self, eslabon_superior=None):
        self.eslabon_superior = eslabon_superior

    # Este método será sobre-escrito en cada escalón para decir qué saben o qué les queda grande.
    @abstractmethod
    def ejecutar_mando(self, problema_nivel: str):
        pass


# ===============================
# 2. LOS ESLABONES CONCRETOS CREADOS UNO POR UNO
# ===============================

# El más bajo de la pirámide de nuestra compañía (El BOT tonto inicial).
class ChatBotFAQ(ManejadorSoporte):
    def ejecutar_mando(self, problema_nivel: str):
        if problema_nivel == "nivel_1_basico":
            # Responde el nivel indicado
            print("[✅ ChatBot] : Oh mi programacion me permite hacer esto! -> Solución genérica: ¡Reinicie el maldito router xd!")
        else:
            # Si el nivel es más alto, le da amnesia y se lo echa al de arriba usando self.eslabon_superior
            if self.eslabon_superior:
                print("[- ChatBot] : Bi-Bup.. Mis datos no dan.. Escalando al humano de soporte técnico...")
                self.eslabon_superior.ejecutar_mando(problema_nivel)

# El eslabón medio
class AgenteTecnico(ManejadorSoporte):
    def ejecutar_mando(self, problema_nivel: str):
        if problema_nivel == "nivel_2_intermedio":
            print("[✅ Agente Real] : Hola humano. Sí señor, le enviaré el Link al formulario para restablecer contraseña secreta. Saludos!")
        else:
            if self.eslabon_superior:
                print("[- Agente Real] : Wow señor cliente, esto ya involucra fallas de servidores mayores, escalando a Soporte Nivel 3...")
                self.eslabon_superior.ejecutar_mando(problema_nivel)

# El Jefe final Supremo de Informática
class IngenieroSeniorLead(ManejadorSoporte):
    def ejecutar_mando(self, problema_nivel: str):
        if problema_nivel == "nivel_3_catastrofico":
            print("[✅ Sysadmin Supremo] : (Tomando de su café negro...) Ingresando al núcleo de Linux para reiniciar base_datos central de Europa.")
        else:
            # Él es el jefe. Si ni él puede, entonces RIP EMPRESA. (La cadena termina)
            print("[❌ Sysadmin Supremo] : Has traído un problema nivel 4 'Dios' a mi puerta. Nadie en esta compañía sabe arreglar esto.")


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN CHAIN OF RESPONSIBILITY ===\n")

# Se arma la larga fila de obreros, desde el jefe supremo hasta el esclavo menor. 
supremo_ceo = IngenieroSeniorLead() # Él no tiene nadie encima suyo
agente_call = AgenteTecnico(eslabon_superior=supremo_ceo) 
bot_tonto_inicio = ChatBotFAQ(eslabon_superior=agente_call) # La interfaz final del usuario

# Siempre inyectamos las dudas del usuario directo contra la cara del elemento más debil (el del front de la tienda).
print("--- Cliente 1 llama a la empresa con duda pequeña ---")
bot_tonto_inicio.ejecutar_mando("nivel_1_basico")

print("\n--- Cliente 2 llama a la empresa con duda regular y de validación legal ---")
bot_tonto_inicio.ejecutar_mando("nivel_2_intermedio")

print("\n--- Cliente 3 llama reportando que los servidores principales se están incendiando fisicamente ---")
bot_tonto_inicio.ejecutar_mando("nivel_3_catastrofico")

print("\n--- Cliente 4 pide que le solucionemos un problema cósmico matemático ---")
# Todos tratarán, bot->agente->ceo->y al final explotará controladamente.
bot_tonto_inicio.ejecutar_mando("nivel_dioses")

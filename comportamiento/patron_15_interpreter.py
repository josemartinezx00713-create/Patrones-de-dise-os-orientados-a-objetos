"""
PATRÓN DE COMPORTAMIENTO: INTERPRETER (Intérprete)

Explicación Detallada:
Literalmente sirve para crear pequeños lenguajes de programación o "Buscadores" dentro de tu propio código fuente.
Si tu usuario debe decirle al programa en texto algo como: "(A o B) y C" ó "(10 sumando a 5) réstale 2"... Ese texto string crudo sin 
procesar (ingresado por humanos lógicos) nadie lo comprende en la computadora.

El patrón Intérprete crea una clase por cada regla de la "Sintaxis / Gramática".
Primero se hace el árbol (Abstract Syntax Tree) usando los nudos como "Suma", "Resta", "Variables" y al final de todo se aprieta "Interpretar()" a la raiz
del árbol para desentrañar un compilador mini casero maravilloso y simple resolviendo la frase gigante paso a paso en cascada en nanosegundos!

¿Cuándo usarlo? Compiladores in-house diminutos, sistemas de queries estilo SQL o "Búsqueda Avanzada de Twitter/Jira" en texto abierto muy rigurosa.
"""

from abc import ABC, abstractmethod

# ===============================
# 1. INTERFAZ AST (El lenguaje puro)
# ===============================
class NodoExpresionGramatical(ABC):
    @abstractmethod
    def ejecutar_interpretacion(self) -> int:
        pass


# ===============================
# 2. LOS NODOS FINALISTAS, "TERMINALES" (El fin del texto, las variables, numeros brutos)
# ===============================
class NodoNroPuro(NodoExpresionGramatical):
    # Ya no invoca cosas anidadas por debajo de sí, su fin se ha encontrado en la piedra filosofal del número atómico.
    def __init__(self, numero_leido_de_texto: int):
        self.numero_puro = numero_leido_de_texto

    def ejecutar_interpretacion(self):
        return self.numero_puro # Simplemente escupe el numero que ya nadie puede restar.


# ===============================
# 3. COMPOSICIÓN NO-TERMINAL (Bifurcaciones, Sumas u OR's que evalúan a 2 o más entidades a la vez)
# ===============================
class NodoSintaxisAdicion(NodoExpresionGramatical):
    # En lugar de tener un número, exige que se le alimenten 2 entes de intepretación
    def __init__(self, rama_izq: NodoExpresionGramatical, rama_derecha: NodoExpresionGramatical):
        self.lado_l = rama_izq
        self.lado_r = rama_derecha

    def ejecutar_interpretacion(self):
        # Manda a llamar a las recursividades y suma las salientes en este árbol colosal.
        return self.lado_l.ejecutar_interpretacion() + self.lado_r.ejecutar_interpretacion()

class NodoSintaxisSubstraccion(NodoExpresionGramatical):
    def __init__(self, rama_izq: NodoExpresionGramatical, rama_derecha: NodoExpresionGramatical):
        self.lado_l = rama_izq
        self.lado_r = rama_derecha

    def ejecutar_interpretacion(self):
        return self.lado_l.ejecutar_interpretacion() - self.lado_r.ejecutar_interpretacion()


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN COMPILADOR/INTERPRETER ===\n")

# Todo el tiempo en los ordenadores oimos del "árbol recursivo de semántica AST". Esto vamos a fabricar y a simular el texto que pasaría a la rama.
# Tarea que el lenguaje string humano envió para procesar:  ((500 - 150) + 50)

# Paso automático a tokens que hace un Lexer en un lenguaje de la vida real (convirtiendo los dígitos de letras a la primera base del lenguaje int):
TokenL1 = NodoNroPuro(500)
TokenL2 = NodoNroPuro(150)
TokenL3 = NodoNroPuro(50)

# El Parser (quien arma la jerarquía a partir de los paréntesis que leyó el sistema):
rama_restando = NodoSintaxisSubstraccion(TokenL1, TokenL2)  # Este bloque ya vale (350 abstractos temporales)

# Raiz gigante jerarquial suprema final:
rama_sumando_al_final = NodoSintaxisAdicion(rama_restando, TokenL3)

print("Imprimiendo en consola el árbol de interpretaciones resuelto (AST) al ejecutar `rama_sumando_al_final.ejecutar_interpretacion()`...")

print(f"\nLA BRUJERÍA TE DA COMO VALOR CALCULADO RECURSIVO: {rama_sumando_al_final.ejecutar_interpretacion()}")

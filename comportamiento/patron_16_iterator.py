"""
PATRÓN DE COMPORTAMIENTO: ITERATOR (Iterador)

Explicación Detallada:
Extrae el comportamiento de "recorrer o iterar" elementos (ej: pasar de página en página, ir de canción en canción)
y lo encapsula en un objeto independiente iterador propio.

Problema original: Imagina que quieres mostrar a los usuarios del programa la Lista de Contactos guardados de una Empresa.
Si la empresa guardó la lista usando Listas, le pedirás al programa 'Imprímeme todos por índice [i]'.
Si un día el programador de Base de Datos cambia esa Lista a un Diccionario o usa un Árbol Binario Gigante, ¡tu ciclo código For [i] clásico dejará de compilar y tirará error para el programa entero!

Solución Patrón Iterador:
El Iterador siempre tiene un mismo único comando divino "Siguiente()". Al utilizarlo, te desconectas por completo
de cómo lo guardó el programador de base de datos adentro. Tú pides 'siguiente' y te aparece mágicamente.
Python lo tiene NATIVO interconectado gracias a los métodos dunder (__iter__ y __next__).

¿Cuándo usarlo? Al exponer al exterior colecciones de datos, listas complejas, grafos a ser recorridos...
"""

# ===============================
# CLASE CUALQUIERA, LA INFORMACION (Una simple entidad sin valor iterativo todavía)
# ===============================
class InfoCancion:
    def __init__(self, titulo_tema):
        self.titulo_tema = titulo_tema

# ===============================
# LA COLECCION DE DAATOS PERSONALIZADA (Nuestra base de datos local Playlist)
# ===============================
class ColeccionMisteriosaPlaylist:
    def __init__(self):
        # Yo guardo en una lista clásica... pero si a futuro lo paso a diccionario de hashes,
        # Nadie lo va a resentir porque la "puerta de salida" que usan es universal gracias al Iterator
        self.bd_musicas = []

    def injectar_a_bdd(self, string_titulo_tema):
        self.bd_musicas.append(InfoCancion(string_titulo_tema))

    # --- MAGIA NATIVA PYTHON PARA HABILITAR EL PATRON ITERATOR (EL DUNDER METHOD MÁGICO) ---
    def __iter__(self):
        # El iterador interno es encajonado junto con el índice virtual en "0". Y devuelto para su operación foránea.
        self._agente_contador_invisible = 0
        return self

    # --- PUERTA DE SALIDA ÚNICA Y UNIVERSAL (EL BOTON SIGUIENTE) ---
    def __next__(self):
        # Verifica hasta encontrar la pared negra y muerta de ListOutOfBordersException limitante.
        if self._agente_contador_invisible < len(self.bd_musicas):
            # Extraerlo con cautela
            tema_al_aire = self.bd_musicas[self._agente_contador_invisible]
            # Paso crucial en la iteracion foránea: Incrementar contador de avance hacia la meta del iterador
            self._agente_contador_invisible += 1
            return tema_al_aire.titulo_tema
        else:
            # En otros lenguajes esto rebotaría Null, pero Python estandarizó y obligó usar raise StopIteration 
            # (El propio for-loop que vamos a ver abajo lo captura de fondo transparente y en el momento indicado se apaga).
            raise StopIteration


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN ITERATOR ===\n")

dispositivo_mp3 = ColeccionMisteriosaPlaylist()
dispositivo_mp3.injectar_a_bdd("La Macarena_HD.mp3")
dispositivo_mp3.injectar_a_bdd("Rock_Espanol.opus")
dispositivo_mp3.injectar_a_bdd("Mozart_Sinfonias_Base.wav")

print("Se armó el Loop del FOR en Python de forma estandarizada e incorruptible:\n")

# Todo bucle FOR `en elemento in var` es un consumidor ciego puro del Patrón Iterator (__iter__).
for elemento_sonoro in dispositivo_mp3:
    print(f"🎵 Sonando pista en los headsets: {elemento_sonoro}")

print("\nTerminó el iterador nativamente y de manera limpia.")

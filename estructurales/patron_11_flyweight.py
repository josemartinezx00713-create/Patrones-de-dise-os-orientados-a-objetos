"""
PATRÓN ESTRUCTURAL: FLYWEIGHT (Peso Mosca)

Explicación Detallada:
El patrón de la 'memoria RAM'. Ayuda inestimablemente cuando tu programa debe cargar o instanciar
literalmente decenas de miles de objetos y te da miedo colapsar la computadora ("Out Of Memory").

Imagínate un bosque 3D. Cada árbol en pantalla tiene Polígonos de corteza y un set de texturas (hojas.png).
Si el programador usa `new Arbol()` 100,000 veces y en el constructor carga esos polígonos pesados, la PC se quema.
El Flyweight divide el árbol en 2 partes:
1. "El Estado Intrínseco" -> Cosas Pesadas iguales para miles (Texturas de pino, Modelos 3D de pino). ESTO SE COMPARTE usando una sola variable universal.
2. "El Estado Extrínseco" -> Cosas Ligeras únicas (x, y, edad del árbol). ESTO SÍ SE INSTANCIA en masa porque ocupa nada y menos.

¿Cuándo usarlo? Partículas en videojuegos (arena, balas, árboles), editores de texto con cientos de miles de caracteres (donde 
dibujar una letra "A" siempre usa la misma textura de fuente vectorial A compartida, pero cada instancia tiene distintas coordenadas posicionales).
"""

# ===============================
# 1. EL ESTADO INTRÍNSECO COMPARTIDO (El "Flyweight" per se, el archivo pesado y único central)
# ===============================
class DatosRendimientoYTexturasTipoArbol:
    # Estos objetos pesaremos 20MB cada unooo. 
    def __init__(self, especie_nombre, color_base, mapa_textura_hd_2k):
        self.especie = especie_nombre
        self.color = color_base
        self.textura = mapa_textura_hd_2k

    def dibujar_graficamente(self, coordenada_x, coordenada_y):
        # Utiliza los valiosísimos datos propios, pero requiere que le presten datos geográficos del mundo
        print(f"🌲 Rasterizando [{self.especie}-{self.color}] en el pixel ({coordenada_x}, {coordenada_y}) de la pantalla usando GPU...")


# ===============================
# 2. EL CACHE / LA FÁBRICA QUE GARANTIZA EL PATRÓN FLYWEIGHT
# ===============================
# Actúa como portero. Nunca deja que un objeto pesado nazca 2 veces. Lo clona con referencias (punteros a memoria).
class FabricaFlyweightVivero:
    _pool_de_tipos = {} # Cache dict de elementos generados pesados

    @classmethod
    def obtener_tipo_de_arbol(cls, especie, color, textura):
        llave_unica_hash = f"{especie}_{color}"
        
        # Si NO EXISTE en cache general, lo cargamos penosamente.
        if llave_unica_hash not in cls._pool_de_tipos:
            print(f"[!] [ALERTA RAM] Se están cargando en memoria RAM Texturas súper pesadas del tipo de árbol: {especie} !!!")
            nuevo_tipo = DatosRendimientoYTexturasTipoArbol(especie, color, textura)
            cls._pool_de_tipos[llave_unica_hash] = nuevo_tipo
            
        # Retornamos el puntero a esa gran zona de memoria.
        return cls._pool_de_tipos[llave_unica_hash]


# ===============================
# 3. EL ESTADO EXTRÍNSECO (El chasis súper ligero del objeto instanciado individualmente)
# ===============================
class ArbolPlasticoIndividual:
    # Esto ocupará unos 5 bits en memoria real, porque la textura viene del Singleton-Fabrica
    def __init__(self, x, y, referencia_al_puntero_pesado: DatosRendimientoYTexturasTipoArbol):
        self.x = x
        self.y = y
        # Guardamos un simple link al archivo central, no lo volvemos a instanciar
        self.tipo_compartido = referencia_al_puntero_pesado

    def invocar_dibujado_en_pantalla(self):
        # A la hora del render, manda a la entidad pesada con sus coordenadas locales diminutas
        self.tipo_compartido.dibujar_graficamente(self.x, self.y)


# --- DEMOSTRACIÓN ---
print("=== DEMOSTRACIÓN DEL PATRÓN FLYWEIGHT ===\n")
memoria_del_mundo_array = []

print("Fase de Reforestación. Empezamos con el primer Pino en todo el juego.")
tipo_pino_frio = FabricaFlyweightVivero.obtener_tipo_de_arbol("Pino Nevado", "Blanco", "texturapinoHD.jpg")
memoria_del_mundo_array.append(ArbolPlasticoIndividual(10, 20, tipo_pino_frio))


print("\nAhora sembramos el segundo pino en la montaña!")
tipo_pino_repetido = FabricaFlyweightVivero.obtener_tipo_de_arbol("Pino Nevado", "Blanco", "texturapinoHD.jpg")
memoria_del_mundo_array.append(ArbolPlasticoIndividual(358, 2011, tipo_pino_repetido))
print("(Arriba no hubo aviso de alerta RAM porque re-usamos exitosamente el bloque pre-cargado de datos = AHORRO MASIVO)")


print("\nPlantamos un árbol totalmente diferente, del cual no hay texturas cargadas previamente:")
tipo_roble = FabricaFlyweightVivero.obtener_tipo_de_arbol("Roble Fuerte", "Verde", "texturarobleMD.png")
memoria_del_mundo_array.append(ArbolPlasticoIndividual(99, 10, tipo_roble))

print("\n--- Renderización final para tarjeta de video ---")
for arbustito in memoria_del_mundo_array:
    arbustito.invocar_dibujado_en_pantalla()

print(f"\nResultado técnico: Hay guardados en array general enormes cantidades de árboles ({len(memoria_del_mundo_array)}), pero realmente las texturas pesadas instanciadas en tu placa madre solo son un total microscópico de: {len(FabricaFlyweightVivero._pool_de_tipos)}")

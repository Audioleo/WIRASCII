# El Proyecto WIRASCII v1.0

**Esquemas eléctricos e ideas claras, impresos en texto plano**

## Introducción

**WIRASCII** es un sistema de convenciones diseñado para representar, de forma simple y práctica, circuitos eléctricos y electrónicos usando solo texto plano (ASCII/Unicode). Fué desarrollado para facilitar la comunicación y el envío rápido de documentación técnica entre personas y/o asistentes de inteligencia artificial, en chats o entornos remotos colaborativos mediante dispositivos cuyas funciones gráficas son ineficientemente soportadas.

>Permite construir y compartir diagramas legibles sin necesidad de recurrir a imágenes ni software especializado, ideal para diseños educativos rápidos, y documentación técnica liviana.

### El orígen de las ideas
WIRASCII es un proyecto que nació de manera espontánea. No estaba planeado, ni pretendía ser un gran desarrollo. Simplemente surgió en medio de una conversación entre una persona (El creador) y una asistente virtual (La IA).

>Su desarrollo parte de una necesidad: la de representar circuitos eléctricos sencillos de manera textual en un entorno con limitaciones gráficas.

A pesar de tales limitaciones, fué posible lograr representaciones bastante comprensibles usando únicamente texto. Así nació WIRASCII: en un intento por estandarizar y compartir esta forma alternativa de diagramación.

>El proyecto WIRASCII inicia como una propuesta colaborativa entre una persona y una inteligencia artificial, con el objetivo de facilitar la representación de circuitos eléctricos, de manera rápida, sencilla y comprensible.

### Aplicaciones

A pesar de de su simplicidad, tiene una aplicación real en entornos, como chats técnicos, o flujos de trabajo colaborativo entre personas y sistemas de asistencia virtual sobre hardware y software con bajo rendimiento gráfico, en donde compartir imágenes se torna imposible o ralentizado.

WIRASCII es ideal para:

- Entornos de terminal textual puro (como Markdown, foros, chats).

- Educación y formación técnica.

- Chats técnico-colaborativo entre humanos e IAs.

- Creación de bocetos y simulación conceptual rápida de circuitos antes de pasar al diseño.

---

## Punto de partida del proyecto

A continuación, se exponen los primeros elementos, conceptos, y especificaciones definidas en la fase inicial de desarrollo del proyecto como un punto de partida.

### Requisitos del entorno y de los símbolos

WIRASCII está diseñado para utilizarse en entornos textuales 100% monoespaciados, y editores de texto, tales como Notepad++, VSCode, Geany, y similares.

Los símbolos deben tener un estilo estandarizado, alineados sin usar el carácter de tabulador, y usando solo características compatibles con la mayoría de editores de texto.

### Base de carácteres

Inicialmente, se ha seleccionado y clasificado una serie de caracteres ASCII/Unicode posiblemente útiles para representar líneas de alambrado y componentes como resistores, capacitores, diodos, puentes, transistores, ICs y bloques funcionales (vea el archivo char-base.txt). 

La base de caracteres WIRASCII, puede seguir extendiéndose a medida que se desarrollen sus siguientes versiones; sin embargo, debe cumplir las siguientes características:

- Ser compatible con editores de texto plano.

- Permitir símbolos normalizados y compactos.

- Diseñar componentes con estilo visual limpio y uniforme, con terminales, conexiones definidas.

### Definición gráfica de símbolos

La representación visual de componentes se realiza mediante la combinando caracteres ASCII/Unicode, de manera que su apariencia sea lo más parecida (dentro de lo posible) a los símbolos de componentes eléctricos y electrónicos estándar.

Al momento de definir la apariencia visual de un símbolo se debe mantener la uniformidad y un estilo coherente. Todos los símbolos deben ser lo más compacto posible en tamaño y proporciones visuales. 

A continuación, se muestran las representaciones gráficas de algunos de símbolos ya definimos en WIRASCII:

```
| Componente   | Gráf. | Ref. |
|--------------|-------|------|
| Resistor     |  [Ω]  |  Rn  |
| Inductor     |  [ω]  |  Ln  |
| Capacitor    |  [=]  |  Cn  |
| Fuente AC    |  (~)  |  En  |
| Fuente DC    |  (±)  |  En  |
| Diodo        |  [▼]  |  Dn  |
| Zener        |  [v]  |  Zn  |
| LED          |  (v→) |  LDn |
| Fusible      |  [~]  |  Fn  |
| Switch       |  [/]  |  Sn  |
```
Para más representaciones gráficas de componentes, consulte el archivo graphic-symbol.txt

### Especificaciones de símbolos, alambrado y conexiones 

A fin de poder definir los parámetros de las librerías de símbolos de componentes WIRASCII, se han definido los siguientes conceptos claves:

1. **Representación gráfica**: es la apariencia visual de cada símbolo. Este concepto está basado en las explicaciones del apartado anterior.

2. **Orientaciones cardinales (N, S, E, O)**: representan las distintas variantes de rotación disponible para cada símbolo.
3. **Puntos de continuidad del alambrado**: posiciones claras donde conectan las líneas de los cables (ej. ─, │). Este concepto está aún en fase de pruebas.
4. **Terminal de conexión numérica**: identificación de terminales reales del componente, mediante números (ej. '1', '2').
5. **Marcación de terminal**: identificación visible de terminales de componentes según su función o polaridad (ej. '+', 'In', 'Out', 'Vcc', 'Gnd', etc.). No todos los terminales se marcan, a menos que éste lo requiera.

6. **Referencia (Rf)**: identificación clave de componentes según su tipo y número de instancia (ej. 'R1', 'C1', 'S1', 'Q1', 'Q2').

### Prueba y depuración 

Para poner a prueba el sistema, y hacer las correcciones y depuraciones necesarias, resulta conveniente poner en marcha el sistema WIRASCII 1.0 a partir de unos pocos símbolos creados al inicio, en lugar de crear una librería extensa con todos sus símbolos esperados.

---

## Visión

De momento no se tienen claras las expectativas futuras de este proyecto; por lo tanto, esta sección del documento está en fase de edición a medida que se desarrolla este proyecto.

---

## Créditos y comunidad

**Autor:** Audioleo

**Asistencia IA:** ChatGPT (OpenAI)

WIRASCII es una iniciativa abierta creada en colaboración entre humanos y modelos de lenguaje IA. Fue concebida como una solución práctica de esquematizar circuitos durante el trabajo conjunto con IA, sin depender de la herramienta de generación de imágenes.

---

## Licencia MIT

Este proyecto es de código abierto bajo la Licencia MIT.
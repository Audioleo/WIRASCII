# WIRASCII

**WIRASCII** es un sistema de representación de circuitos eléctricos y electrónicos en texto plano, diseñado para entornos de chat, terminales y colaboración remota entre humanos e inteligencias artificiales. Permite construir y compartir diagramas legibles sin necesidad de imágenes o software especializado, ideal para diseños rápidos, documentación técnica liviana y educación.

---

## Características

- Representación simple en ASCII de componentes eléctricos y electrónicos.

- Convención clara para nodos, uniones, cruces y polaridades.

- Símbolos compatibles con editores de texto plano y chats colaborativos.

- Sistema modular: los bloques pueden ensamblarse como partes de sistemas más grandes.

- Útil en plataformas con baja resolución o sin soporte gráfico.

---

## Ejemplo

```txt
Fuente AC con puente rectificador:

        ┌─────┐
 AC ────│~   +│────── +V
        │BR1  │
 AC ────│~   -│────── GND
        └─────┘
```

## Convenciones básicas

- Nodo de conexión: +

- Sin conexión: (

- Resistor: [Rn] o [^^^]

- Inductor: [))) ]

- Fuente AC: (~) | Fuente DC: (±)

- Diodo común: [—>—] | Zener: [—>(]

- Fusible: [•~•]

- Transistores: genéricos [Qn], pnp/npn detallados

- Bloques de componentes (hasta 6 pines): símbolo rectangular con etiquetas externas

## Ejemplo de bloque genérico

```
 ┌───────┐
 │6     1│
 │5 REF 2│
 │4     3│
 └───────┘
```
Las etiquetas de los pines pueden mostrarse externamente. Solo se permite conexión en las líneas de pines (1 a 6).

## Aplicaciones

- Chats técnico-colaborativos

- Educación y divulgación técnica

- Diseño y simulación conceptual rápida

- Documentación liviana y multiplataforma

## Licencia

Este proyecto es de código abierto bajo la Licencia MIT.

# WIRASCII

WIRASCII es un lenguaje de diagramas eléctricos en texto plano (ASCII), diseñado para representar circuitos sencillos de forma ligera y colaborativa, ideal para compartir circuitos sencillos o documentación técnica en chats, foros o en entornos con limitaciones gráficas.

## Objetivos

- Crear símbolos estandarizados legibles en texto plano.

- Facilitar la colaboración entre personas, o entre humanos e inteligencias artificiales.

- Ser fácilmente extensible y accesible.

- Utilizarse en plataformas con baja con baja capacidad o sin soporte gráfico.

## Características

- Representación simple en ASCII de componentes eléctricos y electrónicos.

- Convención clara para nodos, uniones, cruces y polaridades.

- Símbolos compatibles con editores de texto plano y chats colaborativos.

- Sistema modular: los circuitos pueden diseñarse como subsistemas de sistemas más grandes.


## Convenciones básicas

- Nodo de conexión: +

- Sin conexión: (

- Resistor: [Rn] o [^^^]

- Inductor: [)))]

- Fuente AC: (~) | Fuente DC: (±)

- Diodo común: [—>—] | Zener: [—>(]

- Fusible: [•~•]

- Transistores: genéricos [Qn], pnp/npn detallados

- Bloques de componentes (hasta 6 pines): símbolo rectangular con etiquetas externas

## Ejemplos

Fuente AC con puente rectificador:
```txt
         ┌─────┐
 AC ────│~    +│────── +V
         │BR1   │
 AC ────│~    -│────── GND
         └─────┘
```

Componente de bloque genérico:
```wrirascii
 ┌───────┐
 │6      1│
 │5 REF  2│
 │4      3│
 └───────┘
```
Las etiquetas de los pines pueden mostrarse externamente. Solo se permite conexión en las líneas de pines (1 a 6).

## Aplicaciones

- Chats técnico-colaborativos

- Educación y divulgación técnica

- Diseño y simulación conceptual rápida

- Documentación liviana y multiplataforma

## Créditos y comunidad

**Versión:** 1.0 (borrador)
 
**Colaboradores:**
- Audioleo (creador humano)
- ChatGPT por OpenAI (asistencia IA)

WIRASCII es una iniciativa abierta creada en colaboración entre humanos y modelos de lenguaje IA. Fue concebida como una solución práctica para esquematizar circuitos durante el trabajo conjunto con IA, sin depender de imágenes en entornos sin soporte o de bajas capacidades gráficas.

## Licencia

Este proyecto se publica bajo la licencia MIT.

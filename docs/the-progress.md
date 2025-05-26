# Avance del proyecto WIRASCII v1.0

## Origen e idea

**¿Cómo surgió?** WIRASCII nació como una propuesta colaborativa entre una persona y una inteligencia artificial en un entorno de chat, con el objetivo de facilitar la representación de circuitos eléctricos en texto plano. Su desarrollo parte de la necesidad de esquemas ligeros, portables y comprensibles para diálogos técnicos rápidos o colaboraciones en plataformas y dispositivos con capacidades gráficas limitadas.

**¿Qué es WIRASCII?** es un sistema de representación de circuitos eléctricos y electrónicos en texto plano, diseñado para entornos de chat, terminales y colaboración remota entre humanos e inteligencias artificiales. Permite construir y compartir diagramas legibles sin necesidad de imágenes o software especializado, ideal para diseños rápidos, documentación técnica liviana y educación.

**Veamos un ejemplo**, una fuente DC con puente rectificador:

```
         ┌─────┐
 AC ────│~    +│────── +V
         │ BR1  │
 AC ────│~    -│────── -V
         └─────┘
```
## Aplicaciones

- Chats técnico-colaborativo.

- Diseño y simulación conceptual rápida.

- Educación y divulgación técnica.

- Documentación liviana y multiplataforma.

## Estado inicial del proyecto

A continuación, se expone el avance que tuvo el proyecto en su punto de partida inicial.

### Características definidas

- Representación simple en ASCII de componentes eléctricos y electrónicos.

- Convención para nodos, uniones, cruces y polaridades; y reglas claras para conexiones.

- Símbolos compatibles con editores de texto plano y chats colaborativos.

- Sistema modular: los bloques pueden ensamblarse como partes de sistemas más grandes.

- Útil en plataformas con baja resolución o sin soporte gráfico.

### Símbolos básicos desarrollados

A continuación, se presentan las convenciones de símbolos de componentes que tenemos hasta ahora. Pero, nos falta añadir más, y corregir los bugs de los componentes que ya existen.

- `[Rn]` o `[^^^]` : Resistor

- `[)))]` : Inductor

- `(~)` : Fuente AC

- `(±)` : Fuente DC

- `[—>—]` : Diodo común

- `[—>(]` : Zener

- `[•~•]` : Fusible

- `[Qn]` : Transistore genérico

- `[REF]` : Componente de bloque genérico (representación simple de componentes, subcircuitos o sistemas)

### Reglas de conexión

Los símbolos a continuación se utilizan para representar cruces entre líneas (cables) de conexión.

- `+` : Nodo o cruce línea con conexión

- `(` : Cruce de línea sin conexión

También, ya se tienen definidas las reglas y convenciones de conexión de terminales de algunos componentes.

### Requisitos del entorno y de símbolos

WIRASCII está diseñado para utilizarse en entornos con características de texto preformateado y editores de texto simple monoespaciado, tales como Notepad++, VSCode, Geany, y similares.

Los símbolos deben tener un estilo estandarizado tipo ASCII, alineados sin usar el carácter de tabulador, y usando solo características compatibles con la mayoría de editores de texto.

## Objetivo actual

Depurar los símbolos existentes para mejorar su consistencia, funcionalidad y flexibilidad de uso en diagramas ASCII.

### Tareas propuestas

- [ ] Corregir bugs del generador de bloque genérico (alineaciones, terminales faltantes o desplazados).

- [ ] Permitir borrar terminales no utilizados sin afectar el formato del símbolo.

- [ ] Implementar la posibilidad de girar símbolos (90°, 180°, 270°) o al menos permitir girar sus terminales.

- [ ] Evaluar el impacto de estas mejoras en la legibilidad y simplicidad de los diagramas.

## Créditos y comunidad

**Autor:** Audioleo

**Asistencia IA:** ChatGPT (OpenAI)

WIRASCII es una iniciativa abierta creada en colaboración entre humanos y modelos de lenguaje IA. Fue concebida por el usuario Audioleo como una solución práctica esquematizar circuitos durante el trabajo conjunto con IA, sin depender de la generación de imágenes.

## Licencia 

Este proyecto es de código abierto bajo la Licencia MIT.

---

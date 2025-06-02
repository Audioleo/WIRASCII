# Biblioteca de símbolos WIRASCII

Esta carpeta contiene los **símbolos gráficos** utilizados por el sistema WIRASCII. Cada símbolo representa un componente eléctrico o electrónico, diseñado para usarse en entornos de texto plano.

## Organización

Los símbolos están clasificados por tipo o función, en subcarpetas como:

```
symbols/
├── basics/ # Componentes básicos (diodos, resistencias, capacitores, etc.)
├── graphs/ # Base de carácteres gráficos para representación de símbolos y alambrado.
├── specs/ # Especificaciones de los símbolos
```

Cada archivo `.txt` contiene una o varias variantes de un mismo símbolo, generalmente en distintas orientaciones (horizontal o vertical).

## Convenciones

- **Formato:** Cada símbolo se dibuja con caracteres Unicode ligero(para superar las limitaciones ASCII).
- **Terminales:** Se indican usando líneas verticales (`│`) u horizontales (`─`), según el sentido.
- **Centro de conexión:** El símbolo se alinea al centro de sus terminales verticales, si corresponde.
- **Wire units (unidades de cableado):** Se utilizan caracteres como `─`, `│`, `┬`, `┴`, `┼`, `├`, `┤` para representar derivaciones, cruces y uniones de líneas.
- **Nombres:** Los nombres de archivos son descriptivos y utilizan guiones (`-`) para separar palabras.

## Ejemplo (símbolo de diodo común)

```text
 │
[▼]
 │
```
## Nota sobre Unicode

Aunque el proyecto se llama WIRASCII, se emplean también caracteres Unicode ligeros para lograr mayor claridad visual. Esto incluye símbolos como ▼, ▶, ─, ┬, etc. Todos los símbolos están diseñados para funcionar correctamente en la mayoría de editores de texto modernos y terminales compatibles.

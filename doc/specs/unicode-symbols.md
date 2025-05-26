## Convención de símbolos WIRASCII (Unicode)

Este documento establece la lógica de diseño de cada símbolo en formato Unicode, con dimensiones, terminales y alineaciones estandarizadas.

---

### Plantilla de definición por símbolo

* **Nombre**:
* **Código**:
* **Orientación**: vertical | horizontal | ambas
* **Dimensiones**: Alto × Ancho
* **Terminales**:

  * Posición semántica (ej. top-center, bottom-center, etc.)
  * Coordenadas relativas (x, y)
* **Referencia (texto)**:

  * Posición: centrado / alineado izquierda / derecha
  * Variante espejo: sí / no
* **Ejemplo visual**:

```

  │
[Q1]
  │

```

---

### Ejemplo 1: Conmutador genérico (transistor)

- **Nombre**: Conmutador genérico
- **Código**: Qn
- **Orientación**: vertical
- **Dimensiones**: 3 × variable (según largo de referencia)
- **Terminales**:
- top-center → (center_x, 0)
- bottom-center → (center_x, 2)
- **Referencia**:
- centrada por defecto
- variante espejo: sí
- **Ejemplo visual**:

```

  │
[Q12]
  │

```
Variante espejo:
```

 │
[Q12]
 │

```

### Ejemplo 2: Diodo

- **Nombre**: Diodo
- **Código**: [▼] / [▲]
- **Orientación**: vertical
- **Dimensiones**: 3 × 3
- **Terminales**:
- top-center → (1, 0)
- bottom-center → (1, 2)
- **Referencia**:
- no aplica (símbolo sin etiqueta numérica)
- variante espejo: no
- **Ejemplo visual**:
```

│
[▼]
│

```

---

(Continuar con otros símbolos...)

---

**Nota:** Todos los símbolos usan caracteres Unicode compatibles con renderizado monoespaciado. Estas definiciones permiten el parseo automatizado y validación de conexiones en futuros scripts.

```

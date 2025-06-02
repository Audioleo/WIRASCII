# Diferencia entre Tierra y Masa

En electrónica, los términos **tierra** y **masa** se usan con frecuencia, pero **no siempre significan lo mismo**. Comprender su diferencia es clave para diseñar circuitos seguros y con buen comportamiento eléctrico.

---

## 🌎 Tierra (Earth Ground)

- Conexión física al suelo, usada principalmente en instalaciones eléctricas.
- Proporciona una ruta de descarga segura para corrientes de falla.
- Se conecta al chasis metálico de equipos para protección.
- Ayuda a evitar acumulación de carga estática.
- Símbolo típico: `┴` o variantes con múltiples líneas.

### Usos típicos:
- Seguridad eléctrica
- Descarga de fallas
- Conexión de chasis

---

## ⚫ Masa (GND - Ground)

- Punto de **referencia de voltaje** dentro del circuito.
- No está necesariamente conectada a tierra física.
- Es el nodo común por donde retornan las corrientes del sistema.
- Se usa para definir los niveles de tensión lógica o analógica.

### Usos típicos:
- Referencia de 0 V
- Retorno de alimentación
- Punto de referencia de señales

---

## ⚠️ Diferencias clave

| Característica       | Tierra                   | Masa (GND)               |
|----------------------|--------------------------|--------------------------|
| Conexión al suelo    | Sí                       | No necesariamente        |
| Función principal    | Seguridad, descarga      | Referencia de voltaje    |
| Común en             | Electricidad industrial  | Electrónica de señales   |
| Símbolo típico       | `┴`                      | `▬`, `GND`, línea simple |

---

## 🧩 En WIRASCII

Ambos conceptos se representan con **símbolos distintos** para evitar ambigüedades:

- `Tierra`: símbolo con `┴`, etiqueta `EAR`.
- `Masa`: símbolo con `▬`, etiqueta `GND`.

Esta diferenciación visual permite mayor claridad en sistemas mixtos o sensibles, como audio, fuentes de alimentación o control industrial.

---

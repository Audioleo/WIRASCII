# WIRASCII

**WIRASCII** es un sistema de representación de circuitos eléctricos y electrónicos mediante símbolos de texto. Está pensado para facilitar la colaboración en entornos de texto plano —como chats, terminales o correos— donde los diagramas visuales tradicionales no son prácticos o posibles.

Este proyecto es abierto y colaborativo. Si te interesa el cruce entre electrónica, herramientas ligeras y creatividad basada en texto, ¡eres bienvenido a contribuir!

---

## Tabla de contenido

- [El proyecto WIRASCII](doc/the-project.md)
- [Símbolos disponibles](symbols/)
- [Herramientas y scripts](tools/)
- [Ejemplos (próximamente)](examples/)

---

## ¿Por qué WIRASCII?

- Permite compartir diagramas eléctricos en texto plano, sin depender de imágenes.
- Ideal para entornos de bajo ancho de banda, terminales, documentación rápida o colaboración remota.
- Útil en chats con IA, foros técnicos, notas personales y documentación embebida.
- Promueve un estilo modular, replicable y colaborativo.

### Ejemplo: Inversor Half-Bridge con Rail-Split

```txt
        +Vbus ───┬──────────────┐
                  │              │
                  │              │
                [Q1]           [C1]
                  │              │
                  │              │
                  ├─A───())))───B─┤
                  │     L        │
                  │              │
                [Q2]           [C2]
                  │              │
                  │              │
         GND ────┴──────────────┘
```
### Notas:

- [Q1] y [Q2]: Conmutadores genéricos (MOSFETs, IGBTs, etc.)

- [C1] y [C2]: Capacitores del divisor de voltaje (rail-split)

- La carga resonante (bobina + pieza de trabajo) está entre los nodos A y B

---

## Nota sobre compatibilidad

Aunque el proyecto se llama **WIRASCII**, muchos símbolos utilizan **caracteres Unicode** para mejorar su claridad visual (como flechas, líneas de conexión y terminales).  
Se recomienda visualizar los diagramas en entornos que soporten Unicode completo (UTF-8).

---

## Estructura del repositorio
```
WIRASCII/
│
├── doc/ # Documentación del proyecto
├── symbols/ # Biblioteca de símbolos (ASCII + Unicode)
├── tools/ # Scripts y utilidades (generadores, validadores, etc.)
├── examples/ # Ejemplos prácticos (en desarrollo)
└── README.md # Este archivo
```

---

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

*Creado y mantenido por [Audioleo](https://github.com/Audioleo), con el apoyo de colaboradores y asistentes IA.*

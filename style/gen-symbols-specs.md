# WIRASCII - Especificaciones Generales para Símbolos

## 1. Representación gráfica

- Cada símbolo tiene un tamaño mínimo de filas y columnas (F x C), el cual puede aumentar al añadir etiquetas de marcación y referencia.

- Cada símbolo se representa mediante una combinación de caracteres que definen la apariencia visual de cada componente. Se recomienda usar caracteres ASCII y Unicode visualmente estables.

- Los símbolos de cada componente deben poder diferenciarse unos de otros.

- Orientaciones: Norte (N), Sur (S), Este (E), Oeste (O), con formato homogéneo. Algunos símbolos solo tienen una o dos orientaciones. 

## 2. Reglas electricas generales

- Categoría de símbolo: "1T", "2T", "3T" y así sucesivamente según el número total de terminales (o "MT" para 3 terminales en adelante).

- Terminales numerados 1, 2, 3, etc.

- Cada terminal numerado tiene un metadato de rol opcional (ejemplo: 1=ánodo, 2=cátodo).

- Alambrado de terminales con líneas '─' o '│'.

## 3. Símbolos terminales de circuito

- Estos símbolos solamente tienen un solo terminal (1T), y se utilizan para representar terminales y conexiones comunes de circuito:

	- Entrada de señal
	- Entrada de alimentación
	- Salida de señal
	- Salida de potencia
	- Tierras
	- Masas

## 4. Símbolos polarizados

- Los símbolos con dos o más terminales que tengan al menos un rol de terminal, se consideran polarizados, o que se deben respetar sus terminales (si es necesario usar el metadato "polarizado: true/false").

## 5. Archivos de símbolos

- Cada símbolo debe tener su propio archivo de librería con sus metadatos generales y específicos.

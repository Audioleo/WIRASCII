# WIRASCII - Reglas para representación de cableado en esquemas

Cumplir las siguientes reglas asegura claridad de las conexiones en sistema WIRASCII.

## 1. Líneas de alambrado válidas (*wire units*):
```
   ─  Línea horizontal  
   │  Línea vertical

   ┌  Línea vértice superior izquierdo
   ┐  Linea vértice superior derecho
     
   └  Linea vértice inferior izquierdo
   ┘  Linea vértice inferior derecho
```
## 2. Nodos de derivación:
```   
   ┬  Derivación superior  
   ┴  Derivación inferior  
   ├  Derivación izquierda  
   ┤  Derivación derecha
```
## 3. Nodo de cruce:
```
   ┼
```
- representa 4 vías conectadas en punto de cruce.

## 4. Modelo de líneas cruzadas:
```
   │
  ─(─
   │
```
- Representa 2 líneas cruzadas no conectadas; en otras palabras, este modelo representa 2 alambres que cruzan (pasando uno por arriba del otro) sin conectarse en el punto de cruce.
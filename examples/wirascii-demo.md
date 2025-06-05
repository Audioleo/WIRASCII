# WIRASCII - Ejemplos de aplicación

A continuación, se presentan algunos ejemplos de componentes, circuito, y subcircuitos representados con WIRASCII.

### Requisito importante:

Para que los diagramas de circuitos hechos en WIRASCII sean visualizados correctamente, es necesario que la pantalla, la terminal, o el marco de visualización textual, utilice fuentes 100% monoespaciadas.

## Diodo común:

```
 a
 │
[▼]  a──[▶]──k
 │
 k
```

## Puentes rectificadores:

```
    ┌───┐
────┤~ +├────
    │ ▶ │
────┤~ -├────
    └───┘
    ┌───┐
────┤~ +├────
────┤~ -├────
    └───┘
```

## Transformadores:

```
   N1:N2
────┐ ┌────
  p ░ ░ s
────┘ └────

    T2
────┐ ┌────
  p █ █ s
────┘ └────

       T12   
───────┐ ┌───────
     p █ █   
───────█ █ s  
     p █ █    
───────┘ └───────
       REF  
```
### Notas

- p, s : primario, secundario.

## Fuente DC de potencia:

```
                    ┌───────┐    ┌───────┐
L >────[~]──[NTC]───┤       ├────┤~ BR1 +├───────────> +Vbus
                    │  EMI  ├────┤~     -├───────┐
N >────[~]──[NTC]───┤       │    └───────┘       │
                    └───┬───┘                  [MOV]   
                        │                        │
                        │                        │
                       ^^^                      ¯¯¯
```

### Notas

- Fusibles lentos (~15–20 A).

- NTC para arranque suave.

- MOV entre Vbus y GND para protección.

## Inversor Resonante:

```
+Vbus >─────┬─────────────┐
            │             │
          ─[/] Q1        [=] C1
            │             │
          A ├────────────(──────────> 
            │             │
            │           B ├─────────>
            │             │
          ─[/] Q2        [=] C2  
            │             │
            │             │
           ¯¯¯           ¯¯¯
```

### Notas

- Red de switchs : half-bridge (Q1, Q2).

- Capacitores rail-split : C1, C2 del tipo MKP.

- Q1, Q2 : interruptores Controlados.

- Nodo A : punto medio del half-bridge.

- Nodo B : punto medio del capacitor rail-split.

- En este circuito no se incluye su parte de control.

## Equivalente de una bobina:

```
>───[ω]──[Ω]───<
       L   Req
```

### Notas

- L : inductancia de bobina L (ω).

- Req : resistencia (Ω) equivalente de bobina.
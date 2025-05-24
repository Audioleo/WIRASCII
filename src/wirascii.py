#-*-coding:utf8;-*-
#qpy:console

def generar_bloque_wirascii(ref='REF', t1='', t2='', t3='', t4='', t5='', t6=''):
    # Limita cada terminal a 3 caracteres y centra
    def fmt(t): return t.center(3) if t.strip() else '   '
    t1, t2, t3, t4, t5, t6 = map(fmt, (t1, t2, t3, t4, t5, t6))
    ref = ref.center(11)

    simbolo = (
        "┌────────────┐\n"
        f"│{t6}     {t1}│\n"
        f"│{t5} {ref} {t2}│\n"
        f"│{t4}     {t3}│\n"
        "└────────────┘"
    )
    return simbolo

# Entrada interactiva
ref = input("Referencia (ej. IC1): ")
t1 = input("Terminal 1 (max 3 chars, enter para omitir): ")
t2 = input("Terminal 2 (max 3 chars, enter para omitir): ")
t3 = input("Terminal 3 (max 3 chars, enter para omitir): ")
t4 = input("Terminal 4 (max 3 chars, enter para omitir): ")
t5 = input("Terminal 5 (max 3 chars, enter para omitir): ")
t6 = input("Terminal 6 (max 3 chars, enter para omitir): ")
    
# Mostrar el símbolo
print("\nSímbolo generado:\n")
print(generar_bloque_wirascii(ref, t1, t2, t3, t4, t5, t6))


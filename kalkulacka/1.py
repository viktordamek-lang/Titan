

# kalkulator nastaevuje funkci pro provádění základních matematických operací

def kalkulacka(cislo1, cislo2, operace):
    if operace == "+":
        return cislo1 + cislo2
    elif operace == "-":
        return cislo1 - cislo2
    elif operace == "*":
        return cislo1 * cislo2
    elif operace == "/":
        if cislo2 != 0:
            return cislo1 / cislo2
        else:
            return "Nelze dělit nulou"
    else:
        return "Neplatná operace"

# Získání vstupu od uživatele
cislo1 = float(input("Zadej první číslo: "))
cislo2 = float(input("Zadej druhé číslo: "))
operace = input("Zadej operaci (+, -, *, /): ")

# Zavolání funkce a výstup výsledku
vysledek = kalkulacka(cislo1, cislo2, operace)
print(f"Výsledek: {vysledek}")
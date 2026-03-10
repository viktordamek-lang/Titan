#karkulator 
1 = print ("Zadej první číslo: ")
2 = print ("Zadej druhé číslo: ")

# kalkulator 

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
4 = print ("Výsledek: ")


# ============================================
# JEDNODUCHÁ KALKULAČKA - Základní operace
# ============================================
# Tento skript implementuje jednoduchou kalkulačku,
# která dokáže provádět 4 základní matematické operace:
# sčítání (+), odčítání (-), násobení (*) a dělení (/)

def kalkulacka(cislo1, cislo2, operace):
    """
    Provede zadanou matematickou operaci na dvou číslech.
    
    Parametry:
    -----------
    cislo1 : float
        První číslo pro operaci (operand)
    cislo2 : float
        Druhé číslo pro operaci (operand)
    operace : str
        Operátor jako řetězec: "+", "-", "*" nebo "/"
        
    Návratová hodnota:
    -------------------
    float nebo str : Výsledek operace, nebo chybová zpráva
    """
    
    # SČÍTÁNÍ: cislo1 + cislo2
    if operace == "+":
        return cislo1 + cislo2
    
    # ODČÍTÁNÍ: cislo1 - cislo2
    elif operace == "-":
        return cislo1 - cislo2
    
    # NÁSOBENÍ: cislo1 * cislo2
    elif operace == "*":
        return cislo1 * cislo2
    
    # DĚLENÍ: cislo1 / cislo2
    # Speciální zpracování: Nelze dělit nulou! (matematická chyba)
    elif operace == "/":
        if cislo2 != 0:  # Ověření, že dělitel není nula
            return cislo1 / cislo2
        else:
            # Chybová zpráva když je cislo2 = 0
            return "Nelze dělit nulou"
    
    # DEFAULT: Pokud operace není z výše uvedených
    else:
        return "Neplatná operace"

# ============ HLAVNÍ PROGRAM ============
# Interaktivní získávání vstupu od uživatele

# Vstup #1: První číslo (uživatel zadá libovolné číslo)
cislo1 = float(input("Zadej první číslo: "))

# Vstup #2: Druhé číslo (uživatel zadá libovolné číslo)
cislo2 = float(input("Zadej druhé číslo: "))

# Vstup #3: Operátor (+, -, *, /)
# Uživatel si vybere operaci, kterou chce provést
operace = input("Zadej operaci (+, -, *, /): ")

# Zavolání funkce kalkulacka() se třemi vstupními parametry
# a uložení výsledku do proměnné vysledek
vysledek = kalkulacka(cislo1, cislo2, operace)

# Výstup: Zobrazení výsledku v přívětivém formátu
# f-string formátuje string s hodnotami z proměnných
print(f"Výsledek: {vysledek}")
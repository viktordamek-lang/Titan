#Prevodnik jednotek je program, který umožňuje převádět mezi různými jednotkami měření. Tento program může být užitečný pro studenty, vědce, inženýry nebo kohokoli, kdo potřebuje rychle převést jednotky bez nutnosti manuálního výpočtu.

def prevodnik_jednotek(jednotka_z, jednotka_do):
    # Definice převodních faktorů pro různé jednotky
    prevodni_faktory = {
        "m": 1,          # metr
        "cm": 0.01,      # centimetr
        "mm": 0.001,     # milimetr
        "km": 1000,      # kilometr
        "in": 0.0254,    # palec
        "ft": 0.3048,    # stopa
        "yd": 0.9144     # yard
    }
    
    if jednotka_z in prevodni_faktory and jednotka_do in prevodni_faktory:
        # Převodní faktor z jednotka_z na jednotka_do
        faktor = prevodni_faktory[jednotka_do] / prevodni_faktory[jednotka_z]
        return faktor
    else:
        return "Neplatné jednotky"
    
# Získání vstupu od uživatele
jednotka_z = input("Zadej jednotku, ze které chceš převést (m, cm, mm, km, in, ft, yd): ")
jednotka_do = input("Zadej jednotku, do které chceš převést (m, cm, mm, km, in, ft, yd): ")


# Zavolání funkce a výstup výsledku
vysledek = prevodnik_jednotek(jednotka_z, jednotka_do)
print(f"Výsledek: {vysledek}")
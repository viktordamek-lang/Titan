from ast import comprehension
from typing import List

# ==============================================================================
# ÚKOL 4: Filtrování dat a List Comprehension (Lekce N03, N15)
# ==============================================================================

class Zbozi:
    def __init__(self, nazev: str, cena: float):
        self.nazev = nazev
        self.cena = cena
        
    def __str__(self):
         return f"{self.nazev}: {self.cena:.0f} Kč"

def filtruj_a_zlevni(zbozi_list: List[Zbozi], max_cena: float, sleva_procenta: float) -> List[Zbozi]:
    """
    DOPLŇTE KÓD ZDE:
    Implementace přes jednu smyčku nebo pokročilou (list comprehension).
    Rozjeďte cyklus a zjistěte které instance `Zbozi` ze `zbozi_list` mají cenu <= `max_cena`.
    Najitým vítězům změňte jejich vnitřní cenu na novou poniženou (`z.cena = stará * procento..`).
    Následně metodu nechejte tyto vybrané produkty vrátit jako nový seznam instancí z funkce ven.
    """
    list = [Zbozi(z.nazev, z.cena * (1 - sleva_procenta / 100)) for z in zbozi_list if z.cena <= max_cena]  # <--- DOPLŇ ZDE
    return list 



# Testovací část pro spuštění
if __name__ == "__main__":
    sklad_zbozi = [
        Zbozi("Kniha Python", 600.0),
        Zbozi("Herní Klávesnice", 1200.0),
        Zbozi("Levná Myš", 400.0),
        Zbozi("Monitor 4K", 5000.0)
    ]

    print("--- 1. Původní Stav Zboží z databáze ---")
    for z in sklad_zbozi: print(z)

    print("\n--- 2. Po slevové akci: Hledáme do <1000 kč s 20% slevou ---")
    # Volání naplněné studentské funkce z Úkolu 4
    dostupne_zlevnene = filtruj_a_zlevni(sklad_zbozi, max_cena=1000.0, sleva_procenta=20.0)
    
    # Výsledek filtrace a slev
    if dostupne_zlevnene is None:
        print("Tvá funkce stále vrací starou prázdnou Nonehodnotu :)")
    else:
        for z in dostupne_zlevnene: print(z)

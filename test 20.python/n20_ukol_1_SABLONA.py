# ==============================================================================
# ÚKOL 1: Ošetření skladu (Lekce N05, N08)
# ==============================================================================

class NedostatekZboziError(Exception):
    """Vyvoláno, když na skladě není dostatek zboží pro odebrání."""
    pass 

class Zbozi:
    def __init__(self, nazev: str, cena: float, mnozstvi: int):
        self.nazev = nazev
        self.cena = cena
        self.__mnozstvi = mnozstvi

    @property
    def mnozstvi(self) -> int:
        return self.__mnozstvi

    def odeber(self, pocet: int) -> None:
        """Odebere zboží ze skladu.
        Args:
            pocet (int): Počet kusů, které se mají odebrat.
        Raises:
            NedostatekZboziError: Pokud není na skladě dostatek zboží.
        """


class Zbozi:
    def __init__(self, nazev: str, cena: float, mnozstvi: int):
        self.nazev = nazev
        self.cena = cena
        self.__mnozstvi = mnozstvi

    @property
    def mnozstvi(self) -> int:
        return self.__mnozstvi 
    
    

    def odeber(self, pocet: int) -> None: 
        """
        DOPLŇTE KÓD ZDE:
        Zkontrolujte, zda je množství na skladě větší nebo rovno parametru 'pocet'.
        Pokud není, tak vyhoďte výjimku NedostatekZboziError s varovnou textovou hláškou.
        V opačném případě, ponižte počty stavu self.__mnozstvi o hodnotu 'pocet'.
        """ 
        if self.__mnozstvi < pocet:
            raise NedostatekZboziError(f"Nedostatek zboží: Nelze odebrat {pocet} kusů, protože na skladě je pouze {self.__mnozstvi} kusů.")
        self.__mnozstvi -= pocet

# Testovací část pro spuštění
if __name__ == "__main__":
    notebook = Zbozi("Herní Notebook", 25000.0, 3)
    
    print(f"Původní stav notebooků: {notebook.mnozstvi} kusů")
    print("Odebírám 2 notebooky...")
    try:
        notebook.odeber(2)
        print(f"Úspěch! Nový zůstatek: {notebook.mnozstvi} kusů")
        
        print("\nOdebírám dalších 5 notebooků...")
        notebook.odeber(5)
    except NedostatekZboziError as e:
        print(f"BOMBA! Úspěšně zachycena výjimka z Úkolu 1: {e}") 
        

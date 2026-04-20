import asyncio

# ==============================================================================
# ÚKOL 5: Asynchronní smyčka a Event Loop (Lekce N20)
# ==============================================================================

async def over_dostupnost_api(nazev_produktu: str) -> bool:
    """
    Spící korutina pro simulaci sítě) asynchronně uspaná na 1 vteřinu.
    
    DOPLŇTE KÓD ZDE:
    Využijte příkazu z balíčku `asyncio`, který asynchronně čeká/uspává funkci na 1 sekundu.
    Nezapomeňte na odjišťovací klauzuli `await`! (Zakázáno použití blokujícího time.sleep).
    Vraťte pomocí returnu hodnotu 'True'.
    """
    await asyncio.sleep(1)
    return True 
  

async def asynchronni_test():
    """Hlavní async loop runner ze kterého startuje program."""
    print("Měřím čas prověrky [Očekávám, že 2 dotazy zaberou jen 1 vteřinu celkem!]\n")
    print("--- Start asynchronní prověrky dodavatelů ---")
    
    # 1. Tvorba nezávislých Tasků (Úloh spuštěných do pozadí)
    task1 = asyncio.create_task(over_dostupnost_api("Kniha Python"))
    task2 = asyncio.create_task(over_dostupnost_api("Klávesnice"))
    
    # 2. Asynchronní sběr všech paralelních výsledků z ringu
    vysledky = await asyncio.gather(task1, task2)
    
    # 3. Konec testování a zobrazení nasbíraných dat
    print(f"--- Asynchronní prověrka dokončena s daty: {vysledky} ---")

# Testovací část pro spuštění
if __name__ == "__main__":
    
    # Nastartování Event Loopu - tenhle příkaz "roztočí" asynchronní motor Pythonu
    asyncio.run(asynchronni_test())

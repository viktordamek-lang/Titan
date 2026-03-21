#jednoduchy chat bot 
import random
import string 
import os 
import sys 

# Tento jednoduchý chatbot je navržen tak, aby poskytoval uživatelům zábavné a užitečné funkce. Můžeš si se mnou povídat o své náladě, požádat mě o pomoc s jednoduchou matematikou, převodník jednotek nebo dokonce vygenerovat náhodné heslo. Stačí si vybrat, co bys chtěl dělat, a já ti rád pomohu!
print("Ahoj, já jsem jednoduchý chatbot. Jak se jmenuješ?")
jmeno = input("Zadej své jméno: ")
print(f"Rád tě poznávám, {jmeno}!")
# Tento chatbot nabízí několik funkcí, které mohou být užitečné pro různé situace. Můžeš si se mnou povídat o své náladě, požádat mě o pomoc s jednoduchou matematikou, převodník jednotek nebo dokonce vygenerovat náhodné heslo. Stačí si vybrat, co bys chtěl dělat, a já ti rád pomohu!
while True:
    print("\nCo bys chtěl, abych ti pomohl s?")
    print("1. Povídat si o náladě")
    print("2. Pomoc s matematikou")
    print("3. Převodník jednotek")
    print("4. Generování náhodného hesla")
    print("5. Konec")
    print("6. Hádání čísla")
    print("7. Generator vtipů")
    print("8. Datum a čas")
    print("9. Citát dnešního dne")
    print("10. Generator přezdívek")
    print("11. Počasí")
    volba = input("Vyber možnost (1-11): ")
     

    # Přidání možnosti pro povídání o náladě
    if volba == "1":
        print("Jak se dnes máš?")
        mood = input("Zadej, jak se dnes cítíš (dobře, špatně, unaveně, nadšeně): ") 
        if mood.lower() == "dobře":
            print("To je skvělé! Rád slyším, že se máš dobře.")
        elif mood.lower() == "špatně":
            print("To mě mrzí. Doufám, že se brzy budeš cítit lépe.")
        elif mood.lower() == "unaveně":
            print("To je normální. Někdy je důležité si odpočinout.")
        elif mood.lower() == "nadšeně":
            print("To je úžasné! Je skvělé být nadšený.")
        else:
            print("To je zajímavé! Každý se cítí jinak, a to je v pořádku.")
    

    # Přidání možnosti pro pomoc s matematikou
    elif volba == "2":
        print("Můžu ti pomoci s jednoduchou matematikou. Zadej dvě čísla a operaci (+, -, *, /): ")
        cislo1 = float(input("Zadej první číslo: "))
        cislo2 = float(input("Zadej druhé číslo: "))
        operation = input("Zadej operaci: ")
        if operation == "+":
            vysledek = cislo1 + cislo2
        elif operation == "-":
            vysledek = cislo1 - cislo2  
        elif operation == "*":
            vysledek = cislo1 * cislo2
        elif operation == "/":
            if cislo2 != 0:
                vysledek = cislo1 / cislo2
            else:
                vysledek = "Nelze dělit nulou"
        else:
            vysledek = "Neplatná operace"
        print(f"Výsledek: {vysledek}")
    

    # Přidání možnosti pro převodník jednotek
    elif volba == "3":
        print("Můžu ti pomoci s převodníkem jednotek.")
        jednotka_z = input("Zadej jednotku, ze které chceš převést (m, cm, mm, km, in, ft, yd): ")
        jednotka_do = input("Zadej jednotku, do které chceš převést (m, cm, mm, km, in, ft, yd): ")
        hodnota = float(input("Zadej hodnotu k převodu: "))
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
            faktor = prevodni_faktory[jednotka_do] / prevodni_faktory[jednotka_z]
            vysledek = hodnota * faktor
            print(f"{hodnota} {jednotka_z} = {vysledek} {jednotka_do}")
        else:
            print("Neplatné jednotky.")




    # Přidání možnosti pro generování náhodného hesla
    elif volba == "4":
        print("Můžu ti také pomoci vygenerovat náhodné heslo. Zadej délku hesla: ")
        delka_hesla = int(input("Zadej délku hesla: "))
        if delka_hesla > 0:
            znaky = string.ascii_letters + string.digits + string.punctuation
            heslo = ''.join(random.choice(znaky) for _ in range(delka_hesla))
            print(f"Vygenerované heslo: {heslo}")
        else:
            print("Délka hesla musí být kladné číslo.")
    

    # Přidání možnosti pro ukončení programu
    elif volba == "5":
        print("Nashledanou!")
        break
    
    # Přidání možnosti pro hádání čísla
    elif volba == "6":
        print("Můžu ti pomoci s hádáním čísla. Zadej rozsah (od - do): ")
        rozsah_od = int(input("Zadej začátek rozsahu: "))
        rozsah_do = int(input("Zadej konec rozsahu: "))
        if rozsah_od < rozsah_do:
            cislo_k_hadani = random.randint(rozsah_od, rozsah_do)
            print(f"Hádej číslo mezi {rozsah_od} a {rozsah_do}.")
            while True:
                hadani = int(input("Zadej své hádání: "))
                if hadani < cislo_k_hadani:
                    print("Příliš nízké, zkus to znovu.")
                elif hadani > cislo_k_hadani:
                    print("Příliš vysoké, zkus to znovu.")
                else:
                    print("Gratulace! Uhodl jsi číslo!")
                    break
        else:
            print("Neplatný rozsah. Začátek musí být menší než konec.")
    
    # Přidání možnosti pro generator vtipů
    elif volba == "7":
        vtipy = [
            "Proč programátoři nemohou řídit? Protože se bojí crashů.",
            "Jaký je rozdíl mezi programátorem a hackerem? Programátor píše kód, hacker ho zneužívá.",
            "Proč se programátoři nikdy nehádají? Protože vždycky najdou společný jazyk.",
            "Co řekl jeden programátor druhému? 'Máš nějaké bugy?'",
            "Proč programátoři nenosí hodinky? Protože čas je relativní."
        ]
        print(random.choice(vtipy))
    

    # Přidání možnosti pro zobrazení data a času
    elif volba == "8":
        import datetime
        print("Aktuální datum a čas: ", datetime.datetime.now())
    
    # Citát dnešního dne
    elif volba == "9":
        citaty = [
            "Život je jako jízda na kole. Abys udržel rovnováhu, musíš se pohybovat vpřed. - Albert Einstein",
            "Největší sláva není v tom, že nikdy nespadneme, ale v tom, že se vždy zvedneme. - Nelson Mandela",
            "Úspěch není konečný, neúspěch není fatální: je to odvaha pokračovat, co se počítá. - Winston Churchill",
            "Nejlepší způsob, jak předpovědět budoucnost, je ji vytvořit. - Peter Drucker",
            "Život je 10% toho, co se nám stane, a 90% toho, jak na to reagujeme. - Charles R. Swindoll"
        ]
        print(random.choice(citaty))
    
    # Generator přezdívek
    elif volba == "10":
        jmena = ["Rychlý", "Tichý", "Silný", "Moudrý", "Zábavný"]
        zvirata = ["Lev", "Tygr", "Medvěd", "Sova", "Delfín"]
        prezdivka = random.choice(jmena) + " " + random.choice(zvirata)
        print(f"Tvoje nová přezdívka je: {prezdivka}")
    
    # Přidání možnosti pro zobrazení aktuálního počasí
    elif volba == "11":
        import requests
        mesto = input("Zadej město pro zobrazení počasí: ")
        url = f"http://wttr.in/{mesto}?format=3"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print(f"Počasí: {response.text.strip()}")
            else:
                print("Nepodařilo se získat počasí pro zadané město.")
        except requests.RequestException:
            print("Chyba při připojování k počasí. Zkus to později.")
    
    else:
        print("Neplatná volba. Zkus to znovu.") 

    
    #prepinani mezi volba 1-11

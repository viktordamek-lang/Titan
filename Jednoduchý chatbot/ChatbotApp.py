# Jednoduchý Chatbot aplikace vytvořená pomocí Tkinter
# Tato aplikace nabízí různé funkce jako povídání o náladě, pomoc s matematikou,
# převodník jednotek, generování hesel, hádání čísel, generátor vtipů,
# zobrazení data a času, citát dne, generátor přezdívek, poznámkový blok,
# převodník měn, kalkulačka BMI, kámen-nůžky-papír, převodník teploty,
# hod kostkou, kalkulačka věku, náhodný fakt, počítadlo slov a Morseova abeceda.

# Import potřebných modulů
# tkinter - pro vytvoření grafického uživatelského rozhraní
# messagebox - pro zobrazování dialogových oken s informacemi/chybami
# random - pro generování náhodných čísel a výběrů
# string - pro práci se znaky při generování hesel
# datetime - pro získání aktuálního data a času
import tkinter as tk
from tkinter import messagebox
import random
import string
import datetime

# Třída pro hlavní aplikaci chatbota
class ChatbotApp:
    # Inicializační metoda pro nastavení hlavního okna a tlačítek
    # Parametr 'self' = instance třídy (objekt), 'root' = hlavní okno Tkinter
    def __init__(self, root):
        self.root = root  # Uložení reference na hlavní okno pro pozdější přístup
        self.root.title("Jednoduchý Chatbot")  # Nastavení titulku okna
        self.root.geometry("400x300")  # Nastavení rozměrů: šířka 400 pixelů, výška 300 pixelů

        # Vytvoření hlavního štítku s uvítáním
        # Label = statický textový prvek bez interakce (jen zobrazuje text)
        self.label = tk.Label(root, text="Ahoj! Vyber možnost:")
        # pack() = umísťuje widget do okna; pady = výška prázdného místa nad a pod prvkem
        self.label.pack(pady=10)

        # Tlačítka pro různé funkce chatbota - každé tlačítko volá odpovídající metodu
        # Button = interaktivní prvek; command = jaká funkce se spustí při kliknutí
        # text = popis zobrazený na tlačítku; command = self.mood_chat = volá metodu mood_chat
        self.button1 = tk.Button(root, text="1. Povídat si o náladě", command=self.mood_chat)
        # pack(fill=tk.X) = rozšíří tlačítko na plnou šířku okna
        # padx = vodorovný spacing (vlevo i vpravo), pady = svislý spacing
        self.button1.pack(fill=tk.X, padx=20, pady=2)

        self.button2 = tk.Button(root, text="2. Pomoc s matematikou", command=self.math_help)
        self.button2.pack(fill=tk.X, padx=20, pady=2)

        self.button3 = tk.Button(root, text="3. Převodník jednotek", command=self.unit_converter)
        self.button3.pack(fill=tk.X, padx=20, pady=2)

        self.button4 = tk.Button(root, text="4. Generování náhodného hesla", command=self.generate_password)
        self.button4.pack(fill=tk.X, padx=20, pady=2)

        self.button5 = tk.Button(root, text="5. Konec", command=self.quit_app)
        self.button5.pack(fill=tk.X, padx=20, pady=2)

        self.button6 = tk.Button(root, text="6. Hádání čísla", command=self.guess_number)
        self.button6.pack(fill=tk.X, padx=20, pady=2)

        self.button7 = tk.Button(root, text="7. Generator vtipů", command=self.joke_generator)
        self.button7.pack(fill=tk.X, padx=20, pady=2)

        self.button8 = tk.Button(root, text="8. Datum a čas", command=self.show_datetime)
        self.button8.pack(fill=tk.X, padx=20, pady=2)

        self.button9 = tk.Button(root, text="9. Citát dnešního dne", command=self.quote_of_day)
        self.button9.pack(fill=tk.X, padx=20, pady=2)

        self.button10 = tk.Button(root, text="10. Generator přezdívek", command=self.nickname_generator)
        self.button10.pack(fill=tk.X, padx=20, pady=2)

        self.button11 = tk.Button(root, text="11. Poznámkový blok", command=self.note_pad)
        self.button11.pack(fill=tk.X, padx=20, pady=2)

        self.button12 = tk.Button(root, text="12. Převodník měn", command=self.currency_converter)
        self.button12.pack(fill=tk.X, padx=20, pady=2)

        self.button13 = tk.Button(root, text="13. Kalkulačka BMI", command=self.bmi_calculator)
        self.button13.pack(fill=tk.X, padx=20, pady=2)

        self.button14 = tk.Button(root, text="14. Kámen-nůžky-papír", command=self.rock_paper_scissors)
        self.button14.pack(fill=tk.X, padx=20, pady=2)

        self.button15 = tk.Button(root, text="15. Převodník teploty", command=self.temperature_converter)
        self.button15.pack(fill=tk.X, padx=20, pady=2)

        self.button16 = tk.Button(root, text="16. Hod kostkou", command=self.roll_dice)
        self.button16.pack(fill=tk.X, padx=20, pady=2)

        self.button17 = tk.Button(root, text="17. Kalkulačka věku", command=self.age_calculator)
        self.button17.pack(fill=tk.X, padx=20, pady=2)

        self.button18 = tk.Button(root, text="18. Náhodný fakt", command=self.random_fact)
        self.button18.pack(fill=tk.X, padx=20, pady=2)

        self.button19 = tk.Button(root, text="19. Počítadlo slov", command=self.word_counter)
        self.button19.pack(fill=tk.X, padx=20, pady=2)

        self.button20 = tk.Button(root, text="20. Morseova abeceda", command=self.morse_code)
        self.button20.pack(fill=tk.X, padx=20, pady=2)

        self.button21 = tk.Button(root, text="21. Konec", command=self.quit_app)
        self.button21.pack(fill=tk.X, padx=20, pady=2)

    # Metoda pro povídání o náladě - otevře nové okno pro zadání nálady
    def mood_chat(self):
        # Vytvoření nového okna (Toplevel) pro dialog o náladě
        # Toplevel = nové samostatné okno (nie je to hlavní okno, ale vedlejší okno)
        mood_window = tk.Toplevel(self.root)
        mood_window.title("Povídání o náladě")
        mood_window.geometry("300x150")

        # Label = statický popisek "Jak se dnes máš?"
        tk.Label(mood_window, text="Jak se dnes máš?").pack(pady=10)
        # Entry = jednořádkové textové pole pro zadání nálady
        # Uživatel sem zadá slovo jako "dobře", "špatně", "unaveně" apod.
        mood_entry = tk.Entry(mood_window)  # Vstupní pole pro zadání nálady
        mood_entry.pack()

        # Vnitřní funkce (closure) pro zpracování odpovědi na náladu
        # Vnitřní funkce má přístup k proměnným vnější funkce (mood_entry)
        def submit_mood():
            mood = mood_entry.get().lower()  # Převedení na malá písmena pro snadnější porovnání
            # Podmíněné větvení pro různé nálady s odpovídajícími reakcemi
            if mood == "dobře":
                messagebox.showinfo("Odpověď", "To je skvělé! Rád slyším, že se máš dobře.")
            elif mood == "špatně":
                messagebox.showinfo("Odpověď", "To mě mrzí. Doufám, že se brzy budeš cítit lépe.")
            elif mood == "unaveně":
                messagebox.showinfo("Odpověď", "To je normální. Někdy je důležité si odpočinout.")
            elif mood == "nadšeně":
                messagebox.showinfo("Odpověď", "To je úžasné! Je skvělé být nadšený.")
            else:
                # Výchozí odpověď pro neznámé nálady
                messagebox.showinfo("Odpověď", "To je zajímavé! Každý se cítí jinak, a to je v pořádku.")
            mood_window.destroy()  # Zavření okna po odpovědi

        # Button = tlačítko "Odeslat" se spouští submit_mood
        tk.Button(mood_window, text="Odeslat", command=submit_mood).pack(pady=10)

    # Metoda pro pomoc s matematikou - jednoduchá kalkulačka
    def math_help(self):
        # Vytvoření nového okna (Toplevel) pro matematické výpočty
        math_window = tk.Toplevel(self.root)
        math_window.title("Pomoc s matematikou")
        math_window.geometry("300x200")

        tk.Label(math_window, text="Zadej první číslo:").pack()
        num1_entry = tk.Entry(math_window)
        num1_entry.pack()

        tk.Label(math_window, text="Zadej druhé číslo:").pack()
        num2_entry = tk.Entry(math_window)
        num2_entry.pack()

        tk.Label(math_window, text="Zadej operaci (+, -, *, /):").pack()
        op_entry = tk.Entry(math_window)
        op_entry.pack()

        # Vnitřní funkce pro provedení matematického výpočtu
        def calculate():
            try:
                # Převedení vstupů na float pro desetinná čísla
                num1 = float(num1_entry.get())
                num2 = float(num2_entry.get())
                op = op_entry.get()
                # Podmíněné větvení pro různé matematické operace
                if op == "+":
                    result = num1 + num2
                elif op == "-":
                    result = num1 - num2
                elif op == "*":
                    result = num1 * num2
                elif op == "/":
                    # Speciální kontrola pro dělení nulou
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        result = "Nelze dělit nulou"
                else:
                    # Výchozí případ pro neplatnou operaci
                    result = "Neplatná operace"
                messagebox.showinfo("Výsledek", f"Výsledek: {result}")
            except ValueError:
                # Zachycení chyby při neplatném vstupu (nečíselné hodnoty)
                messagebox.showerror("Chyba", "Zadej platná čísla.")
            math_window.destroy()  # Zavření okna po výpočtu

        tk.Button(math_window, text="Vypočítat", command=calculate).pack(pady=10)

    # Metoda pro převodník jednotek (délkové jednotky)
    def unit_converter(self):
        # Vytvoření nového okna (Toplevel) pro převod jednotek
        unit_window = tk.Toplevel(self.root)
        unit_window.title("Převodník jednotek")
        unit_window.geometry("300x200")

        tk.Label(unit_window, text="Jednotka z:").pack()
        from_unit = tk.Entry(unit_window)
        from_unit.pack()

        tk.Label(unit_window, text="Jednotka do:").pack()
        to_unit = tk.Entry(unit_window)
        to_unit.pack()

        tk.Label(unit_window, text="Hodnota:").pack()
        value_entry = tk.Entry(unit_window)
        value_entry.pack()

        # Vnitřní funkce pro převod mezi jednotkami
        def convert():
            try:
                val = float(value_entry.get())
                f_unit = from_unit.get()
                t_unit = to_unit.get()
                # Slovník (dict) = datová struktura pro mapování klíčů na hodnoty
                # {"m": 1, "cm": 0.01} = klíč je zkratka jednotky, hodnota je faktor
                # Každý faktor udává, kolik jednotek je v 1 metru (základní jednotka)
                factors = {"m": 1, "cm": 0.01, "mm": 0.001, "km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144}
                if f_unit in factors and t_unit in factors:
                    # Matematický vzorec: hodnota × (faktor_cílové / faktor_výchozí)
                    # Příklad: 100 cm do m = 100 × (1 / 0.01) = 100 × 100 = 1 m
                    result = val * factors[t_unit] / factors[f_unit]
                    messagebox.showinfo("Výsledek", f"{val} {f_unit} = {result} {t_unit}")
                else:
                    # Pokud jednotka není v slovníku, zobrazí chybu
                    messagebox.showerror("Chyba", "Neplatné jednotky.")
            except ValueError:
                # Zachycení chyby při neplatném číselném vstupu (uživatel zadal text místo čísla)
                messagebox.showerror("Chyba", "Zadej platnou hodnotu.")
            unit_window.destroy()  # Zavření okna po převodu

        tk.Button(unit_window, text="Převést", command=convert).pack(pady=10)

    # Metoda pro generování náhodného hesla
    def generate_password(self):
        # Vytvoření nového okna (Toplevel) pro generování hesla
        pass_window = tk.Toplevel(self.root)
        pass_window.title("Generování hesla")
        pass_window.geometry("300x150")

        tk.Label(pass_window, text="Délka hesla:").pack()
        length_entry = tk.Entry(pass_window)
        length_entry.pack()

        # Vnitřní funkce pro generování bezpečného hesla
        def generate():
            try:
                length = int(length_entry.get())
                if length > 0:
                    # Sestavení znakové sady: písmena + číslice + speciální znaky
                    # string.ascii_letters = "abcdefgh...zABCDEFGH...Z"
                    # string.digits = "0123456789"
                    # string.punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
                    chars = string.ascii_letters + string.digits + string.punctuation
                    # List comprehension: [random.choice(chars) for _ in range(length)]
                    # Vytvoří list náhodných znaků délky 'length'
                    # ''.join(...) = spojí seznam znaků do jednoho řetězce bez separátoru
                    pwd = ''.join(random.choice(chars) for _ in range(length))
                    messagebox.showinfo("Heslo", f"Vygenerované heslo: {pwd}")
                else:
                    messagebox.showerror("Chyba", "Délka musí být kladná.")
            except ValueError:
                # Zachycení chyby při neplatném číselném vstupu
                messagebox.showerror("Chyba", "Zadej číslo.")
            pass_window.destroy()  # Zavření okna po generování

        tk.Button(pass_window, text="Generovat", command=generate).pack(pady=10)

    # Metoda pro ukončení aplikace
    def quit_app(self):
        self.root.quit()

    # Metoda pro hru hádání čísla
    def guess_number(self):
        # Vytvoření nového okna (Toplevel) pro nastavení parametrů hry
        guess_window = tk.Toplevel(self.root)
        guess_window.title("Hádání čísla")
        guess_window.geometry("300x200")

        tk.Label(guess_window, text="Začátek rozsahu:").pack()
        start_entry = tk.Entry(guess_window)
        start_entry.pack()

        tk.Label(guess_window, text="Konec rozsahu:").pack()
        end_entry = tk.Entry(guess_window)
        end_entry.pack()

        # Vnitřní funkce pro inicializaci hry
        def start_game():
            try:
                start = int(start_entry.get())
                end = int(end_entry.get())
                if start < end:
                    # Generování náhodného čísla v zadaném rozsahu (včetně konců)
                    self.target = random.randint(start, end)
                    messagebox.showinfo("Začátek", f"Hádej číslo mezi {start} a {end}.")
                    self.guess_input(guess_window)  # Přechod na fázi hádání
                else:
                    messagebox.showerror("Chyba", "Neplatný rozsah.")
            except ValueError:
                messagebox.showerror("Chyba", "Zadej čísla.")

        tk.Button(guess_window, text="Začít", command=start_game).pack(pady=10)

    # Pomocná metoda pro zadávání hádání v hře (iterativní proces)
    def guess_input(self, window):
        # Vytvoření nového okna pro každé kolo hádání
        input_window = tk.Toplevel(window)
        input_window.title("Hádej")
        input_window.geometry("200x100")

        tk.Label(input_window, text="Zadej hádání:").pack()
        guess_entry = tk.Entry(input_window)
        guess_entry.pack()

        # Vnitřní funkce pro vyhodnocení hádání
        def check_guess():
            try:
                guess = int(guess_entry.get())
                # Logika hry: porovnání s uloženým cílovým číslem
                if guess < self.target:
                    messagebox.showinfo("Tip", "Příliš nízké.")
                    input_window.destroy()  # Zavření okna pro další pokus
                    # Rekurze = funkce volá sama sebe (self.guess_input)
                    # Umožňuje nekonečné hádání, dokud se neuhodne správné číslo
                    self.guess_input(window)  # Rekurzivní volání pro nové hádání
                elif guess > self.target:
                    messagebox.showinfo("Tip", "Příliš vysoké.")
                    input_window.destroy()
                    self.guess_input(window)  # Rekurze pro další pokus
                else:
                    # Výhra - konec hry
                    messagebox.showinfo("Výhra", "Gratulace! Uhodl jsi.")
                    input_window.destroy()
                    window.destroy()  # Zavření všech oken hry
            except ValueError:
                messagebox.showerror("Chyba", "Zadej číslo.")

        tk.Button(input_window, text="Hádej", command=check_guess).pack()

    # Metoda pro generování náhodného vtipu
    def joke_generator(self):
        # Seznam (list) = datová struktura pro ukládání více položek
        # Každá položka je řetězec (string) = jeden vtip
        jokes = [
            "Proč programátoři nemohou řídit? Protože se bojí crashů.",
            "Jaký je rozdíl mezi programátorem a hackerem? Programátor píše kód, hacker ho zneužívá.",
            "Proč se programátoři nikdy nehádají? Protože vždycky najdou společný jazyk.",
            "Co řekl jeden programátor druhému? 'Máš nějaké bugy?'",
            "Proč programátoři nenosí hodinky? Protože čas je relativní."
        ]
        # random.choice(jokes) = vybere náhodně jeden prvek ze seznamu
        messagebox.showinfo("Vtip", random.choice(jokes))

    # Metoda pro zobrazení aktuálního data a času
    def show_datetime(self):
        # datetime.datetime.now() = vrátí aktuální datum a čas
        # Formát: YYYY-MM-DD HH:MM:SS.ffffff (rok-měsíc-den hodina:minuta:sekunda.mikrosekunda)
        now = datetime.datetime.now()
        messagebox.showinfo("Datum a čas", f"Aktuální: {now}")

    # Metoda pro zobrazení náhodného citátu dne
    def quote_of_day(self):
        # Seznam motivujících citátů pro inspiraci
        # Každý citát je řetězec (string) s motivujícím příkazem
        quotes = [
            "Život je jako jízda na kole. Abys udržel rovnováhu, musíš se pohybovat vpřed. - Albert Einstein",
            "Největší sláva není v tom, že nikdy nespadneme, ale v tom, že se vždy zvedneme. - Nelson Mandela",
            "Úspěch není konečný, neúspěch není fatální: je to odvaha pokračovat, co se počítá. - Winston Churchill",
            "Nejlepší způsob, jak předpovědět budoucnost, je ji vytvořit. - Peter Drucker",
            "Život je 10% toho, co se nám stane, a 90% toho, jak na to reagujeme. - Charles R. Swindoll"
        ]
        # random.choice(quotes) = vybere náhodně jeden citát ze seznamu
        messagebox.showinfo("Citát", random.choice(quotes))

    # Metoda pro generování náhodné přezdívky
    def nickname_generator(self):
        # Seznamy pro generování přezdívek: adjektiva a zvířata
        names = ["Rychlý", "Tichý", "Silný", "Moudrý", "Zábavný"]
        animals = ["Lev", "Tygr", "Medvěd", "Sova", "Delfín"]
        # Sestavení přezdívky kombinací náhodného adjektiva a zvířete
        nick = random.choice(names) + " " + random.choice(animals)
        messagebox.showinfo("Přezdívka", f"Tvoje přezdívka: {nick}")

    # Metoda pro poznámkový blok - jednoduchý textový editor s ukládáním
    def note_pad(self):
        # Vytvoření nového okna (Toplevel) pro poznámkový blok
        note_window = tk.Toplevel(self.root)
        note_window.title("Poznámkový blok")
        note_window.geometry("400x300")

        tk.Label(note_window, text="Napiš své poznámky:").pack(pady=5)
        # Text = víceřádkové textové pole (na rozdíl od Entry, které je jednohodé)
        # height = počet viditelných řádků, width = počet znaků na řádku (přibližně)
        # Widget Text umožňuje psaní několika řádků textu
        text_area = tk.Text(note_window, height=10, width=40)
        text_area.pack(pady=5)

        # Vnitřní funkce pro uložení poznámek do textového souboru
        def save_notes():
            # get("1.0", tk.END) = Get: "1.0" = řádek 1, znak 0 (začátek); tk.END = konec
            # strip() = odstraní bílé znaky na začátku a konci
            notes = text_area.get("1.0", tk.END).strip()  # Získání textu od začátku do konce
            if notes:
                # open(...) = otevře/vytvoří soubor; "w" = write (zápis), encoding="utf-8" = pro české znaky
                with open("poznamky.txt", "w", encoding="utf-8") as f:
                    f.write(notes)
                messagebox.showinfo("Uloženo", "Poznámky byly uloženy do souboru poznamky.txt")
            else:
                messagebox.showwarning("Prázdné", "Žádné poznámky k uložení.")

        # Vnitřní funkce pro načtení poznámek ze souboru
        def load_notes():
            try:
                # open(...) = otevře soubor; "r" = read (čtení)
                with open("poznamky.txt", "r", encoding="utf-8") as f:
                    notes = f.read()  # read() = přečte celý obsah souboru
                # delete("1.0", tk.END) = vymaže všechen text z pozic 1.0 do konce
                text_area.delete("1.0", tk.END)  # Vymazání aktuálního obsahu
                # insert("1.0", notes) = vloží text na pozici 1.0 (začátek)
                text_area.insert("1.0", notes)  # Vložení načteného textu
                messagebox.showinfo("Načteno", "Poznámky byly načteny ze souboru.")
            except FileNotFoundError:
                # Ošetření chyby, když soubor neexistuje
                messagebox.showwarning("Neexistuje", "Soubor s poznámkami neexistuje.")

        # Tlačítka pro uložení a načtení poznámek
        # side=tk.LEFT = umísťuje button vlevo; side=tk.RIGHT = umísťuje vpravo
        # padx = vodorovný spacing (vlevo-vpravo), pady = svislý spacing (nahoře-dole)
        tk.Button(note_window, text="Uložit poznámky", command=save_notes).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(note_window, text="Načíst poznámky", command=load_notes).pack(side=tk.RIGHT, padx=10, pady=10)

    # Metoda pro převodník měn (jednoduchý s pevnými kurzy)
    def currency_converter(self):
        # Vytvoření nového okna (Toplevel) pro převod měn
        currency_window = tk.Toplevel(self.root)
        currency_window.title("Převodník měn")
        currency_window.geometry("300x200")

        tk.Label(currency_window, text="Částka v CZK:").pack()
        amount_entry = tk.Entry(currency_window)
        amount_entry.pack()

        tk.Label(currency_window, text="Cílová měna (EUR/USD/GBP):").pack()
        currency_entry = tk.Entry(currency_window)
        currency_entry.pack()

        # Vnitřní funkce pro převod měn
        def convert_currency():
            try:
                amount = float(amount_entry.get())
                currency = currency_entry.get().upper()  # Převedení na velká písmena
                # Přibližné kurzy vůči CZK (v reálné aplikaci by se aktualizovaly z API)
                rates = {"EUR": 0.04, "USD": 0.045, "GBP": 0.038}
                if currency in rates:
                    # Výpočet: částka × kurz
                    result = amount * rates[currency]
                    msg = f"{amount} CZK = {result:.2f} {currency}"
                    messagebox.showinfo("Výsledek", msg)
                else:
                    messagebox.showerror("Chyba", "Nepodporovaná měna. Použij EUR, USD nebo GBP.")
            except ValueError:
                messagebox.showerror("Chyba", "Zadej platnou částku.")
            currency_window.destroy()  # Zavření okna po převodu

        tk.Button(currency_window, text="Převést", command=convert_currency).pack(pady=10)

    # Metoda pro kalkulačku BMI (Body Mass Index)
    def bmi_calculator(self):
        # Vytvoření nového okna (Toplevel) pro výpočet BMI
        bmi_window = tk.Toplevel(self.root)
        bmi_window.title("Kalkulačka BMI")
        bmi_window.geometry("300x200")

        tk.Label(bmi_window, text="Váha (kg):").pack()
        weight_entry = tk.Entry(bmi_window)
        weight_entry.pack()

        tk.Label(bmi_window, text="Výška (cm):").pack()
        height_entry = tk.Entry(bmi_window)
        height_entry.pack()

        # Vnitřní funkce pro výpočet BMI a kategorizaci
        def calculate_bmi():
            try:
                weight = float(weight_entry.get())
                height = float(height_entry.get()) / 100  # Převod cm na metry
                if weight > 0 and height > 0:
                    # Standardní vzorec BMI: váha / (výška)^2
                    bmi = weight / (height ** 2)
                    # Kategorizace podle WHO standardů
                    if bmi < 18.5:
                        category = "Podváha"
                    elif 18.5 <= bmi < 25:
                        category = "Normální váha"
                    elif 25 <= bmi < 30:
                        category = "Nadváha"
                    else:
                        category = "Obezita"
                    msg = f"BMI: {bmi:.2f}\nKategorie: {category}"
                    messagebox.showinfo("BMI", msg)
                else:
                    messagebox.showerror("Chyba", "Zadej kladné hodnoty.")
            except ValueError:
                messagebox.showerror("Chyba", "Zadej platná čísla.")
            bmi_window.destroy()  # Zavření okna po výpočtu

        tk.Button(bmi_window, text="Vypočítat BMI", command=calculate_bmi).pack(pady=10)

    # Metoda pro hru kámen-nůžky-papír proti počítači
    def rock_paper_scissors(self):
        # Vytvoření nového okna (Toplevel) pro hru
        game_window = tk.Toplevel(self.root)
        game_window.title("Kámen-nůžky-papír")
        game_window.geometry("300x200")

        tk.Label(game_window, text="Vyber svou volbu:").pack(pady=10)

        # Vnitřní funkce pro logiku hry
        # Parameter 'choice' = co si uživatel vybral (\"kámen\", \"nůžky\" nebo \"papír\")
        def play(choice):
            choices = ["kámen", "nůžky", "papír"]
            # random.choice(choices) = počítač si vybere náhodně jednu z tří možností
            computer_choice = random.choice(choices)  # Náhodný výběr počítače
            user_choice = choice

            # Logika hry: kámen > nůžky > papír > kámen (cyklus)
            # Pravidla:
            # - Kámen drtí nůžky (kámen vyhraje)
            # - Nůžky stříhají papír (nůžky vyhrají)
            # - Papír zabaluje kámen (papír vyhraje)
            if user_choice == computer_choice:
                result = "Remíza!"
            elif (user_choice == "kámen" and computer_choice == "nůžky") or \
                 (user_choice == "nůžky" and computer_choice == "papír") or \
                 (user_choice == "papír" and computer_choice == "kámen"):
                result = "Vyhrál jsi!"
            else:
                result = "Prohrál jsi!"

            messagebox.showinfo("Výsledek", f"Ty: {user_choice}\nPočítač: {computer_choice}\n{result}")
            game_window.destroy()  # Zavření okna po hře

        # Tlačítka pro výběr - používá lambda pro předání parametru
        # lambda = anonymní funkce; lambda: play("kámen") = vytvoří funkci,
        # která zavolá play("kámen") když se tlačítko klikne
        # Bez lambda by command=play("kámen") vyvolal play hned (při vytváření tlačítka), ne až po kliknutí
        tk.Button(game_window, text="Kámen", command=lambda: play("kámen")).pack(fill=tk.X, padx=20, pady=2)
        tk.Button(game_window, text="Nůžky", command=lambda: play("nůžky")).pack(fill=tk.X, padx=20, pady=2)
        tk.Button(game_window, text="Papír", command=lambda: play("papír")).pack(fill=tk.X, padx=20, pady=2)

    # Metoda pro převodník teploty mezi stupni Celsia, Fahrenheita a Kelvina
    def temperature_converter(self):
        # Vytvoření nového okna (Toplevel) pro převod teploty
        # Tři temperaturní stupnice: °C (Celsius), °F (Fahrenheit), K (Kelvin)
        temp_window = tk.Toplevel(self.root)
        temp_window.title("Převodník teploty")
        temp_window.geometry("300x200")

        tk.Label(temp_window, text="Teplota:").pack()
        temp_entry = tk.Entry(temp_window)
        temp_entry.pack()

        tk.Label(temp_window, text="Z jednotky (C/F/K):").pack()
        from_unit = tk.Entry(temp_window)
        from_unit.pack()

        tk.Label(temp_window, text="Do jednotky (C/F/K):").pack()
        to_unit = tk.Entry(temp_window)
        to_unit.pack()

        # Vnitřní funkce pro převod teploty
        def convert_temp():
            try:
                temp = float(temp_entry.get())
                f_unit = from_unit.get().upper()
                t_unit = to_unit.get().upper()

                # Převod NA Kelvin jako mezikrok (absolutní nula = 0 K = -273.15 °C)
                # Kelvin je absolutní temperaturní stupnice, která začíná v absolutní nule
                # Všechny stupnice se převádějí přes Kelvin pro přesnost
                if f_unit == "C":
                    # Celsia na Kelvin: K = °C + 273.15
                    kelvin = temp + 273.15  # Celsia na Kelvin
                elif f_unit == "F":
                    # Fahrenheita na Kelvin: K = (°F - 32) × 5/9 + 273.15
                    kelvin = (temp - 32) * 5/9 + 273.15  # Fahrenheita na Kelvin
                elif f_unit == "K":
                    kelvin = temp  # Už je v Kelvinech
                else:
                    raise ValueError("Neplatná jednotka")

                # Převod Z Kelvina na cílovou jednotku
                if t_unit == "C":
                    # Kelvin na Celsia: °C = K - 273.15
                    result = kelvin - 273.15  # Kelvin na Celsia
                elif t_unit == "F":
                    # Kelvin na Fahrenheita: °F = (K - 273.15) × 9/5 + 32
                    result = (kelvin - 273.15) * 9/5 + 32  # Kelvin na Fahrenheita
                elif t_unit == "K":
                    result = kelvin  # Už je v Kelvinech
                else:
                    raise ValueError("Neplatná jednotka")

                result_msg = f"{temp}°{f_unit} = {result:.2f}°{t_unit}"
                messagebox.showinfo("Výsledek", result_msg)
            except ValueError as e:
                # Ošetření chyby - buď neplatná jednotka, nebo neplatn číselo
                messagebox.showerror("Chyba", str(e) if "Neplatná" in str(e) else "Zadej platné hodnoty.")
            temp_window.destroy()  # Zavření okna po převodu

        tk.Button(temp_window, text="Převést", command=convert_temp).pack(pady=10)

    # Metoda pro hod kostkou
    def roll_dice(self):
        # Generování náhodného čísla od 1 do 6 (jako standardní kostka)
        dice = random.randint(1, 6)
        messagebox.showinfo("Kostka", f"Hodil jsi: {dice}")

    # Metoda pro kalkulačku věku
    def age_calculator(self):
        age_window = tk.Toplevel(self.root)
        age_window.title("Kalkulačka věku")
        age_window.geometry("300x200")

        tk.Label(age_window, text="Rok narození:").pack()
        year_entry = tk.Entry(age_window)
        year_entry.pack()

        tk.Label(age_window, text="Měsíc narození:").pack()
        month_entry = tk.Entry(age_window)
        month_entry.pack()

        tk.Label(age_window, text="Den narození:").pack()
        day_entry = tk.Entry(age_window)
        day_entry.pack()

        def calculate_age():
            try:
                birth_year = int(year_entry.get())
                birth_month = int(month_entry.get())
                birth_day = int(day_entry.get())
                
                today = datetime.date.today()  # Získání dnešního data
                birth_date = datetime.date(birth_year, birth_month, birth_day)  # Vytvoření data narození
                
                # Výpočet věku: rozdíl let minus 1, pokud ještě neproběhly narozeniny v tomto roce
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                messagebox.showinfo("Věk", f"Máš {age} let.")
            except ValueError:
                messagebox.showerror("Chyba", "Zadej platné datum.")
            age_window.destroy()

        tk.Button(age_window, text="Vypočítat věk", command=calculate_age).pack(pady=10)

    # Metoda pro náhodný fakt
    def random_fact(self):
        # Seznam zajímavých faktů pro zobrazení
        facts = [
            "Včely mohou rozpoznat lidské tváře.",
            "Sloni jsou jediná zvířata, která nemohou skákat.",
            "Vesmír se rozpíná rychleji, než světlo.",
            "Lidské tělo má více bakterií než buněk.",
            "Žraloci existují déle než stromy.",
            "Měsíc se vzdaluje od Země rychlostí 3.8 cm za rok.",
            "Voda může být teplejší než led, ale stále zamrzat.",
            "Lidské srdce bije asi 100 000 krát za den.",
            "Hvězda Betelgeuse je tak velká, že by se vešla mezi Slunce a Jupiter.",
            "Med nikdy neexpiruje."
        ]
        # Výběr náhodného faktu ze seznamu
        messagebox.showinfo("Náhodný fakt", random.choice(facts))

    # Metoda pro počítadlo slov
    def word_counter(self):
        word_window = tk.Toplevel(self.root)
        word_window.title("Počítadlo slov")
        word_window.geometry("400x300")

        tk.Label(word_window, text="Zadej text:").pack(pady=5)
        text_area = tk.Text(word_window, height=10, width=40)
        text_area.pack(pady=5)

        def count_words():
            text = text_area.get("1.0", tk.END).strip()  # Získání textu z textového pole
            words = len(text.split()) if text else 0  # Počet slov (rozdělení podle mezer)
            chars = len(text)  # Počet znaků včetně mezer
            lines = len(text.split('\n')) if text else 0  # Počet řádků (rozdělení podle nových řádků)
            messagebox.showinfo("Počet", f"Slova: {words}\nZnaky: {chars}\nŘádky: {lines}")

        tk.Button(word_window, text="Spočítat", command=count_words).pack(pady=10)

    # Metoda pro Morseovu abecedu
    def morse_code(self):
        morse_window = tk.Toplevel(self.root)
        morse_window.title("Morseova abeceda")
        morse_window.geometry("400x300")

        tk.Label(morse_window, text="Zadej text:").pack()
        text_entry = tk.Entry(morse_window, width=40)
        text_entry.pack()

        # Slovník mapující písmena a číslice na Morseovy kódy
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.', ' ': '/'
        }

        def to_morse():
            text = text_entry.get().upper()  # Převedení na velká písmena pro mapování
            morse = []
            for char in text:
                if char in morse_dict:
                    morse.append(morse_dict[char])  # Přidání Morseova kódu pro znak
                else:
                    morse.append('?')  # Neznámý znak
            result = ' '.join(morse)  # Spojení kódů mezerami
            messagebox.showinfo("Morseův kód", result)

        tk.Button(morse_window, text="Převést na Morseův kód", command=to_morse).pack(pady=10)

    # Metoda pro ukončení aplikace
    def quit_app(self):
        self.root.quit()  # Ukončení hlavní smyčky Tkinter aplikace

 
# Hlavní blok pro spuštění aplikace
if __name__ == "__main__":
    # __name__ == "__main__" znamená, že skript běží přímo (ne importován z jiného souboru)
    # Vytvoření instance hlavního okna Tkinter aplikace
    root = tk.Tk()  # tk.Tk() = vytvoří hlavní okno aplikace
    # Inicializace instance ChatbotApp s předáním hlavního okna
    app = ChatbotApp(root)  # Vytvoří objekt ChatbotApp a nastaví všechna tlačítka
    # Spuštění hlavní smyčky aplikace - čeká na události a udržuje okno otevřené
    root.mainloop()  # Spustí event loop, který čeká na uživatelské akce
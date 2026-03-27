# Jednoduchý Chatbot aplikace vytvořená pomocí Tkinter
# Tato aplikace nabízí různé funkce jako povídání o náladě, pomoc s matematikou,
# převodník jednotek, generování hesel, hádání čísel, generátor vtipů,
# zobrazení data a času, citát dne, generátor přezdívek, poznámkový blok,
# převodník měn, kalkulačka BMI, kámen-nůžky-papír a převodník teploty.

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
    def __init__(self, root):
        self.root = root
        self.root.title("Jednoduchý Chatbot")
        self.root.geometry("400x300")

        # Vytvoření hlavního štítku s uvítáním
        self.label = tk.Label(root, text="Ahoj! Vyber možnost:")
        self.label.pack(pady=10)

        # Tlačítka pro různé funkce chatbota - každé tlačítko volá odpovídající metodu
        self.button1 = tk.Button(root, text="1. Povídat si o náladě", command=self.mood_chat)
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

        self.button16 = tk.Button(root, text="16. Konec", command=self.quit_app)
        self.button16.pack(fill=tk.X, padx=20, pady=2)

    # Metoda pro povídání o náladě - otevře nové okno pro zadání nálady
    def mood_chat(self):
        # Vytvoření nového okna (Toplevel) pro dialog o náladě
        mood_window = tk.Toplevel(self.root)
        mood_window.title("Povídání o náladě")
        mood_window.geometry("300x150")

        tk.Label(mood_window, text="Jak se dnes máš?").pack(pady=10)
        mood_entry = tk.Entry(mood_window)  # Vstupní pole pro zadání nálady
        mood_entry.pack()

        # Vnitřní funkce (closure) pro zpracování odpovědi na náladu
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
                # Slovník s faktory převodu na základní jednotku (metry)
                # Každý faktor udává, kolik jednotek je v 1 metru
                factors = {"m": 1, "cm": 0.01, "mm": 0.001, "km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144}
                if f_unit in factors and t_unit in factors:
                    # Matematický vzorec: hodnota × (faktor_cílové / faktor_výchozí)
                    result = val * factors[t_unit] / factors[f_unit]
                    messagebox.showinfo("Výsledek", f"{val} {f_unit} = {result} {t_unit}")
                else:
                    messagebox.showerror("Chyba", "Neplatné jednotky.")
            except ValueError:
                # Zachycení chyby při neplatném číselném vstupu
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
                    chars = string.ascii_letters + string.digits + string.punctuation
                    # Generování hesla pomocí list comprehension a random.choice
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
                    self.guess_input(window)  # Rekurzivní volání pro nové hádání
                elif guess > self.target:
                    messagebox.showinfo("Tip", "Příliš vysoké.")
                    input_window.destroy()
                    self.guess_input(window)
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
        # Seznam předpřipravených programátorských vtipů
        jokes = [
            "Proč programátoři nemohou řídit? Protože se bojí crashů.",
            "Jaký je rozdíl mezi programátorem a hackerem? Programátor píše kód, hacker ho zneužívá.",
            "Proč se programátoři nikdy nehádají? Protože vždycky najdou společný jazyk.",
            "Co řekl jeden programátor druhému? 'Máš nějaké bugy?'",
            "Proč programátoři nenosí hodinky? Protože čas je relativní."
        ]
        # Náhodný výběr vtipu ze seznamu
        messagebox.showinfo("Vtip", random.choice(jokes))

    # Metoda pro zobrazení aktuálního data a času
    def show_datetime(self):
        # Získání aktuálního data a času pomocí datetime modulu
        now = datetime.datetime.now()
        messagebox.showinfo("Datum a čas", f"Aktuální: {now}")

    # Metoda pro zobrazení náhodného citátu dne
    def quote_of_day(self):
        # Seznam motivujících citátů pro inspiraci
        quotes = [
            "Život je jako jízda na kole. Abys udržel rovnováhu, musíš se pohybovat vpřed. - Albert Einstein",
            "Největší sláva není v tom, že nikdy nespadneme, ale v tom, že se vždy zvedneme. - Nelson Mandela",
            "Úspěch není konečný, neúspěch není fatální: je to odvaha pokračovat, co se počítá. - Winston Churchill",
            "Nejlepší způsob, jak předpovědět budoucnost, je ji vytvořit. - Peter Drucker",
            "Život je 10% toho, co se nám stane, a 90% toho, jak na to reagujeme. - Charles R. Swindoll"
        ]
        # Náhodný výběr citátu
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
        # Víceřádkové textové pole pro zadávání poznámek
        text_area = tk.Text(note_window, height=10, width=40)
        text_area.pack(pady=5)

        # Vnitřní funkce pro uložení poznámek do textového souboru
        def save_notes():
            notes = text_area.get("1.0", tk.END).strip()  # Získání textu od začátku do konce
            if notes:
                # Uložení do souboru s kódováním UTF-8 pro české znaky
                with open("poznamky.txt", "w", encoding="utf-8") as f:
                    f.write(notes)
                messagebox.showinfo("Uloženo", "Poznámky byly uloženy do souboru poznamky.txt")
            else:
                messagebox.showwarning("Prázdné", "Žádné poznámky k uložení.")

        # Vnitřní funkce pro načtení poznámek ze souboru
        def load_notes():
            try:
                # Načtení ze souboru s kódováním UTF-8
                with open("poznamky.txt", "r", encoding="utf-8") as f:
                    notes = f.read()
                text_area.delete("1.0", tk.END)  # Vymazání aktuálního obsahu
                text_area.insert("1.0", notes)  # Vložení načteného textu
                messagebox.showinfo("Načteno", "Poznámky byly načteny ze souboru.")
            except FileNotFoundError:
                messagebox.showwarning("Neexistuje", "Soubor s poznámkami neexistuje.")

        # Tlačítka pro uložení a načtení poznámek
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
                    messagebox.showinfo("Výsledek", ".2f")
                else:
                    messagebox.showerror("Chyba", "Nepodporovaná měna. Použij EUR, USD nebo GBP.")
            except ValueError:
                messagebox.showerror("Chyba", "Zadej platnou částku.")
            currency_window.destroy()  # Zavření okna po převodu
                    result = amount * rates[currency]
                    messagebox.showinfo("Výsledek", ".2f")
                else:
                    messagebox.showerror("Chyba", "Nepodporovaná měna. Použij EUR, USD nebo GBP.")
            except ValueError:
                messagebox.showerror("Chyba", "Zadej platnou částku.")
            currency_window.destroy()

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
                    messagebox.showinfo("BMI", ".2f")
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
        def play(choice):
            choices = ["kámen", "nůžky", "papír"]
            computer_choice = random.choice(choices)  # Náhodný výběr počítače
            user_choice = choice

            # Logika hry: kámen > nůžky > papír > kámen
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
        tk.Button(game_window, text="Kámen", command=lambda: play("kámen")).pack(fill=tk.X, padx=20, pady=2)
        tk.Button(game_window, text="Nůžky", command=lambda: play("nůžky")).pack(fill=tk.X, padx=20, pady=2)
        tk.Button(game_window, text="Papír", command=lambda: play("papír")).pack(fill=tk.X, padx=20, pady=2)

    # Metoda pro převodník teploty mezi stupni Celsia, Fahrenheita a Kelvina
    def temperature_converter(self):
        # Vytvoření nového okna (Toplevel) pro převod teploty
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

                # Převod na Kelvin jako mezikrok (absolutní nula = 0 K)
                if f_unit == "C":
                    kelvin = temp + 273.15  # Celsia na Kelvin
                elif f_unit == "F":
                    kelvin = (temp - 32) * 5/9 + 273.15  # Fahrenheita na Kelvin
                elif f_unit == "K":
                    kelvin = temp  # Už je v Kelvinech
                else:
                    raise ValueError("Neplatná jednotka")

                # Převod z Kelvin na cílovou jednotku
                if t_unit == "C":
                    result = kelvin - 273.15  # Kelvin na Celsia
                elif t_unit == "F":
                    result = (kelvin - 273.15) * 9/5 + 32  # Kelvin na Fahrenheita
                elif t_unit == "K":
                    result = kelvin  # Už je v Kelvinech
                else:
                    raise ValueError("Neplatná jednotka")

                messagebox.showinfo("Výsledek", ".2f")
            except ValueError as e:
                messagebox.showerror("Chyba", str(e) if "Neplatná" in str(e) else "Zadej platné hodnoty.")
            temp_window.destroy()  # Zavření okna po převodu

        tk.Button(temp_window, text="Převést", command=convert_temp).pack(pady=10)

    # Metoda pro ukončení aplikace
    def quit_app(self):
        self.root.quit()  # Ukončení hlavní smyčky Tkinter aplikace

# Hlavní blok pro spuštění aplikace
if __name__ == "__main__":
    # Vytvoření instance hlavního okna Tkinter aplikace
    root = tk.Tk()
    # Inicializace instance ChatbotApp s předáním hlavního okna
    app = ChatbotApp(root)
    # Spuštění hlavní smyčky aplikace - čeká na události a udržuje okno otevřené
    root.mainloop()
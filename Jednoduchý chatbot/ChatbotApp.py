# Jednoduchý Chatbot aplikace vytvořená pomocí Tkinter
# Tato aplikace nabízí různé funkce jako povídání o náladě, pomoc s matematikou,
# převodník jednotek, generování hesel, hádání čísel, generátor vtipů,
# zobrazení data a času, citát dne a generátor přezdívek.

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

        # Tlačítka pro různé funkce chatbota
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

        self.button11 = tk.Button(root, text="11. Konec", command=self.quit_app)
        self.button11.pack(fill=tk.X, padx=20, pady=2)

    # Metoda pro povídání o náladě - otevře nové okno pro zadání nálady
    def mood_chat(self):
        # Vytvoření nového okna pro povídání o náladě
        mood_window = tk.Toplevel(self.root)
        mood_window.title("Povídání o náladě")
        mood_window.geometry("300x150")

        tk.Label(mood_window, text="Jak se dnes máš?").pack(pady=10)
        mood_entry = tk.Entry(mood_window)
        mood_entry.pack()

        # Vnitřní funkce pro zpracování odpovědi na náladu
        def submit_mood():
            mood = mood_entry.get().lower()
            if mood == "dobře":
                messagebox.showinfo("Odpověď", "To je skvělé! Rád slyším, že se máš dobře.")
            elif mood == "špatně":
                messagebox.showinfo("Odpověď", "To mě mrzí. Doufám, že se brzy budeš cítit lépe.")
            elif mood == "unaveně":
                messagebox.showinfo("Odpověď", "To je normální. Někdy je důležité si odpočinout.")
            elif mood == "nadšeně":
                messagebox.showinfo("Odpověď", "To je úžasné! Je skvělé být nadšený.")
            else:
                messagebox.showinfo("Odpověď", "To je zajímavé! Každý se cítí jinak, a to je v pořádku.")
            mood_window.destroy()

        tk.Button(mood_window, text="Odeslat", command=submit_mood).pack(pady=10)

    # Metoda pro pomoc s matematikou - jednoduchá kalkulačka
    def math_help(self):
        # Vytvoření nového okna pro matematickou pomoc
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

        # Funkce pro výpočet výsledku
        def calculate():
            try:
                num1 = float(num1_entry.get())
                num2 = float(num2_entry.get())
                op = op_entry.get()
                if op == "+":
                    result = num1 + num2
                elif op == "-":
                    result = num1 - num2
                elif op == "*":
                    result = num1 * num2
                elif op == "/":
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        result = "Nelze dělit nulou"
                else:
                    result = "Neplatná operace"
                messagebox.showinfo("Výsledek", f"Výsledek: {result}")
            except ValueError:
                messagebox.showerror("Chyba", "Zadej platná čísla.")
            math_window.destroy()

        tk.Button(math_window, text="Vypočítat", command=calculate).pack(pady=10)

    # Metoda pro převodník jednotek (délkové jednotky)
    def unit_converter(self):
        # Vytvoření nového okna pro převodník jednotek
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

        # Funkce pro převod jednotek
        def convert():
            try:
                val = float(value_entry.get())
                f_unit = from_unit.get()
                t_unit = to_unit.get()
                # Faktory převodu na metry
                factors = {"m": 1, "cm": 0.01, "mm": 0.001, "km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144}
                if f_unit in factors and t_unit in factors:
                    result = val * factors[t_unit] / factors[f_unit]
                    messagebox.showinfo("Výsledek", f"{val} {f_unit} = {result} {t_unit}")
                else:
                    messagebox.showerror("Chyba", "Neplatné jednotky.")
            except ValueError:
                messagebox.showerror("Chyba", "Zadej platnou hodnotu.")
            unit_window.destroy()

        tk.Button(unit_window, text="Převést", command=convert).pack(pady=10)

    # Metoda pro generování náhodného hesla
    def generate_password(self):
        # Vytvoření nového okna pro generování hesla
        pass_window = tk.Toplevel(self.root)
        pass_window.title("Generování hesla")
        pass_window.geometry("300x150")

        tk.Label(pass_window, text="Délka hesla:").pack()
        length_entry = tk.Entry(pass_window)
        length_entry.pack()

        # Funkce pro generování hesla
        def generate():
            try:
                length = int(length_entry.get())
                if length > 0:
                    # Znaky pro heslo: písmena, číslice, speciální znaky
                    chars = string.ascii_letters + string.digits + string.punctuation
                    pwd = ''.join(random.choice(chars) for _ in range(length))
                    messagebox.showinfo("Heslo", f"Vygenerované heslo: {pwd}")
                else:
                    messagebox.showerror("Chyba", "Délka musí být kladná.")
            except ValueError:
                messagebox.showerror("Chyba", "Zadej číslo.")
            pass_window.destroy()

        tk.Button(pass_window, text="Generovat", command=generate).pack(pady=10)

    # Metoda pro ukončení aplikace
    def quit_app(self):
        self.root.quit()

    # Metoda pro hru hádání čísla
    def guess_number(self):
        # Vytvoření nového okna pro nastavení hry hádání čísla
        guess_window = tk.Toplevel(self.root)
        guess_window.title("Hádání čísla")
        guess_window.geometry("300x200")

        tk.Label(guess_window, text="Začátek rozsahu:").pack()
        start_entry = tk.Entry(guess_window)
        start_entry.pack()

        tk.Label(guess_window, text="Konec rozsahu:").pack()
        end_entry = tk.Entry(guess_window)
        end_entry.pack()

        # Funkce pro začátek hry
        def start_game():
            try:
                start = int(start_entry.get())
                end = int(end_entry.get())
                if start < end:
                    # Náhodné číslo v zadaném rozsahu
                    self.target = random.randint(start, end)
                    messagebox.showinfo("Začátek", f"Hádej číslo mezi {start} a {end}.")
                    self.guess_input(guess_window)
                else:
                    messagebox.showerror("Chyba", "Neplatný rozsah.")
            except ValueError:
                messagebox.showerror("Chyba", "Zadej čísla.")

        tk.Button(guess_window, text="Začít", command=start_game).pack(pady=10)

    # Pomocná metoda pro zadávání hádání v hře
    def guess_input(self, window):
        # Vytvoření okna pro zadání hádání
        input_window = tk.Toplevel(window)
        input_window.title("Hádej")
        input_window.geometry("200x100")

        tk.Label(input_window, text="Zadej hádání:").pack()
        guess_entry = tk.Entry(input_window)
        guess_entry.pack()

        # Funkce pro kontrolu hádání
        def check_guess():
            try:
                guess = int(guess_entry.get())
                if guess < self.target:
                    messagebox.showinfo("Tip", "Příliš nízké.")
                elif guess > self.target:
                    messagebox.showinfo("Tip", "Příliš vysoké.")
                else:
                    messagebox.showinfo("Výhra", "Gratulace! Uhodl jsi.")
                    input_window.destroy()
                    window.destroy()
            except ValueError:
                messagebox.showerror("Chyba", "Zadej číslo.")

        tk.Button(input_window, text="Hádej", command=check_guess).pack()

    # Metoda pro generování náhodného vtipu
    def joke_generator(self):
        # Seznam programátorských vtipů
        jokes = [
            "Proč programátoři nemohou řídit? Protože se bojí crashů.",
            "Jaký je rozdíl mezi programátorem a hackerem? Programátor píše kód, hacker ho zneužívá.",
            "Proč se programátoři nikdy nehádají? Protože vždycky najdou společný jazyk.",
            "Co řekl jeden programátor druhému? 'Máš nějaké bugy?'",
            "Proč programátoři nenosí hodinky? Protože čas je relativní."
        ]
        # Zobrazení náhodného vtipu
        messagebox.showinfo("Vtip", random.choice(jokes))

    # Metoda pro zobrazení aktuálního data a času
    def show_datetime(self):
        # Získání aktuálního data a času
        now = datetime.datetime.now()
        messagebox.showinfo("Datum a čas", f"Aktuální: {now}")

    # Metoda pro zobrazení náhodného citátu dne
    def quote_of_day(self):
        # Seznam motivujících citátů
        quotes = [
            "Život je jako jízda na kole. Abys udržel rovnováhu, musíš se pohybovat vpřed. - Albert Einstein",
            "Největší sláva není v tom, že nikdy nespadneme, ale v tom, že se vždy zvedneme. - Nelson Mandela",
            "Úspěch není konečný, neúspěch není fatální: je to odvaha pokračovat, co se počítá. - Winston Churchill",
            "Nejlepší způsob, jak předpovědět budoucnost, je ji vytvořit. - Peter Drucker",
            "Život je 10% toho, co se nám stane, a 90% toho, jak na to reagujeme. - Charles R. Swindoll"
        ]
        # Zobrazení náhodného citátu
        messagebox.showinfo("Citát", random.choice(quotes))

    # Metoda pro generování náhodné přezdívky
    def nickname_generator(self):
        # Seznamy pro generování přezdívek
        names = ["Rychlý", "Tichý", "Silný", "Moudrý", "Zábavný"]
        animals = ["Lev", "Tygr", "Medvěd", "Sova", "Delfín"]
        # Sestavení přezdívky z náhodného jména a zvířete
        nick = random.choice(names) + " " + random.choice(animals)
        messagebox.showinfo("Přezdívka", f"Tvoje přezdívka: {nick}")

    # Druhá metoda pro ukončení aplikace (duplicitní)
    def quit_app(self):
        self.root.quit()

# Hlavní blok pro spuštění aplikace
if __name__ == "__main__":
    # Vytvoření hlavního okna Tkinter
    root = tk.Tk()
    # Inicializace instance aplikace
    app = ChatbotApp(root)
    # Spuštění hlavní smyčky aplikace
    root.mainloop()
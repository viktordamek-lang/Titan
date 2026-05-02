# Jednoduchý Chatbot aplikace vytvořená pomocí Tkinter
# Tato aplikace nabízí různé funkce jako povídání o náladě, pomoc s matematikou,
# převodník jednotek, generování hesel, hádání čísel, generátor vtipů,
# zobrazení data a času, citát dne, generátor přezdívek, poznámkový blok,
# převodník měn, kalkulačka BMI, kámen-nůžky-papír, převodník teploty,
# hod kostkou, kalkulačka věku, náhodný fakt, počítadlo slov, Morseova abeceda
# a konvertor videa MOV na MP4.

# ====== PŘEHLED HLAVNÍCH FUNKCÍ ======
# 🎮 HRY:
#   - tic_tac_toe() → Hra Piškvorky (3x3 mřížka, 2 hráči)
#   - rock_paper_scissors() → Kámen-nůžky-papír proti počítači
#   - guess_number() → Hádaní čísla (uživatel hádá číslo v rozsahu)
#   - coin_flip_game() → Hra Nula Nebo Jedničky (50/50 šance, odhad)
#
# 🧮 KALKULAČKY:
#   - bmi_calculator() → Výpočet Body Mass Index (váha vs výška)
#   - unit_converter() → Převod délkových jednotek (m, cm, km, in, ft, yd)
#   - temperature_converter() → Převod teploty (°C, °F, K)
#   - currency_converter() → Převod měn (CZK na EUR, USD, GBP)
#   - math_help() → Kalkulačka na 4 základní operace (+, -, *, /)
#   - generate_password() → Generování bezpečného hesla
#
# ℹ️ INFORMACE:
#   - joke_generator() → Náhodný výběr z vtipů
#   - get_random_quote() → Náhodný motivační citát
#   - random_fact() → Zajímavý vědecký fakt
#   - show_datetime() → Aktuální datum a čas
#   - age_calculator() → Výpočet věku z data narození
#
# 📝 TEXTOVÉ NÁSTROJE:
#   - note_pad() → Poznámkový blok se ukládáním
#   - word_counter() → Počítadlo slov, znaků a řádků
#   - morse_code() → Převod textu do Morseovy abecedy
#
# 📊 WEBOVÉ FUNKCE:
#   - open_weather_window() → Zjištění počasí pro město (api wttr.in)
#   - open_search_window() → Vyhledání v prohlížeči (Google)
#
# 🎥 MULTIMÉDIA:
#   - video_converter() → Konverze videa MOV na MP4 (vyžaduje FFmpeg)
#
# 🎲 GENERÁTORY:
#   - nickname_generator() → Vygenerování náhodné přezdívky
#   - recipe_generator() → Vygenerování náhodného receptu
#
# ⚙️ NASTAVENÍ:
#   - open_settings() → Uživatelská nastavení (tema, font, jazyk)
#   - apply_theme() → Aplikace vybraného tématu (tmavý/světlý režim)

# Import potřebných modulů
# tkinter - pro vytvoření grafického uživatelského rozhraní
# messagebox - pro zobrazování dialogových oken s informacemi/chybami
# random - pro generování náhodných čísel a výběrů
# string - pro práci se znaky při generování hesel
# datetime - pro získání aktuálního data a času
import os
import subprocess
import ast
import tkinter as tk
from tkinter import messagebox, filedialog
import random
import string
import datetime
import webbrowser
import urllib.parse
import urllib.request
# webbrowser, urllib.parse a urllib.request umožňují otevřít prohlížeč a načítat data z webu

# Třída pro hlavní aplikaci chatbota
class ChatbotApp:
    # Inicializační metoda pro nastavení hlavního okna a tlačítek
    # Parametr 'self' = instance třídy (objekt), 'root' = hlavní okno Tkinter
    def __init__(self, root):
        self.root = root  # Uložení reference na hlavní okno pro pozdější přístup
        self.root.title("Jednoduchý Chatbot")  # Nastavení titulku okna
        self.root.geometry("800x500")  # Nastavení rozměrů: šířka 800 pixelů, výška 500 pixelů

        # Vytvoření hlavního štítku s uvítáním
        self.label = tk.Label(root, text="Ahoj! Napiš příkaz nebo zprávu:")
        self.label.pack(pady=10)

        # Hlavní rámeček pro layout chatu + boční panel
        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Levý panel: chat
        left_frame = tk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Pravý panel: seznam všech chatů / historie
        right_frame = tk.Frame(main_frame, width=200)
        right_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        tk.Label(right_frame, text="Seznam chatů:").pack(anchor=tk.NW)
        listbox_frame = tk.Frame(right_frame)
        listbox_frame.pack(fill=tk.BOTH, expand=True)

        self.chat_listbox = tk.Listbox(listbox_frame)
        self.chat_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        listbox_scrollbar = tk.Scrollbar(listbox_frame, command=self.chat_listbox.yview)
        listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_listbox.configure(yscrollcommand=listbox_scrollbar.set)
        self.chat_listbox.bind('<<ListboxSelect>>', self.select_chat)

        # Přidání podpory historie příkazů pro klávesy ↑ / ↓
        self.command_history = []
        self.history_index = 0
        # Historie výsledků kalkulačky
        self.calc_history = []

        # ====== UŽIVATELSKÁ NASTAVENÍ ======
        # Výchozí hodnoty: tmavý režim, velikost fontu, barva pozadí, jazyk
        self.settings = {
            "dark_mode": False,           # False = světlý režim, True = tmavý režim
            "font_size": 10,              # Velikost fontu v pixelech (defaultně 10)
            "language": "CZ",             # "CZ" = čeština, "EN" = angličtina
            "bg_color": "white",          # Barva pozadí chatu
            "fg_color": "black",          # Barva textu
            "auto_save": True,            # Automatické ukládání chatu
            "notifications": True,        # Povolení notifikací
            "font_family": "Arial"        # Font pro display
        }

        # Hlavní chatové okno (Text widget) s vertikálním scrollbarem
        chat_text_frame = tk.Frame(left_frame)
        chat_text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.chat_history = tk.Text(chat_text_frame, state=tk.DISABLED, wrap=tk.WORD, fg="black")
        self.chat_history.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.chat_scrollbar = tk.Scrollbar(chat_text_frame, command=self.chat_history.yview)
        self.chat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.chat_history.configure(yscrollcommand=self.chat_scrollbar.set)

        # Nastavení barev pro text
        self.chat_history.tag_configure("user", foreground="black", background="white")
        self.chat_history.tag_configure("bot", foreground="black", background="white")

        # Vstupní pole pro chat
        self.chat_entry = tk.Entry(left_frame, bg="white", fg="green")
        self.chat_entry.pack(fill=tk.X, pady=5)
        self.chat_entry.bind("<Return>", lambda event: self.process_chat())
        self.chat_entry.bind("<Up>", self.navigate_history_up)
        self.chat_entry.bind("<Down>", self.navigate_history_down)
        self.chat_entry.bind("<Return>", lambda event: self.process_chat())

        button_frame = tk.Frame(left_frame)
        button_frame.pack(pady=(0, 10))
        tk.Button(button_frame, text="Odeslat", command=self.process_chat).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Uložit chat", command=self.save_chat).pack(side=tk.LEFT, padx=5)

        quick_frame = tk.Frame(left_frame)
        quick_frame.pack(fill=tk.X, pady=(0, 10))
        tk.Label(quick_frame, text="Rychlé funkce:").pack(anchor=tk.W)
        quick_buttons = tk.Frame(quick_frame)
        quick_buttons.pack(fill=tk.X)
        tk.Button(quick_buttons, text="Vtip", command=self.joke_generator).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(quick_buttons, text="BMI", command=self.bmi_calculator).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(quick_buttons, text="Převod", command=self.unit_converter).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(quick_buttons, text="Video", command=self.video_converter).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(quick_buttons, text="Poznámky", command=self.note_pad).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(quick_buttons, text="Nálada", command=self.mood_chat).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(quick_buttons, text="Matika", command=self.math_help).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(quick_buttons, text="Citát", command=self.quote_of_day).pack(side=tk.LEFT, padx=2, pady=2)
        # Nové funkce pro webovou integraci: počasí a webové hledání
        # Tlačítka otevřou dodatečná okna nebo přímo prohlížeč.
        tk.Button(quick_buttons, text="Počasí", command=self.open_weather_window).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(quick_buttons, text="Vyhledat", command=self.open_search_window).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(quick_buttons, text="Calc historie", command=self.display_calc_history).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(quick_buttons, text="TTT", command=self.tic_tac_toe).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(quick_buttons, text="Recept", command=self.recipe_generator).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(quick_buttons, text="⚙️ Nastavení", command=self.open_settings).pack(side=tk.LEFT, padx=2, pady=2)
        tk.Button(quick_buttons, text="🎰 0/1", command=self.coin_flip_game).pack(side=tk.LEFT, padx=2, pady=2)

        # Základní nápověda pro příkazy
        self.append_chat("Bot: Ahoj! Můžu pomoci se všemi programy. Seznam příkazů:")
        self.append_chat("- help, help all, help chat, clear, history, calc history, ask, weather, search, ahoj, jak se máš, calc, unit, pass, joke, time, quote, nick, currency, bmi, rps, temp, dice, age, fact, words, morse, reverse, tictactoe, recipe, mood, math, exit")
        self.append_chat("📚 Detailní průvodce všech funkcí najdeš v souboru: FUNKCNI_PRUVODCE.md")

        # Při startu načteme poslední chat (pokud existuje) pro lepší plynulost práce
        if os.path.exists("chat_log.txt"):
            try:
                with open("chat_log.txt", "r", encoding="utf-8") as f:
                    lines = f.read().splitlines()
                if lines:
                    self.append_chat("Bot: Načítám poslední chat...")
                    for line in lines:
                        self.append_chat(line)
            except Exception:
                self.append_chat("Bot: Nelze načíst uložený chat; pokračujeme s prázdným chatem.")

        # Podpora přepnutí do převodníků a her přes chat:
        # math, unit, pass, joke, time, quote, nick, note, currency, bmi, rps, temp, dice, age, fact, words, morse

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

    # ====== UŽIVATELSKÁ NASTAVENÍ ======
    # Metoda pro otevření okna s nastavením vzhledu a chování aplikace
    def open_settings(self):
        # Vytvoření nového okna (Toplevel) pro uživatelská nastavení
        settings_window = tk.Toplevel(self.root)
        settings_window.title("⚙️ Nastavení aplikace")
        settings_window.geometry("400x350")

        tk.Label(settings_window, text="UŽIVATELSKÁ NASTAVENÍ", font=("Arial", 14, "bold")).pack(pady=10)
        
        # ===== SEKCE 1: VZHLED =====
        tk.Label(settings_window, text="📊 VZHLED:", font=("Arial", 11, "bold")).pack(anchor=tk.W, padx=15)
        
        # Jazyk
        tk.Label(settings_window, text="Jazyk:").pack(anchor=tk.W, padx=30)
        lang_var = tk.StringVar(value=self.settings["language"])
        tk.OptionMenu(settings_window, lang_var, "CZ", "EN").pack(anchor=tk.W, padx=40)
        
        # Velikost fontu
        tk.Label(settings_window, text="Velikost fontu:").pack(anchor=tk.W, padx=30)
        font_frame = tk.Frame(settings_window)
        font_frame.pack(anchor=tk.W, padx=40)
        font_size_scale = tk.Scale(font_frame, from_=8, to=16, orient=tk.HORIZONTAL, 
                                   length=150, label="px")
        font_size_scale.set(self.settings["font_size"])
        font_size_scale.pack(side=tk.LEFT)
        
        # Tmavý režim
        tk.Label(settings_window, text="Vzhled:").pack(anchor=tk.W, padx=30)
        theme_var = tk.StringVar(value="Světlý" if not self.settings["dark_mode"] else "Tmavý")
        tk.OptionMenu(settings_window, theme_var, "Světlý", "Tmavý").pack(anchor=tk.W, padx=40)
        
        # ===== SEKCE 2: CHOVÁNÍ =====
        tk.Label(settings_window, text="⚡ CHOVÁNÍ:", font=("Arial", 11, "bold")).pack(anchor=tk.W, padx=15, pady=(10,0))
        
        # Automatické ukládání
        auto_save_var = tk.BooleanVar(value=self.settings["auto_save"])
        tk.Checkbutton(settings_window, text="Automatické ukládání chatu", 
                      variable=auto_save_var).pack(anchor=tk.W, padx=30)
        
        # Notifikace
        notif_var = tk.BooleanVar(value=self.settings["notifications"])
        tk.Checkbutton(settings_window, text="Povolit notifikace", 
                      variable=notif_var).pack(anchor=tk.W, padx=30)
        
        # ===== TLAČÍTKA =====
        button_frame = tk.Frame(settings_window)
        button_frame.pack(pady=15)
        
        # Tlačítko Uložit
        def save_settings():
            self.settings["language"] = lang_var.get()
            self.settings["font_size"] = font_size_scale.get()
            self.settings["dark_mode"] = (theme_var.get() == "Tmavý")
            self.settings["auto_save"] = auto_save_var.get()
            self.settings["notifications"] = notif_var.get()
            
            # Aplikuj změny vzhledu
            self.apply_theme()
            
            messagebox.showinfo("Nastavení", "Nastavení bylo uloženo! 🎉")
            settings_window.destroy()
        
        # Tlačítko Zrušit
        def cancel_settings():
            settings_window.destroy()
        
        tk.Button(button_frame, text="💾 Uložit", command=save_settings, bg="green", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="❌ Zrušit", command=cancel_settings, bg="red", fg="white").pack(side=tk.LEFT, padx=5)
        
        # Informační text
        info_text = "Změny se aplikují po kliknutí na 'Uložit'.\nNěkteré změny mohou vyžadovat restart aplikace."
        tk.Label(settings_window, text=info_text, font=("Arial", 9), fg="gray").pack(pady=10)
    
    # Metoda pro aplikaci vybraného tématu (tmavý/světlý režim)
    # Změní barvy pozadí a textu v celé aplikaci podle nastavení
    def apply_theme(self):
        # Pokud je aktivní tmavý režim, nastav tmavé barvy, jinak světlé
        if self.settings["dark_mode"]:
            # Tmavý režim: tmavé pozadí + světlý text
            self.settings["bg_color"] = "#2b2b2b"  # Tmavě šedá
            self.settings["fg_color"] = "#ffffff"  # Bílá
            bg = "#2b2b2b"
            fg = "#ffffff"
        else:
            # Světlý režim: bílé pozadí + tmavý text
            self.settings["bg_color"] = "white"    # Bílá
            self.settings["fg_color"] = "black"    # Černá
            bg = "white"
            fg = "black"
        
        # Aplikuj barvy na hlavní chat window
        self.chat_history.config(bg=bg, fg=fg, font=(self.settings["font_family"], self.settings["font_size"]))
        
        # Pokud je auto_save zapnuto, ulož chat
        if self.settings["auto_save"]:
            self.save_chat()

    # Vloží text do historie chatu a scrolluje dolů automaticky
    # Také přidá text do bočního seznamu (listbox) pro snadný přístup
    # Tagy "user" a "bot" umožňují různé vizuální styly pro každého (barva, font atd.)
    def append_chat(self, text):
        # Umožníme zápis do chatu (je normálně zablokovaný pro ochranu)
        self.chat_history.configure(state=tk.NORMAL)
        # Určení tagu (stylizace) podle toho, zda je to uživatel nebo bot
        # Tag "user" = černý text na bílém pozadí; "bot" = také černý na bílém
        if text.startswith("Ty:"):
            tag = "user"
        else:
            tag = "bot"
        # Vložíme text na konec (tk.END) s daným tagem; "\n" = nový řádek
        self.chat_history.insert(tk.END, text + "\n", tag)
        # Zablokujeme textové pole znovu (jen čtení)
        self.chat_history.configure(state=tk.DISABLED)
        # self.chat_history.see(tk.END) = automaticky scrolluje na poslední zprávu
        # (uživatel vždy vidí nejnovější zprávu bez ručního scrollování)
        self.chat_history.see(tk.END)

        # Zároveň přidat do bočního seznamu všech chatů (historický listbox)
        if hasattr(self, 'chat_listbox'):
            # hasattr = "má tato instance atribut 'chat_listbox'?" (kontrola existence)
            self.chat_listbox.insert(tk.END, text)
            # Udržení posledního zobrazení (show end item)
            # Listbox se automaticky scrolluje na poslední položku
            self.chat_listbox.see(tk.END)

    def select_chat(self, event):
        # Pokud uživatel zvolí položku z historie chatu, vložíme ji zpět do vstupního pole.
        # Tím lze snadno znovu odeslat nebo upravit dřívější zprávu.
        # curselection() vrátí n-tici s indexy vybraných prvků; pokud není nic vybráno, vrátí ()
        if not self.chat_listbox.curselection():
            # Pokud nic není vybráno, opustíme metodu
            return
        # Získáme vybraný text z listboxu: curselection()[0] = index prvního vybraného prvku
        selected = self.chat_listbox.get(self.chat_listbox.curselection()[0])
        # Odstraníme prefix "Ty: " (prvních 4 znaky) nebo "Bot: " (prvních 5 znaků)
        # aby vstupní pole obsahovalo jen samotný příkaz/zprávu
        if selected.startswith("Ty: "):
            # Slicing [4:] = vezmi všechno od 4. znaku dál (přeskočiš "Ty: ")
            selected = selected[4:]
        elif selected.startswith("Bot: "):
            # Slicing [5:] = vezmi všechno od 5. znaku dál (přeskočiš "Bot: ")
            selected = selected[5:]
        # Vymažeme vstupní pole a vložíme vybraný text
        self.chat_entry.delete(0, tk.END)
        self.chat_entry.insert(0, selected)

    # Pohyb v historii příkazů pomocí klávesy ↑ (nahoru)
    # Stisknutí ↑ zobrazí předchozí příkaz ze historie
    def navigate_history_up(self, event):
        # Pokud je historie prázdná, nic neděláme
        if not self.command_history:
            return "break"
        # Zkontrolujeme, zda nejsme na začátku historie
        # self.history_index > 0 = zatím jsme se nevrátili na úplný začátek
        if self.history_index > 0:
            # Snížíme index (jdeme o jeden příkaz zpět v historii)
            self.history_index -= 1
            # Vymažeme vstupní pole (delete(0, tk.END) = smaž všechno)
            self.chat_entry.delete(0, tk.END)
            # Vložíme starší příkaz ze command_history
            self.chat_entry.insert(0, self.command_history[self.history_index])
        # "break" = zastavit další zpracování klávesy (zamezí defaultnímu chování blikání kurzoru)
        return "break"

    # Pohyb v historii příkazů pomocí klávesy ↓ (dolů)
    # Stisknutí ↓ zobrazí příští (novější) příkaz ze historie
    def navigate_history_down(self, event):
        # Pokud je historie prázdná, nic neděláme
        if not self.command_history:
            return "break"
        # Zkontrolujeme, zda nejsme na konci historie (nejnovějším příkazu)
        # len(...) - 1 = index posledního prvku
        if self.history_index < len(self.command_history) - 1:
            # Zvýšíme index (jdeme o jeden příkaz dopředu v historii)
            self.history_index += 1
            # Vymažeme vstupní pole
            self.chat_entry.delete(0, tk.END)
            # Vložíme novější příkaz ze command_history
            self.chat_entry.insert(0, self.command_history[self.history_index])
        else:
            # Pokud jsme už na konci nebo přesáhli konec, resetujeme na prázdný pole
            # self.history_index = len(...) = ukazatel na "jednu pozici za posledním prvkem"
            self.history_index = len(self.command_history)
            # Vymaž vstupní pole pro nový příkaz
            self.chat_entry.delete(0, tk.END)
        return "break"

    # ====== CHAT & HISTORIE ======
    # Metoda pro zpracování uživatelského vstupu z chat pole
    # Zpracovává příkazy a odpovídá vhodnou zprávou nebo akcí
    def process_chat(self):
        # Načteme text z input pole
        user_text = self.chat_entry.get().strip()

        # Pokud je pole prázdné, nic neděláme
        if not user_text:
            return

        # Uložíme do historie příkazů pro navigaci šipkami (klávesy ↑/↓)
        self.command_history.append(user_text)
        self.history_index = len(self.command_history)

        # Zobrazíme zprávu uživatele ve spodní části chatu a do historie
        self.append_chat("Ty: " + user_text)

        # Vyprázdníme vstupní pole pro další zprávu
        self.chat_entry.delete(0, tk.END)

        # Přeposlání textu do parseru příkazů a zobrazení odpovědi
        # Metoda handle_command rozhoduje, zda se jedná o chat, kalkulačku, webové hledání nebo jiný příkaz.
        response = self.handle_command(user_text)
        self.append_chat("Bot: " + response)

    # Pomocná metoda pro kontrolu, zda text obsahuje některý ze zadaných klíčů
    # Vrací True/False; používá se pro rozpoznávání příkazů v chatovém textu
    # Příklad: self._has("jak se máš", "jak se", "co u tebe") vrátí True
    def _has(self, text, *keys):
        return any(key in text for key in keys)

    # Pomocná metoda pro kontrolu, zda text začíná některým ze zadaných prefixů
    # Vrací True/False; používá se pro příkazy, které vyžadují argumenty (např. "calc 2+2")
    # Příklad: self._starts("calc 5*3", "calc ", "math ") vrátí True
    def _starts(self, text, *prefixes):
        return any(text.startswith(prefix) for prefix in prefixes)

    # Bezpečně vyhodnotí matematický výraz pomocí AST (Abstract Syntax Tree)
    # BEZPEČNOST: Zabraňuje spuštění nebezpečného kódu tím, že:
    #            1. Parsuje výraz na AST (stromová struktura, ne spustitelný kód)
    #            2. Ověřuje, že obsahuje jen bezpečné operace (sčítání, násobení atd.)
    #            3. Zakazuje volání funkcí (ast.Call) a access k built-in modulům
    #            4. Vyhodnocuje s prázdným prostředím {{"__builtins__": None}}
    # PŘÍKLAD: "2+3*4" -> OK; "__import__('os').system()" -> ODMÍTNUTO
    def safe_eval_math(self, expr):
        # Parsování textu na AST - nejedná se o spuštění, jen analýza
        expression = ast.parse(expr, mode="eval")
        # Seznam povolených typů uzlů: binární operace (+,-,*,/), unární (-+), konstanty
        allowed_nodes = (
            ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant, ast.Num,
            ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod,
            ast.UAdd, ast.USub, ast.FloorDiv, ast.LShift, ast.RShift,
            ast.Load,
        )
        # Procházení všech uzlů v AST stromu - ověření bezpečnosti
        for node in ast.walk(expression):
            # Zastavit jakékoliv volání funkcí (např. open(), exec(), etc.)
            if isinstance(node, ast.Call):
                raise ValueError("Nepovolený výraz")
            # Zastavit nekanonické konstanty (např. stringy, které by mohly obsahovat kód)
            if isinstance(node, ast.Constant) and not isinstance(node.value, (int, float, complex)):
                raise ValueError("Nepovolený výraz")
            # Zastavit jakékoliv jiné nepovolené operace
            if not isinstance(node, allowed_nodes):
                raise ValueError("Nepovolený výraz")
        # Vyhodnocení bezpečného výrazu s vypnutými built-in funkcemi
        return eval(compile(expression, "<string>", "eval"), {"__builtins__": None}, {})

    # Metoda pro vymazání celého chatu
    # Vymaže obsah textového pole chatu a také listbox s historií
    def clear_chat(self):
        # Umožní zápis do textového pole (je normálně DISABLED pro ochranu)
        self.chat_history.configure(state=tk.NORMAL)
        # Smazání všeho obsahu: "1.0" = prvn řádek, znak 0 (začátek); tk.END = konec dokumentu
        self.chat_history.delete("1.0", tk.END)
        # Zase zablokování textového pole (jen čtení, uživatel nemůže editovat)
        self.chat_history.configure(state=tk.DISABLED)
        # Pokud existuje listbox s historií (boční panel), smazat i ten
        if hasattr(self, "chat_listbox"):
            self.chat_listbox.delete(0, tk.END)
        # Vrácení potvrzovací zprávy uživateli
        return "Chat byl vymazán. Pro nové příkazy napiš 'help'."

    # Metoda pro zobrazení posledních 20 příkazů z historie
    def show_history(self):
        # Pokud uživatel ještě nic nezadal, vrátit varovnou zprávu
        if not self.command_history:
            return "Žádná historie příkazů zatím není."
        # Vezmeme posledních 20 příkazů (command_history[-20:] = poslední 20 prvků)
        # [-20:] = list slicing: od pozice -20 (20. prvek od konce) do konce
        recent = self.command_history[-20:]
        # Spojíme příkazy do jednoho řetězce oddělené čárkou
        return "Historie příkazů: " + ", ".join(recent)

    def show_calc_history(self):
        if not self.calc_history:
            return "Žádná historie výpočtů zatím není."
        return "Historie kalkulačky: " + "; ".join(self.calc_history[-20:])

    def display_calc_history(self):
        history_text = self.show_calc_history()
        messagebox.showinfo("Historie kalkulačky", history_text)

    def chat_mode(self):
        # Otevře okno pro konverzační režim podobný ChatGPT
        # V tomto režimu může uživatel zadávat otázky a dostane jednoduchou odpověď.
        chat_window = tk.Toplevel(self.root)
        chat_window.title("Chat Mode - AI-like odpovědi")
        chat_window.geometry("600x400")

        tk.Label(chat_window, text="Zadej otázku nebo zprávu:").pack(pady=5)
        question_entry = tk.Entry(chat_window, width=50)
        question_entry.pack(pady=5)

        response_text = tk.Text(chat_window, height=10, width=50, state=tk.DISABLED)
        response_text.pack(pady=5)

        def generate_response():
            question = question_entry.get().strip()
            if not question:
                return
            response = self.generate_ai_response(question)
            response_text.configure(state=tk.NORMAL)
            response_text.delete("1.0", tk.END)
            response_text.insert(tk.END, response)
            response_text.configure(state=tk.DISABLED)

        tk.Button(chat_window, text="Odpovědět", command=generate_response).pack(pady=5)

    def generate_ai_response(self, question):
        # Jednoduchý generátor odpovědí podobný ChatGPT
        responses = {
            "jak se máš": ["Mám se skvěle, děkuji! Co ty?", "Jsem jen kód, ale funguji dobře. A ty?"],
            "co je to": ["To je zajímavá otázka. Zkusím vysvětlit...", "Záleží na kontextu, ale obecně..."],
            "proč": ["Důvodů může být mnoho. Možná protože...", "To je filozofická otázka. Možná kvůli..."],
            "jak": ["Zkus to takto: krok 1, krok 2...", "Existuje několik způsobů, ale nejlepší je..."],
            "kde": ["To záleží na místě. Možná v...", "Hledáš konkrétní lokaci? Zkus..."],
            "kdo": ["To může být kdokoliv. Možná...", "Záleží na kontextu, ale často je to..."],
        }
        q_lower = question.lower()
        for key, replies in responses.items():
            if key in q_lower:
                return random.choice(replies)
        # Výchozí odpověď
        return "To je zajímavá otázka! Bohužel jsem jen jednoduchý chatbot, takže nemám plnou AI inteligenci jako ChatGPT. Zkus napsat něco jiného nebo použij příkazy jako 'help'."

    def open_web_search(self, query):
        # Sestaví URL pro Google vyhledávání a otevře ji ve výchozím prohlížeči.
        # urllib.parse.quote() zajistí správné kódování českých a speciálních znaků.
        # Tato metoda pouze spouští externí prohlížeč, nevrací data přímo do aplikace.
        try:
            url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
            webbrowser.open(url)
            return True
        except Exception:
            return False

    def open_search_window(self):
        # Otevře malé okno pro zadání hledaného výrazu.
        # Po kliknutí na tlačítko se provede vyhledání v prohlížeči.
        search_window = tk.Toplevel(self.root)
        search_window.title("Webové vyhledávání")
        search_window.geometry("400x120")

        tk.Label(search_window, text="Hledat: ").pack(pady=5)
        query_entry = tk.Entry(search_window, width=40)
        query_entry.pack(padx=10)

        def search():
            query = query_entry.get().strip()
            if not query:
                messagebox.showwarning("Hledat", "Zadej, co chceš vyhledat.")
                return
            if self.open_web_search(query):
                search_window.destroy()
            else:
                messagebox.showerror("Hledat", "Nepodařilo se otevřít vyhledávání.")

        tk.Button(search_window, text="Hledat", command=search).pack(pady=10)

    def get_weather(self, city):
        # Načte počasí z veřejné služby wttr.in.
        # wttr.in je volně dostupná služba, která vrátí krátký text o počasí bez API klíče.
        try:
            query = urllib.parse.quote(city)
            url = f"http://wttr.in/{query}?format=3&lang=cs"
            with urllib.request.urlopen(url, timeout=10) as response:
                return response.read().decode("utf-8")
        except Exception:
            return "Nelze načíst počasí. Zkontroluj připojení k internetu nebo zkus jiný místní název."

    def open_weather_window(self):
        # Vytvoří jednoduché dialogové okno pro zadání města a zobrazení počasí.
        weather_window = tk.Toplevel(self.root)
        weather_window.title("Počasí")
        weather_window.geometry("400x120")

        tk.Label(weather_window, text="Město nebo lokalita:").pack(pady=5)
        city_entry = tk.Entry(weather_window, width=40)
        city_entry.pack(padx=10)

        def show_weather():
            city = city_entry.get().strip()
            if not city:
                messagebox.showwarning("Počasí", "Zadej název města nebo lokality.")
                return
            result = self.get_weather(city)
            messagebox.showinfo("Počasí", result)
            weather_window.destroy()

        tk.Button(weather_window, text="Zjistit počasí", command=show_weather).pack(pady=10)

    # Hlavní parser příkazů - analyzuje uživatelský vstup a vrátí odpověď
    # Strategie: 1. Normalizuje text (malá písmena) -> 2. Hledá přesné shody v slovníku
    #            3. Hledá příkazy s argumenty (např. "calc ...") -> 4. Vracejí text nebo vyvolávají okna
    def handle_command(self, text):
        # Normalizace textu na malá písmena a odebrání mezer na začátku/konci (jednodušší porovnání)
        t = text.strip().lower()
        if not t:
            return ""

        # Slovník jednoduchých odpovědí na přesné příkazy
        # Klíče jsou příkazy (lowercase); hodnoty jsou lambda funkce (anonymní funkce)
        # Proč lambda? Protože některé hodnoty potřebují volat funkce (clear_chat(), show_history())
        # Bez lambda by se funkce zavolaly hned při vytváření slovníku, ne až během hledání odpovědi
        # Příklady:
        # - "help": lambda: (...) => vrátí seznam příkazů
        # - "clear": lambda: self.clear_chat() => zavolá clear_chat() pouze když je "clear" zadán
        # - "díky": lambda: "Není zač..." => vrátí statický text
        simple_responses = {
            "help": lambda: (
                "Příkazy: help, help all, help chat, ahoj, jak se máš, co umíš, děkuji, calc, unit, pass, joke, "
                "time, quote, nick, currency, bmi, rps, temp, dice, age, fact, words, morse, reverse, video, weather, search, calc history, ask, tictactoe, recipe, coin, mood, math, exit"
            ),
            "?": lambda: (
                "Příkazy: help, help all, help chat, ahoj, jak se máš, co umíš, děkuji, calc, unit, pass, joke, "
                "time, quote, nick, currency, bmi, rps, temp, dice, age, fact, words, morse, reverse, video, weather, search, calc history, ask, tictactoe, recipe, coin, exit"
            ),
            "pomoc": lambda: (
                "Příkazy: help, help all, help chat, ahoj, jak se máš, co umíš, děkuji, calc, unit, pass, joke, "
                "time, quote, nick, currency, bmi, rps, temp, dice, age, fact, words, morse, reverse, video, weather, search, calc history, ask, tictactoe, recipe, coin, exit"
            ),
            "help all": lambda: (
                "Funkce: kalkulačka (calc), převody jednotek (unit), generování hesla (pass), vtipy (joke), "
                "čas (time), citát (quote), nick (nick), BMI (bmi), kostka (dice), věk (age), fact, words, morse, reverse, konvertor videa (video), počasí (weather), hledání webu (search), historie kalkulačky (calc history), AI-like chat (ask), Tic-Tac-Toe (tictactoe), generátor receptů (recipe), hra 0/1 (coin), nálada (mood), matematika (math), exit"
            ),
            "help chat": lambda: "Zkuste: ahoj, jak se máš, co umíš, děkuji, co děláš, počasí, search [text], weather [místo], ask [otázka]",
            "děkuji": lambda: "Není zač, rád pomáhám!",
            "děkuju": lambda: "Není zač, rád pomáhám!",
            "díky": lambda: "Není zač, rád pomáhám!",
            "clear": lambda: self.clear_chat(),
            "vymazat": lambda: self.clear_chat(),
            "clear chat": lambda: self.clear_chat(),
            "vymazat chat": lambda: self.clear_chat(),
            "history": lambda: self.show_history(),
            "command history": lambda: self.show_history(),
            "historie": lambda: self.show_history(),
            "calc history": lambda: self.show_calc_history(),
        }

        # Pokud je zadaný text v simple_responses, zavoláme odpovídající lambda funkci: lambda()
        if t in simple_responses:
            return simple_responses[t]()

        if self._has(t, "co umíš", "co umis", "umíš"):
            return "Umím spočítat, převádět, hrát hry a povídat si (příkazy: help)."

        if self._has(t, "ahoj", "čau", "nazdar", "zdar"):
            return "Ahoj! Jak ti mohu dnes pomoci?"

        if self._has(t, "jak se máš", "jak se mas", "máš se", "mas se"):
            return "Mám se dobře, děkuji za optání! Co ty?"

        if self._has(t, "co děláš", "co delas", "co dělas"):
            return "Právě si povídáme. Jsem tu, abych ti pomohl s programy i klasikou."

        if t in ["počasí", "pocasi"]:
            return "Napiš 'weather [místo]' nebo 'počasí [místo]' pro aktuální předpověď."

        if self._has(t, "den", "dnes", "datum"):
            return f"Dnes je {datetime.datetime.now():%A}, {datetime.datetime.now():%d.%m.%Y}."

        if self._has(t, "povídat", "povidat") or t == "chat":
            return "Jasně, můžeme si popovídat. Napiš cokoli a já odpovím."

        if t in ["mood", "mood chat", "nálada", "nalada"]:
            self.mood_chat()
            return "Otevírám dialog o náladě..."

        if t in ["math", "matika", "matematika"]:
            self.math_help()
            return "Otevírám pomoc s matematikou..."

        if t in ["quote", "citát", "citat"]:
            return self.get_random_quote()

        # Chatový režim: použijeme jednoduché AI-like odpovědi založené na klíčových slovech
        if self._starts(t, "ask ") or self._starts(t, "chat "):
            question = original_text.split(" ", 1)[1]
            return self.generate_ai_response(question)

        # Počasí lze vyžádat příkazem weather nebo českou variantou počasí/pocasi
        if self._starts(t, "weather ", "počasí ", "pocasi "):
            location = original_text.split(" ", 1)[1]
            return self.get_weather(location)

        # Webové vyhledávání otevře Google s dotazem v prohlížeči
        if self._starts(t, "search ", "vyhledat "):
            query = original_text.split(" ", 1)[1]
            self.open_web_search(query)
            return f"Otevírám vyhledávání pro: {query}"

        if t.startswith("calc ") or t.startswith("math "):
            expr = text.split(" ", 1)[1]
            try:
                result = self.safe_eval_math(expr)
                calc_line = f"{expr} = {result}"
                self.calc_history.append(calc_line)
                return calc_line
            except Exception:
                return "Chybný matematický výraz. Použij například: calc 3+4*2"

        if t.startswith("unit "):
            parts = t.split()
            if len(parts) == 4:
                try:
                    val = float(parts[1])
                    f = parts[2].lower()
                    to = parts[3].lower()
                    factors = {"m": 1, "cm": 0.01, "mm": 0.001, "km": 1000, "in": 0.0254, "ft": 0.3048, "yd": 0.9144}
                    if f in factors and to in factors:
                        res = val * factors[to] / factors[f]
                        return f"{val} {f} = {res} {to}"
                except ValueError:
                    pass
            return "Použij: unit 100 cm m"

        if t.startswith("pass ") or t.startswith("password "):
            parts = t.split()
            if len(parts) == 2:
                try:
                    length = int(parts[1])
                    if length > 0:
                        chars = string.ascii_letters + string.digits + string.punctuation
                        return ''.join(random.choice(chars) for _ in range(length))
                    return "Délka musí být kladná."
                except ValueError:
                    return "Použij: pass 12"
            return "Použij: pass 12"

        if "joke" in t or "vtip" in t:
            jokes = [
                "Proč programátoři nemohou řídit? Protože se bojí crashů.",
                "Jaký je rozdíl mezi programátorem a hackerem? Programátor píše kód, hacker ho zneužívá.",
                "Proč se programátoři nikdy nehádají? Protože vždycky najdou společný jazyk.",
                "Co řekl jeden programátor druhému? 'Máš nějaké bugy?'"
            ]
            return random.choice(jokes)

        if "time" in t or "čas" in t:
            return str(datetime.datetime.now())

        if "quote" in t or "citát" in t:
            quotes = [
                "Život je jako jízda na kole... - Albert Einstein",
                "Největší sláva není v tom, že nikdy nespadneme... - Nelson Mandela"
            ]
            return random.choice(quotes)

        if "nick" in t or "přezdívka" in t:
            names = ["Rychlý", "Tichý", "Silný", "Moudrý", "Zábavný"]
            animals = ["Lev", "Tygr", "Medvěd", "Sova", "Delfín"]
            return f"{random.choice(names)} {random.choice(animals)}"

        if "dice" in t or "kostka" in t:
            return f"Hodil jsi: {random.randint(1, 6)}"

        if t.startswith("age "):
            parts = t.split()
            if len(parts) == 4:
                try:
                    birth_date = datetime.date(int(parts[1]), int(parts[2]), int(parts[3]))
                    today = datetime.date.today()
                    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                    return f"Máš {age} let."
                except ValueError:
                    pass
            return "Použij: age 1990 12 31"

        if t.startswith("bmi "):
            parts = t.split()
            if len(parts) == 3:
                try:
                    weight = float(parts[1])
                    height = float(parts[2]) / 100.0
                    if height <= 0:
                        raise ValueError
                    bmi = weight / (height * height)
                    cat = "Normální váha" if 18.5 <= bmi < 25 else "Podváha" if bmi < 18.5 else "Nadváha" if bmi < 30 else "Obezita"
                    return f"BMI {bmi:.2f} ({cat})"
                except ValueError:
                    pass
            return "Použij: bmi 70 175"

        if t.startswith("temp "):
            parts = t.split()
            if len(parts) == 4:
                try:
                    val = float(parts[1])
                    f = parts[2].upper(); to = parts[3].upper()
                    if f == "C":
                        kelv = val + 273.15
                    elif f == "F":
                        kelv = (val - 32) * 5/9 + 273.15
                    elif f == "K":
                        kelv = val
                    else:
                        return "Neplatná jednotka"
                    if to == "C":
                        res = kelv - 273.15
                    elif to == "F":
                        res = (kelv - 273.15) * 9/5 + 32
                    elif to == "K":
                        res = kelv
                    else:
                        return "Neplatná jednotka"
                    return f"{val}{f} = {res:.2f}{to}"
                except ValueError:
                    pass
            return "Použij: temp 100 C F"

        if "fact" in t or "fakt" in t:
            facts = [
                "Včely mohou rozpoznat lidské tváře.",
                "Sloni nemohou skákat.",
                "Měsíc se vzdaluje od Země 3.8 cm za rok."
            ]
            return random.choice(facts)

        if "words" in t or "slova" in t:
            txt = t.replace("words", "").replace("slova", "").strip()
            if not txt:
                return "Napiš: words tvuj text"
            words = len(txt.split())
            chars = len(txt)
            return f"Slova: {words}, Znaky: {chars}"

        if "morse" in t:
            morse_dict = {
                'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
                'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
                'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
                's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
                'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---',
                '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                '8': '---..', '9': '----.', ' ': '/'
            }
            return ' '.join(morse_dict.get(c, '?') for c in t if c in morse_dict or c == ' ')

        if "video" in t or "convert" in t:
            self.video_converter()
            return "Otevírám konvertor videa..."

        # Příkaz pro spuštění hry Tic-Tac-Toe (Piškvorky)
        # Dvě hráči: X a O si střídavě klikají na políčka
        # Vítěz = ten, kdo první dosáhne tří symbolů v řadě
        if "tictactoe" in t or "ttt" in t:
            self.tic_tac_toe()
            return "Otevírám Tic-Tac-Toe..."

        # Příkaz pro generování náhodného receptu
        # Kombinuje náhodné ingredience, přílohy, koření a způsoby přípravy
        # Výstup: Doporučará každý recept se zdrojovými ingrediencemi
        if "recipe" in t or "recept" in t:
            return self.recipe_generator()

        # Příkaz pro hru Nula Nebo Jedničky (0/1) - hra na osud
        # Hráč si volí 0 nebo 1, počítač si vybere náhodně stejně
        # Pokud se volby shodují = VÝHRA! 🎉 (50% šance na výhru)
        # Pokud se liší = PROHRA 😢 (50% šance na prohru)
        # Podporované klíčové slova: "coin", "01", "0/1", "nula", "flip"
        if "01" in t or "coin" in t or "0/1" in t or "nula" in t or "flip" in t:
            self.coin_flip_game()
            return "Otevírám hru Nula Jedna... 🎰"

        if "exit" in t or "konec" in t or "quit" in t:
            self.root.quit()
            return "Ukončuji aplikaci..."

        # Výchozí případ: pokud žádný příkaz nebyl rozpoznán, nabídni pomoc
        # Uživateli se doporučuje zadat "help" pro seznam všech dostupných příkazů
        return "Neznámý příkaz. Napiš 'help'."

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

    # Metoda pro uložení chatu do souboru
    def save_chat(self):
        # Získáme celý text chatu z widgetu a odstraníme prázdné řádky na konci.
        content = self.chat_history.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Uložit chat", "Chat je prázdný.")
            return
        # Zapíšeme obsah do souboru chat_log.txt s kódováním UTF-8.
        with open("chat_log.txt", "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Uložit chat", "Chat byl uložen do chat_log.txt")

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

    # Metoda pro získání náhodného citátu
    def get_random_quote(self):
        quotes = [
            "Život je jako jízda na kole. Abys udržel rovnováhu, musíš se pohybovat vpřed. - Albert Einstein",
            "Největší sláva není v tom, že nikdy nespadneme, ale v tom, že se vždy zvedneme. - Nelson Mandela",
            "Úspěch není konečný, neúspěch není fatální: je to odvaha pokračovat, co se počítá. - Winston Churchill",
            "Nejlepší způsob, jak předpovědět budoucnost, je ji vytvořit. - Peter Drucker",
            "Život je 10% toho, co se nám stane, a 90% toho, jak na to reagujeme. - Charles R. Swindoll"
        ]
        return random.choice(quotes)

    # Metoda pro zobrazení náhodného citátu dne
    def quote_of_day(self):
        quote = self.get_random_quote()
        messagebox.showinfo("Citát", quote)

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

    # Metoda pro konvertor videa (MOV na MP4)
    def video_converter(self):
        # Vytvoření nového okna (Toplevel) pro konvertor videa
        video_window = tk.Toplevel(self.root)
        video_window.title("Konvertor videa MOV -> MP4")
        video_window.geometry("500x150")

        # Proměnné pro cesty k souborům
        input_var = tk.StringVar()
        output_var = tk.StringVar()

        # První řádek: Label, Entry a Button pro vstupní soubor
        tk.Label(video_window, text="Vstupní MOV:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(video_window, textvariable=input_var, width=40).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(video_window, text="Vybrat...", command=lambda: self.browse_input(input_var, output_var)).grid(row=0, column=2, padx=5, pady=5)

        # Druhý řádek: Label, Entry a Button pro výstupní soubor
        tk.Label(video_window, text="Výstupní MP4:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(video_window, textvariable=output_var, width=40).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(video_window, text="Uložit jako...", command=lambda: self.browse_output(output_var)).grid(row=1, column=2, padx=5, pady=5)

        # Třetí řádek: Tlačítko pro spuštění konverze
        tk.Button(video_window, text="Konvertovat", command=lambda: self.start_conversion(input_var, output_var)).grid(row=2, column=0, columnspan=3, pady=10)

    # Pomocná metoda pro výběr vstupního souboru
    def browse_input(self, input_var, output_var):
        # Otevře dialog pro výběr vstupního MOV souboru.
        path = filedialog.askopenfilename(
            title="Vyber MOV soubor",
            filetypes=[("MOV soubory", "*.mov"), ("Vše", "*.*")]
        )
        if path:
            input_var.set(path)
            # Pokud uživatel nevložil výstupní název, vytvoříme ho automaticky.
            if not output_var.get():
                output_var.set(os.path.splitext(path)[0] + ".mp4")

    # Pomocná metoda pro výběr výstupního souboru
    def browse_output(self, output_var):
        # Otevře dialog pro uložení výstupního MP4 souboru.
        path = filedialog.asksaveasfilename(
            title="Uložit jako MP4",
            defaultextension=".mp4",
            filetypes=[("MP4 soubory", "*.mp4"), ("Vše", "*.*")]
        )
        if path:
            output_var.set(path)

    # Pomocná metoda pro spuštění konverze
    def start_conversion(self, input_var, output_var):
        # Kontrola FFmpeg
        if not self.check_ffmpeg():
            messagebox.showerror("Chyba", "FFmpeg není nainstalován nebo není v PATH.")
            return

        input_file = input_var.get().strip()
        output_file = output_var.get().strip()

        if not input_file or not output_file:
            messagebox.showwarning("Chyba", "Vyber vstupní i výstupní soubor.")
            return

        if not os.path.isfile(input_file):
            messagebox.showerror("Chyba", "Neplatný vstupní soubor.")
            return

        ok, msg = self.convert_mov_to_mp4(input_file, output_file)
        if ok:
            messagebox.showinfo("Hotovo", msg)
        else:
            messagebox.showerror("Chyba", msg)

    # Pomocná metoda pro kontrolu FFmpeg
    def check_ffmpeg(self):
        # Kontroluje, zda je příkaz ffmpeg dostupný v systému.
        try:
            subprocess.run(
                ["ffmpeg", "-version"],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            return True
        except (FileNotFoundError, subprocess.CalledProcessError):
            return False

    # Pomocná metoda pro konverzi MOV na MP4
    def convert_mov_to_mp4(self, input_file, output_file):
        # Spustí ffmpeg příkaz pro převod MOV souboru do MP4 s videokodekem H.264 a audio kodekem AAC.
        try:
            cmd = [
                "ffmpeg",
                "-y",
                "-i", input_file,
                "-c:v", "libx264",
                "-c:a", "aac",
                output_file,
            ]
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True, f"Konverze dokončena: {output_file}"
        except subprocess.CalledProcessError as e:
            err = e.stderr.decode("utf-8", errors="ignore")
            return False, "Chyba při konverzi:\n" + err

    # Metoda pro hru Tic-Tac-Toe
    # Metoda pro spuštění hry Tic-Tac-Toe (Piškvorky)
    # Vytvoří GUI s 3x3 mřížkou tlačítek a inicializuje herní logiqu
    def tic_tac_toe(self):
        # Vytvoření nového okna pro hru Tic-Tac-Toe
        ttt_window = tk.Toplevel(self.root)
        ttt_window.title("Tic-Tac-Toe")
        ttt_window.geometry("300x350")

        # Inicializace herní desky (3x3 mřížka)
        # [['', '', ''],  <- řádek 0
        #  ['', '', ''],  <- řádek 1
        #  ['', '', '']]  <- řádek 2
        # '' = prázdné pole; 'X' nebo 'O' = obsazené pole
        self.board = [['' for _ in range(3)] for _ in range(3)]
        # Určení, kdo začíná (X vždy začíná)
        self.current_player = 'X'

        # Label pro zobrazení aktuálního hráče
        # Font=('Arial', 16) = font Arial o velikosti 16 pixelů
        self.player_label = tk.Label(ttt_window, text="Hráč: X", font=('Arial', 16))
        self.player_label.pack(pady=10)

        # Rámeček pro tlačítka - slučuje všechna tlačítka do jednoho prvku
        button_frame = tk.Frame(ttt_window)
        button_frame.pack()

        # Vytvoření 3x3 mřížky tlačítek (9 tlačítek celkem)
        # Vnější smyčka (i) = řádky (0, 1, 2)
        # Vnitřní smyčka (j) = sloupce (0, 1, 2)
        # Každý button má:
        # - command=lambda r=i, c=j: self.make_move(r, c, ttt_window)
        #   Důvod lambda: v cyklu se proměnné i a j mění; lambda zachytí jejich aktuální hodnotu
        # - grid(row=i, column=j) = umístí button na pozici (i, j) v mřížce
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                # Vytvoření tlačítka s prázdným textem (zobrazí 'X' nebo 'O' po kliknutí)
                btn = tk.Button(button_frame, text='', font=('Arial', 20), width=5, height=2,
                                command=lambda r=i, c=j: self.make_move(r, c, ttt_window))
                # grid = layout manažer pro umísťování widgetů do mřížky
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.buttons.append(row)

        # Tlačítko pro restart hry - umožní začít novou hru bez zavírání okna
        tk.Button(ttt_window, text="Nová hra", command=lambda: self.reset_game(ttt_window)).pack(pady=10)

    # Metoda pro provedení tahu hráče v Tic-Tac-Toe
    # Kontroluje: 1. Zda je políčko prázdné -> 2. Zda hra již neskončila
    #             3. Zaznamená tah -> 4. Ověří výhru/remízu -> 5. Změní hráče
    def make_move(self, row, col, window):
        # Kontrola: políčko je prázdné ('' = neobsazené) a hra ještě neskončila
        if self.board[row][col] == '' and not self.check_winner():
            # Zaznamená tah do herní desky (row, col) s aktuálním hráčem (X nebo O)
            self.board[row][col] = self.current_player
            # Aktualizuje tlačítko na GUI - zobrazí X nebo O
            self.buttons[row][col].config(text=self.current_player)

            # Ověření výsledku tahu: výhra, remíza, nebo pokračování hry
            if self.check_winner():
                # Hráč vyhrál - zobrazit zprávu a deaktivovat tlačítka (hra skončila)
                messagebox.showinfo("Konec hry", f"Hráč {self.current_player} vyhrál!")
                self.disable_buttons()
            elif self.is_draw():
                # Všechna políčka obsazena bez vítěze = remíza
                messagebox.showinfo("Konec hry", "Remíza!")
                self.disable_buttons()
            else:
                # Hra pokračuje - přepnutí na dalšího hráče
                # Ternární operátor: pokud je X, změní na O; jinak na X
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.player_label.config(text=f"Hráč: {self.current_player}")

    # Metoda pro kontrolu vítěze v Tic-Tac-Toe
    # Vrací True pokud je na desce tři stejné symboly v řadě (řádek, sloupec nebo diagonála)
    # Kombinace testů: 3 řádky + 3 sloupce + 2 diagonály = 8 možných výher
    def check_winner(self):
        # Kontrola řádků (i-tý řádek: board[i][0], board[i][1], board[i][2])
        for i in range(3):
            # Ternární srovnání: všechny tři prvky musí být stejné a ne prázdné ('' = prázdné pole)
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True  # Řádek je vyplněn jedním hráčem
            # Kontrola sloupců (i-tý sloupec: board[0][i], board[1][i], board[2][i])
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True  # Sloupec je vyplněn jedním hráčem
        # Kontrola hlavní diagonály (levý horní -> pravý dolní)
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        # Kontrola vedlejší diagonály (pravý horní -> levý dolní)
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        # Pokud žádná podmínka neukazuje na výhru, vítěz dosud není
        return False

    # Metoda pro kontrolu remízy
    # Metoda pro kontrolu remízy v Tic-Tac-Toe
    # Vrací True pokud jsou všechna políčka obsazena bez zjištěného vítěze (=remíza)
    def is_draw(self):
        # Prochází všechny řádky herní desky
        for row in self.board:
            # Pokud najde alespoň jedno prázdné políčko (''), hra ještě pokračuje, není remíza
            if '' in row:
                return False
        # Pokud žádné prázdné políčko nenajde, jsou všechna políčka obsazena = remíza
        return True

    # Metoda pro zakázání tlačítek po konci hry
    # Zabraňuje dalším tahům a zmrazí desku v konečném stavu
    def disable_buttons(self):
        # Procházíme všechny řádky a sloupce 3x3 desky
        for row in self.buttons:
            for btn in row:
                # Nastavujeme stav tlačítka na DISABLED = uživatel nemůže klikat
                btn.config(state=tk.DISABLED)

    # Metoda pro reset/restartování hry Tic-Tac-Toe
    # Vrátí hru do počátečního stavu a vymaže desku
    def reset_game(self, window):
        # Resetování herní desky - všechna políčka na ''
        self.board = [['' for _ in range(3)] for _ in range(3)]
        # Vrácení na prvního hráče (X)
        self.current_player = 'X'
        # Aktualizace labelu na obrazovce
        self.player_label.config(text="Hráč: X")
        # Vymazání textu na všech tlačítcích a umožnění klikání (state=tk.NORMAL)
        for i in range(3):
            for j in range(3):
                # text='' = vymaž obsah; state=tk.NORMAL = aktivuj tlačítko (było DISABLED po konci hry)
                self.buttons[i][j].config(text='', state=tk.NORMAL)

    # Metoda pro generátor náhodných receptů
    def recipe_generator(self):
        # Seznamy pro náhodný výběr
        mains = ["kuřecí maso", "hovězí maso", "vepřové maso", "ryby", "tofu", "cizrna", "špagety", "rýže", "brambory"]
        sides = ["špenát", "mrkev", "cibule", "česnek", "rajčata", "paprika", "zelenina", "salát", "kukuřice"]
        seasonings = ["sůl", "pepř", "oregano", "bazalka", "kurkuma", "paprika", "tymián", "kmín"]
        methods = ["pečte v troubě při 180°C po dobu 30 minut", "vařte na páře 20 minut", "smažte na olivovém oleji 15 minut", "duchte pod pokličkou 25 minut", "grilujte 10 minut z každé strany"]

        # Náhodný výběr
        main = random.choice(mains)
        side = random.choice(sides)
        seasoning = random.choice(seasonings)
        method = random.choice(methods)

        # Sestavení receptu
        recipe = f"Náhodný recept:\n\nHlavní ingredience: {main}\nPříloha: {side}\nKoření: {seasoning}\nZpůsob přípravy: {method}\n\nBon appétit!"
        messagebox.showinfo("Náhodný recept", recipe)
        return recipe

    # ====== HRA 0/1 (NULA JEDNA) ======
    # Jednoduchá hra na osud: hráč volí 0 nebo 1, počítač si vybere náhodně
    # Pokud správně uhodneš, vítězíš! 50/50 šance na výhru
    def coin_flip_game(self):
        # Vytvoření nového okna (Toplevel) pro hru 0/1
        game_window = tk.Toplevel(self.root)
        game_window.title("🎰 Hra Nula Jedna")
        game_window.geometry("350x200")

        # Popis hry a instrukce
        tk.Label(game_window, text="🎰 NULA NEBO JEDNA?", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(game_window, text="Vyber nulu (0) nebo jedničku (1).\nPočítač si vybere náhodně.\nJsou stejné? Vítězíš! 🎉", 
                font=("Arial", 11), justify=tk.CENTER).pack(pady=5)

        # Proměnná pro uložení skutečné volby počítače
        self.computer_choice = None

        # Vnitřní funkce pro logiku hry
        def play(choice):
            # Počítač si vybere náhodně (0 nebo 1)
            self.computer_choice = random.choice([0, 1])
            # Konverze volby na číslo (string → int)
            user_choice = int(choice)

            # Vyhodnocení výsledku
            if user_choice == self.computer_choice:
                # Správní odhad - uživatel vyhrál! 🎉
                result = f"🎉 VYHRÁL JSI! 🎉\n\nTy: {user_choice}\nPočítač: {self.computer_choice}\n✅ Jsou stejné!"
                title = "Vítězství!"
            else:
                # Špatný odhad - uživatel prohrál 😢
                result = f"😢 Ops, prohráls!\n\nTy: {user_choice}\nPočítač: {self.computer_choice}\n❌ Nejsou stejné!"
                title = "Porážka!"

            # Zobrazení výsledku v dialogu
            messagebox.showinfo(title, result)
            game_window.destroy()  # Zavření okna po skončení hry

        # Tlačítka pro výběr - hráč si klika na 0 nebo 1
        # lambda je potřeba pro předání parametru (0 nebo 1) do funkce play()
        button_frame = tk.Frame(game_window)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="0️⃣ NULA", command=lambda: play(0), 
                 bg="#FF6B6B", fg="white", font=("Arial", 12, "bold"), 
                 width=12, height=2).pack(side=tk.LEFT, padx=10)
        
        tk.Button(button_frame, text="1️⃣ JEDIČKA", command=lambda: play(1), 
                 bg="#4ECDC4", fg="white", font=("Arial", 12, "bold"), 
                 width=12, height=2).pack(side=tk.LEFT, padx=10)

        # Informace o šancích
        tk.Label(game_window, text="Šance na výhru: 50% | Šance na prohru: 50%", 
                font=("Arial", 9), fg="gray").pack(pady=10)

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
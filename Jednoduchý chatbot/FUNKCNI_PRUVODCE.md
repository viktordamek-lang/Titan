# 📚 PRŮVODCE FUNKCEMI CHATBOTA

## 🎮 HRY

### Tic-Tac-Toe (Piškvorky)
- **Příkaz:** `tictactoe` / `ttt` nebo Tlačítko "TTT"
- **Co dělá?** Hra pro 2 hráče na 3×3 mřížce. Hráči střídavě klikají na políčka, vítěz je ten, kdo má 3 symboly v řadě (řádek, sloupec nebo diagonála)
- **Jak hrát?** Klikej na prázdná políčka, X vždy začíná. Po konci hry klikni "Nová hra" pro restart

### Kámen-Nůžky-Papír
- **Příkaz:** `rps`
- **Co dělá?** Hra proti počítači. Ty vybeřeš kámen, nůžky nebo papír, počítač si vybere náhodně
- **Pravidla:** Kámen > nůžky > papír > kámen (cyklus)

### Hádání Čísla
- **Příkaz:** `guess` nebo `hádej`
- **Co dělá?** Počítač si myslí číslo v zadaném rozsahu, ty ho hádáš. Program ti řekne, zda je příliš nízké/vysoké

---

## 🧮 KALKULAČKY

### BMI Kalkulačka (Body Mass Index)
- **Tlačítko:** "BMI"
- **Co dělá?** Vypočítá tvůj BMI na základě váhy a výšky. Řekne ti, zda máš normální váhu, podváhu, nadváhu nebo obezitu
- **Vzorec:** BMI = váha (kg) / (výška (m))²
- **Př.:** Váha 70kg, výška 175cm → BMI ≈ 22.9 (Normální)

### Převodník Jednotek
- **Příkaz:** `unit 100 cm m` 
- **Co dělá?** Převádí délkové jednotky
- **Podporované:** m (metr), cm, mm, km, in (palec), ft (stopa), yd (yard)
- **Př.:** `unit 1000 m km` → 1000 m = 1.0 km

### Převodník Teploty
- **Příkaz:** `temp 32 F C`
- **Co dělá?** Konvertuje mezi Celsia (°C), Fahrenheita (°F) a Kelvinem (K)
- **Př.:** `temp 0 C F` → 0°C = 32.0°F

### Převodník Měn
- **Tlačítko:** "Měna" (po přidání)
- **Co dělá?** Převádí z CZK na EUR, USD, GBP (přibližné kurzy)
- **Př.:** 1000 CZK = 40 EUR

### Pomoc s Matematikou
- **Tlačítko:** "Matika"
- **Co dělá?** Jednoduchá kalkulačka na 4 operace: +, -, *, /
- **Upozornění:** Hlásí chybu při dělení nulou

### Kalkulačka (příkazem)
- **Příkaz:** `calc 2+3*4` nebo `math 10/2`
- **Co dělá?** Vypočítá matematický výraz bezpečně (bez spouštění nebezpečného kódu)
- **Příklady:** 
  - `calc 100/5` → 20
  - `calc 2**8` → 256 (mocnina)

### Generování Hesla
- **Příkaz:** `pass 12` nebo `password 16`
- **Co dělá?** Vygeneruje náhodné bezpečné heslo zadané délky (s písmeny, číslicemi, speciálními znaky)
- **Př.:** `pass 12` → vygeneruje 12-znakové heslo

---

## ℹ️ INFORMACE

### Vtip Dne
- **Tlačítko:** "Vtip"
- **Příkaz:** `joke` nebo `vtip`
- **Co dělá?** Zobrazí náhodný programátorský vtip

### Citát Dne
- **Tlačítko:** "Citát"
- **Příkaz:** `quote` nebo `citát`
- **Co dělá?** Zobrazí motivační citát od slavných osobností

### Náhodný Fakt
- **Příkaz:** `fact` nebo `fakt`
- **Co dělá?** Sdělí ti zajímavý vědecký fakt (např. o zvířatech, vesmíru)

### Datum a Čas
- **Příkaz:** `time`, `čas`, `den`, `dnes` nebo `datum`
- **Co dělá?** Zobrazí aktuální datum a čas v detailu

### Kalkulačka Věku
- **Příkaz:** `age 1990 5 15`
- **Co dělá?** Vypočítá tvůj věk na základě data narození (rok měsíc den)
- **Forma:** `age YYYY MM DD`

---

## 📝 TEXTOVÉ NÁSTROJE

### Poznámkový Blok
- **Tlačítko:** "Poznámky"
- **Co dělá?** Textový editor pro psaní a ukládání poznámek do souboru `poznamky.txt`
- **Možnosti:** Uložit poznámky, Načíst uložené poznámky

### Počítadlo Slov
- **Příkaz:** `words Ahoj světe jak se máš`
- **Co dělá?** Spočítá počet slov, znaků a řádků
- **Výstup:** Slova: 5, Znaky: 23, Řádky: 1

### Morseova Abeceda
- **Příkaz:** `morse SOS` nebo `morse HELP`
- **Co dělá?** Převede text do Morseovy abecedy (. = tečka, - = čárka)
- **Př.:** `morse SOS` → `... --- ...`

---

## 📊 WEBOVÉ FUNKCE

### Počasí
- **Tlačítko:** "Počasí"
- **Příkaz:** `weather Praha` nebo `počasí Brno`
- **Co dělá?** Zjistí aktuální počasí pro zadané město (zdarma API wttr.in)
- **Výstup:** Teplota, popis počasí, vlhkost

### Webové Vyhledávání
- **Tlačítko:** "Vyhledat"
- **Příkaz:** `search Python tutoriál` nebo `vyhledat recepty`
- **Co dělá?** Otevře prohlížeč s výsledky Googlu na zadaný dotaz

---

## 🎥 MULTIMÉDIA

### Konvertor Videa (MOV → MP4)
- **Tlačítko:** "Video"
- **Co dělá?** Konvertuje video v režimu MOV do formátu MP4 (H.264 video + AAC audio)
- **Požadavek:** Musíš mít nainstalován **FFmpeg**
- **Instalace FFmpeg:** 
  - Mac: `brew install ffmpeg`
  - Linux: `apt-get install ffmpeg`
  - Windows: Stáhni z ffmpeg.org

---

## 🎲 GENERÁTORY

### Generátor Přezdívek
- **Příkaz:** `nick` nebo `přezdívka`
- **Co dělá?** Vygeneruje náhodnou přezdívku (adjektivum + zvířě)
- **Př.:** "Rychlý Lev", "Moudrý Delfín"

### Generátor Receptů
- **Tlačítko:** "Recept"
- **Příkaz:** `recipe` nebo `recept`
- **Co dělá?** Vygeneruje náhodný recept kombinací ingrediencí a způsobů přípravy

---

## 🎯 HODINOVKY

### Hod Kostkou
- **Příkaz:** `dice` nebo `kostka`
- **Co dělá?** Simuluje hod šestistrannou kostkou (1-6)

### Kalkulačka Věku (Speedrun)
- **Příkaz:** `age 2005 3 14`
- **Co dělá?** Vypočítá věk rychle (včetně kontroly, zda byly narozeniny letos)

---

## 📱 HISTÓRIA & SPRÁVA

### Uložit Chat
- **Tlačítko:** "Uložit chat"
- **Co dělá?** Uloží celou historii chatu do souboru `chat_log.txt`

### Vymazat Chat
- **Příkaz:** `clear` / `vymazat` / `clear chat`
- **Co dělá?** Smaže všechny zprávy z chatu (VRÁTIT SE NEDÁ!)

### Historie Příkazů
- **Příkaz:** `history` / `historie`
- **Co dělá?** Zobrazí poslední 20 příkazů, které jsi zadal/a
- **Klávesnice:** ↑ / ↓ šipky pro navigaci v historii

### Historie Kalkulačky
- **Tlačítko:** "Calc historie"
- **Příkaz:** `calc history`
- **Co dělá?** Zobrazí poslední 20 matematických výpočtů

---

## ⚙️ NASTAVENÍ

### Uživatelská Nastavení
- **Tlačítko:** "⚙️ Nastavení"
- **Co tam je:**
  
  **Vzhled:**
  - 🌐 Jazyk: CZ (čeština) / EN (angličtina)
  - 🔤 Velikost fontu: 8-16 pixelů
  - 🌓 Tema: Světlý (bílé pozadí) / Tmavý (tmavé pozadí)
  
  **Chování:**
  - 💾 Automatické ukládání: chat se sám ukládá
  - 🔔 Notifikace: zobrazují se upozornění

### Tmavý Režim
- **Co dělá?** Změní barvy na tmavé (oči si odpočinou 👀)
- **Barvy v tmavém režimu:**
  - Pozadí: Tmavě šedá (#2b2b2b)
  - Text: Bílá (#ffffff)

---

## 🔧 POKROČILÉ TIPY

### Bezpečné Výpočty
- Kalkulačka (`calc`) používá AST (Abstract Syntax Tree) pro bezpečnost
- Zabraňuje nebezpečným příkazům jako `__import__('os').system()`

### List Slicing v Historii
- Příkaz `history` vrátí poslední 20 prvků: `command_history[-20:]`
- `-20` znamená počítej od 20. prvku od konce

### Lambda Funkce v Tlačítkách
- Tlačítka používají lambda pro předání parametrů: `lambda: self.make_move(r, c, window)`
- Bez lambda by se funkce zavolala hned při vytváření tlačítka

---

## ❓ POMOC V APLIKACI

### Příkaz Help
- **Příkaz:** `help` / `?` / `pomoc`
- **Co vrátí?** Seznam všech dostupných příkazů

### Podrobná Nápověda
- **Příkaz:** `help all` 
- **Co vrátí?** Seznam všech funkcí s kratším popisem

### Chat Nápověda
- **Příkaz:** `help chat`
- **Co vrátí?** Příklady chatových příkazů

---

## 🚀 SPUŠTĚNÍ APLIKACE

```bash
python3 ChatbotApp.py
```

---

## 📋 SEZNAM VŠECH PŘÍKAZŮ

```
help, help all, help chat, ahoj, jak se máš, co umíš, děkuji,
calc, unit, pass, joke, time, quote, nick, currency, bmi, rps, temp,
dice, age, fact, words, morse, reverse, video, weather, search,
calc history, ask, tictactoe, recipe, mood, math,
clear, history, exit
```

---

**Poslední aktualizace:** 25. dubna 2026
**Verze:** 2.0 (s nastavením a komentáři)

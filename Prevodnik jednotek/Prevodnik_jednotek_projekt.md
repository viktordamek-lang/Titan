# Převodník jednotek

## Popis a cíl projektu

Převodník jednotek je jednoduchá konzolová aplikace napsaná v jazyce Python. Program umožňuje převádět hodnoty mezi různými jednotkami délky. Cílem projektu je vytvořit nástroj, který uživateli umožní rychle a jednoduše převést zadanou hodnotu z jedné jednotky do druhé bez nutnosti ručního výpočtu.

Program je určen především pro studenty, kteří potřebují převádět jednotky při studiu matematiky, fyziky nebo technických oborů. Může být však užitečný pro každého uživatele, který potřebuje rychlý převod mezi běžnými jednotkami délky.

## Funkcionalita programu

Program obsahuje následující funkce:

* Zadání jednotky, ze které se má převádět.
* Zadání jednotky, do které se má převádět.
* Výpočet převodního faktoru mezi zadanými jednotkami.
* Zobrazení výsledku převodu uživateli.

Program pracuje s těmito jednotkami délky:

* metr (m)
* centimetr (cm)
* milimetr (mm)
* kilometr (km)
* palec (in)
* stopa (ft)
* yard (yd)

Pokud uživatel zadá neplatnou jednotku, program vrátí informaci o chybě.

## Technická část

Program je napsán v programovacím jazyce **Python** a využívá pouze základní funkce jazyka bez externích knihoven.

### Použité prvky programu

* **Funkce** `prevodnik_jednotek()` pro výpočet převodu mezi jednotkami.
* **Slovník (dictionary)** pro uložení převodních faktorů jednotlivých jednotek vůči metru.
* **Podmínky (if)** pro kontrolu, zda zadané jednotky existují v seznamu.
* **Vstup od uživatele (input)** pro zadání jednotek.
* **Výstup na obrazovku (print)** pro zobrazení výsledku.

### Datové struktury

Program využívá datovou strukturu **dictionary**, která ukládá převodní faktory jednotlivých jednotek.

Příklad:

* metr = 1
* centimetr = 0.01
* milimetr = 0.001
* kilometr = 1000

Díky této struktuře lze jednoduše vypočítat převod mezi libovolnými dvěma jednotkami.

### Možná rozšíření programu

Program lze v budoucnu rozšířit například o:

* převody dalších jednotek (hmotnost, objem, teplota),
* grafické uživatelské rozhraní,
* možnost převádět více hodnot za sebou bez restartování programu.

Projektová dokumentace
Jednoduchý chatbot v Pythonu
1. Úvod
Tento projekt představuje jednoduchého chatbota naprogramovaného v programovacím jazyce Python. Chatbot je určen pro práci v textové konzoli a umožňuje uživateli využívat několik různých funkcí, například jednoduché matematické výpočty, převod jednotek, generování hesel nebo hraní jednoduché hry.
Cílem projektu je vytvořit interaktivní program, který kombinuje více funkcí do jednoho přehledného menu a zároveň demonstruje základní principy programování v Pythonu, jako jsou cykly, podmínky, funkce knihoven a práce se vstupem uživatele.
2. Cíl projektu
Cílem projektu je vytvořit jednoduchého chatbota, který:
komunikuje s uživatelem pomocí textu
nabízí více užitečných nebo zábavných funkcí
využívá základní programovací konstrukce Pythonu
je přehledný a snadno rozšiřitelný
Program má také sloužit jako praktická ukázka práce s knihovnami a interaktivním menu.
3. Použité technologie
Programovací jazyk
Python 3
Použité knihovny
random – generování náhodných čísel, hesel, vtipů a přezdívek
string – obsahuje znaky pro generování hesel
datetime – zobrazení aktuálního data a času
requests – získání aktuálního počasí z internetové služby
4. Funkce programu
Program obsahuje 11 hlavních funkcí, které si uživatel vybírá z menu.
4.1 Povídání o náladě
Uživatel zadá svou aktuální náladu a chatbot na ni reaguje jednoduchou odpovědí.
Podporované odpovědi:
dobře
špatně
unaveně
nadšeně
4.2 Pomoc s matematikou
Chatbot provede jednoduchý matematický výpočet.
Podporované operace:
sčítání (+)
odčítání (-)
násobení (*)
dělení (/)
Program kontroluje dělení nulou.
4.3 Převodník jednotek
Uživatel může převádět délkové jednotky mezi sebou.
Podporované jednotky:
metr (m)
centimetr (cm)
milimetr (mm)
kilometr (km)
palec (in)
stopa (ft)
yard (yd)
Převod probíhá pomocí převodních faktorů uložených ve slovníku.
4.4 Generování náhodného hesla
Program vytvoří náhodné heslo podle délky, kterou zadá uživatel.
Heslo může obsahovat:
malá a velká písmena
čísla
speciální znaky
4.5 Ukončení programu
Tato volba ukončí hlavní smyčku programu a chatbot se vypne.
4.6 Hádání čísla
Jednoduchá hra, ve které:
uživatel zadá rozsah
program vygeneruje náhodné číslo
uživatel se ho snaží uhodnout
Program dává nápovědu:
příliš nízké
příliš vysoké
4.7 Generátor vtipů
Program náhodně vybere jeden vtip ze seznamu uloženého v programu.
4.8 Datum a čas
Program zobrazí aktuální datum a čas pomocí knihovny datetime.
4.9 Citát dne
Chatbot náhodně vybere jeden motivační citát z připraveného seznamu.
4.10 Generátor přezdívek
Program vytvoří náhodnou přezdívku kombinací:
přídavného jména
zvířete
Například:
Rychlý Lev
Tichá Sova
4.11 Zobrazení počasí
Program využívá webovou službu wttr.in a zobrazí aktuální počasí pro zadané město.
Používá knihovnu requests pro komunikaci s webovým API.
5. Struktura programu
Program je založen na nekonečné smyčce (while True), která zobrazuje menu.
Hlavní kroky programu:
přivítání uživatele
zadání jména
zobrazení menu
výběr funkce
provedení vybrané funkce
návrat do menu nebo ukončení programu
6. Ošetření chyb
Program obsahuje základní kontrolu chyb:
kontrola dělení nulou
kontrola správnosti rozsahu při hádání čísla
kontrola platnosti jednotek
ošetření chyby při připojení k internetu při načítání počasí
7. Možná rozšíření programu
Do budoucna by bylo možné přidat například:
grafické rozhraní (Tkinter nebo PyQt)
více matematických funkcí
ukládání historie konverzace
připojení k API pro skutečného AI chatbota
více her
lepší generátor citátů a vtipů
8. Závěr
Projekt jednoduchého chatbota ukazuje základní možnosti programování v Pythonu. Program kombinuje několik funkcí do jednoho interaktivního systému a umožňuje uživateli využívat různé nástroje i zábavné prvky.
Program je jednoduchý, přehledný a může sloužit jako základ pro další rozšiřování a učení programování.

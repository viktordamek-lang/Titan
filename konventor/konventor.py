# Import potřebných modulů
# os - pro práci se souborovými cestami a kontrolu existence souborů
# subprocess - pro spouštění externích příkazů (FFmpeg)
# tkinter - pro vytvoření grafického uživatelského rozhraní
import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

# Funkce pro kontrolu, zda je FFmpeg nainstalován
# Spustí příkaz 'ffmpeg -version' a zkontroluje, zda skončí úspěšně
# stdout a stderr jsou přesměrovány do PIPE, aby se nezobrazovaly v konzoli
def check_ffmpeg():
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            check=True,  # Vyhodí výjimku, pokud příkaz skončí s nenulovým exit kódem
            stdout=subprocess.PIPE,  # Přesměruje standardní výstup
            stderr=subprocess.PIPE,  # Přesměruje chybový výstup
        )
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

# Funkce pro konverzi MOV souboru na MP4 pomocí FFmpeg
# Parametry FFmpeg:
# -y: přepíše výstupní soubor bez dotazu
# -i: vstupní soubor
# -c:v libx264: kodek pro video (H.264)
# -c:a aac: kodek pro audio (AAC)
def convert_mov_to_mp4(input_file, output_file):
    try:
        cmd = [
            "ffmpeg",
            "-y",  # Přepíše výstup bez dotazu
            "-i", input_file,  # Vstupní soubor
            "-c:v", "libx264",  # Video kodek H.264
            "-c:a", "aac",  # Audio kodek AAC
            output_file,  # Výstupní soubor
        ]
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True, f"Konverze dokončena: {output_file}"
    except subprocess.CalledProcessError as e:
        # Zachytí chybu a dekóduje chybový výstup z FFmpeg
        err = e.stderr.decode("utf-8", errors="ignore")
        return False, "Chyba při konverzi:\n" + err

# Funkce pro výběr vstupního souboru
# Otevře dialog pro výběr MOV souboru
# Automaticky nastaví výstupní cestu, pokud není zadána
def browse_input():
    path = filedialog.askopenfilename(
        title="Vyber MOV soubor",
        filetypes=[("MOV soubory", "*.mov"), ("Vše", "*.*")]  # Filtry pro typy souborů
    )
    if path:
        input_var.set(path)
        # Pokud není nastaven výstup, vytvoří cestu s .mp4 příponou
        if not output_var.get():
            output_var.set(os.path.splitext(path)[0] + ".mp4")

# Funkce pro výběr výstupního souboru
# Otevře dialog pro uložení jako MP4 soubor
def browse_output():
    path = filedialog.asksaveasfilename(
        title="Uložit jako MP4",
        defaultextension=".mp4",  # Výchozí přípona
        filetypes=[("MP4 soubory", "*.mp4"), ("Vše", "*.*")]
    )
    if path:
        output_var.set(path)

# Funkce pro spuštění konverze
# Provede všechny kontroly před konverzí a spustí ji
def start_conversion():
    # Kontrola, zda je FFmpeg dostupný
    if not check_ffmpeg():
        messagebox.showerror("Chyba", "ffmpeg není nainstalovaný nebo není v PATH.")
        return

    # Získání a očištění cest k souborům
    input_file = input_var.get().strip()
    output_file = output_var.get().strip()

    # Kontrola, zda jsou oba soubory zadány
    if not input_file or not output_file:
        messagebox.showwarning("Chyba", "Vyber vstupní i výstupní soubor.")
        return

    # Kontrola existence vstupního souboru
    if not os.path.isfile(input_file):
        messagebox.showerror("Chyba", "Neplatný vstupní soubor.")
        return

    # Spuštění konverze
    ok, msg = convert_mov_to_mp4(input_file, output_file)
    if ok:
        messagebox.showinfo("Hotovo", msg)
    else:
        messagebox.showerror("Chyba", msg)

# Hlavní část programu - vytvoření grafického uživatelského rozhraní
if __name__ == "__main__":
    # Vytvoření hlavního okna aplikace
    root = tk.Tk()
    root.title("MOV -> MP4 konvertor")  # Titulek okna
    root.geometry("660x140")  # Velikost okna (šířka x výška)

    # Proměnné pro ukládání cest k souborům
    input_var = tk.StringVar()   # Pro vstupní soubor
    output_var = tk.StringVar()  # Pro výstupní soubor

    # První řádek: Label, Entry a Button pro vstupní soubor
    tk.Label(root, text="Vstupní MOV:").grid(row=0, column=0, padx=5, pady=5, sticky="w")  # Popisek
    tk.Entry(root, textvariable=input_var, width=50).grid(row=0, column=1, padx=5, pady=5)  # Vstupní pole
    tk.Button(root, text="Vybrat...", command=browse_input).grid(row=0, column=2, padx=5, pady=5)  # Tlačítko pro výběr

    # Druhý řádek: Label, Entry a Button pro výstupní soubor
    tk.Label(root, text="Výstupní MP4:").grid(row=1, column=0, padx=5, pady=5, sticky="w")  # Popisek
    tk.Entry(root, textvariable=output_var, width=50).grid(row=1, column=1, padx=5, pady=5)  # Vstupní pole
    tk.Button(root, text="Uložit jako...", command=browse_output).grid(row=1, column=2, padx=5, pady=5)  # Tlačítko pro uložení

    # Třetí řádek: Tlačítko pro spuštění konverze
    tk.Button(root, text="Konvertovat", command=start_conversion, width=20).grid(row=2, column=0, columnspan=3, pady=10)

    # Spuštění hlavní smyčky aplikace (čeká na události)
    root.mainloop()



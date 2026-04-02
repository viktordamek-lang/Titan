# Program pro odstranění okolního hluku z videa - zachování lidské řeči
# Používá FFmpeg pro zpracování audio s bandpass filtrem pro izolaci řeči (300-3400 Hz)

import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
import cv2  # Pro nahrávání z kamery

# Funkce pro kontrolu FFmpeg
def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

# Funkce pro nahrávání videa z kamery
def record_video(output_file):
    cap = cv2.VideoCapture(0)  # 0 pro výchozí kameru
    if not cap.isOpened():
        messagebox.showerror("Chyba", "Nelze otevřít kameru.")
        return False

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    messagebox.showinfo("Nahrávání", "Začíná nahrávání. Stiskněte 'q' pro zastavení.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        cv2.imshow('Nahrávání', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    return True

# Funkce pro zpracování videa - odstranění hluku
def process_video(input_file, output_file):
    try:
        # Extrakce audio z videa
        audio_temp = "temp_audio.wav"
        cmd_extract = [
            "ffmpeg", "-y", "-i", input_file, "-vn", "-acodec", "pcm_s16le", audio_temp
        ]
        subprocess.run(cmd_extract, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Aplikace bandpass filtru pro řeč (300-3400 Hz) - odstranění nízkého a vysokého hluku
        audio_filtered = "temp_filtered.wav"
        cmd_filter = [
            "ffmpeg", "-y", "-i", audio_temp, "-af", "highpass=f=300,lowpass=f=3400", audio_filtered
        ]
        subprocess.run(cmd_filter, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Spojení filtrovaného audio s původním video
        cmd_merge = [
            "ffmpeg", "-y", "-i", input_file, "-i", audio_filtered, "-c:v", "copy", "-c:a", "aac", "-map", "0:v:0", "-map", "1:a:0", output_file
        ]
        subprocess.run(cmd_merge, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Vyčištění dočasných souborů
        os.remove(audio_temp)
        os.remove(audio_filtered)

        return True, f"Zpracování dokončeno: {output_file}"
    except subprocess.CalledProcessError as e:
        err = e.stderr.decode("utf-8", errors="ignore")
        return False, "Chyba při zpracování:\n" + err

# Funkce pro výběr vstupního souboru
def browse_input():
    path = filedialog.askopenfilename(
        title="Vyber video soubor",
        filetypes=[("Video soubory", "*.mp4 *.mov *.avi *.mkv"), ("Vše", "*.*")]
    )
    if path:
        input_var.set(path)
        # Automaticky nastavit výstup
        if not output_var.get():
            base, ext = os.path.splitext(path)
            output_var.set(base + "_bez_hluku" + ext)

# Funkce pro nahrávání z kamery
def start_recording():
    path = filedialog.asksaveasfilename(
        title="Uložit nahrané video",
        defaultextension=".mp4",
        filetypes=[("MP4 soubory", "*.mp4"), ("Vše", "*.*")]
    )
    if path:
        if record_video(path):
            messagebox.showinfo("Hotovo", f"Video nahráno: {path}")
            input_var.set(path)
            # Automaticky nastavit výstup
            base, ext = os.path.splitext(path)
            output_var.set(base + "_bez_hluku" + ext)

# Funkce pro výběr výstupního souboru
def browse_output():
    path = filedialog.asksaveasfilename(
        title="Uložit zpracované video",
        defaultextension=".mp4",
        filetypes=[("MP4 soubory", "*.mp4"), ("Vše", "*.*")]
    )
    if path:
        output_var.set(path)

# Funkce pro spuštění zpracování
def start_processing():
    if not check_ffmpeg():
        messagebox.showerror("Chyba", "FFmpeg není nainstalován.")
        return

    input_file = input_var.get().strip()
    output_file = output_var.get().strip()

    if not input_file or not output_file:
        messagebox.showwarning("Chyba", "Vyber vstupní i výstupní soubor.")
        return

    if not os.path.isfile(input_file):
        messagebox.showerror("Chyba", "Neplatný vstupní soubor.")
        return

    ok, msg = process_video(input_file, output_file)
    if ok:
        messagebox.showinfo("Hotovo", msg)
    else:
        messagebox.showerror("Chyba", msg)

# Hlavní GUI
root = tk.Tk()
root.title("Odstranění okolního hluku z videa")
root.geometry("600x180")

input_var = tk.StringVar()
output_var = tk.StringVar()

tk.Label(root, text="Vstupní video:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
tk.Entry(root, textvariable=input_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Vybrat...", command=browse_input).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Nebo nahrát z kamery:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.Button(root, text="Nahrát video", command=start_recording).grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Výstupní video:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
tk.Entry(root, textvariable=output_var, width=50).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text="Uložit jako...", command=browse_output).grid(row=2, column=2, padx=5, pady=5)

tk.Button(root, text="Zpracovat video", command=start_processing, width=20).grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
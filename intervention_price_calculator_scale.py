import tkinter as tk
import webbrowser

def calculeaza_valoare_interventie():
    curs_valutar = float(curs_valutar_entry.get())
    tarif_interventie = (curs_valutar * 25) * 1.19
    valoare_interventie_label.config(text=f"Valoarea interventiei este {tarif_interventie:.2f} Ron")

def calculeaza_tarif_deplasare():
    curs_valutar = float(curs_valutar_entry.get())
    numar_km = float(numar_km_entry.get())
    deplasare = (0.25 * curs_valutar * numar_km) * 1.19
    tarif_deplasare_label.config(text=f"Tarif deplasare este {deplasare:.2f} Ron")

def aduna_rezultate():
    curs_valutar = float(curs_valutar_entry.get())
    tarif_interventie = (curs_valutar * 25) * 1.19
    numar_km = float(numar_km_entry.get())
    tarif_deplasare = (0.25 * curs_valutar * numar_km) * 1.19
    total = tarif_interventie + tarif_deplasare
    total_label.config(text=f"Total: {total:.2f} Ron")
    # Sub linia asta introducem textul explicativ al aplicatiei
    print("***********************************************")
    text_informativ_label.config(text="Interventia se calculeaza la un tarif de 25 Euro / Interventie + TVA")
    text2_informativ_label.config(text="Deplasarea se calculeaza la un tarif de 0.25 Euro/ Kilometru / Deplasare + TVA")

def deschide_link_curs_valutar():
    webbrowser.open_new("https://www.cursbnr.ro/")


# Crearea ferestrei principale
root = tk.Tk()
root.title("Aplicatie Calculator Tarife Interventie Scale Expert")
#root.option_add("*Font", "Arial 20 bold") # Dimensiune si stil font titlu

# Rezolutie fereastra grafica
root.geometry("640x480")

# Eticheta pentru introducerea cursului valutar
curs_valutar_label = tk.Label(root, text="Introduceti cursul valutar de azi:", fg="grey", font=("Arial", 14,))
curs_valutar_label.grid(row=0, column=0)

# Caseta de text pentru introducerea cursului valutar
curs_valutar_entry = tk.Entry(root, width=10, fg="grey",  font=("Arial", 16)) # Modific latimea casetei de text cu width si cu font modific inaltimea prin marimea textului
curs_valutar_entry.grid(row=0, column=1, padx=5, pady=5)

#Linkul web pentru cursul valutar
link_curs_valutar = tk.Label(root, text="Vezi cursul valutar aici", fg="blue", cursor="hand2", font=("Arial", 12, "bold"))
link_curs_valutar.grid(row=0, column=2)
link_curs_valutar.bind("<Button-1>", lambda e: deschide_link_curs_valutar())

# Buton pentru calculul valorii interventiei
valoare_interventie_button = tk.Button(root, text="Calculeaza Valoare Interventie", fg="grey", command=calculeaza_valoare_interventie, font=("Arial", 13))
valoare_interventie_button.grid(row=1, column=0, columnspan=3, pady=5)

# Eticheta pentru afișarea valorii interventiei
valoare_interventie_label = tk.Label(root, text="Valoarea interventiei este: ", fg="grey",  font=("Arial", 14, "bold")) # Marime si tip font
valoare_interventie_label.grid(row=2, column=0, columnspan=3)

# Eticheta pentru introducerea numărului de kilometri
numar_km_label = tk.Label(root, text="Introduceti nr. de KM parcursi: ",font=("Arial", 14), fg="grey")
numar_km_label.grid(row=3, column=0)

# Caseta de text pentru introducerea numărului de kilometri
numar_km_entry = tk.Entry(root, width=10, fg="grey", font=("Arial", 16)) # Modificarea lățimii casetei de text si inaltimea cu font
numar_km_entry.grid(row=3, column=1, padx=5, pady=5)

# Buton pentru calculul tarifului deplasării
tarif_deplasare_button = tk.Button(root, text="Calculeaza Tarif Deplasare", command=calculeaza_tarif_deplasare, fg="grey", font=("Arial", 13))
tarif_deplasare_button.grid(row=4, column=0, columnspan=3, pady=5)

# Eticheta pentru afișarea tarifului deplasării
tarif_deplasare_label = tk.Label(root, text="Tariful deplasarii este: ", fg="grey", font=("Arial", 14))
tarif_deplasare_label.grid(row=5, column=0, columnspan=3)

# Buton pentru calculul totalului
total_button = tk.Button(root, text="Calculeaza Total", command=aduna_rezultate, font=("Arial", 14, "bold"))
total_button.grid(row=6, column=0, columnspan=3, pady=10)

# Eticheta pentru afișarea totalului
total_label = tk.Label(root, text="Totalul interventiei este: ", font=("Arial", 15, "bold"))
total_label.grid(row=7, column=0, columnspan=3)

# Eticheta pentru textul informativ sub total
text_informativ_label = tk.Label(root, text="Interventia se calculeaza la un tarif de 25 Euro / Interventie + TVA", fg="red", font=("Arial", 10))
text_informativ_label.grid(row=13, column=0, columnspan=3)

# Eticheta pentru textul informativ sub total
text2_informativ_label = tk.Label(root, text="Deplasarea se calculeaza la un tarif de 0.25 Euro/ Kilometru / Deplasare + TVA", fg="red", font=("Arial", 10))
text2_informativ_label.grid(row=15, column=0, columnspan=3)

# Rulează bucla evenimentelor
root.mainloop()

 # de creat executabil , program testat 
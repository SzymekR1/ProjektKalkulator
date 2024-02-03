import tkinter as tk
import time


def oblicz():
    liczba_nr_1 = float(entry_liczba_nr_1.get())
    liczba_nr_2 = float(entry_liczba_nr_2.get())
    wybor = wybor_var.get()

    if wybor == "Dodawanie":
        wynik = liczba_nr_1 + liczba_nr_2
    elif wybor == "Odejmowanie":
        wynik = liczba_nr_1 - liczba_nr_2
    elif wybor == "Mnożenie":
        wynik = liczba_nr_1 * liczba_nr_2
    elif wybor == "Dzielenie":
        if liczba_nr_2 == 0:
            wynik = "Nie można dzielić przez zero!"
        else:
            wynik = liczba_nr_1 / liczba_nr_2
    else:
        wynik = "Błąd"

    label_wynik.config(text="Wynik: " + str(wynik))


root = tk.Tk()
root.title("Prosty kalkulator")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

entry_liczba_nr_1 = tk.Entry(frame)
entry_liczba_nr_1.grid(row=0, column=1)

entry_liczba_nr_2 = tk.Entry(frame)
entry_liczba_nr_2.grid(row=1, column=1)

label_liczba_nr_1 = tk.Label(frame, text="Liczba 1:")
label_liczba_nr_1.grid(row=0, column=0)

label_liczba_nr_2 = tk.Label(frame, text="Liczba 2:")
label_liczba_nr_2.grid(row=1, column=0)

wybor_var = tk.StringVar()
wybor_var.set("Dodawanie")
wybor_label = tk.Label(frame, text="Wybierz działanie:")
wybor_label.grid(row=2, column=0)
wybor_menu = tk.OptionMenu(frame, wybor_var, "Dodawanie", "Odejmowanie", "Mnożenie", "Dzielenie")
wybor_menu.grid(row=2, column=1)

button_oblicz = tk.Button(frame, text="Oblicz", command=oblicz)
button_oblicz.grid(row=3, column=0, columnspan=2)

label_wynik = tk.Label(frame, text="Wynik: ")
label_wynik.grid(row=4, column=0, columnspan=2)

root.mainloop()
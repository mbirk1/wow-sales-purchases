import tkinter
from tkinter import *
from tkinter import messagebox

import requests
import ttkbootstrap as tb
from PIL import ImageTk, Image
from ttkbootstrap.constants import *

# Erstellen des Anwendungsfensters
root = tb.Window(themename="superhero")
root.geometry("1000x400")
root.title("WoW: Sales and Purchases")

# Erstellen des Frames, in dem Tabelle, Dropdown-Menüs und Button sind.
frame = tkinter.Frame(root)

# Pfeilsymbol für Dropdown-Menüs konvertieren.
img = (Image.open("img/arrow-down-solid.png"))
img_resized = img.resize((10, 12))
dropdown_menu_arrow_symbol = ImageTk.PhotoImage(img_resized)

# Liste der Optionen, die ein User wählen kann
options = [
    "aktueller Preis",
    "höchster Preis",
    "niedrigster Preis",
    "alle Preise",
    "zurücksetzen"
]

# Erstellen der Tabelle, in der die Daten eingetragen werden.
name_of_item = Label(frame, text="Name", width=20, height=3, borderwidth=1, relief="solid")
recent_price = Label(frame, text="aktueller Preis", width=20, height=3, borderwidth=1, relief="solid")
highest_price = Label(frame, text="höchster Preis", width=20, height=3, borderwidth=1, relief="solid")
lowest_price = Label(frame, text="niedrigster Preis", width=20, height=3, borderwidth=1, relief="solid")
name_of_item.grid(row=0, column=0)
recent_price.grid(row=0, column=1)
highest_price.grid(row=0, column=2)
lowest_price.grid(row=0, column=3)

welpling = Label(frame, text="Welpling", width=20, height=4, borderwidth=1, relief="solid")
welpling_recent_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
welpling_highest_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
welpling_lowest_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
welpling.grid(row=1, column=0)
welpling_recent_price.grid(row=1, column=1)
welpling_highest_price.grid(row=1, column=2)
welpling_lowest_price.grid(row=1, column=3)

adamantiterz = Label(frame, text="Adamantiterz", width=20, height=4, borderwidth=1, relief="solid")
adamantiterz_recent_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
adamantiterz_highest_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
adamantiterz_lowest_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
adamantiterz.grid(row=2, column=0)
adamantiterz_recent_price.grid(row=2, column=1)
adamantiterz_highest_price.grid(row=2, column=2)
adamantiterz_lowest_price.grid(row=2, column=3)

elementiumband = Label(frame, text="Elementiumband", width=20, height=4, borderwidth=1, relief="solid")
elementiumband_recent_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
elementiumband_highest_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
elementiumband_lowest_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
elementiumband.grid(row=3, column=0)
elementiumband_recent_price.grid(row=3, column=1)
elementiumband_highest_price.grid(row=3, column=2)
elementiumband_lowest_price.grid(row=3, column=3)

# Erstellen der Variable, die die aktuell ausgewählte Option für die Dropdown-Menüs enthält.
please_choose = "Bitte auswählen"

clicked_welpling = StringVar()
clicked_welpling.set(please_choose)
clicked_adamantiterz = StringVar()
clicked_adamantiterz.set(please_choose)
clicked_elementiumband = StringVar()
clicked_elementiumband.set(please_choose)

# Erstellen der Dropdown-Menüs
dropdown_frame_welpling = Frame(frame, width=130, height=60)
dropdown_frame_welpling.grid_propagate(False)
dropdown_frame_welpling.columnconfigure(0, weight=1)
dropdown_frame_welpling.rowconfigure(0, weight=1)
dropdown_frame_welpling.grid(row=1, column=5)
menu_item_a = OptionMenu(dropdown_frame_welpling, clicked_welpling, *options)
menu_item_a.configure(indicatoron=False, compound=LEFT, image=dropdown_menu_arrow_symbol, width=120)
menu_item_a.grid(sticky="wens")

dropdown_frame_adamantiterz = Frame(frame, width=130, height=60)
dropdown_frame_adamantiterz.grid_propagate(False)
dropdown_frame_adamantiterz.columnconfigure(0, weight=1)
dropdown_frame_adamantiterz.rowconfigure(0, weight=1)
dropdown_frame_adamantiterz.grid(row=2, column=5)
menu_item_b = OptionMenu(dropdown_frame_adamantiterz, clicked_adamantiterz, *options)
menu_item_b.configure(indicatoron=False, compound=LEFT, image=dropdown_menu_arrow_symbol, width=120)
menu_item_b.grid(sticky="wens")

dropdown_frame_elementiumband = Frame(frame, width=130, height=60)
dropdown_frame_elementiumband.grid_propagate(False)
dropdown_frame_elementiumband.columnconfigure(0, weight=1)
dropdown_frame_elementiumband.rowconfigure(0, weight=1)
dropdown_frame_elementiumband.grid(row=3, column=5)
menu_item_c = OptionMenu(dropdown_frame_elementiumband, clicked_elementiumband, *options)
menu_item_c.configure(indicatoron=False, compound=LEFT, image=dropdown_menu_arrow_symbol)
menu_item_c.config(width=250)
menu_item_c.grid(sticky="wens")


# Methoden zur Datenauswertung
def evaluate_item_welpling(item_name: str):
    if clicked_welpling.get() == options[0]:
        recent_price_welpling = get_recent_price(1)
        welpling_recent_price.configure(text=recent_price_welpling)
    elif clicked_welpling.get() == options[1]:
        highest_price_welpling = get_highest_or_lowest_price(item_name, "highest")
        welpling_highest_price.configure(text=highest_price_welpling)
    elif clicked_welpling.get() == options[2]:
        lowest_price_welpling = get_highest_or_lowest_price(item_name, "lowest")
        welpling_lowest_price.configure(text=lowest_price_welpling)
    elif clicked_welpling.get() == options[3]:
        recent_price_welpling = get_recent_price(1)
        welpling_recent_price.configure(text=recent_price_welpling)
        highest_price_welpling = get_highest_or_lowest_price(item_name, "highest")
        welpling_highest_price.configure(text=highest_price_welpling)
        lowest_price_welpling = get_highest_or_lowest_price(item_name, "lowest")
        welpling_lowest_price.configure(text=lowest_price_welpling)
    elif clicked_welpling.get() == options[4]:
        welpling_recent_price.configure(text="")
        welpling_highest_price.configure(text="")
        welpling_lowest_price.configure(text="")


def evaluate_item_adamantiterz(item_name: str):
    if clicked_adamantiterz.get() == options[0]:
        recent_price_adamantiterz = get_recent_price(2)
        adamantiterz_recent_price.configure(text=recent_price_adamantiterz)
    elif clicked_adamantiterz.get() == options[1]:
        highest_price_adamantiterz = get_highest_or_lowest_price(item_name, "highest")
        adamantiterz_highest_price.configure(text=highest_price_adamantiterz)
    elif clicked_adamantiterz.get() == options[2]:
        lowest_price_adamantiterz = get_highest_or_lowest_price(item_name, "lowest")
        adamantiterz_lowest_price.configure(text=lowest_price_adamantiterz)
    elif clicked_adamantiterz.get() == options[3]:
        recent_price_adamantiterz = get_recent_price(2)
        adamantiterz_recent_price.configure(text=recent_price_adamantiterz)
        highest_price_adamantiterz = get_highest_or_lowest_price(item_name, "highest")
        adamantiterz_highest_price.configure(text=highest_price_adamantiterz)
        lowest_price_adamantiterz = get_highest_or_lowest_price(item_name, "lowest")
        adamantiterz_lowest_price.configure(text=lowest_price_adamantiterz)
    elif clicked_adamantiterz.get() == options[4]:
        adamantiterz_recent_price.configure(text="")
        adamantiterz_highest_price.configure(text="")
        adamantiterz_lowest_price.configure(text="")


def evaluate_item_elementiumband(item_name: str):
    if clicked_elementiumband.get() == options[0]:
        recent_price_elementiumband = get_recent_price(3)
        elementiumband_recent_price.configure(text=recent_price_elementiumband)
    elif clicked_elementiumband.get() == options[1]:
        highest_price_elementiumband = get_highest_or_lowest_price(item_name, "highest")
        elementiumband_highest_price.configure(text=highest_price_elementiumband)
    elif clicked_elementiumband.get() == options[2]:
        lowest_price_elementiumband = get_highest_or_lowest_price(item_name, "lowest")
        elementiumband_lowest_price.configure(text=lowest_price_elementiumband)
    elif clicked_elementiumband == options[3]:
        recent_price_elementiumband = get_recent_price(3)
        elementiumband_recent_price.configure(text=recent_price_elementiumband)
        highest_price_elementiumband = get_highest_or_lowest_price(item_name, "highest")
        elementiumband_highest_price.configure(text=highest_price_elementiumband)
        lowest_price_elementiumband = get_highest_or_lowest_price(item_name, "lowest")
        elementiumband_lowest_price.configure(text=lowest_price_elementiumband)
    elif clicked_elementiumband.get() == options[4]:
        elementiumband_recent_price.configure(text="")
        elementiumband_highest_price.configure(text="")
        elementiumband_lowest_price.configure(text="")


def get_recent_price(item_id):
    r = requests.get("http://localhost:8000/items/{itemId}?item_id=" + str(item_id))
    data = r.json()
    pricing = create_string_from_item(data)
    return pricing


def get_highest_or_lowest_price(item_name, parameter: str):
    r = requests.get("http://localhost:8000/items/" + parameter + "/" + str(item_name))
    data = r.json()
    pricing = create_string_from_item(data)
    return pricing


def create_string_from_item(data):
    gold = "Gold: " + str(data["gold"])
    silver = ", \nSilber: " + str(data["silver"])
    copper = ", \nKupfer: " + str(data["copper"])
    pricing = gold + silver + copper
    return pricing


# Buttons für die Auswertung der Items erstellen
evaluate_btn_item_a = Button(frame, text="auswerten", command=lambda: evaluate_item_welpling(welpling.cget("text")))
evaluate_btn_item_a.configure(width=9, height=3, padx=38, borderwidth=4)
evaluate_btn_item_a.grid(row=1, column=6)
evaluate_btn_item_b = Button(frame, text="auswerten",
                             command=lambda: evaluate_item_adamantiterz(adamantiterz.cget("text")))
evaluate_btn_item_b.configure(width=9, height=3, padx=38, borderwidth=4)
evaluate_btn_item_b.grid(row=2, column=6)
evaluate_btn_item_c = Button(frame, text="auswerten",
                             command=lambda: evaluate_item_elementiumband(elementiumband.cget("text")))
evaluate_btn_item_c.configure(width=9, height=3, padx=38, borderwidth=4)
evaluate_btn_item_c.grid(row=3, column=6)


# Exit-Button erstellen
def exit():
    response_exit = messagebox.askokcancel("Programm beenden", "Möchtest du das Programm wirklich schließen?")
    if response_exit == 1:
        root.quit()


exit_button = Button(frame, text="Beenden", command=exit)
exit_button.configure(width=9, height=1, padx=39, borderwidth=4)
exit_button.grid(row=5, column=6)

frame.pack(pady=10)
root.mainloop()
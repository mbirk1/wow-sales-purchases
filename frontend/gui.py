import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
import ttkbootstrap as tb
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
    "alle Preise"
]

# Erstellen der Tabelle, in der die Daten eingetragen werden.
name = Label(frame, text="Name", width=20, height=3, borderwidth=1, relief="solid")
rec_price = Label(frame, text="aktueller Preis", width=20, height=3, borderwidth=1, relief="solid")
highest_price = Label(frame, text="höchster Preis", width=20, height=3, borderwidth=1, relief="solid")
lowest_price = Label(frame, text="niedrigster Preis", width=20, height=3, borderwidth=1, relief="solid")
name.grid(row=0, column=0)
rec_price.grid(row=0, column=1)
highest_price.grid(row=0, column=2)
lowest_price.grid(row=0, column=3)

item_a = Label(frame, text="Welpling", width=20, height=4, borderwidth=1, relief="solid")
item_a_recent_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
item_a_highest_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
item_a_lowest_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
item_a.grid(row=1, column=0)
item_a_recent_price.grid(row=1, column=1)
item_a_highest_price.grid(row=1, column=2)
item_a_lowest_price.grid(row=1, column=3)

item_b = Label(frame, text="Adamantiterz", width=20, height=4, borderwidth=1, relief="solid")
item_b_recent_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
item_b_highest_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
item_b_lowest_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
item_b.grid(row=2, column=0)
item_b_recent_price.grid(row=2, column=1)
item_b_highest_price.grid(row=2, column=2)
item_b_lowest_price.grid(row=2, column=3)

item_c = Label(frame, text="Elementiumband", width=20, height=4, borderwidth=1, relief="solid")
item_c_recent_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
item_c_highest_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
item_c_lowest_price = Label(frame, width=20, height=4, borderwidth=1, relief="solid")
item_c.grid(row=3, column=0)
item_c_recent_price.grid(row=3, column=1)
item_c_highest_price.grid(row=3, column=2)
item_c_lowest_price.grid(row=3, column=3)

# Erstellen der Variable, die die aktuell ausgewählte Option für die Dropdown-Menüs enthält.
please_choose = "Bitte auswählen"

clicked_item_a = StringVar()
clicked_item_a.set(please_choose)
clicked_item_b = StringVar()
clicked_item_b.set(please_choose)
clicked_item_c = StringVar()
clicked_item_c.set(please_choose)

# Erstellen der Dropdown-Menüs
dropdown_frame_a = Frame(frame, width=130, height=60)
dropdown_frame_a.grid_propagate(False)
dropdown_frame_a.columnconfigure(0, weight=1)
dropdown_frame_a.rowconfigure(0, weight=1)
dropdown_frame_a.grid(row=1, column=5)
menu_item_a = OptionMenu(dropdown_frame_a, clicked_item_a, *options)
menu_item_a.configure(indicatoron=False, compound=LEFT, image=dropdown_menu_arrow_symbol, width=120)
menu_item_a.grid(sticky="wens")

dropdown_frame_b = Frame(frame, width=130, height=60)
dropdown_frame_b.grid_propagate(False)
dropdown_frame_b.columnconfigure(0, weight=1)
dropdown_frame_b.rowconfigure(0, weight=1)
dropdown_frame_b.grid(row=2, column=5)
menu_item_b = OptionMenu(dropdown_frame_b, clicked_item_b, *options)
menu_item_b.configure(indicatoron=False, compound=LEFT, image=dropdown_menu_arrow_symbol, width=120)
menu_item_b.grid(sticky="wens")

dropdown_frame_c = Frame(frame, width=130, height=60)
dropdown_frame_c.grid_propagate(False)
dropdown_frame_c.columnconfigure(0, weight=1)
dropdown_frame_c.rowconfigure(0, weight=1)
dropdown_frame_c.grid(row=3, column=5)
menu_item_c = OptionMenu(dropdown_frame_c, clicked_item_c, *options)
menu_item_c.configure(indicatoron=False, compound=LEFT, image=dropdown_menu_arrow_symbol)
menu_item_c.config(width=250)
menu_item_c.grid(sticky="wens")


# Methoden zur Datenauswertung
def evaluate_item_a(item_name: str):
    if clicked_item_a.get() == options[0]:
        recent_price_a = get_recent_price(1)
        item_a_recent_price.configure(text=recent_price_a)
    elif clicked_item_a.get() == options[1]:
        highest_price_a = get_highest_or_lowest_price(item_name, "highest")
        item_a_highest_price.configure(text=highest_price_a)
    elif clicked_item_a.get() == options[2]:
        lowest_price_a = get_highest_or_lowest_price(item_name, "lowest")
        item_a_lowest_price.configure(text=lowest_price_a)
    elif clicked_item_a.get() == options[3]:
        recent_price_a = get_recent_price(1)
        item_a_recent_price.configure(text=recent_price_a)
        highest_price_a = get_highest_or_lowest_price(item_name, "highest")
        item_a_highest_price.configure(text=highest_price_a)
        lowest_price_a = get_highest_or_lowest_price(item_name, "lowest")
        item_a_lowest_price.configure(text=lowest_price_a)


def evaluate_item_b(item_name: str):
    if clicked_item_b.get() == options[0]:
        recent_price_b = get_recent_price(2)
        item_b_recent_price.configure(text=recent_price_b)
    elif clicked_item_b.get() == options[1]:
        highest_price_b = get_highest_or_lowest_price(item_name, "highest")
        item_b_highest_price.configure(text=highest_price_b)
    elif clicked_item_b.get() == options[2]:
        lowest_price_b = get_highest_or_lowest_price(item_name, "lowest")
        item_b_lowest_price.configure(text=lowest_price_b)
    elif clicked_item_b.get() == options[3]:
        recent_price_b = get_recent_price(2)
        item_b_recent_price.configure(text=recent_price_b)
        highest_price_b = get_highest_or_lowest_price(item_name, "highest")
        item_b_highest_price.configure(text=highest_price_b)
        lowest_price_b = get_highest_or_lowest_price(item_name, "lowest")
        item_b_lowest_price.configure(text=lowest_price_b)


def evaluate_item_c(item_name: str):
    if clicked_item_c.get() == options[0]:
        recent_price_c = get_recent_price(3)
        item_c_recent_price.configure(text=recent_price_c)
    elif clicked_item_c.get() == options[1]:
        highest_price_c = get_highest_or_lowest_price(item_name, "highest")
        item_c_highest_price.configure(text=highest_price_c)
    elif clicked_item_c.get() == options[2]:
        lowest_price_c = get_highest_or_lowest_price(item_name, "lowest")
        item_c_lowest_price.configure(text=lowest_price_c)
    elif clicked_item_c == options[3]:
        recent_price_c = get_recent_price(3)
        item_c_recent_price.configure(text=recent_price_c)
        highest_price_c = get_highest_or_lowest_price(item_name, "highest")
        item_c_highest_price.configure(text=highest_price_c)
        lowest_price_c = get_highest_or_lowest_price(item_name, "lowest")
        item_c_lowest_price.configure(text=lowest_price_c)


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
    gold = "gold: " + str(data["gold"])
    silver = ", \nsilver: " + str(data["silver"])
    copper = ", \ncopper: " + str(data["copper"])
    pricing = gold + silver + copper
    return pricing


# Buttons für die Auswertung der Items erstellen
evaluate_btn_item_a = Button(frame, text="auswerten", command=lambda: evaluate_item_a(item_a.cget("text")))
evaluate_btn_item_a.configure(width=9, height=3, padx=38, borderwidth=4)
evaluate_btn_item_a.grid(row=1, column=6)
evaluate_btn_item_b = Button(frame, text="auswerten", command=lambda: evaluate_item_b(item_b.cget("text")))
evaluate_btn_item_b.configure(width=9, height=3, padx=38, borderwidth=4)
evaluate_btn_item_b.grid(row=2, column=6)
evaluate_btn_item_c = Button(frame, text="auswerten", command=lambda: evaluate_item_c(item_c.cget("text")))
evaluate_btn_item_c.configure(width=9, height=3, padx=38, borderwidth=4)
evaluate_btn_item_c.grid(row=3, column=6)


# Exit-Button erstellen
def exit():
    response_exit = messagebox.askokcancel("Exit", "Möchtest du wirklich das Programm schließen?")
    if response_exit == 1:
        root.quit()


exit_button = Button(frame, text="Exit", command=exit)
exit_button.configure(width=9, height=1, padx=39, borderwidth=4)
exit_button.grid(row=5, column=6)

frame.pack(pady=10)
root.mainloop()

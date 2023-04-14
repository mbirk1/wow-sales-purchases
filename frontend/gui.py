from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# starte die Motoren mit C:\Users\MarjanSchneider\PycharmProjects\wow-sales-purchases\backend> uvicorn main:app --reload

root = tb.Window(themename="superhero")
root.geometry("1500x1000")
root.title("lf11: Python-Project")

bbs_logo_ico_file = Image.open("img/bbs-haarentor.png")
bbs_logo = ImageTk.PhotoImage(bbs_logo_ico_file)
root.wm_iconphoto(False, bbs_logo)

img = (Image.open("img/arrow-down-solid.png"))
img_resized = img.resize((10, 12))
new = ImageTk.PhotoImage(img_resized)

# list of placeholder items
options = [
    "Aktueller Preis",
    "Höchster Preis",
    "Niedrigster Preis"
]

# here we go create another table

name = Label(root, text="Name", width=20, height=3, borderwidth=1, relief="solid")
rec_price = Label(root, text="aktueller Preis", width=20, height=3, borderwidth=1, relief="solid")
highest_price = Label(root, text="höchster Preis", width=20, height=3, borderwidth=1, relief="solid")
lowest_price = Label(root, text="niedrigster Preis", width=20, height=3, borderwidth=1, relief="solid")
name.grid(row=0, column=0)
rec_price.grid(row=0, column=1)
highest_price.grid(row=0, column=2)
lowest_price.grid(row=0, column=3)

item_a = Label(root, text="Item A", width=20, height=4, borderwidth=1, relief="solid")
item_a_recent_price = Label(root, text="Item A", width=20, height=4, borderwidth=1, relief="solid")
item_a_highest_price = Label(root, text="Item A", width=20, height=4, borderwidth=1, relief="solid")
item_a_lowest_price = Label(root, text="Item A", width=20, height=4, borderwidth=1, relief="solid")
item_a.grid(row=1, column=0)
item_a_recent_price.grid(row=1, column=1)
item_a_highest_price.grid(row=1, column=2)
item_a_lowest_price.grid(row=1, column=3)

item_b = Label(root, text="Item B", width=20, height=4, borderwidth=1, relief="solid")
item_b_recent_price = Label(root, text="Item B", width=20, height=4, borderwidth=1, relief="solid")
item_b_highest_price = Label(root, text="Item B", width=20, height=4, borderwidth=1, relief="solid")
item_b_lowest_price = Label(root, text="Item B", width=20, height=4, borderwidth=1, relief="solid")
item_b.grid(row=2, column=0)
item_b_recent_price.grid(row=2, column=1)
item_b_highest_price.grid(row=2, column=2)
item_b_lowest_price.grid(row=2, column=3)

item_c = Label(root, text="Item C", width=20, height=4, borderwidth=1, relief="solid")
item_c_recent_price = Label(root, text="Item C", width=20, height=4, borderwidth=1, relief="solid")
item_c_highest_price = Label(root, text="Item C", width=20, height=4, borderwidth=1, relief="solid")
item_c_lowest_price = Label(root, text="Item C", width=20, height=4, borderwidth=1, relief="solid")
item_c.grid(row=3, column=0)
item_c_recent_price.grid(row=3, column=1)
item_c_highest_price.grid(row=3, column=2)
item_c_lowest_price.grid(row=3, column=3)

# create dropdown menu
clicked_item_a = StringVar()
clicked_item_a.set("Bitte auswählen")

clicked_item_b = StringVar()
clicked_item_b.set("Bitte auswählen")

clicked_item_c = StringVar()
clicked_item_c.set("Bitte auswählen")

dropdown_frame_a = Frame(root, width=250, height=62)
dropdown_frame_a.grid_propagate(False)
dropdown_frame_a.columnconfigure(0, weight=1)
dropdown_frame_a.rowconfigure(0, weight=1)
dropdown_frame_a.grid(row=1, column=5)
menu_item_a = OptionMenu(dropdown_frame_a, clicked_item_a, *options)
menu_item_a.configure(indicatoron=False, compound=LEFT, image=new, width=120)
menu_item_a.grid(sticky="wens")

dropdown_frame_b = Frame(root, width=250, height=62)
dropdown_frame_b.grid_propagate(False)
dropdown_frame_b.columnconfigure(0, weight=1)
dropdown_frame_b.rowconfigure(0, weight=1)
dropdown_frame_b.grid(row=2, column=5)
menu_item_b = OptionMenu(dropdown_frame_b, clicked_item_b, *options)
menu_item_b.configure(indicatoron=False, compound=LEFT, image=new, width=120)
menu_item_b.grid(sticky="wens")

dropdown_frame_c = Frame(root, width=250, height=62)
dropdown_frame_c.grid_propagate(False)
dropdown_frame_c.columnconfigure(0, weight=1)
dropdown_frame_c.rowconfigure(0, weight=1)
dropdown_frame_c.grid(row=3, column=5)
menu_item_c = OptionMenu(dropdown_frame_c, clicked_item_c, *options)
menu_item_c.configure(indicatoron=False, compound=LEFT, image=new, width=120)
menu_item_c.grid(sticky="wens")


# create evaluate button: Takes values from whatever and exchange old content with new values

def evaluate_item_a():
    if clicked_item_a.get() == options[0]:
        pass
    elif clicked_item_a.get() == options[1]:
        recent_price_a = get_recent_price(1)
        item_a_recent_price.configure(text=recent_price_a)
    elif clicked_item_a.get() == options[2]:
        highest_price_a = get_highest_or_lowest("hallo", "highest")
        item_a_highest_price.configure(text=highest_price_a)
    elif clicked_item_a.get() == options[3]:
        lowest_price_a = get_highest_or_lowest("hallo", "lowest")
        item_a_lowest_price.configure(text=lowest_price_a)

def evaluate_item_b():
    if clicked_item_b.get() == options[0]:
        pass
    elif clicked_item_b.get() == options[1]:
        recent_price_b = get_recent_price(2)
        item_b_recent_price.configure(text=recent_price_b)
    elif clicked_item_b.get() == options[2]:
        highest_price_b = get_highest_or_lowest("test", "highest")
        item_b_highest_price.configure(text=highest_price_b)
    elif clicked_item_b.get() == options[3]:
        lowest_price_b = get_highest_or_lowest("test", "lowest")
        item_b_lowest_price.configure(text=lowest_price_b)


def evaluate_item_c():
    if clicked_item_c.get() == options[0]:
        pass
    elif clicked_item_c.get() == options[1]:
        recent_price_c = get_recent_price(3)
        item_c_recent_price.configure(text=recent_price_c)
    elif clicked_item_c.get() == options[2]:
        highest_price_c = get_highest_or_lowest("mar", "highest")
        item_c_highest_price.configure(text=highest_price_c)
    elif clicked_item_c.get() == options[3]:
        lowest_price_c = get_highest_or_lowest("mar", "lowest")
        item_c_lowest_price.configure(text=lowest_price_c)


# create evaluate button for each item
evaluate_btn_item_a = Button(root, text="A auswerten", command=evaluate_item_a)
evaluate_btn_item_a.configure(width=9, height=3, padx=38)
evaluate_btn_item_a.grid(row=1, column=6)
evaluate_btn_item_b = Button(root, text="B auswerten", command=evaluate_item_b)
evaluate_btn_item_b.configure(width=9, height=3, padx=38)
evaluate_btn_item_b.grid(row=2, column=6)
evaluate_btn_item_c = Button(root, text="C auswerten", command=evaluate_item_c)
evaluate_btn_item_c.configure(width=9, height=3, padx=38)
evaluate_btn_item_c.grid(row=3, column=6)


def insert_chosen_operation_to_table():
    item_a_recent_price.configure(text=clicked_item_a.get())
    item_a_highest_price.configure(text=clicked_item_a.get())
    item_a_lowest_price.configure(text=clicked_item_a.get())
    item_b_recent_price.configure(text=clicked_item_b.get())
    item_b_highest_price.configure(text=clicked_item_b.get())
    item_b_lowest_price.configure(text=clicked_item_b.get())
    item_c_recent_price.configure(text=clicked_item_c.get())
    item_c_highest_price.configure(text=clicked_item_c.get())
    item_c_lowest_price.configure(text=clicked_item_c.get())


# evaluate_button = Button(root, width=20, height=4, text="auswerten", command=evaluate_item_a)
# evaluate_button.grid(row=4, column=5)


def get_recent_price(item_id):
    r = requests.get("http://localhost:8000/items/{itemId}?item_id=" + str(item_id))
    data = r.json()
    pricing = create_string_from_item(data)
    return pricing
    # insert new stuff
    # item_ccccc.configure(text=pricing)
    # val_label = Label(root, text=pricing)
    # val_label.grid(row=4, column=0)


def get_highest_or_lowest(item_name, parameter: str):
    r = requests.get("http://localhost:8000/items/" + parameter + "/" + str(item_name))
    data = r.json()
    pricing = create_string_from_item(data)
    return pricing


def create_string_from_item(data):
    item_name = "name: " + str(data["name"])
    gold = "\ngold: " + str(data["gold"])
    silver = ", \nsilver: " + str(data["silver"])
    copper = ", \ncopper: " + str(data["copper"])
    pricing = item_name + gold + silver + copper
    return pricing


# exit button
def exit():
    response_exit = messagebox.askokcancel("Exit", "Möchtest du wirklich das Programm schließen?")
    if response_exit == 1:
        root.quit()


exit_button = Button(root, text="Exit", command=exit)
exit_button.configure(width=9, height=3, padx=38)
exit_button.grid(row=5, column=6)

root.mainloop()

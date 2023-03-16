from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.geometry("1000x1000")
root.title("lf11: Python-Project")

img = (Image.open("img/arrow-down-solid.png"))
img_resized = img.resize((10, 12))
new = ImageTk.PhotoImage(img_resized)

# list of placeholder items

options = [
    "Auswertung A",
    "Auswertung B",
    "Auswertung C",
    "Auswertung D"
]

# here we go create another table

name = Label(root, text="Name", width=20, height=3, borderwidth=1, relief="solid")
rec_price = Label(root, text="aktueller Preis", width=20, height=3, borderwidth=1, relief="solid")
highest_price = Label(root, text="höchster Preis", width=20, height=3, borderwidth=1, relief="solid")
lowest_price = Label(root, text="niedrigster Preis", width=20, height=3, borderwidth=1, relief="solid")
whatever = Label(root, text="...", width=20, height=3, borderwidth=1, relief="solid")
name.grid(row=0, column=0)
rec_price.grid(row=0, column=1)
highest_price.grid(row=0, column=2)
lowest_price.grid(row=0, column=3)
whatever.grid(row=0, column=4)

item_a = Label(root, text="Item A", width=20, height=4, borderwidth=1, relief="solid")
item_aa = Label(root, text=options[0], width=20, height=4, borderwidth=1, relief="solid")
item_aaa = Label(root, text="Item A", width=20, height=4, borderwidth=1, relief="solid")
item_aaaa = Label(root, text="Item A", width=20, height=4, borderwidth=1, relief="solid")
item_aaaaa = Label(root, text="Item A", width=20, height=4, borderwidth=1, relief="solid", bg="white")
item_a.grid(row=1, column=0)
item_aa.grid(row=1, column=1)
item_aaa.grid(row=1, column=2)
item_aaaa.grid(row=1, column=3)
item_aaaaa.grid(row=1, column=4)

item_b = Label(root, text="Item B", width=20, height=4, borderwidth=1, relief="solid")
item_bb = Label(root, text="Item B", width=20, height=4, borderwidth=1, relief="solid")
item_bbb = Label(root, text="Item B", width=20, height=4, borderwidth=1, relief="solid")
item_bbbb = Label(root, text="Item B", width=20, height=4, borderwidth=1, relief="solid")
item_bbbbb = Label(root, text="Item B", width=20, height=4, borderwidth=1, relief="solid")
item_b.grid(row=2, column=0)
item_bb.grid(row=2, column=1)
item_bbb.grid(row=2, column=2)
item_bbbb.grid(row=2, column=3)
item_bbbbb.grid(row=2, column=4)

item_c = Label(root, text="Item C", width=20, height=4, borderwidth=1, relief="solid")
item_cc = Label(root, text="Item C", width=20, height=4, borderwidth=1, relief="solid")
item_ccc = Label(root, text="Item C", width=20, height=4, borderwidth=1, relief="solid")
item_cccc = Label(root, text="Item C", width=20, height=4, borderwidth=1, relief="solid")
item_ccccc = Label(root, text="Item C", width=20, height=4, borderwidth=1, relief="solid")
item_c.grid(row=3, column=0)
item_cc.grid(row=3, column=1)
item_ccc.grid(row=3, column=2)
item_cccc.grid(row=3, column=3)
item_ccccc.grid(row=3, column=4)

# create dropdown menu
clicked_item_a = StringVar()
clicked_item_a.set(options[0])

clicked_item_b = StringVar()
clicked_item_b.set(options[0])

clicked_item_c = StringVar()
clicked_item_c.set(options[0])

dropdown_frame_a = Frame(root, width=250, height=68)
dropdown_frame_a.grid_propagate(False)
dropdown_frame_a.columnconfigure(0, weight=1)
dropdown_frame_a.rowconfigure(0, weight=1)
dropdown_frame_a.grid(row=1, column=5)
menu_item_a = OptionMenu(dropdown_frame_a, clicked_item_a, *options)
menu_item_a.configure(width=100)
menu_item_a.configure(indicatoron=False, compound=LEFT, image=new, width=120)
menu_item_a.grid(sticky="wens")

dropdown_frame_b = Frame(root, width=250, height=68)
dropdown_frame_b.grid_propagate(False)
dropdown_frame_b.columnconfigure(0, weight=1)
dropdown_frame_b.rowconfigure(0, weight=1)
dropdown_frame_b.grid(row=2, column=5)
menu_item_b = OptionMenu(dropdown_frame_b, clicked_item_b, *options)
menu_item_b.configure(indicatoron=False, compound=LEFT, image=new, width=120)
menu_item_b.grid(sticky="wens")

dropdown_frame_c = Frame(root, width=250, height=68)
dropdown_frame_c.grid_propagate(False)
dropdown_frame_c.columnconfigure(0, weight=1)
dropdown_frame_c.rowconfigure(0, weight=1)
dropdown_frame_c.grid(row=3, column=5)
menu_item_c = OptionMenu(dropdown_frame_c, clicked_item_c, *options)
menu_item_c.configure(indicatoron=False, compound=LEFT, image=new, width=120)
menu_item_c.grid(sticky="wens")


def evaluate_items():
    item_aa.configure(text=clicked_item_a.get())
    item_aaa.configure(text=clicked_item_a.get())
    item_aaaa.configure(text=clicked_item_a.get())
    item_aaaaa.configure(text=clicked_item_a.get())

    item_bb.configure(text=clicked_item_b.get())
    item_bbb.configure(text=clicked_item_b.get())
    item_bbbb.configure(text=clicked_item_b.get())
    item_bbbbb.configure(text=clicked_item_b.get())

    item_cc.configure(text=clicked_item_c.get())
    item_ccc.configure(text=clicked_item_c.get())
    item_cccc.configure(text=clicked_item_c.get())
    item_ccccc.configure(text=clicked_item_c.get())


evaluate_button = Button(root, width=20, height=4, text="auswerten", command=evaluate_items)
evaluate_button.grid(row=4, column=5)


# exit button

def exit():
    response_exit = messagebox.askokcancel("Exit", "Möchtest du wirklich das Programm schließen?")
    if response_exit == 1:
        root.quit()
    else:
        messagebox.showinfo("Dann nicht", "Ok, dann nicht!")


exit_button = Button(root, text="👽Exit👽", command=exit)
exit_button.configure(width=23, height=2, padx=38, pady=10, borderwidth=2)
exit_button.grid(row=5, column=5)

root.mainloop()

from tkinter import *
import tkinter.ttk as t
tk = Tk()
tk.title("Simple python tkinter GUI")

#========Tkinter widgets========
'''
Menu
Button
Label
Entry
ttk.Progressbar
Spinbox
Scale
Scrollbar
Labelframe
ttk.Notebook
Combobox
Listbox
Checkbutton
Radiobutton
'''
#===============================

menu = Menu(tk)
tk.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Files", menu=filemenu)
filemenu.add_command(label="Save...")
filemenu.add_command(label="Open...")
filemenu.add_separator()
filemenu.add_command(label="Quit")
b = Button(tk, text="Button").pack()
l = Label(tk, text="Label").pack()
e = Entry(tk, show="*").pack()
p = t.Progressbar(tk, value=0, mode="indeterminate")
p.pack()
for x in range(0,101,10):
	p.config(value=x)
	tk.update_idletasks()
s = Spinbox(tk, from_=10, to=40).pack()
sc = Scale(tk, from_=10, to=80, orient="horizontal").pack()
sb = Scrollbar(tk).pack()
f = LabelFrame(tk, text="LabelFrame")
f.pack()
r = Radiobutton(f, text="Male").pack()
r2 = Radiobutton(f, text="Female").pack()
c = Checkbutton(f, text="Hy").pack()
tb = t.Notebook(tk)
tab1 = t.Frame(tb)
tab2 = t.Frame(tb)
tb.add(tab1, text="Listbox")
tb.add(tab2, text="Combobox")
tb.pack()
lb = Listbox(tab1, height=5, selectmode="multiple")
for num in [12, "ciao", 67, "Hy"]:
	lb.insert("end", str(num))
lb.pack()
cb = t.Combobox(tab2, values=("Io", "sono", "Giorgia")).pack()
rb = Button(tk, text="Relief", relief="groove").pack()
rb2 = Button(tk, text="Relief2", relief="sunken").pack()

tk.mainloop()

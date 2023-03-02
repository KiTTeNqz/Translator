from machineClass import Machine
from tkinter import *

def clear():
    textOut.delete('1.0', END)

def getResult():
    clear()
    textOut.replace('1.0', END, Machine.start(text.get('1.0',END)))

#fname = input("Введите имя файла: ")
file_opened = False
while file_opened == False:
    try:
        inf = open("example.cs", "r")
        file_opened = True
    except FileNotFoundError:
        print("Файл '%s' не найден. Попробуйте еще.")
        fname = input("Введите имя файла: ")

lines=inf.read()
inf.close()

lines=lines[3:]

root = Tk()

text = Text(root, height=20, width=70)
text.insert('1.0', lines)

textOut = Text(root, height=20, width=75)

photo = PhotoImage(file=r"grarrow.png")

btn = Button(root,
             text="Translate",
             command = getResult,
             width=20,height=20,
             image = photo,
             bg="white",fg="black")

text.pack(side=LEFT, padx=16, pady=16)
btn.pack(side=LEFT, padx=16, pady=16)

textOut.pack(side=LEFT, padx=16, pady=16)

root.mainloop()

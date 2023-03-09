from machineClass import Machine
from tkinter import *
from tkinter import ttk

def clear():
    textOut.delete('1.0', END)


def updateTreeViewR():
    treeR.delete(*treeR.get_children())
    lst = []
    for div in Machine.dividers:
        lst.append((Machine.dividers.index(div), div))
    # добавляем данные
    for row in lst:
        treeR.insert("", END, values=row)



def updateTreeViewI():
    treeI.delete(*treeI.get_children())
    lst = []
    for ident in Machine.identifics:
        lst.append((Machine.identifics.index(ident), ident))
    # добавляем данные
    for row in lst:
        treeI.insert("", END, values=row)


def updateTreeViewO():
    treeO.delete(*treeO.get_children())
    lst = []
    for op in Machine.operators:
        lst.append((Machine.operators.index(op), op))
    # добавляем данные
    for row in lst:
        treeO.insert("", END, values=row)


def updateTreeViewW():
    treeW.delete(*treeW.get_children())
    lst = []
    for serv in Machine.service:
        lst.append((Machine.service.index(serv), serv))
    # добавляем данные
    for row in lst:
        treeW.insert("", END, values=row)


def updateTreeViewC():
    treeC.delete(*treeC.get_children())
    lst = []
    for const in Machine.constants:
        lst.append((Machine.constants.index(const), const))
    # добавляем данные
    for row in lst:
        treeC.insert("", END, values=row)


def updateTreeView():
    updateTreeViewR()
    updateTreeViewI()
    updateTreeViewO()
    updateTreeViewW()
    updateTreeViewC()

def getResult():
    clear()
    textOut.replace('1.0', END, Machine.start(text.get('1.0',END)))
    updateTreeView()

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

frame1=Frame(root)
frame1.grid()

frame2=Frame(root)
frame2.grid()

text = Text(frame1, height=20, width=70)
text.insert('1.0', lines)
textOut = Text(frame1, height=20, width=75)
photo = PhotoImage(file=r"grarrow.png")
btn = Button(frame1,
             text="Translate",
             command = getResult,
             width=20,height=20,
             image = photo,
             bg="white",fg="black")

text.grid(row=0, column=0, padx=10, pady=10)
btn.grid(row=0, column=1, padx=10, pady=10)
textOut.grid(row=0, column=2,padx=10, pady=10)

#div
columns = ("No", "Value")
treeR = ttk.Treeview(frame2, columns=columns, show="headings")
treeR.grid(row=0, column=0, padx=10, pady=10)
# определяем заголовки
treeR.heading("No", text="NUM", anchor=W)
treeR.heading("Value", text="R", anchor=W)
treeR.column("#1", stretch=NO, width=70)
treeR.column("#2", stretch=NO, width=60)
lst=[]
for div in Machine.dividers:
    lst.append((Machine.dividers.index(div), div))
# добавляем данные
for row in lst:
    treeR.insert("", END, values=row)

#ident
columns = ("No", "Value")
treeI = ttk.Treeview(frame2, columns=columns, show="headings")
treeI.grid(row=0, column=1, padx=10, pady=10)
# определяем заголовки
treeI.heading("No", text="NUM", anchor=W)
treeI.heading("Value", text="I", anchor=W)
treeI.column("#1", stretch=NO, width=70)
treeI.column("#2", stretch=NO, width=60)
lst=[]
for ident in Machine.identifics:
    lst.append((Machine.identifics.index(ident), ident))
# добавляем данные
for row in lst:
    treeI.insert("", END, values=row)

#const
columns = ("No", "Value")
treeC = ttk.Treeview(frame2, columns=columns, show="headings")
treeC.grid(row=0, column=2, padx=10, pady=10)
# определяем заголовки
treeC.heading("No", text="NUM", anchor=W)
treeC.heading("Value", text="C", anchor=W)
treeC.column("#1", stretch=NO, width=70)
treeC.column("#2", stretch=NO, width=60)
lst=[]
for const in Machine.constants:
    lst.append((Machine.constants.index(const), const))
# добавляем данные
for row in lst:
    treeC.insert("", END, values=row)

#service
columns = ("No", "Value")
treeW = ttk.Treeview(frame2, columns=columns, show="headings")
treeW.grid(row=0, column=3, padx=10, pady=10)
# определяем заголовки
treeW.heading("No", text="NUM", anchor=W)
treeW.heading("Value", text="W", anchor=W)
treeW.column("#1", stretch=NO, width=70)
treeW.column("#2", stretch=NO, width=60)
lst=[]
for serv in Machine.service:
    lst.append((Machine.service.index(serv), serv))
# добавляем данные
for row in lst:
    treeW.insert("", END, values=row)

#opers
columns = ("No", "Value")
treeO = ttk.Treeview(frame2, columns=columns, show="headings")
treeO.grid(row=0, column=4, padx=10, pady=10)
# определяем заголовки
treeO.heading("No", text="NUM", anchor=W)
treeO.heading("Value", text="O", anchor=W)
treeO.column("#1", stretch=NO, width=70)
treeO.column("#2", stretch=NO, width=60)
lst=[]
for op in Machine.operators:
    lst.append((Machine.operators.index(op), op))
# добавляем данные
for row in lst:
    treeO.insert("", END, values=row)

# # добавляем вертикальную прокрутку
# scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)
# tree.configure(yscroll=scrollbar.set)
# scrollbar.pack()

root.mainloop()

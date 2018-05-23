from tkinter import *

info = Tk()
info.geometry("425x270")
info.resizable(False, False)
info.title("Formula 1 (TM) Wheel - Info")
info["background"] = "white"

title = Label(info, text = "Formula 1 (TM) Wheel - Info", bg = "white", fg = "black", font = ("Tahoma", 20))
title.pack()
one = Label(info, text = "A: Shift Up", bg = "white", fg = "black", font = ("Tahoma", 10))
one.place(x = 70, y = 50)
two = Label(info, text = "Z: Shift Down", bg = "white", fg = "black", font = ("Tahoma", 10))
two.place(x = 70, y = 70)
three = Label(info, text = "+: Brake Rep. to Front", bg = "white", fg = "black", font = ("Tahoma", 10))
three.place(x = 70, y = 90)
four = Label(info, text = "-: Brake Rep. to Rear", bg = "white", fg = "black", font = ("Tahoma", 10))
four.place(x = 70, y = 110)
five = Label(info, text = "O: Differential Power Up", bg = "white", fg = "black", font = ("Tahoma", 10))
five.place(x = 70, y = 130)
six = Label(info, text = "K: Differential Power Down", bg = "white", fg = "black", font = ("Tahoma", 10))
six.place(x = 70, y = 150)
seven = Label(info, text = "1: Charging Mode", bg = "white", fg = "black", font = ("Tahoma", 10))
seven.place(x = 70, y = 170)
eight = Label(info, text = "2: Race Mode", bg = "white", fg = "black", font = ("Tahoma", 10))
eight.place(x = 70, y = 190)
nine = Label(info, text = "3: Quali Mode", bg = "white", fg = "black", font = ("Tahoma", 10))
nine.place(x = 70, y = 210)
ten = Label(info, text = "4: Attack Mode", bg = "white", fg = "black", font = ("Tahoma", 10))
ten.place(x = 70, y = 230)

def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def shiftUp(root, frame1, g, b, d, m):
    frame1.destroy()
    root.withdraw()

    if(g == "N"):
        g = 1

    elif(g == "R"):
        g = "N"

    elif(int(g) < 8):
        g += 1
        
    main(g, b, d, m)

def shiftDown(root, frame1, g, b, d, m):
    frame1.destroy()
    root.withdraw()
    
    if(g == 0):
        g = "N"

    elif(g == "N"):
        g = "R"

    elif(type(g) is int):
        if(g <= 8 and g >= 0):
            if(g == 1):
                g = "N"

            else:
                g -= 1

    main(g, b, d, m)

def brakeUp(root, frame1, b, g, d, m):
    frame1.destroy()
    root.withdraw()

    root2 = Tk()
    root2.geometry("425x270")
    root2.resizable(False, False)
    root2.title("Formula 1 (TM) Wheel")
    root2["background"] = "black"
    center(root2)

    frame2 = Frame(root2)
    frame2["background"] = "white"
    frame2.pack(expand = YES, fill = BOTH)

    if(float(b) <= 69.0):
        b = float(b) + 1
    
    title = Label(frame2, text = "BRK REP", bg = "white", fg = "black", font = ("Tahoma", 20))
    title.pack()
    brk = Label(frame2, text = b, bg = "white", fg = "black", font = ("Tahoma", 125))
    brk.pack()

    root2.bind("+", lambda bu: [root2.withdraw(), main(g, b, d, m)])

def brakeDown(root, frame1, b, g, d, m):
    frame1.destroy()
    root.withdraw()

    root2 = Tk()
    root2.geometry("425x270")
    root2.resizable(False, False)
    root2.title("Formula 1 (TM) Wheel")
    root2["background"] = "black"
    center(root2)

    frame2 = Frame(root2)
    frame2["background"] = "white"
    frame2.pack(expand = YES, fill = BOTH)

    if(float(b) > 50.0):
        b = float(b) - 1

    title = Label(frame2, text = "BRK REP", bg = "white", fg = "black", font = ("Tahoma", 20))
    title.pack()
    brk = Label(frame2, text = b, bg = "white", fg = "black", font = ("Tahoma", 125))
    brk.pack()

    root2.bind("-", lambda bd: [root2.withdraw(), main(g, b, d, m)])

def diffUp(root, frame1, b, g, d, m):
    frame1.destroy()
    root.withdraw()

    root2 = Tk()
    root2.geometry("425x270")
    root2.resizable(False, False)
    root2.title("Formula 1 (TM) Wheel")
    root2["background"] = "black"
    center(root2)

    frame2 = Frame(root2)
    frame2["background"] = "#b22222"
    frame2.pack(expand = YES, fill = BOTH)

    if(float(d) <= 99.0):
        d = float(d) + 1

    title = Label(frame2, text = "DIFF PWR", bg = "#b22222", fg = "white", font = ("Tahoma", 20))
    title.pack()
    dif = Label(frame2, text = d, bg = "#b22222", fg = "white", font = ("Tahoma", 125))
    dif.pack()

    root2.bind("o", lambda du: [root2.withdraw(), main(g, b, d, m)])

def diffDown(root, frame1, b, g, d, m):
    frame1.destroy()
    root.withdraw()

    root2 = Tk()
    root2.geometry("425x270")
    root2.resizable(False, False)
    root2.title("Formula 1 (TM) Wheel")
    root2["background"] = "black"
    center(root2)

    frame2 = Frame(root2)
    frame2["background"] = "#b22222"
    frame2.pack(expand = YES, fill = BOTH)

    if(float(d) > 60.0):
        d = float(d) - 1

    title = Label(frame2, text = "DIFF PWR", bg = "#b22222", fg = "white", font = ("Tahoma", 20))
    title.pack()
    dif = Label(frame2, text = d, bg = "#b22222", fg = "white", font = ("Tahoma", 125))
    dif.pack()

    root2.bind("k", lambda dd: [root2.withdraw(), main(g, b, d, m)])

def charging(root, frame1, b, g, d, m):
    frame1.destroy()
    root.withdraw()

    root2 = Tk()
    root2.geometry("425x270")
    root2.resizable(False, False)
    root2.title("Formula 1 (TM) Wheel")
    root2["background"] = "black"
    center(root2)

    frame2 = Frame(root2)
    frame2["background"] = "#1e90ff"
    frame2.pack(expand = YES, fill = BOTH)

    m = "1 - CHRG"

    title = Label(frame2, text = "ENGINE MODE", bg = "#1e90ff", fg = "black", font = ("Tahoma", 20))
    title.pack()
    space = Label(frame2, text = "", bg = "#1e90ff", fg = "#1e90ff", font = ("Tahoma", 30))
    space.pack()
    mn = Label(frame2, text = m, bg = "#1e90ff", fg = "black", font = ("Tahoma", 60))
    mn.pack()

    root2.bind("1", lambda cg: [root2.withdraw(), main(g, b, d, m)])

def race(root, frame1, b, g, d, m):
    frame1.destroy()
    root.withdraw()

    root2 = Tk()
    root2.geometry("425x270")
    root2.resizable(False, False)
    root2.title("Formula 1 (TM) Wheel")
    root2["background"] = "black"
    center(root2)

    frame2 = Frame(root2)
    frame2["background"] = "#1e90ff"
    frame2.pack(expand = YES, fill = BOTH)

    m = "2 - RACE"

    title = Label(frame2, text = "ENGINE MODE", bg = "#1e90ff", fg = "black", font = ("Tahoma", 20))
    title.pack()
    space = Label(frame2, text = "", bg = "#1e90ff", fg = "#1e90ff", font = ("Tahoma", 30))
    space.pack()
    mn = Label(frame2, text = m, bg = "#1e90ff", fg = "black", font = ("Tahoma", 60))
    mn.pack()

    root2.bind("2", lambda cg: [root2.withdraw(), main(g, b, d, m)])

def quali(root, frame1, b, g, d, m):
    frame1.destroy()
    root.withdraw()

    root2 = Tk()
    root2.geometry("425x270")
    root2.resizable(False, False)
    root2.title("Formula 1 (TM) Wheel")
    root2["background"] = "black"
    center(root2)

    frame2 = Frame(root2)
    frame2["background"] = "#1e90ff"
    frame2.pack(expand = YES, fill = BOTH)
    m = "3 - QUALI"

    title = Label(frame2, text = "ENGINE MODE", bg = "#1e90ff", fg = "black", font = ("Tahoma", 20))
    title.pack()
    space = Label(frame2, text = "", bg = "#1e90ff", fg = "#1e90ff", font = ("Tahoma", 30))
    space.pack()
    mn = Label(frame2, text = m, bg = "#1e90ff", fg = "black", font = ("Tahoma", 60))
    mn.pack()

    root2.bind("3", lambda cg: [root2.withdraw(), main(g, b, d, m)])

def attack(root, frame1, b, g, d, m):
    frame1.destroy()
    root.withdraw()

    root2 = Tk()
    root2.geometry("425x270")
    root2.resizable(False, False)
    root2.title("Formula 1 (TM) Wheel")
    root2["background"] = "black"
    center(root2)

    frame2 = Frame(root2)
    frame2["background"] = "#1e90ff"
    frame2.pack(expand = YES, fill = BOTH)

    m = "4 - ATTK"

    title = Label(frame2, text = "ENGINE MODE", bg = "#1e90ff", fg = "black", font = ("Tahoma", 20))
    title.pack()
    space = Label(frame2, text = "", bg = "#1e90ff", fg = "#1e90ff", font = ("Tahoma", 30))
    space.pack()
    mn = Label(frame2, text = m, bg = "#1e90ff", fg = "black", font = ("Tahoma", 60))
    mn.pack()

    root2.bind("4", lambda cg: [root2.withdraw(), main(g, b, d, m)])

def main(g, b, d, m):
    root = Tk()
    root.geometry("425x270")
    root.resizable(False, False)
    root.title("Formula 1 (TM) Wheel")
    root["background"] = "black"
    center(root)

    frame1 = Frame(root)
    frame1["background"] = "black"
    frame1.pack(expand = YES, fill = BOTH)

    gear = Label(frame1, text = g, bg = "black", fg = "white", font = ("Tahoma", 90))
    gear.pack()

    ers1 = Label(frame1, text = "| | | | | | |", bg = "#b22222", fg = "red", font = ("Tahoma", 15))
    ers1.place(x = 4, y = 220)
    ers2 = Label(frame1, text = "| | | | | | | | | | | | | | | | | | | | | | | | | ", bg = "green", fg = "#32cd32", font = ("Tahoma", 15))
    ers2.place(x = 93, y = 220)

    brake_rep = Label(frame1, text = b, bg = "black", fg = "white", font = ("Tahoma", 30))
    brake_rep.place(x = 10, y = 5)

    diff_rep = Label(frame1, text = d, bg = "black", fg = "white", font = ("Tahoma", 30))
    diff_rep.place(x = 322, y = 5)

    speed = Label(frame1, text = "000", bg = "black", fg = "white", font = ("Tahoma", 35))
    speed.place(x = 10, y = 120)

    ers = Label(frame1, text = "ERS", bg = "black", fg = "blue", font = ("Tahoma", 35))
    ers.place(x = 322, y = 120)

    mode = Label(frame1, text = m, bg = "black", fg = "red", font = ("Tahoma", 15))
    mode.place(x = 166, y = 135)

    root.bind("a", lambda x: shiftUp(root, frame1, g, b, d, m))
    root.bind("z", lambda y: shiftDown(root, frame1, g, b, d, m))
    root.bind("+", lambda z: brakeUp(root, frame1, b, g, d, m))
    root.bind("-", lambda a: brakeDown(root, frame1, b, g, d, m))
    root.bind("o", lambda df: diffUp(root, frame1, b, g, d, m))
    root.bind("k", lambda dff: diffDown(root, frame1, b, g, d, m))
    root.bind("1", lambda ch: charging(root, frame1, b, g, d, m))
    root.bind("2", lambda rc: race(root, frame1, b, g, d, m))
    root.bind("3", lambda ql: quali(root, frame1, b, g, d, m))
    root.bind("4", lambda at: attack(root, frame1, b, g, d, m))

    root.mainloop()
    
g = "N"
b = "60.0"
d = "75.0"
m = "1 - CHRG"

main(g, b, d, m)

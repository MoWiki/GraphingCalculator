# Bailey Thompson
# Graphing Calculator (1.1.1)
# 31 January 2017
# Info: This program graphs functions based on user-input.

from tkinter import *
from tkinter import ttk
import math as m

# size constants
MAX_SIZE = 64.0
MIN_SIZE = 1.0
INCREMENT = 2.0

# approximation constants
COMPUTATION_DISTANCE = 0.001
ASYMPTOTE = 2.0

# global variables
formula = "(x**3-2*x)/(2*(x**2-5))"
size = 8.0


def print_formula(pre_text):
    Label(root, text=pre_text + "[{0:.0f}".format(size) + "] f(x) = " + formula, relief=RIDGE,
          width=1).grid(row=1, column=0, columnspan=5, sticky=W + E)


def translate(x, y):
    tc = [0, 0]
    x_mul = int(canvas["width"]) / (size * 2)
    y_mul = (int(canvas["height"]) / (size * -2))
    x = (x + size) * x_mul
    y = (y + size) * y_mul + int(canvas["height"])
    tc[0] = x
    tc[1] = y
    return tc


def draw_line(xfrom, yfrom, xto, yto, colour):
    fromcoords = translate(xfrom, yfrom)
    tocoords = translate(xto, yto)
    if yto - yfrom > size * ASYMPTOTE or yfrom - yto > size * ASYMPTOTE:
        fromcoords = tocoords
    canvas.create_line(fromcoords[0], fromcoords[1], tocoords[0], tocoords[1], fill=colour)


def draw_grid():
    draw_line(size * -1, 0, size, 0, "darkgray")
    draw_line(0, size * -1, 0, size, "darkgray")


def draw_graph(event):
    canvas.delete("all")
    draw_grid()
    yprev = 0.0
    x = size * -1
    while x <= size:
        try:
            y = eval(formula)
        except ValueError:
            y = 1000000000
            x = COMPUTATION_DISTANCE * size
            if eval(formula) < 0:
                y *= -1
        except:
            print_formula("SYNTAX ERROR   ")
            break
        try:
            draw_line(x - COMPUTATION_DISTANCE * size, yprev, x, y, "black")
        except:
            print_formula("NON-INT PWR (dbl click ^)   ")
            break
        yprev = y
        x += COMPUTATION_DISTANCE * size


def append_formula(thing):
    global formula
    if formula.endswith('.') and thing == '.':
        formula = formula[:-1]
        formula += ","
    else:
        formula += thing
    print_formula("")


def clear_formula():
    global formula
    while formula != "":
        delete_formula()
    print_formula("")


def delete_formula():
    global formula
    formula = formula[:-1]
    print_formula("")


def zoom_in():
    global size, btn_zoom_in, btn_zoom_out
    btn_zoom_out = ttk.Button(root, text="Zoom Out", command=lambda: zoom_out()).grid(row=8, column=3)
    if size > MIN_SIZE:
        size /= INCREMENT
        draw_graph("event")
    if size == MIN_SIZE:
        btn_zoom_in = ttk.Button(root, text="Zoom In", command=lambda: zoom_in(), state=DISABLED).grid(row=8, column=2)
    print_formula("")


def zoom_out():
    global size, btn_zoom_out, btn_zoom_in
    btn_zoom_in = ttk.Button(root, text="Zoom In", command=lambda: zoom_in()).grid(row=8, column=2)
    if size < MAX_SIZE:
        size *= INCREMENT
        draw_graph("event")
    if size == MAX_SIZE:
        btn_zoom_out = ttk.Button(root, text="Zoom Out", command=lambda: zoom_out(), state=DISABLED).grid(row=8, column=3)
    print_formula("")


def correct_ending_no_number(name):
    return name.endswith('x') or name.endswith('e') or (name.endswith('i') and name[-2:] != "si") or name.endswith(')')


def correct_ending(thing):
    return thing[-1:].isdigit() or correct_ending_no_number(thing)


def append_implicit(thing):
    global formula
    if correct_ending(formula):
        if thing == "**":
            formula += thing
        else:
            formula += "*" + thing
    elif formula[-2:] == "**" and thing == "**":
        formula = formula[:-2]
        if correct_ending(formula):
            formula += "*m.pow(x,"
        else:
            formula += "m.pow(x,"
    else:
        formula += thing
    print_formula("")


def append_number_formula(thing):
    global formula
    if correct_ending_no_number(formula) and thing.isdigit():
        formula += "*"
    formula += thing
    print_formula("")


def append_closing_parentheses_formula(thing):
    global formula
    if correct_ending(formula) and thing == '(':
        formula += "*"
    formula += thing
    print_formula("")


root = Tk()

root.wm_title("Graphing Calculator")
root.resizable(width=False, height=False)

horizontalScreen = root.winfo_screenwidth() / 2 - root.winfo_reqwidth()
verticalScreen = root.winfo_screenheight() / 2 - root.winfo_reqheight()
root.geometry("+%d+%d" % (horizontalScreen, verticalScreen))

canvas = Canvas(root)

print_formula("")

btn0 = ttk.Button(root, text="0", command=lambda: append_number_formula("0")).grid(row=2, column=0)
btn1 = ttk.Button(root, text="1", command=lambda: append_number_formula("1")).grid(row=2, column=1)
btn2 = ttk.Button(root, text="2", command=lambda: append_number_formula("2")).grid(row=2, column=2)
btn3 = ttk.Button(root, text="3", command=lambda: append_number_formula("3")).grid(row=2, column=3)
btn4 = ttk.Button(root, text="4", command=lambda: append_number_formula("4")).grid(row=2, column=4)

btn5 = ttk.Button(root, text="5", command=lambda: append_number_formula("5")).grid(row=3, column=0)
btn6 = ttk.Button(root, text="6", command=lambda: append_number_formula("6")).grid(row=3, column=1)
btn7 = ttk.Button(root, text="7", command=lambda: append_number_formula("7")).grid(row=3, column=2)
btn8 = ttk.Button(root, text="8", command=lambda: append_number_formula("8")).grid(row=3, column=3)
btn9 = ttk.Button(root, text="9", command=lambda: append_number_formula("9")).grid(row=3, column=4)

btnSin = ttk.Button(root, text="sin", command=lambda: append_implicit("m.sin(")).grid(row=4, column=0)
btnCos = ttk.Button(root, text="cos", command=lambda: append_implicit("m.cos(")).grid(row=4, column=1)
btnTan = ttk.Button(root, text="tan", command=lambda: append_implicit("m.tan(")).grid(row=4, column=2)
btnPi = ttk.Button(root, text="π", command=lambda: append_implicit("m.pi")).grid(row=4, column=3)
btnE = ttk.Button(root, text="e", command=lambda: append_implicit("m.e")).grid(row=4, column=4)

btnCsc = ttk.Button(root, text="sinh", command=lambda: append_implicit("m.sinh(")).grid(row=5, column=0)
btnSec = ttk.Button(root, text="cosh", command=lambda: append_implicit("m.cosh(")).grid(row=5, column=1)
btnCot = ttk.Button(root, text="tanh", command=lambda: append_implicit("m.tanh(")).grid(row=5, column=2)
btnLog = ttk.Button(root, text="log", command=lambda: append_implicit("m.log10(")).grid(row=5, column=3)
btnLn = ttk.Button(root, text="ln", command=lambda: append_implicit("m.log(")).grid(row=5, column=4)

btnPlus = ttk.Button(root, text="+", command=lambda: append_formula("+")).grid(row=6, column=0)
btnMinus = ttk.Button(root, text="-", command=lambda: append_formula("-")).grid(row=6, column=1)
btnMultiply = ttk.Button(root, text="*", command=lambda: append_formula("*")).grid(row=6, column=2)
btnDivide = ttk.Button(root, text="/", command=lambda: append_formula("/")).grid(row=6, column=3)
btnExponent = ttk.Button(root, text="^", command=lambda: append_implicit("**")).grid(row=6, column=4)

btnLeftBracket = ttk.Button(root, text="(", command=lambda: append_closing_parentheses_formula("(")).grid(row=7, column=0)
btnRightBracket = ttk.Button(root, text=")", command=lambda: append_formula(")")).grid(row=7, column=1)
btnPeriod = ttk.Button(root, text=".", command=lambda: append_formula(".")).grid(row=7, column=2)
btnDelete = ttk.Button(root, text="Delete", command=lambda: delete_formula()).grid(row=7, column=3)
btnClear = ttk.Button(root, text="Clear", command=lambda: clear_formula()).grid(row=7, column=4)

btnX = ttk.Button(root, text="x", command=lambda: append_implicit("x")).grid(row=8, column=0)
btn_enter = ttk.Button(root, text="Enter")
btn_zoom_in = ttk.Button(root, text="Zoom In", command=lambda: zoom_in()).grid(row=8, column=2)
btn_zoom_out = ttk.Button(root, text="Zoom Out", command=lambda: zoom_out()).grid(row=8, column=3)
btnExit = ttk.Button(root, text="Exit App", command=lambda: exit(0)).grid(row=8, column=4)

btn_enter.bind('<Button-1>', draw_graph)

btn_enter.grid(row=8, column=1)
canvas.grid(row=0, column=0, columnspan=5)

draw_grid()
draw_graph("event")

root.mainloop()

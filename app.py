from tkinter import *
import parser



root = Tk()
root.title("CALCULATOR")


display = Entry(root)
display.grid(row=1, columnspan=8, sticky=W+E)


# guardamos el indice en una variable
indice = 0


# obtener numeros
def get_numbers(n):
    global indice
    display.insert(indice, n)
    indice += 1

# obtener las operaciones
def get_operacions(operator):
    global indice
    operator_lenght = len(operator)
    display.insert(indice, operator)
    indice += operator_lenght


# clear display
def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, 'Error')


#CALCULATE
def calculate():
   display_state = display.get()
   try:
     math_expression =  parser.expr(display_state).compile()
     eval(math_expression)
     clear_display()
     display.insert(0, result)
   except expression as identifier:
       clear_display()
       display.insert(0,'ERROR')
        

# NUMERIC BUTTON
Button(root, text="1", command=lambda: get_numbers(1)).grid(
    row=2, column=1, sticky=W+E)
Button(root, text="2", command=lambda: get_numbers(2)).grid(
    row=2, column=2, sticky=W+E)
Button(root, text="3", command=lambda: get_numbers(3)).grid(
    row=2, column=3, sticky=W+E)

Button(root, text="4", command=lambda: get_numbers(4)).grid(
    row=3, column=1, sticky=W+E)
Button(root, text="5", command=lambda: get_numbers(5)).grid(
    row=3, column=2, sticky=W+E)
Button(root, text="6", command=lambda: get_numbers(6)).grid(
    row=3, column=3, sticky=W+E)

Button(root, text="7", command=lambda: get_numbers(7)).grid(
    row=4, column=1, sticky=W+E)
Button(root, text="8", command=lambda: get_numbers(8)).grid(
    row=4, column=2, sticky=W+E)
Button(root, text="9", command=lambda: get_numbers(9)).grid(
    row=4, column=3, sticky=W+E)

# OPERATIONS BUTTONS
Button(root, text="AC", command=lambda: clear_display()).grid(
    row=5, column=1, sticky=W+E)
Button(root, text="0", command=lambda: get_numbers(0)).grid(
    row=5, column=2, sticky=W+E)
Button(root, text="%", command=lambda: get_operacions(
    "%")).grid(row=5, column=3, sticky=W+E)

Button(root, text="+", command=lambda: get_operacions("+")
       ).grid(row=2, column=4, sticky=W+E)
Button(root, text="-", command=lambda: get_operacions("-")
       ).grid(row=3, column=4, sticky=W+E)
Button(root, text="*", command=lambda: get_operacions("*")
       ).grid(row=4, column=4, sticky=W+E)
Button(root, text="/", command=lambda: get_operacions("/")
       ).grid(row=5, column=4, sticky=W+E)

Button(root, text="←",command=lambda: undo()).grid(row=2, column=5, sticky=W+E, columnspan=2)
Button(root, text="expo", command=lambda: get_operacions(
    "**")).grid(row=3, column=5, sticky=W+E)
Button(root, text="^2", command=lambda: get_operacions(
    "**2")).grid(row=3, column=6, sticky=W+E)
Button(root, text="(", command=lambda: get_operacions(
    "(")).grid(row=4, column=5, sticky=W+E)
Button(root, text=")", command=lambda: get_operacions(
    ")")).grid(row=4, column=6, sticky=W+E)
Button(root, text="=",command=lambda: calculate()).grid(row=5, column=5, sticky=W+E, columnspan=2)


root.mainloop()

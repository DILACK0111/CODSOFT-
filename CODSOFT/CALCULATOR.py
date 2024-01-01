import tkinter as tk

def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operator.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    else:
        result = "Invalid operation"

    label_result.config(text=f"Result: {result}")

root = tk.Tk()
root.title("Simple Calculator")

frame = tk.Frame(root)
frame.pack()

entry_num1 = tk.Entry(frame)
entry_num1.grid(row=0, column=0)

operator = tk.StringVar()
operator.set("+")  # Default operation is addition

option_menu = tk.OptionMenu(frame, operator, "+", "-", "*", "/")
option_menu.grid(row=0, column=1)

entry_num2 = tk.Entry(frame)
entry_num2.grid(row=0, column=2)

button_calculate = tk.Button(frame, text="Calculate", command=calculate)
button_calculate.grid(row=1, columnspan=3)

label_result = tk.Label(frame, text="Result: ")
label_result.grid(row=2, columnspan=3)

root.mainloop()

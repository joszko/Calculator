from tkinter import *
from tkinter import ttk


class Calculator:

    def __init__(self, root):
        # initial value
        self.calculator_value = 0.0
        # catching the function button press
        self.add_press = False
        self.minus_press = False
        self.multiply_press = False
        self.divide_press = False
        # setting the looks
        root.title('Calculator')
        root.resizable(width=False, height=False)

        # styling
        style = ttk.Style()
        style.configure("TButton", font='Serif 15', padding=10)
        style.configure('TEntry', font='Serif 18', padding=10)

        # adding buttons and entry
        self.entry_box = ttk.Entry(root, width=12, justify=RIGHT, font='Serif 18')
        self.entry_box.grid(row=0, columnspan=3)
        self.button_clear = ttk.Button(root, text='C', width=3, command=lambda: self.clear()).grid(row=0, column=3)

        self.button_7 = ttk.Button(root, text='7', width=3, command=lambda: self.digit('7')).grid(row=1, column=0)
        self.button_8 = ttk.Button(root, text='8', width=3, command=lambda: self.digit('8')).grid(row=1, column=1)
        self.button_9 = ttk.Button(root, text='9', width=3, command=lambda: self.digit('9')).grid(row=1, column=2)
        self.button_divide = ttk.Button(root, text='/', width=3, command=lambda: self.function('/')).grid(row=1, column=3)

        self.button_4 = ttk.Button(root, text='4', width=3, command=lambda: self.digit('4')).grid(row=2, column=0)
        self.button_5 = ttk.Button(root, text='5', width=3, command=lambda: self.digit('5')).grid(row=2, column=1)
        self.button_6 = ttk.Button(root, text='6', width=3, command=lambda: self.digit('6')).grid(row=2, column=2)
        self.button_multiply = ttk.Button(root, text='*', width=3, command=lambda: self.function('*')).grid(row=2, column=3)

        self.button_1 = ttk.Button(root, text='1', width=3, command=lambda: self.digit('1')).grid(row=3, column=0)
        self.button_2 = ttk.Button(root, text='2', width=3, command=lambda: self.digit('2')).grid(row=3, column=1)
        self.button_3 = ttk.Button(root, text='3', width=3, command=lambda: self.digit('3')).grid(row=3, column=2)
        self.button_minus = ttk.Button(root, text='-', width=3, command=lambda: self.function('-')).grid(row=3, column=3)

        self.button_dot = ttk.Button(root, text='.', width=3, command=lambda: self.digit('.')).grid(row=4, column=0)
        self.button_0 = ttk.Button(root, text='0', width=3, command=lambda: self.digit('0')).grid(row=4, column=1)
        self.button_equals = ttk.Button(root, text='=', width=3, command=lambda: self.equals()).grid(row=4, column=2)
        self.button_add = ttk.Button(root, text='+', width=3, command=lambda: self.function('+')).grid(row=4, column=3)

    def clear(self):
        self.entry_box.delete(0, END)
        # making sure that all the setting are set to False
        self.add_press = False
        self.minus_press = False
        self.multiply_press = False
        self.divide_press = False

    def digit(self, value):
        # gets the value from the entry box
        entry_value = self.entry_box.get()
        # adds next digit to the right side
        # if statement protects from adding more than 1 decimal point
        if value == '.' and entry_value.find('.') == -1:
            entry_value += value
        elif value != '.':
            entry_value += value
        # clear the entry boc
        self.entry_box.delete(0, 'end')
        # insert new value
        self.entry_box.insert(0, entry_value)

    def function(self, value):
        self.calculator_value = self.entry_box.get()
        self.entry_box.delete(0, END)

        # making sure that all the setting are set to False
        self.add_press = False
        self.minus_press = False
        self.multiply_press = False
        self.divide_press = False

        if value == '+':
            self.add_press = True
        elif value == '-':
            self.minus_press = True
        elif value == '/':
            self.divide_press = True
        elif value == '*':
            self.multiply_press = True

    def equals(self):
        new_value = self.entry_box.get()
        self.entry_box.delete(0, 'end')
        result = 0
        if self.add_press:
            result = float(self.calculator_value) + float(new_value)
        if self.minus_press:
            result = float(self.calculator_value) - float(new_value)
        if self.multiply_press:
            result = float(self.calculator_value) * float(new_value)
        if self.divide_press:
            try:
                result = float(self.calculator_value) / float(new_value)
            except ZeroDivisionError:
                result = r"Division by 0"

        self.entry_box.insert(0, result)


window = Tk()
calc = Calculator(window)
window.mainloop()

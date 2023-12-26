from tkinter import *

def validate_input(value):
    try:
        float_value = float(value)
        return True, float_value
    except ValueError:
        return False, None

def convert_unit(value, unit):
    conversion_factor = {
        "mm": 1,
        "cm": 10,
        "m": 1000,
        "in": 25.4,
        "ft": 304.8,
        "yd": 914.4
    }
    return value * conversion_factor[unit]

def display_result(result_field, result):
    result_field.delete(0, END)
    result_field.insert(0, str(result))

class UnitConverter():
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.root.geometry("300x300")

        # Input section
        self.input_label = Label(self.root, text="Enter value:")
        self.input_label.pack()

        self.input_field = Entry(self.root)
        self.input_field.pack()

        # Units selection
        self.unit_label = Label(self.root, text="Select unit:")
        self.unit_label.pack()

        self.unit_var = StringVar()
        self.unit_var.set("mm")

        self.unit_menu = OptionMenu(self.root, self.unit_var, "mm", "cm", "m", "in", "ft", "yd")
        self.unit_menu.pack()
        
        self.unit_label1 = Label(self.root, text="To unit:")
        self.unit_label1.pack()
        
        self.unit_var = StringVar()
        self.unit_var.set("mm")

        self.unit_menu = OptionMenu(self.root, self.unit_var, "mm", "cm", "m", "in", "ft", "yd")
        self.unit_menu.pack()

        # Result section
        self.result_label = Label(self.root, text="Result:")
        self.result_label.pack()

        self.result_field = Entry(self.root)
        self.result_field.pack()

        # Convert button
        self.convert_button = Button(self.root, text="Convert", command=self.convert)
        self.convert_button.pack()

    def convert(self):
        value = self.input_field.get()
        unit = self.unit_var.get()

        is_valid, float_value = validate_input(value)

        if is_valid:
            result = convert_unit(float_value, unit)
            display_result(self.result_field, result)
        else:
            self.result_field.delete(0, END)
            self.result_field.insert(0, "Invalid input")


root = Tk()
unit_converter = UnitConverter(root)
root.mainloop()
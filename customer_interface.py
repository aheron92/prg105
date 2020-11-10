"""
Lesson Objective(s):
-Learn to use radio buttons
-Perform calculations when a button is clicked


Lesson:
Make up an interface for a business offering 7-10 services or product options with prices. Write a GUI program to allow
the user to click buttons to add services or products and show total at the bottom. Make sure all necessary labels and
instructions to the user are included in your GUI. Provide options using data fields, radio buttons, or check boxes.

Possibilities: Garage, Salon, Coffee shop, etc...
"""

import tkinter


class Drink:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.coffee_frame = tkinter.Frame(self.main_window)
        self.size_frame = tkinter.Frame(self.main_window)
        self.add_ins_frame = tkinter.Frame(self.main_window)
        self.order_frame = tkinter.Frame(self.main_window)
        self.charges_frame = tkinter.Frame(self.main_window)

        self.coffee_var = tkinter.IntVar()
        self.size_var = tkinter.IntVar()

        self.coffee_var.set(1)
        self.size_var.set(1)

        self.coffee_label = tkinter.Label(self.coffee_frame, text="Coffee")
        self.buzz1 = tkinter.Radiobutton(self.coffee_frame, text="Caffeinated", variable=self.coffee_var, value=1)
        self.buzz2 = tkinter.Radiobutton(self.coffee_frame, text='Half-Caf', variable=self.coffee_var, value=2)
        self.buzz3 = tkinter.Radiobutton(self.coffee_frame, text='De-Caf', variable=self.coffee_var, value=3)

        self.coffee_label.pack()
        self.buzz1.pack(side='left')
        self.buzz2.pack(side='left')
        self.buzz3.pack(side='left')

        self.size_label = tkinter.Label(self.size_frame, text='Size')
        self.size1 = tkinter.Radiobutton(self.size_frame, text='8 oz. - $1.00', variable=self.size_var, value=1)
        self.size2 = tkinter.Radiobutton(self.size_frame, text="12 oz. - $1.25", variable=self.size_var, value=2)
        self.size3 = tkinter.Radiobutton(self.size_frame, text='16 oz. - $1.50', variable=self.size_var, value=3)

        self.size_label.pack()
        self.size1.pack(side='left')
        self.size2.pack(side='left')
        self.size3.pack(side='left')

        self.cream_var = tkinter.IntVar()
        self.sugar_var = tkinter.IntVar()
        self.artificial_var = tkinter.IntVar()

        self.cream_var.set(0)
        self.sugar_var.set(0)
        self.artificial_var.set(0)

        self.add_label = tkinter.Label(self.add_ins_frame, text="Add Ins")
        self.cream = tkinter.Checkbutton(self.add_ins_frame, text="Cream", variable=self.cream_var)
        self.sugar = tkinter.Checkbutton(self.add_ins_frame, text='Sugar', variable=self.sugar_var)
        self.artificial = tkinter.Checkbutton(self.add_ins_frame, text='Artificial Sweetener',
                                              variable=self.artificial_var)

        self.add_label.pack()
        self.cream.pack(side='left')
        self.sugar.pack(side='left')
        self.artificial.pack(side='left')

        self.order_button = tkinter.Button(self.order_frame, text="Order", command=self.display)
        self.quit_button = tkinter.Button(self.order_frame, text='Quit', command=self.main_window.destroy)

        self.order_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.order_info = tkinter.StringVar()
        self.order_output = tkinter.Label(self.charges_frame, textvariable=self.order_info)
        self.order_output.pack()

        self.coffee_frame.pack()
        self.size_frame.pack()
        self.add_ins_frame.pack()
        self.order_frame.pack()
        self.charges_frame.pack()

        tkinter.mainloop()

    def display(self):
        output = "You ordered a "
        if self.size_var.get() == 1:
            output += ' an 8oz. '
        elif self.size_var.get() == 2:
            output += ' a 12 oz. '
        elif self.size_var.get() == 3:
            output += ' a 16 oz.'

        if self.coffee_var.get() == 1:
            output += "regular coffee "
        elif self.coffee_var.get() == 2:
            output += "half caf "
        elif self.coffee_var.get() == 3:
            output += "decaf "

        if self.size_var.get() == 1:
            output += " for $1.00 "
        elif self.size_var.get() == 2:
            output += " for $1.25 "
        elif self.size_var.get() == 3:
            output += " for $1.50 "

        if self.cream_var.get() == 1:
            output += "\nwith cream"
        if self.sugar_var.get() == 1:
            output += "\nwith sugar"
        if self.artificial_var.get() == 1:
            output += "\nwith artificial sweetener"

        self.order_info.set(output)


coffee = Drink()

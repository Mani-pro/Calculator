import tkinter as tk

LIGHT_GRAY = "#F5F5F5"
LBL_COLOR = '#25265E'
SMALL_FONT_STYLE = ("Arial", 16)
LARG_FONT_STYLE = ("Arial", 40, 'bold')
BTNS_FONT_STYLE = ("Arial", 24, 'bold')
DEFAULT_FONT_STYLE = ("Arial", 20)
WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFF"
LIGHT_BLUE = '#CCEDFF'


class Calc:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("357x667")
        self.root.resizable(0, 0)
        self.root.iconbitmap('calculator-icon_34473.ico')

        self.display_frame = frame = tk.Frame(
            self.root, height=221, bg=LIGHT_GRAY)
        self.display_frame.pack(expand=True, fill='both')

        self.btnframe = frame = tk.Frame(self.root, bg="#F5F5F5")
        self.btnframe.pack(expand=True, fill='both')

        self.total_expression = ""
        self.expression = ""

        self.total_lbl, self.lbl = self.create_display_lbls()

        self.radical_btn = tk.Button(self.btnframe, text="√", bg=OFF_WHITE,
                                     fg=LBL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.sqrt)
        self.radical_btn.grid(row=0, column=2, sticky=tk.NSEW)

        self.power_btn = tk.Button(self.btnframe, text="^", bg=OFF_WHITE,
                                   fg=LBL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        self.power_btn.grid(row=0, column=3, sticky=tk.NSEW)

        self.clear_btn = tk.Button(self.btnframe, text='C', bg=OFF_WHITE,
                                   fg=LBL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.clear)
        self.clear_btn.grid(row=0, column=1, sticky=tk.NSEW)

        self.equals_btn = tk.Button(self.btnframe, text='=', bg=LIGHT_BLUE,
                                    fg=LBL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.evaulate)
        self.equals_btn.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

        self.digits_num = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.create_btns()

        self.operations = {'/': "\u00F7", '*': '\u00D7', '-': '-', '+': '+'}

        self.create_operator_btns()

        self.btnframe.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.btnframe.columnconfigure(x, weight=1)
            self.btnframe.rowconfigure(x, weight=1)
        self.bind_keys()

    def square(self):
        self.expression = str(eval(f"{self.expression}**2"))
        self.update_lbl()

    def sqrt(self):
        self.expression = str(eval(f"{self.expression}**0.5"))
        self.update_lbl()
    
    def evaulate(self):
        self.total_expression += self.expression
        self.update_total_lbl()
        try:
            self.expression = str(eval(self.total_expression))
            self.total_expression = ''
        except:
            self.expression = "ERROR"
        finally:
            self.update_lbl()

    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.evaulate())
        for key in self.digits_num:
            self.root.bind(
                str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.root.bind(
                str(key), lambda event, operator=key: self.append_operator(operator))

    def clear(self):
        self.total_expression = ''
        self.expression = ''
        self.update_lbl()
        self.update_total_lbl()

    def append_operator(self, operator):
        self.total_expression += self.expression + operator
        self.expression = ''
        self.update_total_lbl()
        self.update_lbl()

    def add_to_expression(self, value):
        self.expression += str(value)
        self.update_lbl()

    def update_total_lbl(self):
        exp = self.total_expression
        for operator, symbol in self.operations.items():
            exp = exp.replace(operator, f' {symbol} ')
        self.total_lbl.config(text=exp)

    def update_lbl(self):
        self.lbl.config(text=self.expression[:11])

    def create_operator_btns(self):
        i = 0
        for operator, symbol in self.operations.items():
            btn = tk.Button(self.btnframe, text=symbol, bg=OFF_WHITE,
                            fg=LBL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            btn.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_opr(self):
        for digits, grid_value in self.digits_num.items():
            btn = tk.Button(self.btnframe, text=str(
                digits), bg=WHITE, fg=LBL_COLOR, font=BTNS_FONT_STYLE, borderwidth=0)
            btn.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_btns(self):
        for digits, grid_value in self.digits_num.items():
            btn = tk.Button(self.btnframe, text=str(
                digits), bg=WHITE, fg=LBL_COLOR, font=BTNS_FONT_STYLE, borderwidth=0, command=lambda x=digits: self.add_to_expression(x))
            btn.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_display_lbls(self):
        total_lbl = tk.Label(self.display_frame, text=self.total_expression,
                             anchor=tk.E, bg=LIGHT_GRAY, fg=LBL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_lbl.pack(expand=True, fill='both')

        lbl = tk.Label(self.display_frame, text=self.expression,
                       anchor=tk.E, bg=LIGHT_GRAY, fg=LBL_COLOR, padx=24, font=LARG_FONT_STYLE)
        lbl.pack(expand=True, fill='both')

        return total_lbl, lbl


if __name__ == "__main__":
    cal = Calc().root.mainloop()

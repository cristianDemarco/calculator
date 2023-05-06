from abc import abstractmethod
from Costants import OPERATORS
import sys

class CalcButton:
    def __init__(self, text, row, column, background = "white"):
        self.text = text
        self.row = row
        self.column = column
        self.background = background
        self.width = 14
        self.height = 3
        self.font_size = 10

class ButtonOperator(CalcButton):
    def create_button(self, tk, buttons, font, calc_display, calc_result):
        button = tk.Button(
            master = buttons,
            text = self.text,
            background = "cyan",
            width = self.width,
            height = self.height,
            command = lambda : self.display_value(calc_display))
        button.grid(row = self.row, column = self.column)
        button["font"] = font.Font(size = self.font_size)

    def display_value(self, calc_display):
        calc_text = calc_display.cget("text")
        if(calc_text[-1:] in OPERATORS):
            calc_text = calc_text[:-1] + self.text
        else:
            calc_text += self.text

        calc_display.configure(text = calc_text)

class ButtonThatDisplayValue(CalcButton):
    def create_button(self, tk, buttons, font, calc_display, calc_result):
        button = tk.Button(
            master = buttons,
            text = self.text,
            background = self.background,
            width = self.width,
            height = self.height,
            command = lambda : self.display_value(calc_display))
        button.grid(row = self.row, column = self.column)
        button["font"] = font.Font(size = self.font_size)

    def display_value(self, calc_display):
        calc_text = calc_display.cget("text") + self.text        
        calc_display.configure(text=calc_text)

class ButtonWithSpecialUtil(CalcButton):
    def create_button(self, tk, buttons, font, calc_display, calc_result):
        button = tk.Button(
            master = buttons,
            text = self.text,
            background = self.background,
            width = self.width,
            height = self.height,
            command = lambda : self.command(calc_display, calc_result)
        )
        button.grid(row = self.row, column = self.column)
        button["font"] = font.Font(size = self.font_size)

    @abstractmethod
    def command(self, calc_display, calc_result):
        pass

class ButtonEqual(ButtonWithSpecialUtil):
    def command(self, calc_display, calc_result):
        result = calc_display.cget("text")

        for key in OPERATORS:
            result = result.replace(key, OPERATORS.get(key))  

        calc_result.configure(text = + eval(result))

class ButtonCanc(ButtonWithSpecialUtil):
    def command(self, calc_display, calc_result):
        calc_display.configure(text = calc_display.cget("text")[:-1])
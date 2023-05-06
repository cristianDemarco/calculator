
from Button import ButtonThatDisplayValue, ButtonOperator, ButtonCanc, ButtonEqual



def create_buttons(tk, buttons_frame, font, calc_display, calc_result):
    buttons = [
        ButtonThatDisplayValue("(", 0, 0),
        ButtonThatDisplayValue(")", 0, 1),
        ButtonThatDisplayValue("7", 1, 0),
        ButtonThatDisplayValue("4", 2, 0),
        ButtonThatDisplayValue("1", 3, 0),
        ButtonCanc("C", 0, 3, "red"),
        ButtonThatDisplayValue("8", 1, 1),
        ButtonThatDisplayValue("5", 2, 1),
        ButtonThatDisplayValue("2", 3, 1),
        ButtonThatDisplayValue("%", 0, 2),
        ButtonThatDisplayValue("0", 4, 0),
        ButtonThatDisplayValue("6", 2, 2),
        ButtonThatDisplayValue("3", 1, 2),
        ButtonThatDisplayValue(".", 4, 1),
        ButtonThatDisplayValue("9", 3, 2),
        ButtonOperator("÷", 1, 3),
        ButtonOperator("x", 2, 3),
        ButtonOperator("-", 3, 3),
        ButtonOperator("+", 4, 3),
        ButtonEqual("=", 4, 2, "green")
    ]

    for button in buttons:
        button.create_button(tk, buttons_frame, font, calc_display, calc_result)

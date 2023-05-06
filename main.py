import tkinter as tk
import tkinter.font as font
import create_button

window = tk.Tk()
window.title("Tkinter Calculator")
window.geometry("600x600")
window.configure(background = "#4d4d4d")

calc_display = tk.Label(
    text="",
    width = 45,
    height = 8,
    relief = tk.RAISED,
    borderwidth=5,
    foreground="black",
    background="#bfbfbf",
    anchor=tk.NW,
    font = ("Arial", 16),
    pady=15,
    padx = 15)

calc_display.pack(pady = 10)

calc_result = tk.Label(
    text="",
    foreground="black",
    background="#bfbfbf",
    anchor=tk.SE,
    font = ("Arial", 22))

calc_result.place(x = 30, y = 200)

buttons_frame = tk.Frame(master = window)
create_button.create_buttons(tk, buttons_frame, font, calc_display, calc_result)
buttons_frame.pack()

window.mainloop()
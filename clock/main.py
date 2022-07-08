import tkinter as ui
import time

window = ui.Tk()


def update_clock():
    second = time.strftime("%S")
    minute = time.strftime("%M")
    hour = time.strftime("%I")
    am_or_pm = time.strftime("%p")

    timefmt = hour + " : " + minute + " : " + second + " " + am_or_pm

    clock_label.config(text=timefmt)
    clock_label.after(1000, update_clock)


clock_label = ui.Label(window, text="00:00:00", font="lavender 72 bold")
clock_label.pack()

update_clock()
window.mainloop()

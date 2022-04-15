from tkinter import *
from tkinter import ttk

def convert():
    try:
        outtext = "Here's your conversion:"
        input_inches = int(txt_inchentry.get())
        input_intervals = int(txt_intervalentry.get())
        starting_inches = 0
        for num in range(0, input_intervals+1):
            starting_inches += input_inches
            feet_conversion = int(starting_inches/12)
            inch_conversion = int(starting_inches%12)
            outtext += f"\n{num}. {feet_conversion}ft {inch_conversion}in"
        outputstr.set(outtext)

    except:
        outputstr.set("There has been an error. Try entering \nnon-decimal numbers above.")

root = Tk()
root.title("Interval converter (in to ft and in)")
root.geometry("350x350")

outputstr = StringVar(root)

lbl_inchentry = ttk.Label(root, text="Insert inches between each interval here: ")
lbl_inchentry.grid(column=0, row=0, padx=2, pady=2)

lbl_intervalentry = ttk.Label(root, text="Insert amount of intervals here: ")
lbl_intervalentry.grid(column=0, row=1, padx=2, pady=2)

txt_inchentry = ttk.Entry(root, width=15)
txt_inchentry.grid(column=1, row=0, padx=2, pady=2)

txt_intervalentry = ttk.Entry(root, width=15)
txt_intervalentry.grid(column=1, row=1, padx=2, pady=2)

frm_outline = ttk.Frame(root)
frm_outline.grid(column=0, row=2, columnspan=2)

btn_convert = ttk.Button(frm_outline, text="Convert to ft and in", command=convert)
btn_convert.grid(column=0, row=0, padx=2, pady=2)

lbl_output = ttk.Label(frm_outline, textvariable=outputstr, width=40)
lbl_output.grid(column=0, row=1, padx=2, pady=2)

root.mainloop()
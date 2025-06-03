import tkinter

# Window
window = tkinter.Tk()
window.minsize(width=300, height=200)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

def calculate():
    res_label.config(text=int(miles_input.get()) * 1.6)

# Label
miles_label = tkinter.Label(text="Miles", font=("Poppins", 12))
miles_label.grid(row=0, column=2)
miles_label.config(padx=5, pady=5)

km_label = tkinter.Label(text="Km", font=("Poppins", 12))
km_label.grid(row=1, column=2)
km_label.config(padx=5, pady=5)

cal_label = tkinter.Label(text="is equal to", font=("Poppins", 12))
cal_label.grid(row=1, column=0)
cal_label.config(padx=5, pady=5)

res_label = tkinter.Label(text="0", font=("Poppins", 12))
res_label.grid(row=1, column=1)
res_label.config(padx=5, pady=5)

# Entry
miles_input = tkinter.Entry(width=10)
miles_input.grid(row=0, column=1)

# Button
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
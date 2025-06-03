import tkinter

# Window
window = tkinter.Tk()
window.minsize(width=500, height=300)

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

# Label
my_label = tkinter.Label(text="This is my label", font=("Poppins", 24, "bold"))
my_label.grid(row=0, column=0)

# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

# New Button
new_button = tkinter.Button(text="Also Click Me", command=button_clicked)
new_button.grid(row=0, column=2)

# Entry
input = tkinter.Entry(width=10)
input.grid(row=3, column=3)

window.mainloop()

from tkinter import *

root = Tk()
root.title("Calculate student scores")

prompt = Label(root, text="How many tests?").grid(row=0)
text_input = Entry(root).grid(row=0, column=1)

def submit_int():
    while True:
        try:
            tests = int(text_input.get())
            break
        
        except ValueError:
            Label(root, text="Enter a number instead.")

Button(root, text="Submit", command=submit_int).grid(row=0, column=2)

root.mainloop()
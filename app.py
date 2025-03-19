from tkinter import *

def show():
    text_box.config(text="What did the bison say to his son when he left the ranch? Bi-son.")

root = Tk()
root.title("AWESOME JOKES, please laugh")

text_box = Label(root, text="Why did the electric car feel discriminated against? Because the rules weren't current.", width=75).pack()

button = Button(root, text="Ew what is this cringe. (Exit program)", width=50, command=root.destroy).pack()

show_button = Button(root, text="Show me another dad joke", width=50, command=show).pack()

Label(root, text="Please laugh").pack()
text_input = Entry(root).pack()

root.mainloop()
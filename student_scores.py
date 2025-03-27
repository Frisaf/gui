from tkinter import *
from time import sleep

root = Tk()
root.title("Calculate student scores")

prompt = Label(root, text="How many tests?")
prompt.grid(row=0)
text_input = Entry(root)
text_input.grid(row=0, column=1)
error_msg = Label(root, text="")
error_msg.grid(row=100)

names = []
scores = []
student_scores = []
count = 0

def submit_tests():
    try:
        global tests, student_btn

        tests = int(text_input.get())
        Label(root, text=f"{tests} tests").grid(row=1)
        student_btn = Button(root, text="Submit", command=submit_students)
        student_btn.grid(row=0, column=2)
        prompt.config(text="Student name")
        error_msg.config(text="")
        submit_button.destroy()
        
    except ValueError:
        error_msg.config(text="Enter a number instead")

def submit_students():
    student_btn.grid_forget()

    global student_name

    student_name = text_input.get()

    while True:
        if student_name == "":
            break

        else:
            names.append(student_name)
            student_scores.append([])
            student_scores[count].append(student_name)
            break

def submit_scores():
    score_input = Entry(root).grid(row=3, column=2)

    score_prompt = Label(root, text=f"Enter the student's scores one by one.\n{student_name}'s score")
    score_prompt.grid(row=3)

    try:
        score = int(score_input.get())
        scores.append(score)
    
    except ValueError:
        error_msg.config(text="Enter a number instead")


submit_button = Button(root, text="Submit", command=submit_tests)
submit_button.grid(row=0, column=2)

root.mainloop()
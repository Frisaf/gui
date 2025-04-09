from tkinter import *

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
student_avg = []
count = 0

def submit_tests():
    try:
        global tests, student_btn

        tests = int(text_input.get())

        if tests < 1 or tests > 10:
            error_msg.config(text="The number of tests cannot be below 1 or exceed 10.")
            return
        
        Label(root, text=f"{tests} tests").grid(row=1)
        student_btn = Button(root, text="Submit", command=submit_students)
        student_btn.grid(row=0, column=2)
        prompt.config(text="Student name\nLeave empty if done")
        error_msg.config(text="")
        submit_button.destroy()
        
    except ValueError:
        error_msg.config(text="Enter a number instead")

def submit_students():
    student_btn.grid_forget()
    error_msg.config(text="")

    global student_name

    student_name = text_input.get()

    if student_name == "":
        calculate()

    else:
        global score_input, score_prompt, score_btn

        names.append(student_name)
        student_scores.append([])
        student_scores[count].append(student_name)
        score_input = Entry(root)
        score_input.grid(row=3, column=1)

        score_prompt = Label(root, text=f"Enter the student's scores one by one.\n{student_name}'s score")
        score_btn = Button(root, text="Submit", command=submit_scores)
        print(score_btn.grid_info())

        score_prompt.grid(row=3, column=0)
        score_btn.grid(row=3, column=2)

def submit_scores():
    global count

    try:
        score = int(score_input.get())
        scores.append(score)
        print(names, scores, student_scores)
    
    except ValueError:
        error_msg.config(text="Enter a number instead")
    
    if len(scores) == tests:
        score_prompt.grid_forget()
        score_btn.grid_forget()
        score_input.grid_forget()
        student_btn.grid(row=0, column=2)
        
        for i in range(len(scores)):
            student_scores[count].append(scores[i])
        
        count += 1
        scores.clear()
        print(names, scores, student_scores)

def calculate():
    r = 0

    error_msg.config(text="")
    prompt.grid_forget()
    text_input.grid_forget()

    for item in student_scores:
        for x in item:
            if type(x) == str:
                name = x
            
            elif type(x) == int:
                student_avg.append(x)
        
        Label(root, text=f"{name}'s average score: {sum(student_avg)/len(student_avg)}").grid(row=4+r)
        student_avg.clear()
        r += 1
    
    c = 0

    for i in range(tests):
        total_scoring = 0

        for a in range(len(names)):
            b = student_scores[a][1+c]
            total_scoring += b

        avg = total_scoring/len(names)
        Label(root, text=f"Average score for test {i+1}: {avg}").grid(row=5+r+c)
        c += 1

submit_button = Button(root, text="Submit", command=submit_tests)
submit_button.grid(row=0, column=2)

root.mainloop()
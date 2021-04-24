from tkinter import *
q = [
    "What is the capital of india?",
    "Which of the following is not a Java features?",
    "What is used to find and fix bugs in the Java programs?",
    "Which of the following is a reserved keyword in Java?",
    "The keyword used to transfer control from a function back to the calling function in C is?",
    "Which header file should be included to use functions like malloc() and calloc()?",
    "Where does the swap space reside ?(OS)",
    "Which of the following scheduling algorithms is non-preemptive?(OS)"
]
options = [
["Delhi" , "mumbai" , "kanpur" , "hydrebad"],
["Dynamic" , "Architecture Neutral" , "Use of pointers" , "Object-oriented"],
["JVM" , "JDK" , "JRE" , "JDB"],
["object" , "strictfp" ,  "main" , "system"],
["switch" , "goto" , "goback" , "return"],
["string.h" , " stdlib.h" , "dos.h" , "Memory.h"],
["RAM" , "DISK" , "ROM" , "ON-CHIP CACHE"],
["Round robin" , "First-in-First-Out" , "MultiLevel Queue Scheduling" , "none"]


]

a = [1, 3, 4, 2, 2, 2, 2, 2]

class Quiz:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.button = Button(master, text="Back", command=self.back_btn)
        self.button.pack(side = BOTTOM)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def create_q(self, master, qn):
        w = Label(master, text=q[qn])
        w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master , text="foo" , variable=self.opt_selected, value=b_val+1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
            self.opts[b_val] ['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True
        return False

    def printresults(self):
        print("score: ", self.correct, "/", len(q))

    def back_btn(self):
        print("Go back")

    def next_btn(self):
        if self.check_q(self.qn):
            print("correct")
            self.correct += 1
        else:
            print("Wrong")
        self.qn = self.qn + 1
        if self.qn >= len(q):
            self.printresults()
        else:
            self.display_q(self.qn)


root = Tk()
root.geometry("500x300")
root.title("Sakshi's Quiz")
root.configure(background="pink")


app = Quiz(root)
root.mainloop()












import tkinter as tk
import random as r

def ran_win():
    num = r.randint(1,3)
    if num == 1:
        return "rock"
    elif num == 2:
        return "paper"
    elif num == 3:
        return "rock"

def gameresults(comp,user):
    if comp == user:
        return "TIE"
    elif (comp == "rock") & (user == "scissors"):
        return "LOSE"
    elif (user == "rock") & (comp == "scissors"):
        return "WIN"
    elif (comp == "paper") & (user == "rock"):
        return "LOSE"
    elif (user == "paper") & (comp == "rock"):
        return "WIN"
    elif (comp == "scissors") & (user == "paper"):
        return "LOSE"
    elif (user == "scissors") & (comp == "paper"):
        return "WIN"


class Application(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.go = tk.Button(self)
        self.go["text"] = "rock paper scissors go"
        self.go["command"] = self.set_go
        self.go.pack(side="top")

        self.userin = tk.Entry(self)
        self.userin.pack(side="left")
        self.userin.focus_set()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def set_go(self):
        user = self.userin.get().lower()
        winlose = gameresults(ran_win(), user)
        label = tk.Label(root, width=700, bg="white", text="you " + winlose, borderwidth=0, font=("Calibri", 20))
        label.pack(side="right")


root = tk.Tk()
app = Application(master=root)
app.mainloop()
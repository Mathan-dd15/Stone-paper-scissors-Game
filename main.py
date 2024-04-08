import tkinter as tk
from tkinter import messagebox
import random

def computer_choice():
    return random.choice(['stone','paper','scissor'])

def winner(user,computer):
    if user == computer:
        return 'It is a tie'
    elif (user == 'stone' and computer == 'scissor') or (user == 'paper' and computer == 'stone') or (user == 'scissor' and computer == 'paper'):
        return 'you win'
    else:
        return 'computer win' 

def final(choice):
    computer_selection=computer_choice()
    result = winner(choice,computer_selection)
    messagebox.showinfo("Result",f"you chose : {choice}.\nComputer chose: {computer_selection}.\n result is {result}")
    
table = tk.Tk()
table.title('stone-paper-scissor')
table.geometry('300x100')

label = tk.Label(table,text = 'click your choice')
label.pack(padx=10,pady=10)

b_stone = tk.Button(table,text = "stone",command = lambda: final('stone'))
b_stone.pack(side=tk.LEFT,pady=30)

b_paper = tk.Button(table,text = "paper", command = lambda: final('paper'))
b_paper.pack(side=tk.LEFT,padx=75)

b_scissor = tk.Button(table,text = "scissor", command = lambda: final('scissor'))
b_scissor.pack(side=tk.RIGHT,pady=5)

table.mainloop()

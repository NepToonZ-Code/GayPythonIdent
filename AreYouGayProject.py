#Just so you know this is pure irony. This wasn't made to tolerate homophobia and discriminative behavior. I, the owner myself am not the straighest either.
import tkinter as tk
from tkinter import ttk 
import random  
import time 

root = tk.Tk()
root.title("Am I gay?")
root.geometry("500x115")
root.configure(
        bg="green",
)

content = [
          "Idk, are you?",
          "If you don't play Gayshit Impact, no.",
          "Definitely, get off fucking Gayshit Impact.",
          "Just stop playing Gayshit Impact",
          "Yes.",
]

def onclickfunc():
          for i in range(30):
                    progress_bar.step(10)
                    root.update_idletasks()
                    time.sleep(0.1)

          result_label.config(text=random.choice(content))

          print("user got: " + random.choice(content))
          print("Command executed successfully, yay =)")


loading_frame = tk.Frame(root)
loading_frame.pack()

progress_bar = ttk.Progressbar(loading_frame, orient='horizontal', length=200, mode='determinate')
progress_bar.pack(pady=10)

result_frame = tk.Frame(root)
result_frame.pack()

# Label to display the result
result_label = tk.Label(result_frame, text="")
result_label.pack(pady=10)
   

button = tk.Button(root, text="Find out", command=onclickfunc)
button.pack()


root.mainloop()
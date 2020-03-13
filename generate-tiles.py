#!/usr/bin/python3

from tkinter import Tk, Label, Button, Entry, END, E, W, filedialog
import generator

class TileMaker:
  def __init__(self, master):
    self.master = master
    master.title("Tile Maker")

    self.label = Label(master, text="File to convert")
    self.pick_file_button = Button(master, text="Choose File", command=lambda: self.pickFile()) 
    self.label.grid(row=0, column=0, sticky=E)
    self.pick_file_button.grid(row=0, column=1, sticky=W)

  def pickFile(self):
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    generator.some_func(root.filename)
    return

root = Tk()
gui = TileMaker(root)
root.mainloop()

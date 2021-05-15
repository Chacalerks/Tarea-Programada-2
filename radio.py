import tkinter as Tkinter
parent_widget = Tkinter.Tk()
v = Tkinter.IntVar()
v.set(1) # need to use v.set and v.get to
# set and get the value of this variable
radiobutton_widget1 = Tkinter.Radiobutton(parent_widget,
                                   text="Radiobutton 1",
                                   variable=v, value=1)
radiobutton_widget2 = Tkinter.Radiobutton(parent_widget,
                                   text="Radiobutton 2",
                                   variable=v, value=2)
radiobutton_widget1.pack()
radiobutton_widget2.pack()
Tkinter.mainloop()
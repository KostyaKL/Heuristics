import _tkinter
top = _tkinter.create()

B = _tkinter.butt(top, text ="Hello", command = helloCallBack)

B.pack()

top.mainloop()
import tkinter as tk

class Page(tk.Frame):
		def __init__(self, *args, **kwargs):
				tk.Frame.__init__(self, *args, **kwargs)
		def show(self):
				self.lift()

class Page1(Page):
	 def __init__(self, *args, **kwargs):
			 Page.__init__(self, *args, **kwargs)
			 label = tk.Label(self, text="This is page 1")
			 label.pack(side="top", fill="both", expand=True)

class Page2(Page):
	 def __init__(self, *args, **kwargs):
			 Page.__init__(self, *args, **kwargs)
			 label = tk.Label(self, text="This is page 2")
			 label.pack(side="top", fill="both", expand=True)

class Page3(Page):
	 def __init__(self, *args, **kwargs):
			 Page.__init__(self, *args, **kwargs)
			 label = tk.Label(self, text="This is page 3")
			 label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
		def __init__(self, *args, **kwargs):
				tk.Frame.__init__(self, *args, **kwargs)
				p1 = Page1(self)
				p2 = Page2(self)
				p3 = Page3(self)

				title = tk.Label(text="Pokemon Timer")
				title.grid(column=1, row = 1, columnspan = 4)
				title.config(anchor="center")

				buttonframe = tk.Frame(self)
				container = tk.Frame(self)
				buttonframe.pack(side="top", fill="x", expand=False)
				container.pack(side="top", fill="both", expand=True)

				p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
				p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
				p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

				b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
				b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
				b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)

				b1.pack(side="left")
				b2.pack(side="left")
				b3.pack(side="left")

				p1.show()

if __name__ == "__main__":
		root = tk.Tk()
		main = MainView(root)
		main.grid(column=0, row = 0)
		root.wm_geometry("400x400")
		root.mainloop()

		for i in range(5):
			root.grid_rowconfigure(i, weight=1)

		for i in range(4):
			root.grid_columnconfigure(i, weight =1)
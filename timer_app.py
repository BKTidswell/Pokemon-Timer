# for python 3.x use 'tkinter' rather than 'Tkinter'
import tkinter as tk
from random import *
from PIL import Image, ImageTk
import time
from pkmn_library import *

start_seconds = 360
timer = "{m}:{s}"

timer_options = [
"1 minute",
"5 minutes",
"10 minutes",
"15 minutes",
"20 minutes",
"25 minutes",
"30 minutes",
]

env_options = [
"Beach",
#"Cave",
#"Field",
"Forest",
#"Mountain",
#"Town",
"Volcano",
]

size = (100,100)


def createImageLabels(imagePaths):
	images = []
	photos = []
	imageLabels = []

	for i,im in enumerate(imagePaths):
		images.append(Image.open(im))
		images[i].thumbnail(size,Image.ANTIALIAS)
		photos.append(ImageTk.PhotoImage(images[i]))
		imageLabels.append(tk.Label(image = photos[i]))
		imageLabels[i].image = photos[i]

	return imageLabels

def addToCaught(pkmnCaught):
	

class App():

	def __init__(self):
		self.root = tk.Tk()
		self.root.resizable(height = 0, width = 0)

		for i in range(5):
			self.root.grid_rowconfigure(i,  weight=1)

		for i in range(4):
			self.root.grid_columnconfigure(i,  weight =1)

		title = tk.Label(text="Pokemon Timer")
		title.grid(column=0, row = 0, columnspan = 4)
		title.config(anchor="center")

		self.timer_text = tk.Label(text="")
		self.catchText = tk.Label(text="")
		self.catchStatusText = tk.Label(text="")

		self.timer_mins = tk.StringVar()
		self.timer_mins.set(timer_options[0])

		self.explore_env = tk.StringVar()
		self.explore_env.set(env_options[0])

		self.time_selector = tk.OptionMenu(self.root, self.timer_mins, *timer_options)
		self.env_selector = tk.OptionMenu(self.root, self.explore_env, *env_options)
		
		self.button1 = tk.Button(text='Start Timer', command=self.getStartTime)
		self.button2 = tk.Button(text='Cancel Timer', command=self.endTimer)
		self.button3 = tk.Button(text='Restart Timer', command=self.getStartTime)

		self.backButton = tk.Button(text='Run Away', command=self.MainPage)
		self.catchButton = tk.Button(text='Catch!', command=self.catchPkmn)

		self._job = None
		self.env_label = None

		env_path = "Pokemon_Smile_Envs/{}.png".format(self.explore_env.get())
		self.env_label = createImageLabels([env_path])[0]

		pkmn_path = "Pokemon_Smile_Pokemon/{}.png".format("001")
		self.pkmn_label = createImageLabels([pkmn_path])[0]

		self.MainPage()

		self.root.mainloop()

	def MainPage(self):
		pkmn_imgs = []

		for i in range(4):
			pkmn_num = str(randint(1,151)).zfill(3)
			pkmn_imgs.append("Pokemon_Smile_Pokemon/{}.png".format(pkmn_num))
			
		self.img_labels = createImageLabels(pkmn_imgs)

		for i,im in enumerate(self.img_labels):
			im.grid(row = 1, column = i)

		self.env_label.grid_forget()

		self.timer_text.grid_forget()

		self.time_selector.grid(column=0, row = 3, columnspan = 2)
		self.time_selector.config(anchor="center")

		self.env_selector.grid(column=2, row = 3, columnspan = 2)
		self.env_selector.config(anchor="center")

		self.button1.grid(column=0, row = 4, columnspan = 4)
		self.button1.config(anchor="center")

		self.catchText.grid_forget()
		self.backButton.grid_forget()
		self.pkmn_label.grid_forget()
		self.button2.grid_forget()
		self.button3.grid_forget()

	def TimerPage(self):
		env_path = "Pokemon_Smile_Envs/{}.png".format(self.explore_env.get())
		env_img = Image.open(env_path)
		env_img.thumbnail(size,Image.ANTIALIAS)
		env_photos = ImageTk.PhotoImage(env_img)
		self.env_label = tk.Label(image = env_photos)
		self.env_label.image = env_photos

		for im in self.img_labels:
			im.grid_forget()

		self.timer_text.grid(column=0, row = 1, columnspan = 4)
		self.timer_text.config(anchor="center")

		self.env_label.grid(column=0, row = 2, columnspan = 4)
		self.env_label.config(anchor="center")

		self.time_selector.grid_forget()
		self.env_selector.grid_forget()

		self.button1.grid_forget()

		self.button2.grid(column=2, row = 3, columnspan = 2)
		self.button2.config(anchor="center")

		self.button3.grid(column=0, row = 3, columnspan = 2)
		self.button3.config(anchor="center")

	def CatchPage(self):
		self.timer_text.grid_forget()
		self.env_label.grid_forget()
		self.button2.grid_forget()
		self.button3.grid_forget()

		env_name = self.explore_env.get()
		pkmn_found = choices(pkmn_env[env_name][0],pkmn_env[env_name][1])[0]
		self.pkmn_found_class = core_pkmn_dict[pkmn_found]

		pkmn_path = "Pokemon_Smile_Pokemon/{}.png".format(self.pkmn_found_class.img)
		pkmn_img = Image.open(pkmn_path)
		pkmn_img.thumbnail(size,Image.ANTIALIAS)
		pkmn_photos = ImageTk.PhotoImage(pkmn_img)
		self.pkmn_label = tk.Label(image = pkmn_photos)
		self.pkmn_label.image = pkmn_photos

		self.catchText.configure(text="You found a {}!".format(pkmn_found))
		self.catchText.grid(column=0, row = 1, columnspan = 2)
		self.catchText.config(anchor="center")

		self.pkmn_label.grid(column=0, row = 2, columnspan = 2)
		self.pkmn_label.config(anchor="center")

		self.backButton.configure(text="Run Away")
		self.backButton.grid(column=0, row = 3)
		self.catchButton.grid(column=1, row = 3)
		

	def cancel(self):
		if self._job is not None:
			self.root.after_cancel(self._job)
			self._job = None

	def update_clock(self,timer_seconds):
		m = str(int(timer_seconds/60)).zfill(2)
		s = str(timer_seconds%60).zfill(2)

		time_left = timer.format(m=m,s=s)

		self.timer_text.configure(text=time_left)

		if timer_seconds > 0:
			 self._job = self.root.after(1000, self.update_clock, timer_seconds-1)
		else:
			self.cancel()

			#Only Long Timers get to catch, not in testing tho
			if int(self.timer_mins.get()[0:2]) >= 0.5:
				self.CatchPage()
			else:
				self.MainPage()

	def getStartTime(self):  
		self.cancel()  
		self.TimerPage() 
		#Now is seconds not minutes
		self.update_clock(int(self.timer_mins.get()[0:2]))

	def endTimer(self):
		self.cancel()
		self.MainPage() 
		self.timer_text.configure(text="Timer Ended")

	def catchPkmn(self):
		if randint(0,100) - int(self.timer_mins.get()[0:2]) < self.pkmn_found_class.catch_rate:
			self.catchText.configure(text="You caught the {}!".format(self.pkmn_found_class.species))
		else:
			self.catchText.configure(text="The {} got away...".format(self.pkmn_found_class.species))

		self.catchButton.grid_forget()
		self.backButton.configure(text="Go Back")
		self.pkmn_label.config(anchor="center")

app=App()
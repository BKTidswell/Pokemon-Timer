# for python 3.x use 'tkinter' rather than 'Tkinter'
import tkinter as tk
from random import *
from PIL import Image, ImageTk
import time, os, sys
from pkmn_library import *
import pickle
from functools import partial
from datetime import date
import os
from playsound import playsound

timer = "{m}:{s}"

#Timer minute options so I don't have to deal with 
# user input
timer_options = [
"1 minute",
"5 minutes",
"10 minutes",
"15 minutes",
"20 minutes",
"25 minutes",
"30 minutes",
]

#Places where you can go to find pokemon
env_options = [
"Beach",
#"Cave",
#"Field",
"Forest",
#"Mountain",
#"Town",
"Volcano",
]

#Sort Options 
sort_options = [
"Old to New",
"New to Old",
"High to Low",
"Low to High",
"A to Z",
"Z to A"
]

#Set Background color
bgColor = "white"

#Set size of images and box images
size = (100,100)
smallSize = (50,50)

boxSize = (110,110)
smallBoxSize = (60,60)


#Set number of box rows and columns
boxCols = 6
boxRows = 6
pkmnPerBox = boxCols*boxRows

#Set grid limits
maxGridCols = 8
maxGridRows = 8

#This takes an array of image paths and returns an array of image labels 
def createImageLabels(imagePaths,imSize):
	images = []
	photos = []
	imageLabels = []

	#Most of this is just taken from a tutorial online
	for i,im in enumerate(imagePaths):
		images.append(Image.open(im))
		images[i].thumbnail(imSize,Image.ANTIALIAS)
		photos.append(ImageTk.PhotoImage(images[i]))
		imageLabels.append(tk.Label(image = photos[i], bg=bgColor))
		imageLabels[i].image = photos[i]

	return imageLabels

#This adds a Pokemon to the caught list
def addToCaught(pkmn):
	today = date.today()
	caughtPokemon.append(Pkmn_Captured(pkmn.species,
									   pkmn.species,
									   randint(pkmn.minLvl,pkmn.maxLvl),
									   False,
									   False,
									   today.strftime("%m/%d/%y"),
									   pkmn.img))

#Sets all the values to an evolved pokemon
def evolvePkmn(pkmn):
	#Get the data from one of the random evolved forms
	#The random choice is only so I can do eevee
	#	Now that is thinking ahead! Otherwise idk how I would do that
	evolvedForm = core_pkmn_dict[choice(core_pkmn_dict[pkmn.species].evolution)]

	pkmn.name = evolvedForm.species
	pkmn.species = evolvedForm.species
	pkmn.can_evolve = False
	pkmn.img = evolvedForm.img


def lvlUpPkmn(pkmn):
	pkmn.level += 1

	if core_pkmn_dict[pkmn.species].evolution[0] and pkmn.level >= core_pkmn_dict[pkmn.species].evolution_lvl:
		pkmn.can_evolve = True

#Makes the save file	
def savePkmn():
	with open('save.ini', 'wb') as f:
		pickle.dump([candy, caughtPokemon], f, protocol=2)

#loads the save file
def loadPkmn():
	with open('save.ini', 'rb') as f:
		try:
			candy, caughtPokemon = pickle.load(f)
		except EOFError:
			candy, caughtPokemon = []
		
	return candy, caughtPokemon

def makeFavs():
	favPokemon = []

	for pkmn in caughtPokemon:
		if pkmn.favorite:
			favPokemon.append(pkmn)

	return(favPokemon)

#If there is a save file load it
if os.path.exists("save.ini"):
	candy, caughtPokemon = loadPkmn()


#To Do:

#	Evolution:
#		Add ability to level up pokemon

#	Stats:
#		Save timer runs to CSV
#		Add stats page
#		Add export stats ability


class App():

	def __init__(self):

		self.favePokemon = makeFavs()

		self.makeSortedPkmn()

		self.root = tk.Tk()
		self.root.title('Pokemon Timer')
		self.root.resizable(height = 0, width = 0)
		self.root.configure(bg=bgColor)

		#Set weights on all grids and rows in order to allow for resizing
		for i in range(maxGridRows):
			self.root.grid_rowconfigure(i,  weight=1)

		for i in range(maxGridCols):
			self.root.grid_columnconfigure(i,  weight=1)

		#Create the title, make it big, and set it across all rows
		self.title = tk.Label(text="Pokemon Timer", bg=bgColor)
		self.title.config(font=("Arial", 44))
		self.title.grid(column=0, row = 0, columnspan = maxGridCols)
		self.title.config(anchor="center")

		#Create Labels for the timer, catching, and the status of your catch, and candy
		self.timerText = tk.Label(text="", bg=bgColor)
		self.timerText.config(font=("Arial", 44))

		self.catchText = tk.Label(text="", bg=bgColor)
		self.catchStatusText = tk.Label(text="", bg=bgColor)

		self.candyText = tk.Label(text="", bg=bgColor)
		self.candyCounter =  tk.Label(text="You have {} candy".format(candy), bg=bgColor)

		#Create the varible to set your timer time
		self.timer_mins = tk.StringVar()
		self.timer_mins.set(timer_options[0])

		#Create the varible to set your environment to explore
		self.explore_env = tk.StringVar()
		self.explore_env.set(env_options[0])

		#Create the varible to set the sorting variable
		self.pkmn_sort = tk.StringVar()
		self.pkmn_sort.set(sort_options[0])

		#Makes an option menu to choose your times
		self.time_selector = tk.OptionMenu(self.root, self.timer_mins, *timer_options)
		self.time_selector.config(bg=bgColor)

		#Makes an option menu to choose your environment
		self.env_selector = tk.OptionMenu(self.root, self.explore_env, *env_options)
		self.env_selector.config(bg=bgColor)

		#Makes an option menu to choose sorting
		self.sort_selector = tk.OptionMenu(self.root, self.pkmn_sort, *sort_options, command=partial(self.BoxesPage,0))
		self.sort_selector.config(bg=bgColor)
		
		#Makes the buttons to start, cancel, and restart the timer
		self.startButton = tk.Button(text='Start Timer', command=self.getStartTime, highlightbackground=bgColor)
		self.pauseButton = tk.Button(text='Pause Timer', command=self.PauseTimer, highlightbackground=bgColor)
		self.cancelButton = tk.Button(text='Cancel Timer', command=self.endTimer, highlightbackground=bgColor)
		self.restartButton = tk.Button(text='Restart Timer', command=self.getStartTime, highlightbackground=bgColor)

		#Makes the buttons to Run Away (Return to main menu) and catch a pokemon
		self.backButton = tk.Button(text='Run Away', command=self.MainPage, highlightbackground=bgColor)
		self.catchButton = tk.Button(text='Catch!', command=self.catchPkmn, highlightbackground=bgColor)

		#Make button to go to candy page
		self.candyButton = tk.Button(text='Candy!', command=self.CandyPage, highlightbackground=bgColor)

		#Create the button to go to the first box page
		self.boxButton = tk.Button(text='Boxes', command=lambda: self.BoxesPage(0), highlightbackground=bgColor)

		#Make the other buttons to go to other box pages
		# They start at 0 but need a placeholder here
		self.boxBackButton = tk.Button(text='<', command=lambda: self.BoxesPage(0), highlightbackground=bgColor)
		self.boxNextButton = tk.Button(text='>', command=lambda: self.BoxesPage(0), highlightbackground=bgColor)

		#Make Pokemon evolution button
		self.evolveButton = tk.Button(text='Evolve!', command=lambda: evolvePkmn(caughtPokemon[0]), highlightbackground=bgColor)

		#Make level up button
		self.levelUpButton = tk.Button(text='Level Up!', command=lambda: lvlUpPkmn(caughtPokemon[0]), highlightbackground=bgColor)

		#Makes job for timer so it can be stopped
		#Honestly it's funny how little of this is about the timer lol
		self._job = None
		self.paused = False

		#Make place holder for box images and env label so they can be removed on the Main page
		self.envLabel = None
		self.boxImages = []
		self.boxOutImages = []

		#Make labels for pokemon details
		self.nameText = tk.Label(text="Name: {}", bg=bgColor)
		self.nameText.config(font=("Arial", 20))
		self.levelText = tk.Label(text="Level: {}", bg=bgColor)
		self.levelText.config(font=("Arial", 20))
		self.favText = tk.Label(text="Favorite: {}", bg=bgColor)
		self.favText.config(font=("Arial", 20))
		self.dateText = tk.Label(text="Date Caught: {}", bg=bgColor)
		self.dateText.config(font=("Arial", 20))

		#Makes the envionment image so it can be removed on the Main page
		env_path = "Pokemon_Smile_Envs/{}.png".format(self.explore_env.get())
		self.envLabel = createImageLabels([env_path],size)[0]

		#Makes the found pokemon image so it can be removed on the Main page
		pkmn_path = "Pokemon_Smile_Pokemon/{}.png".format("001")
		self.pkmn_label = createImageLabels([pkmn_path],size)[0]

		#Makes the candy image so it can be removed on the Main page
		candy_path = "Pokemon_Smile_Envs/Candy.png"
		self.candyLabel = createImageLabels([candy_path],size)[0]

		#Make pokemon details so they can be removed
		self.currentPkmn = createImageLabels(["Pokemon_Smile_Pokemon/{}.png".format("001")],size)[0]
		self.currentBox = createImageLabels(["Pokemon_Smile_Envs/Pokemon_Box.png"],boxSize)[0]

		#Go to the main page
		self.MainPage()

		#Start the app
		self.root.mainloop()

	def MainPage(self):
		#Creates the array for the images
		pkmnImgs = []

		#Get up to 4 of the favorite pokemon
		favChoices = sample(self.favePokemon, k=min(4,len(self.favePokemon)) )

		#Add each of those to the list of paths to choose
		for fav in favChoices:
			pkmnImgs.append("Pokemon_Smile_Pokemon/{}.png".format(fav.img))

		#Randomly generate the pokemon numbers and then makes the labels of them
		for i in range( max(0,4-len(favChoices)) ):
			pkmn_num = str(randint(1,151)).zfill(3)
			pkmnImgs.append("Pokemon_Smile_Pokemon/{}.png".format(pkmn_num))
			
		self.imgLabels = createImageLabels(pkmnImgs,size)

		#Add all four labels to main menu
		for i,im in enumerate(self.imgLabels):
			im.grid(row = 1, column = i*2, columnspan = 2)
			im.config(anchor="center")

		#Place the time options menu on the next row on the first half
		self.time_selector.grid(column=0, row = 3, columnspan = int(maxGridCols/2))
		self.time_selector.config(anchor="center")

		#Place the env options menu on the next row on the other half
		self.env_selector.grid(column=int(maxGridCols/2), row = 3, columnspan = int(maxGridCols/2))
		self.env_selector.config(anchor="center")

		#Place the start button on the next row
		self.startButton.grid(column=0, row = 4, columnspan = maxGridCols)
		self.startButton.config(anchor="center")

		#Place the boxes button on the bottom right 
		self.boxButton.grid(column=maxGridCols-1, row = 5, columnspan = 2)
		self.startButton.config(anchor="center")

		#Make sure that the title spans the whole thing again
		self.title.configure(text="Pokemon Timer")
		self.title.grid(column=0, row = 0, columnspan = maxGridCols)

		self.candyCounter.configure(text="You have {} candy".format(candy))
		self.candyCounter.grid(column=2, row = 5, columnspan = 4)
		
		#Remove all the many things that are not on this page
		self.envLabel.grid_forget()
		self.timerText.grid_forget()
		self.catchText.grid_forget()
		self.backButton.grid_forget()
		self.pkmn_label.grid_forget()
		self.cancelButton.grid_forget()
		self.restartButton.grid_forget()
		self.pauseButton.grid_forget()
		self.catchButton.grid_forget()
		self.candyText.grid_forget()
		self.candyLabel.grid_forget()

		for im in self.boxImages:
			im.grid_forget()

		for im in self.boxOutImages:
			im.grid_forget()

		self.boxBackButton.grid_forget()
		self.boxNextButton.grid_forget()
		self.sort_selector.grid_forget()


	def TimerPage(self):
		#Creates the environment image to show
		env_path = "Pokemon_Smile_Envs/{}.png".format(self.explore_env.get())
		self.envLabel = createImageLabels([env_path],size)[0]

		#Adds the timer text to the page
		self.timerText.grid(column=0, row = 1, columnspan = maxGridCols)
		self.timerText.config(anchor="center")

		#Adds the environment image text to the page
		self.envLabel.grid(column=0, row = 2, columnspan = maxGridCols)
		self.envLabel.config(anchor="center")

		#Adds the restart button to the page
		self.restartButton.grid(column=0, row = 3, columnspan = 3)
		self.restartButton.config(anchor="center")

		#Adds button to pause the timer
		self.pauseButton.grid(column=4, row = 3, columnspan = 1)
		self.pauseButton.config(anchor="center")

		#Adds the cancel button to the page
		self.cancelButton.grid(column=5, row = 3, columnspan = 3)
		self.cancelButton.config(anchor="center")
		
		#Remove all the many things that are not on this page
		for im in self.imgLabels:
			im.grid_forget()

		self.title.grid_forget()
		self.time_selector.grid_forget()
		self.env_selector.grid_forget()
		self.startButton.grid_forget()
		self.boxButton.grid_forget()
		self.candyCounter.grid_forget()

	def CandyOrCatchPage(self):
		self.catchButton.config(command=self.CatchPage)
		self.catchButton.grid(column=4, row = 8, columnspan = 4)
		self.catchButton.config(anchor="center")

		#self.candyButton = tk.Button(text='Candy!', command=self.CandyPage, highlightbackground=bgColor)
		self.candyButton.grid(column=0, row = 8, columnspan = 4)
		self.candyButton.config(anchor="center")

		#Remove all the many things that are not on this page
		self.cancelButton.grid_forget()
		self.restartButton.grid_forget()
		self.pauseButton.grid_forget()

	def CandyPage(self):
		global candy

		#Calculate the candy they get
		candy_received = int( int(self.timer_mins.get()[0:2]) * 5)
		candy += candy_received

		savePkmn()

		#Add Candy image
		self.candyLabel.grid(column=0, row = 1, columnspan = maxGridCols)

		#Show how many
		self.candyText.configure(text = "You reveived {} candy!".format(candy_received))
		self.candyText.grid(column=0, row = 2, columnspan = maxGridCols)

		self.backButton.config(text = "Back")
		self.backButton.grid(column=0, row = 3, columnspan = maxGridCols)

		#Remove all the many things that are not on this page
		self.timerText.grid_forget()
		self.envLabel.grid_forget()
		self.candyButton.grid_forget()
		self.catchButton.grid_forget()

	def CatchPage(self):
		self.catchButton.config(command=self.catchPkmn)

		#Get the environment name
		env_name = self.explore_env.get()

		#Find a pokemon from that enviornment with the rarity wights
		pkmn_found = choices(pkmn_env[env_name][0],pkmn_env[env_name][1])[0]
		
		#Set that as the found pokemon by getting the class from the dict
		self.pkmn_found_class = core_pkmn_dict[pkmn_found]

		#Get the imae path and then make an image label for it
		pkmn_path = "Pokemon_Smile_Pokemon/{}.png".format(self.pkmn_found_class.img)
		self.pkmn_label = createImageLabels([pkmn_path],size)[0]

		#Change the caught text for that pokemon and display it
		self.catchText.configure(text="You found a {}!".format(pkmn_found))
		self.catchText.grid(column=0, row = 1, columnspan = maxGridCols)
		self.catchText.config(anchor="center")

		#Add the pokemon image 
		self.pkmn_label.grid(column=0, row = 2, columnspan = maxGridCols)
		self.pkmn_label.config(anchor="center")

		#Change the back button text to "Run Away" and display it
		self.backButton.configure(text="Run Away")
		self.backButton.grid(column=0, row = 3, columnspan = int(maxGridCols/2))

		#Display the catch button
		self.catchButton.grid(column=int(maxGridCols/2), row = 3, columnspan = int(maxGridCols/2))

		#Remove all the many things that are not on this page
		self.candyButton.grid_forget()
		self.timerText.grid_forget()
		self.envLabel.grid_forget()
		self.cancelButton.grid_forget()
		self.restartButton.grid_forget()
		self.pauseButton.grid_forget()

	def BoxesPage(self,boxNum,*args):
		#Remove pokemon box images first so they reset when going from one box to another
		for im in self.boxImages:
			im.grid_forget()

		for im in self.boxOutImages:
			im.grid_forget()

		#If this is not the first box then make a back button to the back before this
		if boxNum > 0:
			self.boxBackButton.configure(text='<', command= lambda: self.BoxesPage(boxNum-1))

		#If there are more boxes of pokemon after this one make the next buton go to the next one
		if (boxNum+1)*pkmnPerBox < len(caughtPokemon):
			self.boxNextButton.configure(text='>', command= lambda: self.BoxesPage(boxNum+1))

		#Selected the current box based on sort preferences
		currentBox = self.sortingDict[self.pkmn_sort.get()][boxNum*pkmnPerBox:((boxNum+1)*pkmnPerBox)]

		#Only get a list of the next 16 and make them into images
		pkmnImgs = ["Pokemon_Smile_Pokemon/{}.png".format(pkmn.img) for pkmn in currentBox]
		self.boxImages = createImageLabels(pkmnImgs,smallSize)

		boxOutImgs = ["Pokemon_Smile_Envs/Pokemon_Box.png" for x in range(pkmnPerBox)]
		self.boxOutImages = createImageLabels(boxOutImgs,smallBoxSize)

		for i,im in enumerate(self.boxOutImages):
			col = (i%boxCols)
			row = int(i/boxRows)

			im.grid(row = row+1, column = col+1)
			#Lower to make under pokemon pngs
			im.lower()

		#Add pokemon images by rows and columns 
		for i,im in enumerate(self.boxImages):
			col = (i%boxCols)
			row = int(i/boxRows)

			im.grid(row = row+1, column = col+1)

			#Bind each image so that when clicked they go to their own page
			self.boxImages[i].bind("<Button>",partial(self.PokemonPage, currentBox[i], boxNum))

		#Adds the sort button
		self.sort_selector.grid(column = maxGridCols, row = 0)
		self.sort_selector.config(anchor="center")

		#Makes the button back say "Back" and adds it
		self.backButton.configure(text="Back")
		self.backButton.grid(column=0, row = 0)

		#Adds the box back and next buttons
		self.boxBackButton.grid(column=0, row = boxRows+2)
		self.boxNextButton.grid(column=boxCols+2, row = boxRows+2)

		#Changes the title so that it
		self.title.configure(text="Box {}".format(boxNum+1))
		self.title.grid(column=1, row = 0, columnspan = maxGridCols-1)

		#Remove all the many things that are not on this page
		self.time_selector.grid_forget()
		self.env_selector.grid_forget()
		self.startButton.grid_forget()
		self.boxButton.grid_forget()
		self.nameText.grid_forget()
		self.levelText.grid_forget()
		self.currentPkmn.grid_forget()
		self.currentBox.grid_forget()
		self.favText.grid_forget()
		self.dateText.grid_forget()
		self.evolveButton.grid_forget()
		self.candyCounter.grid_forget()
		self.levelUpButton.grid_forget()

		for im in self.imgLabels:
			im.grid_forget()
		
	def PokemonPage(self,pkmn,boxNum,*args):
		#Makes the back button go back to the box
		self.boxBackButton.configure(text='<', command= lambda: self.BoxesPage(boxNum))
		self.boxBackButton.grid(row = 0, column = 0)

		#Get the pokemon and a box around it
		self.currentPkmn = createImageLabels(["Pokemon_Smile_Pokemon/{}.png".format(pkmn.img)],size)[0]
		self.currentBox = createImageLabels(["Pokemon_Smile_Envs/Pokemon_Box.png"],boxSize)[0]

		#Place the box and lower it, then place the pokemon 
		self.currentBox.grid(row = 1, column = 1, rowspan=6, columnspan=4)
		self.currentBox.lower()
		self.currentBox.config(anchor="center")

		self.currentPkmn.grid(row = 1, column = 1, rowspan=6, columnspan=4)
		self.currentPkmn.config(anchor="center")

		#Get character if it is a favorite or not
		if pkmn.favorite:
			favChar = "✓"
		else:
			favChar = "X"

		#Add the name, level, favorite, and date caught
		self.nameText.config(text="Name: {}".format(pkmn.name))
		self.nameText.grid(row = 1, column = 5, columnspan=4, sticky="w")

		self.levelText.config(text="Level: {}".format(pkmn.level))
		self.levelText.grid(row = 2, column = 5,columnspan=4, sticky="w")

		self.favText.config(text="Favorite: {}".format(favChar))
		self.favText.grid(row = 3, column = 5, columnspan=4, sticky="w")
		self.favText.bind("<Button>",partial(self.makeFav, pkmn))

		self.dateText.config(text="Date Caught: {}".format(pkmn.caughtDate))
		self.dateText.grid(row = 4, column = 5, columnspan=4, sticky="w")

		#Add evolution button
		#Only show when level is high enough and can evolve
		# I want to use the flag but we'll see after I add leveling
		if pkmn.can_evolve:
			self.evolveButton.config(command=partial(self.EvolvePokemon, pkmn, boxNum))
			self.evolveButton.grid(row = 7, column = 4, columnspan=4)
			self.evolveButton.config(anchor="center")

		#Add ability to level up if less than 100:
		if pkmn.level < 100 and candy > 0:
			self.levelUpButton.config(command=partial(self.LevelUpPokemon, pkmn, boxNum))
			self.levelUpButton.grid(row = 7, column = 0, columnspan=4)
			self.levelUpButton.config(anchor="center")

		self.candyCounter.configure(text="You have {} candy".format(candy))
		self.candyCounter.grid(column=0, row = 8, columnspan = 8)

		#Remove all the many things that are not on this page
		self.boxNextButton.grid_forget()
		self.backButton.grid_forget()
		self.title.grid_forget()
		self.sort_selector.grid_forget()

		for im in self.boxImages:
			im.grid_forget()

		for im in self.boxOutImages:
			im.grid_forget()

	def EvolvePokemon(self,pkmn,boxNum,*args):
		#Evolve the pokemon
		evolvePkmn(pkmn)

		#Save the new pokemon
		savePkmn()

		#Resort the lists
		self.makeSortedPkmn()

		#Remove the current box
		self.currentPkmn.grid_forget()
		self.currentBox.grid_forget()
		self.favText.grid_forget()
		self.dateText.grid_forget()
		self.evolveButton.grid_forget()

		#Remake the box
		self.PokemonPage(pkmn,boxNum)

	def LevelUpPokemon(self,pkmn,boxNum,*args):
		global candy

		#Evolve the pokemon
		lvlUpPkmn(pkmn)

		candy -= 1

		#Save the new pokemon
		savePkmn()

		#Resort the lists
		self.makeSortedPkmn()

		#Remove the current box
		self.currentPkmn.grid_forget()
		self.currentBox.grid_forget()
		self.favText.grid_forget()
		self.dateText.grid_forget()
		self.evolveButton.grid_forget()

		#Remake the box
		self.PokemonPage(pkmn,boxNum)

	#Cancels the current timer
	def cancel(self):
		if self._job is not None:
			self.root.after_cancel(self._job)
			self._job = None

	def update_clock(self,timer_seconds):
		m = str(int(timer_seconds/60)).zfill(2)
		s = str(timer_seconds%60).zfill(2)

		time_left = timer.format(m=m,s=s)

		self.timerText.configure(text=time_left)

		if timer_seconds > 0:
			#If paused do not reduce clock time
			if self.paused:
				self._job = self.root.after(1000, self.update_clock, timer_seconds)
			else:
			 	self._job = self.root.after(1000, self.update_clock, timer_seconds-1)
		else:
			playsound('chime.mp3')

			#Only Long Timers get to catch, not in testing tho

			#REMOVE IN FULL
			if int(self.timer_mins.get()[0:2]) >= 0.5:
				self.CandyOrCatchPage()
			else:
				self.MainPage()

	#Cancels any timer, goes to timer page, and starts timer
	def getStartTime(self):  
		self.cancel()  
		self.TimerPage() 

		#Now is seconds not minutes
		#REMOVE IN FULL
		self.update_clock(int(self.timer_mins.get()[0:2]))

	def PauseTimer(self):
		self.paused = not self.paused

	#Cancels the time, goes to main page
	def endTimer(self):
		self.cancel()
		self.MainPage() 
		self.timerText.configure(text="Timer Ended")

	def makeFav(self,pkmn,*args):
		pkmn.favorite = not pkmn.favorite

		if pkmn.favorite:
			favChar = "✓"
		else:
			favChar = "X"

		self.favText.config(text="Favorite: {}".format(favChar))

		self.favePokemon = makeFavs()
		savePkmn()

	def makeSortedPkmn(self):
		pkmnOldToNew = caughtPokemon
		pkmnNewToOld = list(reversed(caughtPokemon))

		pkmnLowToHigh = sorted(caughtPokemon, key=lambda x: x.level)
		pkmnHighToLow = list(reversed(pkmnLowToHigh))

		pkmnAToZ = sorted(caughtPokemon, key=lambda x: x.name)
		pkmnZToA = list(reversed(pkmnAToZ))

		self.sortingDict = {"Old to New":pkmnOldToNew,"New to Old":pkmnNewToOld,
							"High to Low":pkmnHighToLow,"Low to High":pkmnLowToHigh,
							"A to Z":pkmnAToZ,"Z to A":pkmnZToA}

	def catchPkmn(self):
		#If you get a value under their catch rate

		#REMOVE IN FULL
		if True: #randint(0,100) - int(self.timer_mins.get()[0:2]) < self.pkmn_found_class.catch_rate:
			#Say that they caught it, add it to caught list, and then save it
			self.catchText.configure(text="You caught the {}!".format(self.pkmn_found_class.species))
			addToCaught(self.pkmn_found_class)
			savePkmn()
			self.makeSortedPkmn()
		else:
			#Say that it got away
			self.catchText.configure(text="The {} got away...".format(self.pkmn_found_class.species))

		#Remove the catch button
		self.catchButton.grid_forget()

		#Change button to go back
		self.backButton.grid_forget()
		self.backButton.configure(text="Go Back")
		self.backButton.grid(column=0, row = 3, columnspan = maxGridCols)

#Run the app
app=App()
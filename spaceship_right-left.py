from tkinter import *
import time

class App():
	def __init__(self):
		self.tk = Tk()
		self.tk.title("Move spaceship right and left")
		self.app_running = True
		self.canvas = Canvas(self.tk, width=200, height=200)
		self.canvas.pack()
		self.canvas.bind("<ButtonPress-1>", self.click)
		self.canvas.bind("<ButtonRelease-1>", self.rel)
		self.release = False
		self.clickside = None
	def click(self, event):
		self.release = False
		if event.x <= 100:
			self.clickside = "Left"
		elif event.x > 100:
			self.clickside = "Right"
	def rel(self, event):
		self.release = True
	def mainloop(self, *sprites):
		while True:
			if self.app_running:
				for spr in sprites:
					spr.draw()
				time.sleep(0.01)
				self.tk.update()

class Spaceship():
	def __init__(self, window, x, y, width=35, color="red"):
		self.app = window
		self.id = self.app.canvas.create_rectangle(x, y, x+width, y+width, fill=color)
		self.x = 0
	def draw(self):
		self.app.canvas.move(self.id, self.x, 0)
		if self.app.clickside == "Right":
			self.x = 1
		elif self.app.clickside == "Left":
			self.x = -1
		if self.app.release:
			self.x = 0
try:
        app = App()
        sp = Spaceship(app, 150, 150)
        app.mainloop(sp)
except:
        pass

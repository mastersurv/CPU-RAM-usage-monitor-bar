import tkinter as tk
from tkinter import ttk  # tk for window (more pretty)
import sys


class Application(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		self.attributes('-alpha', 1)  # set transparency (clarity)
		self.attributes('-topmost', True)  # on top of other windows
		self.overrideredirect(True)  # delete borders
		self.resizable(False, False)  # forbid to change size of window
		self.title('CPU-RAM usage monitor bar')  # set title

		self.set_ui()

	def set_ui(self):
		"""Function of graphic interface (buttons, labels)"""
		exit_but = ttk.Button(self, text='Exit', command=self.app_exit)
		exit_but.pack(fill=tk.X)

		self.bar2 = ttk.LabelFrame(self, text='Manual')  # Our frame on which we'll set UI
		self.bar2.pack(fill=tk.X)

		self.combo_win = ttk.Combobox(self.bar2,
		                              values=["hide", "don't hide", "min"],
		                              width=9, state='readonly')

		self.combo_win.current(1)
		self.combo_win.pack(side=tk.LEFT)

		ttk.Button(self.bar2, text='move').pack(side=tk.LEFT)  # will be on the left on the frame
		ttk.Button(self.bar2, text='>>>').pack(side=tk.LEFT)

		# Our frame on which we'll set progress bars with information about CPU and RAM
		self.bar2 = ttk.LabelFrame(self, text='Power')
		self.bar2.pack(fill=tk.BOTH)  # BOTH - to pull to the maximum width

		self.bind_class('Tk', '<Enter>', self.enter_mouse)  # mouse hover
		self.bind_class('Tk', '<Leave>', self.leave_mouse)  # mouse leaves the window of app

	def enter_mouse(self, event):  # event - information about activity (coordinates), mandatory argument
		"""function when mouse will hover the window of our app"""
		if self.combo_win.current() == 0 or 1:  # if value is hide or don't hide
			self.geometry('')  # default value, which we set

	def leave_mouse(self, event):
		"""function when mouse will leave the window of app"""
		if self.combo_win.current() == 0:  # if value is hide
			self.geometry(f'{self.winfo_width()}x1')  # get current width and change height to 1px

	def app_exit(self):
		"""function which closes app"""
		self.destroy()
		sys.exit()


root = Application()
root.mainloop()

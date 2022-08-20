import tkinter as tk
from tkinter import ttk
import sys
from process import CpuBar
from widget_update import Configure_widgets


class Application(tk.Tk, Configure_widgets):

	def __init__(self):
		tk.Tk.__init__(self)
		self.attributes('-alpha', 1)  # set transparency (clarity)
		self.attributes('-topmost', True)  # on top of other windows
		self.overrideredirect(True)  # delete borders
		self.resizable(False, False)  # forbid to change size of window
		self.title('CPU-RAM usage monitor bar')  # set title

		self.cpu = CpuBar()
		self.set_ui()
		self.make_bar_cpu_usage()
		self.configure_cpu_bar()

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

		ttk.Button(self.bar2, text='move', command=self.configure_win).pack(side=tk.LEFT)  # will be on the left on the frame
		ttk.Button(self.bar2, text='>>>').pack(side=tk.LEFT)

		# Our frame on which we'll set progress bars with information about CPU and RAM
		self.bar = ttk.LabelFrame(self, text='Power')
		self.bar.pack(fill=tk.BOTH)  # BOTH - to pull to the maximum width

		self.bind_class('Tk', '<Enter>', self.enter_mouse)  # mouse hover
		self.bind_class('Tk', '<Leave>', self.leave_mouse)  # mouse leaves the window of app
		self.combo_win.bind('<<ComboboxSelected>>', self.choise_combo)

	def make_bar_cpu_usage(self):
		ttk.Label(self.bar, text=f'physical cores: {self.cpu.cpu_count}, logical cores: {self.cpu.cpu_count_logical}',
		          anchor=tk.CENTER).pack(fill=tk.X)  # argument anchor need to set position of label

		self.list_label = []
		self.list_pbar = []

		for i in range(self.cpu.cpu_count_logical):
			# append widgets in lists
			self.list_label.append(ttk.Label(self.bar, anchor=tk.CENTER))
			self.list_pbar.append(ttk.Progressbar(self.bar, length=100))  # it will be divided into 100 divisions

		for i in range(self.cpu.cpu_count_logical):
			self.list_label[i].pack(fill=tk.X)
			self.list_pbar[i].pack(fill=tk.X)

		self.ram_lab = ttk.Label(self.bar, text='', anchor=tk.CENTER)
		self.ram_lab.pack(fill=tk.X)
		self.ram_bar = ttk.Progressbar(self.bar, length=100)
		self.ram_bar.pack(fill=tk.X)


	def enter_mouse(self, event):  # event - information about activity (coordinates), mandatory argument
		"""function when mouse will hover the window of our app"""
		if self.combo_win.current() == 0 or 1:  # if value is hide or don't hide
			self.geometry('')  # default value, which we set

	def leave_mouse(self, event):
		"""function when mouse will leave the window of app"""
		if self.combo_win.current() == 0:  # if value is hide
			self.geometry(f'{self.winfo_width()}x1')  # get current width and change height to 1px

	def choise_combo(self, event):
		"""function which will untie widgets"""
		if self.combo_win.current() == 2:  # if value is min
			self.enter_mouse('')
			self.unbind_class('Tk', '<Enter>')
			self.unbind_class('Tk', '<Leave>')
			self.combo_win.unbind('<<ComboboxSelected>>')
			self.after_cancel(self.wheel)



	def app_exit(self):
		"""function which closes app"""
		self.destroy()
		sys.exit()


if __name__ == '__main__':
	root = Application()
	root.mainloop()

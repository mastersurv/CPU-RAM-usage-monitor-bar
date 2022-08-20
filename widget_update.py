# class which will update configuration of our widgets
class Configure_widgets:

	def configure_cpu_bar(self):

		r = self.cpu.cpu_percent_return()  # example: [42.0, 29.7, 40.6, 28.1] - list with info about workload
		for i in range(self.cpu.cpu_count_logical):  # count of streams
			self.list_label[i].configure(text=f'core {i+1} usage: {r[i]}%')  # configure changes some info
			self.list_pbar[i].configure(value=r[i])

		r2 = self.cpu.ram_usage()
		self.ram_lab.configure(text=f'RAM usage: {r2[2]}%, used {round(r2[3]/104857)} Mb, '
		                            f'available: {round(r2[1]/1048576)} Mb')
		self.ram_bar.configure(value=r2[2])

		# method after allows to restart in cycle another method, 1000 - count of ms
		self.wheel = self.after(1000, self.configure_cpu_bar)

	def configure_win(self):
		if self.wm_overrideredirect():  # if window is with border
			self.overrideredirect(False)  # delete border
		else:
			self.overrideredirect(True)  # set border
		self.update()  # update the widnow
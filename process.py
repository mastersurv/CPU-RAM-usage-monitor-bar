import psutil as pt  # module which works with hardware
from time import sleep

class CpuBar:

	def __init__(self):
		self.cpu_count = pt.cpu_count(logical=False)  # shows count of processor cores
		self.cpu_count_logical = pt.cpu_count()  # without argument logical it shows count of streams

	def cpu_percent_return(self):
		return pt.cpu_percent(percpu=True)  # it shows average workload of each stream

	def ram_usage(self):
		return pt.virtual_memory()

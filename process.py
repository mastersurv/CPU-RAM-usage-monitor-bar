import psutil as pt  # module which works with hardware


class CpuBar:

	def __init__(self):
		self.cpu_count = pt.cpu_count(logical=False)  # shows count of processor cores
		self.cpu_count_logical = pt.cpu_count()  # without argument logical it shows count of streams





CpuBar()
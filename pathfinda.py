#import imp
#tick = imp.load_source('tick', '../Sis3302DataHandling/pathfinder.py')
#track= imp.load_source('track', '../DecayAnalysis/pathfinder.py')

class scoutmaster():
	def __init__(self):
		self.libPyOrcaROOT="~/software/OrcaROOT/Bindings/libPyOrcaROOT"
		self.libWaveWaveBase="~/software/TWaveform/lib/libWaveWaveBase"
		self.OrcaFileFolder="/Volumes/HgLaser/Data/Orca"
		self.ROOTFileFolder="/Volumes/HgLaser/Data/Rootified/"
		self.TxtFileFolder="/Volumes/HgLaser/Data/Txtified/"
	def updateOrcaFolder(self, orcafolder):
		self.OrcaFileFolder=orcafolder
#		tick.updateOrcaFolder(orcafolder)
#		track.updateOrcaFolder(orcafolder)
	def updateROOTFolder(self, ROOTfolder):
		self.ROOTFileFolder=ROOTfolder
#		track.updateROOTFolder(ROOTfolder)
#		tick.updateROOTFolder(ROOTfolder)
	def updateTxtFolder(self, Txtfolder):
		self.TxtFileFolder=Txtfolder
#		tick.updateTxtFolder(Txtfolder)
#		track.updateTxtFolder(Txtfolder)


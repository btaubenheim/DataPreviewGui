print "before import"
import sys
import pathfinda
from os.path import abspath
sys.path.append(abspath("../Sis3302Datahandling"))
sys.path.append(abspath("../DecayAnalysis"))
import sis3302Datahandling
import decayFit
print "after import"

class TopModel():
	def __init__(self):
		self.scoutmaster=pathfinda.scoutmaster()
		self.sisdatatrans=sis3302Datahandling.orcadatamanipulation()
		self.fidfit=decayFit.fidfit()
		self.sisdatatrans.orcafilefolder=self.scoutmaster.OrcaFileFolder	
		self.sisdatatrans.rootfilefolder=self.scoutmaster.ROOTFileFolder
		self.sisdatatrans.txtfilefolder=self.scoutmaster.TxtFileFolder
		self.sisdatatrans.orcafile=''
		self.sisdatatrans.rootfile=''
		self.sisdatatrans.channelnum=1#make this flexible
		self.sisdatatrans.numtriggers=1#flexi

	def txtify(self):
		self.sisdatatrans.txtify(10,1)

	def rootify(self):
		self.sisdatatrans.rooter()
	def fit(self):
		self.fidfit.loadfile()
		self.fidfit.fit()
	def draw(self):
		pass



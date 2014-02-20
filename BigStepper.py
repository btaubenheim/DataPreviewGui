import FamilyGui
import sys
import time
import threading
from PySide import QtGui
import TopModel
import pathfinda


#todo: run und count checken. load all???
#get rid of "jump ma die leider weider"
#clean up the pathfinder mess?
#when a file gets rootified: show on the gui that it is automatically loaded

class BigStepper():
	def __init__(self):
		self.model=TopModel.TopModel()
		self.ui=FamilyGui.SimplePrev()
		self.ui.orcafilepathdisp.setText(self.model.sisdatatrans.orcafilefolder)
		self.ui.rootfilepathdisp.setText(self.model.sisdatatrans.rootfilefolder)
		self.ui.channeldisp.setText('channel: '+str(self.model.sisdatatrans.channelnum))
		self.ui.countdisp.setText('count: '+str(self.model.sisdatatrans.numtriggers))
		self.ui.txtifyButton.clicked.connect(self.ontxtifyButton)
		self.ui.OrcaFileBrowseButton.clicked.connect(self.onOrcaFileBrowseButton)
		self.ui.RootFileBrowseButton.clicked.connect(self.onRootFileBrowseButton)
		self.ui.txtifyButton.clicked.connect(self.ontxtifyButton)
		self.ui.rootifyButton.clicked.connect(self.onrootifyButton)
		self.ui.previewButton.clicked.connect(self.onpreviewButton)
		self.ui.fitButton.clicked.connect(self.onfitButton)
		self.ui.setchan.clicked.connect(self.updatechan)
		self.ui.setcount.clicked.connect(self.updatecount)
		self.scoutmaster=pathfinda.scoutmaster()
	def onfitButton(self):
		self.model.fit()
	def onrootifyButton(self):
		self.model.rootify()	
		self.ui.rootfilepathdisp.setText(self.model.sisdatatrans.rootfile)
	def ontxtifyButton(self):
		self.model.txtify()

	def onOrcaFileBrowseButton(self):
		self.model.sisdatatrans.orcafile=self.ui.FileyCyrus(self.scoutmaster.OrcaFileFolder)
		
		self.ui.orcafilepathdisp.setText(self.model.sisdatatrans.orcafile)
		print self.model.sisdatatrans.orcafile

	def onRootFileBrowseButton(self):
		self.model.sisdatatrans.rootfile=self.ui.FileyCyrus(self.scoutmaster.ROOTFileFolder)
#		self.updatechan()
#		self.updatecount()
		self.model.fidfit.rootfile=self.model.sisdatatrans.rootfile
		self.ui.rootfilepathdisp.setText(self.model.sisdatatrans.rootfile)
		print self.model.sisdatatrans.rootfile

	def onpreviewButton(self):
		self.model.sisdatatrans.draw_all_counts()

	def updatechan(self):
		channel=self.ui.chan()
		self.model.sisdatatrans.channelnum=channel
		self.ui.channeldisp.setText("channel: "+str(self.model.sisdatatrans.channelnum))
	def updatecount(self):
		count=self.ui.count()
		if count == "All" or "all":
			self.model.sisdatatrans.numtriggers=None
		else:
			self.model.sisdatatrans.numtriggers=count
		self.ui.countdisp.setText("count: "+str(self.model.sisdatatrans.numtriggers))
def main():
	app=QtGui.QApplication(sys.argv)
	big=BigStepper()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()

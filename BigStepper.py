import FamilyGui
import sys
import time
import threading
from PySide import QtGui


class BigStepper():
	def __init__(self):
		#self.gatzensmodel = model.model()
		self.ui=FamilyGui.SimplePrev()
		self.ui.txtifyButton.clicked.connect(self.ontxtifyButton)
		self.ui.OrcaFileBrowseButton.clicked.connect(self.onOrcaFileBrowseButton)
		self.ui.RootFileBrowseButton.clicked.connect(self.onRootFileBrowseButton)
	
	def onOrcaFileBrowseButton(self):
		orcafilename=self.ui.FileyCyrus(OrcaFilePath)
		print orcafilename

	def onRootFileBrowseButton=(self):
		rootfilename=self.ui.FileyCyrus(ROOTFilePath)
		print rootfilename

	def ontxtifyButton(self):
		print "mumu"

def main():
	app=QtGui.QApplication(sys.argv)
	big=BigStepper()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()

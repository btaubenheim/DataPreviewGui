import sys
from PySide import QtGui

class SimplePrev(QtGui.QWidget):
	def __init__(self):
		super(SimplePrev, self).__init__()

		self.initUI()

	def initUI(self):
		self.orcafilepathdisp=QtGui.QLabel(self)
		self.rootfilepathdisp=QtGui.QLabel(self)
		self.channeldisp=QtGui.QLabel(self)
		self.countdisp=QtGui.QLabel(self)
		self.setchan=QtGui.QPushButton('choose channel')
		self.setcount=QtGui.QPushButton('choose count')
		self.rootifyButton=QtGui.QPushButton("rootify")
		self.txtifyButton=QtGui.QPushButton("asciify") #include option to set averaging
		self.numpyfButton=QtGui.QPushButton("numpyfyNOT")
		self.previewButton=QtGui.QPushButton("preview")
		self.fitButton=QtGui.QPushButton("fitDecay")
		self.OrcaFileBrowseButton=QtGui.QPushButton("Browse")
		self.RootFileBrowseButton=QtGui.QPushButton("Browse")

		grid=QtGui.QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(self.orcafilepathdisp, 1, 0, 1, 1)
		grid.addWidget(self.rootfilepathdisp, 2, 0, 2, 1)
		grid.addWidget(self.OrcaFileBrowseButton, 1, 2)
		grid.addWidget(self.RootFileBrowseButton, 2, 2)
		grid.addWidget(self.channeldisp, 4, 0)
		grid.addWidget(self.countdisp, 5, 0)
		grid.addWidget(self.setchan, 4, 2)
		grid.addWidget(self.setcount, 5, 2)
		grid.addWidget(self.rootifyButton, 1, 3)
		grid.addWidget(self.txtifyButton, 1, 4)
		grid.addWidget(self.previewButton, 2, 3)
		grid.addWidget(self.fitButton, 2, 4)
		self.setLayout(grid)
		self.show()

	def chan(self):
		self.chaner, ok=QtGui.QInputDialog.getText(self, '', 'choose channel')
		if ok:
			return int(self.chaner)
	def count(self):
		self.counter, ok=QtGui.QInputDialog.getText(self, '', 'choose count. Type All to choose all counts')
		if ok:
			if self.counter=='All' or 'all':
				return self.counter
			else:
				return int(self.counter)
	def FileyCyrus(self, startpath):
		self.filey,_=QtGui.QFileDialog.getOpenFileName(self, 'Select file', startpath)
		return self.filey

def main():
	app=QtGui.QApplication(sys.argv)
	ui=SimplePrev()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()

			

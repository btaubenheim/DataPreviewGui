import sys
from PySide import QtGui

class SimplePrev(QtGui.QWidget):
	def __init__(self):
		super(SimplePrev, self).__init__()

		self.initUI()

	def initUI(self):
		self.orcafilepathdisp=QtGui.QLineEdit()
		self.rootfilepathdisp=QtGui.QLineEdit()
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
		grid.addWidget(self.rootifyButton, 1, 3)
		grid.addWidget(self.txtifyButton, 1, 4)
		grid.addWidget(self.previewButton, 2, 3)
		grid.addWidget(self.fitButton, 2, 4)
		self.setLayout(grid)
		self.show()
	
	def FileyCyrus(self):
		self.filey,_=QtGui.QFileDialog.getOpenFileName(self, 'Select file', '/home/bernd/Dropbox/work')
		return self.filey

def main():
	app=QtGui.QApplication(sys.argv)
	ui=SimplePrev()
	sys.exit(app.exec_())

if __name__=='__main__':
	main()

	

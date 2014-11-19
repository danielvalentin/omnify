from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QUrl

class win(QtGui.QDialog):

	def __init__(self, url):
		super(win, self).__init__()
		self.url = url
		self.setup_window()

	def setup_window(self):
		#self.resize(400, 200)
		#self.center()
		self.setWindowTitle("Add Twitter account")

		self.buttonBox = QtGui.QDialogButtonBox(self)
		self.buttonBox.centerButtons()
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
		self.buttonBox.rejected.connect(self.close)
		self.buttonBox.accepted.connect(self.save_pin)

		self.pinText = QtGui.QLabel('<a href="'+self.url+'">Click here</a> to get a pincode')
		self.pinText.linkActivated.connect(self.openBrowser)

		self.pinInput = QtGui.QLineEdit()

		self.verticalLayout = QtGui.QVBoxLayout(self)
		self.verticalLayout.addWidget(self.pinText)
		self.verticalLayout.addWidget(self.pinInput)
		self.verticalLayout.addWidget(self.buttonBox)


	def openBrowser(self):
		QtGui.QDesktopServices.openUrl(QUrl(self.url))


	def save_pin(self):
		pin = self.pinInput.text()
		if len(pin) > 0:
			self.pin = pin
			self.accept()

	def get_pin(self):
		return self.pin


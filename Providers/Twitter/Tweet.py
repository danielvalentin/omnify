from PyQt4 import QtGui,QtCore,QtWebKit,Qt
import urllib

class widget(QtGui.QWidget):



	def __init__(self, tweet):
		super(widget, self).__init__()

		self.layout = QtGui.QHBoxLayout()
		self.layout.setAlignment(QtCore.Qt.AlignTop)

		self.setLayout(self.layout)

		imglabel = QtGui.QLabel()
		data = urllib.urlopen(tweet['user']['profile_image_url_https']).read()
		pix = QtGui.QPixmap()
		pix.loadFromData(data)
		imglabel.setPixmap(pix)
		self.layout.addWidget(imglabel)

		self.html = ''
		self.html = self.html + tweet["text"]

		self.tweetText = QtGui.QTextBrowser()
		self.tweetText.setHtml(QtCore.QString(self.html))
		self.tweetText.setOpenExternalLinks(True)
		self.tweetText.setReadOnly(True)
		self.tweetText.setFrameStyle(self.tweetText.NoFrame)

		self.layout.addWidget(self.tweetText)
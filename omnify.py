#!/usr/bin/env python

import sys
import threading
import time
from PyQt4 import QtGui, QtCore

from Omnify import Window
from Providers.Twitter import Twitter

class Omnify:

	def __init__(self):
		self.win = Window.Window()
		self.twitter = Twitter.Accounts()

		self.getUpdates()

	def getUpdates(self):
		timeline = self.twitter.get_timeline()

		i = 1
		for tweet in timeline:
			if len(timeline) > 1:
				if i == len(timeline):
					self.win.add_twitter_widget(tweet, True)
				else:
					self.win.add_twitter_widget(tweet, False)
			else:
				self.win.add_twitter_widget(tweet, True)
			i += 1


		self.t = QtCore.QTimer()
		self.t.setSingleShot(False)
		self.t.timeout.connect(self.getUpdates)
		self.t.start(60000)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	omnify = Omnify()
	sys.exit(app.exec_())


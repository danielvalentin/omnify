#!/usr/bin/env python

import sys
from PyQt4 import QtGui

from Omnify import Window
from Providers.Twitter import Twitter

class Omnify:
	
	def __init__(self):
		self.win = Window.Window()
		self.twitter = Twitter.Accounts()

		timeline = self.twitter.get_timeline()

		for tweet in timeline:
			self.win.add_twitter_widget(timeline[tweet])


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	omnify = Omnify()
	sys.exit(app.exec_())


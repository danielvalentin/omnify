from PyQt4 import QtGui,QtCore

from Providers.Twitter import Twitter
from Providers.Twitter import Tweet

class Window(QtGui.QMainWindow):

	def __init__(self):
		super(Window, self).__init__()
		#QtGui.QMainWindow.__init__(self, parent)
		#self.setup_window()
		#self.setup_trayicon()
		#self.setup_menubar()
		#self.show()
		self.setup_window()
		self.setup_menubar()
		self.setup_trayicon()

	def setup_window(self):
		self.resize(400, 700)
		self.center()
		self.setWindowTitle("Omnify")
		self.statusBar()
		self.setWindowIcon(QtGui.QIcon('resources/img/important.png'))

		self.scroll = QtGui.QScrollArea(self)
		self.scroll.setWidgetResizable(True)
		self.scroll.setMaximumSize(400, 700)
		self.scrollArea = QtGui.QWidget()
		self.scrollArea.setGeometry(QtCore.QRect(0, 0, 400, 700))
		self.scroll.setWidget(self.scrollArea)

		self.grid = QtGui.QGridLayout()

		self.mainLayout = QtGui.QHBoxLayout(self.scrollArea)
		self.mainLayout.addLayout(self.grid)
		#self.mainLayout.addWidget(self.scroll)

		self.setCentralWidget(self.scroll)

		self.show()

	def add_twitter_widget(self, tweet):
		tst = Tweet.widget(tweet)
		self.grid.addWidget(tst)


	def center(self):
		frameGm = self.frameGeometry()
		centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
		frameGm.moveCenter(centerPoint)
		self.move(frameGm.topLeft())

	def setup_menubar(self):
		exitAction = QtGui.QAction(QtGui.QIcon('resources/img/quit.png'), '&Quit', self)
		exitAction.setStatusTip('Quit application')
		exitAction.triggered.connect(QtGui.qApp.quit)

		twitterAction = QtGui.QAction(QtGui.QIcon('resources/img/twitter.png'), 'Add new', self)
		twitterAction.setStatusTip('Add a new twitter account')
		twitterAction.triggered.connect(self.addTwitterAccount)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&Omnify')
		#fileMenu.addAction(twitterAction)
		fileMenu.addAction(exitAction)

		accountsMenu = menubar.addMenu('&Accounts')
		self.twitterAccountsMenu = accountsMenu.addMenu('&Twitter')
		self.twitterAccountsMenu.addAction(twitterAction)

		twitter = Twitter.Accounts()
		accounts = twitter.get_accounts()
		for account in accounts:
			account = accounts[account]
			accountAction = QtGui.QAction(account['screen_name'], self)
			self.twitterAccountsMenu.addAction(accountAction)

		#self.toolbar = self.addToolBar('Tools')
		#self.toolbar.addAction(twitterAction)

	def addTwitterAccount(self):
		twit = Twitter.Accounts()
		twit.add_new_account(self)

	def update_twitter_menu(self, account):
		action = QtGui.QAction(account['screen_name'], self)
		self.twitterAccountsMenu.addAction(action)

	def setup_trayicon(self):
		self.trayIcon = QtGui.QSystemTrayIcon(self)
		self.trayIcon.setIcon(QtGui.QIcon('resources/img/important.png'))

		menu = QtGui.QMenu()
		exitAction = menu.addAction('Quit')
		exitAction.triggered.connect(QtGui.qApp.quit)

		self.trayIcon.setContextMenu(menu)
		self.trayIcon.show()




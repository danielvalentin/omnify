# https://github.com/ryanmcgrath/twython
# https://twython.readthedocs.org/en/latest/usage/streaming_api.html
from twython import Twython
from twython import TwythonError
from PyQt4.QtGui import *

import config
from Omnify import data
from Providers.Twitter import PinWindow

import json

class Accounts:

	since = False

	def __init__(self):
		self.store = data.Store()
		self.data = self.get_data()
		self.api = self.get_api()

	def get_data(self):
		data = self.store.get('twitter', {})
		if not 'accounts' in data:
			data['accounts'] = {}
			self.store.save('twitter', data)
		return data

	def get_api(self):
		if self.is_authed():
			return Twython(config.APP_KEY, config.APP_SECRET, self.data['oauth_token'], self.data['oauth_token_secret'])
		else:
			return Twython(config.APP_KEY, config.APP_SECRET)

	def is_authed(self):
		if not 'oauth_token' in self.data or not 'oauth_token_secret' in self.data:
			return False
		return True

	def get_accounts(self):
		return self.data['accounts']

	def get_timeline(self, testdata = False):
		if testdata:
			with open('timeline.tweets', 'r') as f:
				try:
					timeline = json.load(f)
				except:
					timeline = {}
					print("empty data file exception")
			f.close()
			return timeline

		accounts = self.get_accounts()
		tweets = {}
		i = 0
		for account in accounts:
			if 'oauth_token' in accounts[account] and 'oauth_token_secret' in accounts[account]:
				api = Twython(config.APP_KEY, config.APP_SECRET, accounts[account]['oauth_token'], accounts[account]['oauth_token_secret'])
				tweetcount = 10;
				if self.since:
					timeline = api.get_home_timeline(count=tweetcount, since_id=self.since)
				else:
					timeline = api.get_home_timeline(count=tweetcount)
				for tweet in timeline:
					tweets.update({i:tweet})
					i += 1
					self.since = tweet['id']
		return timeline

	def add_account(self, account, window):
		self.data['accounts'].update({account['screen_name']:account})
		self.store.save("twitter",self.data)
		window.update_twitter_menu(account)

	def add_new_account(self, window):
		api = Twython(config.APP_KEY, config.APP_SECRET)
		tokens = api.get_authentication_tokens()
		pinwin = PinWindow.win(tokens['auth_url'])
		if pinwin.exec_():
			pin = pinwin.get_pin()
			pin = str(pin)
		else:
			return
		self.api = Twython(config.APP_KEY, config.APP_SECRET, tokens['oauth_token'], tokens['oauth_token_secret'])
		try:
			account = self.api.get_authorized_tokens(pin)
			self.add_account(account, window)
		except TwythonError:
			QMessageBox.about(None, "Error", "Twitter responded with an error message. Are you sure you entered the right pin?")


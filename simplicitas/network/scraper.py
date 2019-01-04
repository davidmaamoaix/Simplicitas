'''A webpage scraper with some templates.'''

import bs4
import requests

def Page(bs4.BeautifulSoup):
	'''A wrapper for BeautifulSoup. Scrap a single web page.'''

	def __init__(self, url, parser='lxml'):
		'''Instantiate a page object.

		Args:
			url: str, the url for the web page.
			parser: str, the parser to use for the web page.
		'''
		html = requests.get(url)
		super().__init__(self, html, parser)
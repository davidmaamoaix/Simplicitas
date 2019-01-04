'''A webpage scraper with some templates.'''

__all__ = [
	'Page',
	'Wikipedia',
]

import bs4
import requests

class Page(bs4.BeautifulSoup):
	'''A wrapper for BeautifulSoup. Scrap a single web page.'''

	def __init__(self, url, parser='lxml', redirect=True, timeout=5):
		'''Instantiate a page object.

		Args:
			url: str, the url for the web page.
			parser: str, the parser to use for the web page.
			redirect: bool, whether to allow auto redirect.
			timeout, float, timeout.
		'''
		self._response = requests.get(
			url,
			allow_redirects=redirect,
			timeout=timeout
		)
		super().__init__(self._response.text, parser)

	@property
	def url(self):
		return self._response.url

	def __str__(self):
		return f'<Page of {self.url}>'

	def __repr__(self):
		return str(self)

class Wikipedia(Page):

	def __init__(self, topic, lang='en'):
		'''Instantiate a Wikipedia search for keyword.

		Args:
			topic: str, the topic to search for.
			lang: str, the language of wikipedia.
		'''
		topic = topic.replace(' ', '_')
		base_url = f'https://{lang}.wikipedia.org/w/index.php?search={topic}'
		search_page = Page(base_url)
		print(search_page.url)
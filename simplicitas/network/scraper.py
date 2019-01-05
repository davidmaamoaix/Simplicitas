'''A webpage scraper with some templates.'''

__all__ = [
	'Page',
	'Wikipedia',
]

import re
import bs4
import requests

class Page(bs4.BeautifulSoup):
	'''A wrapper for BeautifulSoup. Scrap a single web page.'''

	def __init__(self, url='', redirect=True, timeout=5, **kwargs):
		'''Instantiate a page object.

		Args:
			url: str, the url for the web page.
			redirect: bool, whether to allow auto redirect.
			timeout, float, timeout.
		'''
		prev_response = kwargs.get('response', False)
		self._response = requests.get(
			url,
			allow_redirects=redirect,
			timeout=timeout
		) if prev_response == False else prev_response

		super().__init__(self._response.text, 'lxml')

	@property
	def url(self):
		return self._response.url

	@property
	def response(self):
		return self._response


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
		page = Page(base_url)

		'''If on search page.'''
		reg = 'https?:\/\/(www\.)?.*\.wikipedia\.org\/w\/index\.php\?search=.*'
		if re.match(reg, page.url):
			'''Search for first result.'''
			is_result = lambda x: x.get('data-serp-pos', '').isdigit()
			result = page.find('a', {'data-serp-pos': 0})
			branch = result['href']

			super().__init__(f'https://{lang}.wikipedia.org{branch}')
		else:
			'''Already on target page.'''
			super().__init__(response=page.response)

		'''Compile page content.'''



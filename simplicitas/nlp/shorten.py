'''A text summarizer based on word frequency.'''

import nltk
from nltk.corpus import stopwords

def summarize(text: str, max_length: int = 5):
	'''Summarize a given text.

	Args:
		text: str, the text to be summarized.
		sents: int, the length (sentences) of the summarized conclusion.

	Returns:
		str, the summarized text.

	Raises:
		Nothing, what could go wrong?
	'''
	sents = nltk.sent_tokenize(text)
	words = [nltk.word_tokenize(sent) for sent in sents]

	'''Remove stopwords.'''
	del_words = stopwords.words('english')
	not_sign = lambda x: len(x) > 1 or x.isdigit() or x.isalpha()
	removal_func = lambda x: x.lower() not in del_words and not_sign(x)
	words = [list(filter(removal_func, sent)) for sent in words]

	'''Word frequency.'''
	freq = {}
	most_freq = 1
	for sent in words:
		for word in sent:
			if word not in freq:
				freq[word] = 0
			freq[word] += 1
			most_freq = max(most_freq, freq[word])

	'''Weighted frequency.'''
	for word in freq:
		freq[word] /= most_freq

	'''Sentence weight.'''
	sent_weights = [sum(map(lambda x: freq[x], sent)) for sent in words]

	'''Sort sentences by weights.'''
	sents = [sent for _, sent in sorted(zip(sent_weights, sents))]

	return sents[:max_length]
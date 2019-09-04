import bs4
from bs4 import BeautifulSoup  
import urllib.request  
import re
import heapq  

import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

# Dataset
uri='https://fr.wikipedia.org/wiki/Napol%C3%A9on_Ier'

# Retrieving text from Html paragraphs
scraped_data = urllib.request.urlopen(uri)  
article = scraped_data.read()
parsed_article = BeautifulSoup(article,'lxml')
paragraphs = parsed_article.find_all('p')

def summarize(article_text, val):
  summary_sentences = []
    
  # Removing Square Brackets and Extra Spaces
  article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)  
  article_text = re.sub(r'\s+', ' ', article_text)  

  # Removing special characters and digits
  formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )  
  formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)  

  if not len(formatted_article_text) <= 1: 

    # Tokenizing content
    sentence_list = nltk.sent_tokenize(article_text)  
    stopwords = nltk.corpus.stopwords.words('french')

    word_frequencies = {}  
    for word in nltk.word_tokenize(formatted_article_text):  
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

    sentence_scores = {}  
    for sent in sentence_list:  
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    summary_sentences = heapq.nlargest(val, sentence_scores, key=sentence_scores.get)
  return summary_sentences

# 1st Loop to summarize paragraphs
tmp = []
for p in paragraphs:  
  s = summarize(p.text, 1)
  tmp = tmp + s

# 2nd Loop to select sentences
summary = ""
print('\n'.join(summarize('\n'.join(tmp), 15)))

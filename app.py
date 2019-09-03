!pip install pyteaser 
from pyteaser import SummarizeUrl

url = 'https://fr.wikipedia.org/wiki/Napol%C3%A9on_Ier'
summaries = SummarizeUrl(url)
print (summaries)

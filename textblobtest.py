import sys
from textblob import TextBlob
 
b = TextBlob(sys.argv[1])
c = b.translate(to='es')
print('Sentiment: {0} Polarity: {1} In Spanish: {2} '.format(b.sentiment.subjectivity,b.sentiment.polarity,c))

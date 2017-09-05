from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys
sid = SentimentIntensityAnalyzer()
ss = sid.polarity_scores(sys.argv[1])
if ss['compound'] == 0.00:
  print('Neutral')
elif ss['compound'] < 0.00:
  print ('Negative')
else:
  print('Positive')

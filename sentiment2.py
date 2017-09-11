from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import sys
sid = SentimentIntensityAnalyzer()
if len(sys.argv) > 1 :
  ss = sid.polarity_scores(sys.argv[1])
  if ss['compound'] == 0.00:
    print('Neutral')
  elif ss['compound'] < 0.00:
    print ('Negative')
  else:
    print('Positive')

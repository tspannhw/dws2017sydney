from nltk.sentiment.vader import SentimentIntensityAnalyzer
import sys
sid = SentimentIntensityAnalyzer()
if len(sys.argv) > 1 :
  ss = sid.polarity_scores(sys.argv[1])
  print('Compound {0} Negative {1} Neutral {2} Positive {3} '.format(ss['compound'],ss['neg'],ss['neu'],ss['pos']))

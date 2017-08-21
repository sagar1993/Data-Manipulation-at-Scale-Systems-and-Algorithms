import sys
import json

def hw():
	print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))

def extract(sent_file):
	sent_file.seek(0)
	scores = {}
	#afinnfile = open(sent_file)
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.
	return scores

def find_sentiment(scores, tweet_file):
	tweet_file.seek(0)
	for i in tweet_file.readlines():
		data = json.loads(i)
		if 'text' not in data:
			print 0
		else:
			text = data['text'].encode('utf_8')
			text = text.strip()
			text = text.split(' ')
			score = 0
			for word in text:
				if word in scores:
					score += scores[word]
			print(score)		

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	#hw()
	#lines(sent_file)
	#lines(tweet_file)
	scores = extract(sent_file)
	find_sentiment(scores, tweet_file)

if __name__ == '__main__':
	main()

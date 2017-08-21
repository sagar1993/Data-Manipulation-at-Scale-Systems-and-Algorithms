import sys
import json

def find_sentiment(tweet_file):	
	new_words = {}
	totalWordCount = 0 	
	tweet_file.seek(0)
	for i in tweet_file.readlines():
		data = json.loads(i)
		if 'text' in data:
			text = data['text'].encode('utf_8')
			text = text.strip()
			text = text.split(' ')
			for word in text:
				totalWordCount += 1
				if word in new_words:
					new_words[word] += 1
				else:
					new_words[word] = 1				
	for key in new_words:
		print str(key)+ " " + str(float(new_words[key])/ totalWordCount)			

def main():
	tweet_file = open(sys.argv[1])
	find_sentiment(tweet_file)
	
if __name__ == '__main__':
	main()

import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
stateSentiment = dict.fromkeys(states.keys(), 0);

def extract(sent_file):
	sent_file.seek(0)
	scores = {}
	#afinnfile = open(sent_file)
	for line in sent_file:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.
	return scores

def find_sentiment(scores, tweet_file):
	global stateSentiment
	tweet_file.seek(0)
	for i in tweet_file.readlines():
		data = json.loads(i)
		if 'text' in data:
			text = data['text'].encode('utf_8')
			text = text.strip()
			text = text.split(' ')
			score = 0
			for word in text:
				if word in scores:
					score += scores[word]
			if 'user' in data and 'location' in data['user']:
				locationTokens = data["text"].encode('utf-8').split(", ")
				if len(locationTokens) == 2:
					for stateAbbr, stateName in states:
					    if locationTokens[1] == stateAbbr or locationTokens[1] == stateName:
						stateSentiment[stateAbbr] += score	

	happiestState = sorted(stateSentiment, key = stateSentiment.get, reverse=True)
    	#stateAbbr, stateSentiment = happiestState    	
	print happiestState[0]					
				

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	scores = extract(sent_file)
	find_sentiment(scores, tweet_file)
if __name__ == '__main__':
	main()

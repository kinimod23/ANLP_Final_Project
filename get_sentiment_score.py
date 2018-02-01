#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
from nltk.sentiment.vader import SentimentIntensityAnalyzer
snt = SentimentIntensityAnalyzer()

from tokenize_articles import read_corpus

# polarity score: dict with overall, neg, neu, pos
def get_sentiment_score(sentences):
	scores = []
	for sentence in sentences:
		score = snt.polarity_scores(sentence)
		#score_values = [ val for key, val in score.items] not right order
		score_values = []
		score_values.append(str(score["compound"]))
		score_values.append(str(score["neg"]))
		score_values.append(str(score["neu"]))
		score_values.append(str(score["pos"]))
		scores.append(score_values)
	return scores

def write_scores_to_file(out_file, scores):
	with open(out_file, "w") as o:
		o.write("Overall score\tNegative\tNeutral\tPositive\n")
		for score in scores:
			o.write("\t".join(score))
			o.write("\n")

def main(args):
	if len(args) != 3:
		print("usage: {} headlines_input score_output".format(args[0]))
		sys.exit(-1)
	corpus = read_corpus(args[1])
	scores = get_sentiment_score(corpus)
	write_scores_to_file(args[2], scores)

if __name__ == '__main__':
	main(sys.argv)



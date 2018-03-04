#!/usr/bin/python
# -*- coding: utf8 -*-

import sys

def get_headlines(article):
	articles = []
	with open(article) as art:
		for line in art.readlines():
			articles.append(line.strip().split())
	return articles


def get_topic_words(topic_array):
	topics = []
	with open(topic_array) as t:
		for line in t.readlines():
			line = line.split("[")
			topic_words = []
			for topic in line:
				topic = topic.replace("\'", "")
				topic = topic.replace("]", "")
				topic = topic.replace(",", "")
				topic = topic.split()
				topics.append(topic)
	return(topics[1:])

def get_article_topic_dist(t_dist):
	most_imp = []
	with open(t_dist) as t:
		for line in t.readlines():
			line = line.strip().split()
			most_imp.append(line)
	return most_imp


def get_imp_words(topics, topic_dist):
	most_imp_words = []
	for dist in topic_dist:
		most_imp_per_art = []
		for topic_ind in dist:
			most_imp_per_art.extend(topics[int(topic_ind)])
		most_imp_words.append(most_imp_per_art)
	#print(most_imp_words[:10])
	return most_imp_words

def get_imp_headline_words(most_imp_words, headlines):
	words_in_headline = []
	for words, headline in zip(most_imp_words, headlines):
		headline_words = []
		for word in words:
			if word in headline:
				headline_words.append(word)
		words_in_headline.append(headline_words)
	return(words_in_headline)

def get_percentage_imp_word_headline(most_imp_words, words_in_headline):
	percentages = []
	for imp_w, w_in_h in zip(most_imp_words, words_in_headline):
		if len(w_in_h) != 0:
			percentage = 100/ (float(len(imp_w)) / float(len(w_in_h)))
		else:
			percentage = 0
		percentages.append(percentage)
	articles_with_imp_words_in_headlines = 0
	fifty_percent_in_headline = 0
	for per in percentages:
		print(per)
		if per > 0.0:
			articles_with_imp_words_in_headlines += 1
		if per >= 10.0:
			fifty_percent_in_headline += 1

	print(articles_with_imp_words_in_headlines, fifty_percent_in_headline)



def main(args):
	topic_words = get_topic_words(args[1])
	topic_dist = get_article_topic_dist(args[2])
	most_imp_words = get_imp_words(topic_words, topic_dist)
	headlines = get_headlines(args[3])
	words_in_headline = get_imp_headline_words(most_imp_words, headlines)
	get_percentage_imp_word_headline(most_imp_words, words_in_headline)

if __name__ == '__main__':
	main(sys.argv)
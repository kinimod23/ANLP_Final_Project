#!/usr/bin/python
# -*- coding: utf8 -*-

from nltk.tokenize import word_tokenize
import sys

def read_corpus(input_file):
	corpus = []
	with open(input_file) as f:
		for line in f.readlines():
			if line != '\n':
				corpus.append(line.strip())
	return corpus

def tokenize_corpus(articles):
	tokenized_articles = []
	for sentence in articles:
		tokenized_articles.append(word_tokenize(sentence))
	return tokenized_articles

def write_to_file(tokenized_articles, output_file):
	with open(output_file, 'w') as o:
		for article in tokenized_articles:
			o.write(" ".join(article))
			o.write("\n")

def main(args):
	if len(args) != 3:
		print("usage {} input_file output_file".format(args[0]))
		sys.exit(1)
	corpus = read_corpus(args[1])
	tokenized = tokenize_corpus(corpus)
	write_to_file(tokenized, args[2])

if __name__ == '__main__':
	main(sys.argv)


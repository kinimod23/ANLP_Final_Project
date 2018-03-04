#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
from subprocess import Popen, PIPE, STDOUT

def get_sentences(input_file):
	sentences = []
	with open(input_file) as f:
		for line in f.readlines():
			if line != "\n":
				sentences.append(line.strip())
	return sentences

def annotate_articles(sentences):
	annotated_articles = []
	for sentence in sentences:
		sentence.lower()
		p = Popen(['/Applications/Treetagger/cmd/tree-tagger-english'], stdout=PIPE, stdin=PIPE, stderr=PIPE, encoding="utf8")
		out = p.communicate(input=sentence)[0]
		article = []
		annotated_words = out.split("\n")
		for word_anno in annotated_words:
			word_anno = word_anno.split("\t")
			if len(word_anno) == 3:
				annotation = (word_anno[0], (word_anno[1], word_anno[2]))
				article.append(annotation)
		annotated_articles.append(article)
	return annotated_articles 

def get_lemma(articles):
	lemma_articles = []
	for article in articles:
		lemma_article = []
		for word, anno in article:
			if anno[1] == "<unknown>":
				lemma_article.append(word)
			else:
				lemma_article.append(anno[1])
		lemma_articles.append(lemma_article)
	return lemma_articles

def write_to_file(lemma_articles, out_file):
	with open(out_file, "w") as out:
		for article in lemma_articles:
			out.write(" ".join(article))
			out.write("\n")
		

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("usage: {} input_file output_file".format(sys.argv[0]))
		sys.exit(1)
	sentences = get_sentences(sys.argv[1])
	annotated_articles = annotate_articles(sentences)
	article_lemma = get_lemma(annotated_articles)
	write_to_file(article_lemma, sys.argv[2])

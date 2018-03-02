#!/usr/bin/python
# -*- coding: utf8 -*-

import sys

def get_overall_score(scored_file):
	overall_scores = []
	with open(scored_file, 'r') as f: 
		for line in f.readlines():
			if line != "\n":
				overall_scores.append(round(float(line.split("\t")[0]), 1))
	return overall_scores

def read_manual_sa_score(manual_sa_file):
	manual_scores = []
	with open(manual_sa_file, 'r') as f:
		for line in f.readlines():
			if line != "\n":
				manual_scores.append(float(line.strip()))
	return manual_scores

def compare_scores(automatic, manual, ok_range):
	right = 0
	wrong = 0
	wrong_indices = []
	ok_range = float(ok_range)
	for i, (m_score, a_score) in enumerate(zip(automatic, manual)):
		if abs(m_score - a_score) <= ok_range: #and (m_score - a_score) >= 0.0:
			right += 1
			print("right")
			print(m_score, a_score)
		else:
			wrong += 1
			print("wrong")
			print(m_score, a_score)
			wrong_indices.append(i)
	return right, wrong, wrong_indices

def get_score_neg_pos_neut(automatic, manual):
	same_pol = 0
	diff_pol = 0
	wrong_indices = []
	for i, (m_score, a_score) in enumerate(zip(automatic, manual)):
		if (m_score > 0 and a_score > 0) or  (m_score < 0 and a_score < 0) or (m_score == 0 and a_score == 0):
			same_pol += 1
		else:
			diff_pol += 1
			wrong_indices.append(i)
	return same_pol, diff_pol, wrong_indices

def main(args):
	if len(args) != 4:
		print("usage: {} automatic_score manual_score range".format(args[0]))
		sys.exit(-1)
	automatic_score = get_overall_score(args[1])
	manual_score = read_manual_sa_score(args[2])
	right, wrong, wrong_indices = compare_scores(automatic_score, manual_score,args[3])
	same_pol, diff_pol, pol_worng_indices = get_score_neg_pos_neut(automatic_score, manual_score)
	print("Right: {}\nWrong: {}".format(right, wrong))
	print(wrong_indices)
	print("Same polarity: {}\nDifferent polarity: {}".format(same_pol, diff_pol))
	print(pol_worng_indices)

if __name__ == '__main__':
	main(sys.argv)

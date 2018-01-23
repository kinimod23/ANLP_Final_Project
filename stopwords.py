#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:41:59 2018

@author: freyahewett
"""

from nltk.corpus import stopwords
import string
import re

stop_words = list(stopwords.words('english'))
to_delete = ["brexit", "``", "''", "'s", "·", "wo", "n't", "..."]

for elem1 in to_delete:
    stop_words.append(elem1)
for elem in string.punctuation:
    stop_words.append(elem)

tokenized_files = ["just_hl_guardian_tokenized.txt", "just_hl_article_tokenized.txt", 
                   "just_hl_article_guardian_tokenized.txt", "just_hl_sun_tokenized.txt"]

for t_file in tokenized_files:
    with open("filtered" + t_file, "w") as output_file:
    
        to_be_filtered = open(t_file).read()
        words = to_be_filtered.split()
        for word in words:
            word = re.sub(r"^(\')", "", word) #getting rid of the ' at the beginning of some words
            if word.lower() not in stop_words:
                print(word, file=output_file)
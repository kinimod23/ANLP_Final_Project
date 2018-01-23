#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 12:41:59 2018

@author: freyahewett
"""

from nltk.corpus import stopwords
import string

stop_words = list(stopwords.words('english'))

stop_words.append("brexit")
stop_words.append("``")
stop_words.append("''")
for elem in string.punctuation:
    stop_words.append(elem)

tokenized_files = ["just_hl_guardian_tokenized.txt", "just_hl_article_tokenized.txt", 
                   "just_hl_article_guardian_tokenized.txt", "just_hl_sun_tokenized.txt"]

for t_file in tokenized_files:
    with open("filtered" + t_file, "w") as output_file:
    
        to_be_filtered = open(t_file).read()
        words = to_be_filtered.split()
        for word in words:
            if word.lower() not in stop_words:
                print(word, file=output_file)
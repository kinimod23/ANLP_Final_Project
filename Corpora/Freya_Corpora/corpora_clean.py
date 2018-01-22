#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 09:29:42 2018

@author: freyahewett
"""
import re

sun_text = open("sun.txt").read()
sun_text2 = sun_text.strip().split("All Rights Reserved")

guardian_text = open("guardian.txt").read()
guardian_text2 = guardian_text.strip().split("All Rights Reserved")
    
#Sun, headlines and articles

with open("just_hl_article.txt", "w") as output_file:
    for article in sun_text2:
        article2 = article.replace("\n", " ")
        article4 = re.sub(r"^(.*National Edition)", "", article2)
        article5 = re.sub(r"^(.*Edition [0-9]*;)", "", article4)
<<<<<<< HEAD
        article6 = re.sub(r"([a-zA-Z.]*@the[-]*sun\.co\.uk.*)$", "", article5)
=======
        article6 = re.sub(r"(@the[-]*sun\.co\.uk.*)$", "", article5)
>>>>>>> f7a808591dcc39c990accf08fd1349ed69a14253
        article7 = re.sub(r"(BYLINE: .* [0-9]* words)", "", article6)
        article8 = re.sub(r"(LOAD-DATE.*)$", "", article7)
        article9 = re.sub(r"(SECTION: .* LETTER)", "", article8)
        article10 = re.sub(r"(SECTION: .* words)", "", article9)
        print(article10, file=output_file)
        print("\n", file=output_file)
        
#Sun, just headlines
        
with open("just_hl_sun.txt", "w") as output_file:
    for article in sun_text2:
        article2 = article.replace("\n", " ")
        article3 = article2.replace("\\", "")
        article4 = re.sub(r"^(.*National Edition)", "", article3)
        article5 = re.sub(r"^(.*Edition [0-9]*;)", "", article4)
        article7 = re.sub(r"(BYLINE: .*)$", "", article5)
        article9 = re.sub(r"(SECTION: .*)$", "", article7)
        print(article9, file=output_file)
        print("\n", file=output_file)
        
#Guardian, headlines and articles
        
with open("just_hl_article_guardian.txt", "w") as output_file:
    for article in guardian_text2:
        article2 = article.replace("\n", " ")
        article3 = article2.replace("\\", "")
        article4 = re.sub(r"^(.*GMT)", "", article3)
        article6 = re.sub(r"(LOAD-DATE)$", "", article4)
        article7 = re.sub(r"(BYLINE: .* [0-9]* words)", "", article6)
        article8 = re.sub(r"(LOAD-DATE:.*)$", "", article7)
        article9 = re.sub(r"(SECTION: .* LETTER)", "", article8)
        article10 = re.sub(r"(SECTION: .* words)", "", article9)
        print(article10, file=output_file)
        print("\n", file=output_file)
        
#Guardian, just headlines
        
with open("just_hl_guardian.txt", "w") as output_file:
    for article in guardian_text2:
        article2 = article.replace("\n", " ")
        article3 = article2.replace("\\", "")
        article4 = re.sub(r"^(.*GMT)", "", article3)
        article7 = re.sub(r"(BYLINE:.*)$", "", article4)
        article8 = re.sub(r"(SECTION:.*)$", "", article7)
        print(article8, file=output_file)
        print("\n", file=output_file)


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

        to_be_filtered = open(t_file).readlines()
        corpus_list = [line.strip() for line in to_be_filtered]
        corpus_nlist = [each_word.split() for each_word in corpus_list]
        for sentence in range(0, len(corpus_nlist)):
            for word in corpus_nlist[sentence]:
                word = re.sub(r"^(\')", "", word) #getting rid of the ' at the beginning of some words
                if word.lower() not in stop_words:
                    output_file.write(word)
                    output_file.write(" ")
            output_file.write("\n") #line break after each article/hl


# improved list from Stone, Denis, Kwantes (2010)
STOPWORDS = """
a about above across after afterwards again against all almost alone along already also although always am among amongst amoungst amount an and another any anyhow anyone anything anyway anywhere are around as at back be
became because become becomes becoming been before beforehand behind being below beside besides between beyond bill both bottom but by call can
cannot cant co computer con could couldnt cry de describe
detail did do doc doesn done down due during
each eg eight either eleven else elsewhere empty enough etc even ever every everyone everything everywhere except few fifteen
fify fill find fire first five for former formerly forty found four from front full further get give go
had has hasnt have he hence her here hereafter hereby herein hereupon hers herself him himself his how however http hundred i ie
if in inc indeed interest into is it its itself keep last latter latterly least less ltd
just
kg km
ll
made many may me meanwhile might mill mine more moreover most mostly move much must my myself name namely
neither never nevertheless next nine no nobody none noone nor not nothing now nowhere nt of off
often on once one only onto or org other others otherwise our ours ourselves out over own part per
perhaps please pdf put rather re
quite
rather really regarding
same see seem seemed seeming seems serious several she should show side since sincere six sixty so some somehow someone something sometime sometimes somewhere still such system take ten
than that the their them themselves then thence there thereafter thereby therefore therein thereupon these they thick thin third this those though three through throughout thru thus to together too top toward towards twelve twenty two un under
until up unless upon us used using
various very very via
was we well were what whatever when whence whenever where whereafter whereas whereby wherein whereupon wherever whether which while whither who whoever whole whom whose why will with within without would www
xls
yet you
your yours yourself yourselves
i ii iii iv v vi vii viii ix x xi xii xiii xiv xv xvi xvii xviii xix xx xxi xxii xxiii xxiv xxv xxvi xxvii xxviii xxix xxx
"""
STOPWORDS = frozenset(w.encode('utf8') for w in STOPWORDS.split() if w)



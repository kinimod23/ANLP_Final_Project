from gensim import corpora, models
import gensim
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

def train_lda(filename,stopword):
     '''applies LDA to tokenized articles in a txt-file where each article is
     separated by a newsline'''
     with open(filename,encoding="utf-8") as f:
        all_articles = f.readlines()
        tokens = [[token for token in article.strip().split(" ") if token not in stopword] for article in all_articles]
        #print(tokens[0])
     dictionary = corpora.Dictionary(tokens)
     corpus = [dictionary.doc2bow(token) for token in tokens]
     ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=3, id2word=dictionary, passes=10)
     return ldamodel



stopword = stopwords.words("english") + list(string.punctuation)

model = train_lda("just_hl_article_guardian_lemmatized.txt",stopword)
print(model.print_topics(num_topics=10, num_words=10))
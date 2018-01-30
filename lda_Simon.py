from gensim import corpora, models
import gensim
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
#import scikit


######### Das gehört zu Simons Änderungen ##########
from pprint import pprint
from textblob import TextBlob

def createCorpus(filename1, filename2, stopwords):
    with open(filename1,encoding="utf-8") as f1:
        with open(filename2, encoding="utf-8") as f2:
            all_articles = f1.readlines()
            all_articles.extend(f2.readlines())
            tokens = [[token for token in article.strip().split(" ") if token not in stopword] for article in all_articles[:20]]
    return tokens

def createModelCorpus(tokens):
    dictionary = corpora.Dictionary(tokens)
    dictionary.filter_extremes(no_below=20, no_above=0.5)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    return corpus

def train_lda(tokens):
    '''applies LDA to tokenized articles in a txt-file where each article is
    separated by a newsline'''
    dictionary = corpora.Dictionary(tokens)
    dictionary.filter_extremes(no_below=20, no_above=0.5)
    corpus = [dictionary.doc2bow(token) for token in tokens]
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=10, id2word=dictionary, passes=10)
    return ldamodel

def apply_lda(lda_model, tokens):
    corpus_feature_vectors = []
    for article in tokens:
        corpus_feature_vectors.append(lda_model(token))
    return corpus_feature_vectors


stopword = stopwords.words("english") + list(string.punctuation)

corpus = createCorpus("Corpora/filtered/filteredjust_hl_article_guardian_tokenized.txt","Corpora/filtered/filteredjust_hl_article_tokenized.txt" ,stopword)
model_corpus = createModelCorpus(corpus)
lda_model = train_lda(model_corpus)
corpus_feature_vectors = apply_lda(lda_model, tokens)

pprint(model.print_topics(num_topics=10, num_words=15))

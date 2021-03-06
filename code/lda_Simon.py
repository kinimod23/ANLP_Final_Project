from gensim import corpora, models
import gensim
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
#from k_means import kmeans
from pprint import pprint

class LDA():
    def __init__(self, filename1, filename2, stopwords, num_topics=10, no_below=20, no_above=0.5):
        self.num_topics = num_topics
        self.corpus = self.createCorpus(filename1, filename2, stopwords)
        self.model_corpus, self.dictionary = self.createModelCorpus(no_below, no_above)
        try:
            self.model = gensim.models.LdaModel.load("LDA_Models/ldamodel_topics="+str(num_topics)+"_no_above="+str(no_above))
        except:
            self.model = self.train_lda()
            self.model.save("LDA_Models/ldamodel_topics="+str(num_topics)+"_no_above="+str(no_above))

        self.corpus_feature_vectors = self.apply_lda()
        self.final_output = self.createFinalOutput()

    def createCorpus(self, filename1, filename2, stopwords):
        with open(filename1,encoding="utf-8") as f1:
            with open(filename2, encoding="utf-8") as f2:
                all_articles = f1.readlines()
                all_articles.extend(f2.readlines())
                corpus = [[token for token in article.strip().split(" ") if token not in stopwords] for article in all_articles]
        return corpus

    def createModelCorpus(self, no_below, no_above):
        dictionary = corpora.Dictionary(self.corpus)
        dictionary.filter_extremes(no_below=no_below, no_above=no_above)
        model_corpus = [dictionary.doc2bow(token) for token in self.corpus]
        return model_corpus, dictionary

    def train_lda(self):
        '''applies LDA to tokenized articles in a txt-file where each article is
        separated by a newsline'''
        ldamodel = gensim.models.ldamulticore.LdaMulticore(self.model_corpus, num_topics=self.num_topics, id2word=self.dictionary, passes=10)
        return ldamodel

    def apply_lda(self):
        corpus_feature_vectors = []
        for article in self.model_corpus:
            corpus_feature_vectors.append(self.model[article])
        return corpus_feature_vectors

    def createFinalOutput(self):
        output = []
        for vec in self.corpus_feature_vectors:
            vec_dic = dict(vec)
            output.append([(vec_dic[topic] if topic in vec_dic else 0) for topic in range(10)])
        return output

    def get_topics(self,num_topics=10,num_words=10,probs=False):
        #return topics without probabilites
        topics = self.model.show_topics(num_topics=num_topics,num_words=num_words,formatted=False)
        #print(topics)
        if not(probs):
            all_topics = []
            for topic in topics:
                all_words = []
                for word in topic[1]:
                    all_words.append(word[0])
                all_topics.append(all_words)
                #print(all_words)

            return(all_topics)
        else:
            return topics

stopword = stopwords.words("english") + list(string.punctuation) + ["Mrs", "Mr"]

filename1 = "Corpora/filtered/filteredjust_hl_article_guardian_lemmatized.txt"
filename2 = "Corpora/filtered/filteredhl_article_tele_lemmatized.txt"


# no_below : No words which appear in less than X articles
# no_above : No words which appear in more than X % of the articles
if __name__ == '__main__':
    for num_topics in range(6,11,2):
        for no_above in [0.5,0.6,0.7]:
            print('Number Topics: ', num_topics, '   no above :', no_above)
            lda = LDA(filename1, filename2 ,stopword, num_topics=num_topics, no_below=20, no_above=no_above)

            corpus_feature_vectors = lda.corpus_feature_vectors
            output = lda.final_output

            #pprint(output[:2])

            k_means = kmeans(output,str(num_topics)+"_"+str(no_above))
            k_means.plot_elbow(range(2, 10), "Elbow_plot", individ_plot=True)

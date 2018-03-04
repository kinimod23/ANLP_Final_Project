from k_means import kmeans
from lda_Simon import LDA
from nltk.corpus import stopwords
import string


more_stopwords = ["Mrs", "Mr"]
stopword = stopwords.words("english") + list(string.punctuation) + more_stopwords

#print(stopword)
filename1 = "Corpora/filtered/filteredjust_hl_article_guardian_lemmatized.txt"
filename2 = "Corpora/filtered/filteredhl_article_tele_lemmatized.txt"


# no_below : No words which appear in less than X articles
# no_above : No words which appear in more than X % of the articles

for num_topics in range(6, 15, 2):
    for no_above in [0.5, 0.6, 0.7]:
        lda = LDA(filename1, filename2, stopword, num_topics=num_topics, no_below=20, no_above=no_above)
        corpus_feature_vectors = lda.corpus_feature_vectors
        output = lda.final_output
        with open("cluster_images/top10topics.csv", "a") as top:
            top.write("num_topics=" + str(num_topics) + "_no_above=" + str(no_above).replace(".", "") + ",")
            topics = lda.get_topics(num_words=5)
            for topic_words in topics:
                top.write(str(topic_words) + ",")
            top.write("\n")
        for k in range(4,17,2):
            k_means = kmeans(output, "histograms")
            labels,score = k_means.cluster(k)
            k_means.plot_histogram2("num_topics="+str(num_topics)+"_no_above="+str(no_above).replace(".","")+"_k="+str(k),k)


from k_means import kmeans
from lda_Simon import LDA
from nltk.corpus import stopwords
import string


more_stopwords = ["Mrs", "says", "Mr"]
stopword = stopwords.words("english") + list(string.punctuation) + more_stopwords

filename1 = "Corpora/filtered/filtered_just_hl_guardian.txt"
filename2 = "Corpora/filtered/filteredhl_article_tele_lemmatized.txt"


# no_below : No words which appear in less than X articles
# no_above : No words which appear in more than X % of the articles
lda = LDA(filename1, filename2, stopword, num_topics=10, no_below=20, no_above=0.5)
corpus_feature_vectors = lda.corpus_feature_vectors
output = lda.final_output

for k in range(7, 17):
    k_means = kmeans(output, "histograms")
    labels,score = k_means.cluster(k)
    k_means.plot_histogram2("histogram",k)

print(lda.get_topics())

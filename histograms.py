from k_means import kmeans
from lda_Simon import LDA

stopword = stopwords.words("english") + list(string.punctuation)

filename1 = "Corpora/filtered/filteredjust_hl_article_guardian_tokenized.txt"
filename2 = "Corpora/filtered/filteredjust_hl_article_tokenized.txt"


# no_below : No words which appear in less than X articles
# no_above : No words which appear in more than X % of the articles
lda = LDA(filename1, filename2, stopword, num_topics=7, no_below=20, no_above=0.5)

corpus_feature_vectors = lda.corpus_feature_vectors
output = lda.final_output

for k in range(2,10):
    k_means = kmeans(output, "histograms")
    labels,score = k_means.cluster(k)
    k_means.plot_histogram("histo",k)



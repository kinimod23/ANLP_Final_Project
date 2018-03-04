from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA, TruncatedSVD
import matplotlib.pyplot as plt
import numpy as np
import os
from itertools import groupby
from nltk.corpus import stopwords
import string
from lda_Simon import LDA

class kmeans():

    def __init__(self,feature_vector,image_dir,r_state=42):

        self.feature_vector = feature_vector
        self.r_state = r_state
        self.dir = "cluster_images/"+image_dir+"/"
        guardian = np.ones(998)
        sun = np.zeros(876)
        self.both = np.concatenate([guardian, sun])
        self.centroids=None


    def cluster(self,k):
        '''
        partitions the data into k clusters using the k_means algorithm
        '''
        clustering = KMeans(n_clusters=k,random_state=self.r_state)
        labels = clustering.fit_predict(self.feature_vector)
        self.labels = labels

        self.centroids = clustering.cluster_centers_
        return(labels,clustering.inertia_)

    def visualize_data(self,fname):
        '''
        shows a 2-dimensional scatter plot of data with each color representing the cluster and the
        form of the data point (triange/circle) indicates from which newspaper the article is
        '''
        X_reduced = PCA(n_components=2).fit_transform(self.feature_vector)
        fig = plt.figure()

        ax = fig.add_subplot(111)
        ax.scatter(X_reduced[:, 0], X_reduced[:, 1], c=self.labels,marker="^", s=self.both*10, edgecolor="red", linewidth=0.3)
        ax.scatter(X_reduced[:,0], X_reduced[:,1], c=self.labels,marker="o", s=((self.both-1)*-1)*10, edgecolor="black", linewidth=0.3)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        #plt.colorbar(scatter)

        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        plt.savefig(self.dir+fname,dpi=600)
        plt.close()

    def plot_elbow(self,k_range,fname,individ_plot=False):
        '''
        plots the intra-cluster distance of all clustr against different number of cluster. Needs the range of k.
        '''
        distorsions = []
        for k in k_range:
            labels, score = self.cluster(k)
            distorsions.append(score)
            if individ_plot:
                self.visualize_data("cluster_"+str(k))

        plt.figure(figsize=(15, 5))
        plt.xlabel("number of clusters: k")
        plt.ylabel("Sum of squared distances of samples to their closest cluster center.")
        plt.plot(k_range, distorsions)
        plt.grid(True)
        plt.savefig(self.dir+fname,dpi=600)
        plt.close()

    def plot_histogram2(self, fname, k):
        '''
        plots the histogram for the distribution of articles in each cluster
        '''
        grouped = [[] for x in range(k)]
        hist = [[] for x in range(k)]
        # the histogram of the data
        verteilung = list(zip(self.both, self.labels))
        verteilung = sorted(verteilung, key=lambda x: x[1])

        for key, group in groupby(verteilung, lambda x: x[1]):
            for thing in group:
                #print(key, thing)
                grouped[key].append(int(thing[0]))
            hist[key].append(np.histogram(grouped[key],bins=2)[0])

        guardian = []
        telegraph = []
        for cluster in hist:
            guardian.append(cluster[0][0])
            telegraph.append(cluster[0][1])

        ind = np.arange(k)  # the x locations for the groups
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(ind, guardian, width, color='b')
        rects2 = ax.bar(ind + width, telegraph, width, color='y')

        # add some text for labels, title and axes ticks
        ax.set_ylabel('Frequency in topic clusters')
        ax.set_title('Distribution of Guardian/Telegraph articles in each cluster')
        ax.set_xticks(ind + width / 2)
        ax.set_xticklabels(range(k))

        ax.legend((rects1[0], rects2[0]), ('The Guardian', 'Telegraph'))

        print(str(self.dir + fname))
        plt.savefig(str(self.dir + fname))
        plt.clf()

if __name__ == '__main__':
    more_stopwords = ["Mrs", "Mr"]
    stopword = stopwords.words("english") + list(string.punctuation) + more_stopwords

    # print(stopword)
    filename1 = "Corpora/filtered/filteredjust_hl_article_guardian_lemmatized.txt"
    filename2 = "Corpora/filtered/filteredhl_article_tele_lemmatized.txt"

    # no_below : No words which appear in less than X articles
    # no_above : No words which appear in more than X % of the articles
    for num_topics in range(10, 15, 2):
        for no_above in [0.5, 0.6, 0.7]:
            lda = LDA(filename1, filename2, stopword, num_topics=num_topics, no_below=20, no_above=no_above)
            corpus_feature_vectors = lda.corpus_feature_vectors
            output = lda.final_output

            k_means = kmeans(output, "num_topics="+str(num_topics)+"_no_above="+str(no_above).replace(".",""))

            #print(k_means.centroids)
            k_means.plot_elbow(range(4,17,2), "Elbow plot", individ_plot=True)


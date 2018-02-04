from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA, TruncatedSVD
import matplotlib.pyplot as plt
import numpy as np
import os
from itertools import groupby

class kmeans():

    def __init__(self,feature_vector,image_dir,r_state=42):

        self.feature_vector = feature_vector
        self.r_state = r_state
        self.dir = "cluster_images/"+image_dir+"/"
        guardian = np.ones(998)
        sun = np.zeros(876)
        self.both = np.concatenate([guardian, sun])


    def cluster(self,k):
        clustering = KMeans(n_clusters=k,random_state=self.r_state)
        labels = clustering.fit_predict(self.feature_vector)
        self.labels = labels
        return(labels,clustering.inertia_)

    def visualize_data(self,fname):

        X_reduced = PCA(n_components=2).fit_transform(self.feature_vector)
        fig = plt.figure()

        ax = fig.add_subplot(111)
        ax.scatter(X_reduced[:, 0], X_reduced[:, 1], c=self.labels,marker="^", s=both*10, edgecolor="red", linewidth=0.3)
        ax.scatter(X_reduced[:,0], X_reduced[:,1], c=self.labels,marker="o", s=((both-1)*-1)*10, edgecolor="black", linewidth=0.3)
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        #plt.colorbar(scatter)

        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        plt.savefig(self.dir+fname,dpi=600)
        plt.close()

    def plot_elbow(self,k_range,fname,individ_plot=False):
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

    def plot_histogram(self, fname, k):
        #does not work
        grouped = [[] for x in range(k)]
        # the histogram of the data
        verteilung = list(zip(self.both, self.labels))
        verteilung = sorted(verteilung,key=lambda x: x[1])

        for key, group in groupby(verteilung, lambda x: x[1]):
            for thing in group:
                print(key,thing)
                grouped[key].append(int(thing[0]))

        plt.hist(grouped, k, histtype='bar',normed=1, alpha=0.75)
        plt.tight_layout()
        plt.savefig(self.dir+fname+str(k))
        plt.clf()

    def plot_histogram2(self, fname, k):
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
        sun = []
        for cluster in hist:
            guardian.append(cluster[0][0])
            sun.append(cluster[0][1])

        ind = np.arange(k)  # the x locations for the groups
        width = 0.35  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(ind, guardian, width, color='b')
        rects2 = ax.bar(ind + width, sun, width, color='y')

        # add some text for labels, title and axes ticks
        ax.set_ylabel('Frequency in topic clusters')
        ax.set_title('Distribution of Guardian/Sun articles in each cluster')
        ax.set_xticks(ind + width / 2)
        ax.set_xticklabels(range(k))

        ax.legend((rects1[0], rects2[0]), ('The Guardian', 'Sun'))
        plt.savefig(self.dir + fname + str(k))
        plt.clf()

if __name__ == '__main__':
    data = [[0,1,2,3,4,5],[0,1,4,5,6,3],[7,4,3,2,3,4]]

    k_means = kmeans(data,"test")
    labels,score = k_means.cluster(2)
    print(list(zip(data,labels)))
    k_means.visualize_data("cluster1")

    #k_means.plot_elbow(range(1,3),"Elbow plot",individ_plot=True)


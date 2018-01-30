from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA, TruncatedSVD
import matplotlib.pyplot as plt
import numpy as np


class kmeans():

    def __init__(self,feature_vector,r_state=42):
        self.feature_vector = feature_vector
        self.r_state = r_state


    def cluster(self,k):
        clustering = KMeans(n_clusters=k,random_state=self.r_state)
        labels = clustering.fit_predict(self.feature_vector)
        self.labels = labels
        return(labels,clustering.inertia_)

    def visualize_data(self,fname):

        X_reduced = PCA(n_components=2).fit_transform(self.feature_vector)
        fig = plt.figure()

        ax = fig.add_subplot(111)
        scatter = ax.scatter(X_reduced[:,0], X_reduced[:,1], c=self.labels, s=5)

        ax.set_xlabel('x')
        ax.set_ylabel('y')
        plt.colorbar(scatter)

        plt.savefig(fname,dpi=600)

    def plot_elbow(self,k_range,fname,individ_plot=False):
        distorsions = []
        for k in k_range:
            labels, score = k_means.cluster(k)
            distorsions.append(score)
            if individ_plot:
                k_means.visualize_data("cluster_"+str(k))

        plt.figure(figsize=(15, 5))
        plt.xlabel("number of clusters: k")
        plt.ylabel("Sum of squared distances of samples to their closest cluster center.")
        plt.plot(k_range, distorsions)
        plt.grid(True)
        plt.savefig(fname,dpi=600)

if __name__ == '__main__':
    data = [[0,1,2,3,4,5],[0,1,4,5,6,3],[7,4,3,2,3,4]]

    k_means = kmeans(data)
    labels = k_means.cluster(2)
    print(list(zip(data,labels)))
    k_means.visualize_data("cluster1")

    k_means.plot_elbow(range(1,3),"Elbow plot")


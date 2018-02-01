from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA, TruncatedSVD
import matplotlib.pyplot as plt
import numpy as np
import os


class kmeans():

    def __init__(self,feature_vector,image_dir,r_state=42):

        self.feature_vector = feature_vector
        self.r_state = r_state
        self.dir = "cluster_images/"+image_dir+"/"
        guardian = np.ones(998)
        sun = np.zeros(876)
        self.both = np.concatenate([sun, guardian])


    def cluster(self,k):
        clustering = KMeans(n_clusters=k,random_state=self.r_state)
        labels = clustering.fit_predict(self.feature_vector)
        self.labels = labels
        return(labels,clustering.inertia_)

    def visualize_data(self,fname):

        X_reduced = PCA(n_components=2).fit_transform(self.feature_vector)
        fig = plt.figure()

        ax = fig.add_subplot(111)
        ax.scatter(X_reduced[:,0], X_reduced[:,1], c=self.labels,marker="^", s=self.both)
        ax.scatter(X_reduced[:, 0], X_reduced[:, 1], c=self.labels,marker="o", s=(self.both-1)*-1)
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

    def plot_histogram(self,fname,k):
        filename = fname+str(k)
        # the histogram of the data
        verteilung = zip(self.both,self.feature_vector)
        #plt.hist(, k, normed=1, facecolor='g', alpha=0.75)


        plt.xlabel('Smarts')
        plt.ylabel('Probability')
        plt.title('Histogram of IQ')
        plt.grid(True)
        plt.savefig(filename)

if __name__ == '__main__':
    data = [[0,1,2,3,4,5],[0,1,4,5,6,3],[7,4,3,2,3,4]]

    k_means = kmeans(data,"test")
    labels,score = k_means.cluster(2)
    print(list(zip(data,labels)))
    k_means.visualize_data("cluster1")

    #k_means.plot_elbow(range(1,3),"Elbow plot",individ_plot=True)


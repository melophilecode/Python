from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
X,y=make_blobs(n_samples=100,centers=4,random_state=42)
km=KMeans(n_clusters=4,random_state=42)
km.fit(X)
plt.scatter(X[:,0],X[:,1],c=km.labels_)
plt.title("K_Means Clustering")
plt.show()

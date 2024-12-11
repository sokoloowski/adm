### Mini-Batch K-Means clustering

It is a faster, memory-efficient variant of the K-Means. It is designed to handle large datasets by working on small, random subsets (mini-batches) of data during each iteration.

Steps:

1. Initialize: Randomly initialize $K$ centroids, as in standard K-Means.
2. Random Mini-Batches: At each iteration, sample a small random subset of the dataset (a mini-batch).
3. Cluster Assignment: Assign points in the mini-batch to the nearest centroids.
4. Centroid Update: Update the centroids based on the mini-batch using a weighted moving average: $C_t = C_{t-1} + \eta (x - C_{t-1})$, where $C_t$ is the updated centroid, $x$ is a data point, and $\eta$ is a learning rate.
5. Repeat: Iterate until convergence or a maximum number of iterations is reached.

Results:

![](images/cluster_TruncatedSVD_MiniBatchKMeans_CountVectorizer.png){#fig:minibatch-kmeans-count widh=80%}

![](images/cluster_TruncatedSVD_MiniBatchKMeans_TfidfVectorizer.png){#fig:minibatch-kmeans-tfidf widh=80%}

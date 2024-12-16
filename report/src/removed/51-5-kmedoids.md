### K-Medoids clustering

This method is similar to K-Means, but instead of using the mean as the cluster center, it uses an actual data point (called a medoid) as the center of each cluster. This makes it more robust to noise and outliers compared to K-Means.

Steps of the Algorithm:

1. Initialization: Select $K$ data points randomly as the initial medoids.
2. Cluster Assignment: Assign each data point to the nearest medoid based on a chosen distance metric (e.g., Euclidean, Manhattan).
3. Medoid Update: For each cluster, replace the medoid with another data point in the cluster if it reduces the total cost (sum of distances between points and the medoid).
4. Repeat: Reassign points and update medoids until there is no change or the maximum number of iterations is reached.

![](images/cluster_TruncatedSVD_KMedoids_CountVectorizer.png){#fig:agglomerative-count widh=80%}

![](images/cluster_TruncatedSVD_KMedoids_TfidfVectorizer.png){#fig:agglomerative-tfidf widh=80%}

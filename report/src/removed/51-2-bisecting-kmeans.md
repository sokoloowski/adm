### Bisecting K-Means clustering

This algorithm improves traditional K-Means by iteratively splitting clusters to form $K$ groups:

1. Start with All Data in One Cluster: Treat the entire dataset as a single cluster.
2. Bisect a Cluster: Select a cluster to split, then perform K-Means with $K=2$ (split into two subclusters).
3. Choose the Best Split: Evaluate the splits (e.g., by minimizing intra-cluster distances or maximizing separation), then select the split that provides the most meaningful division.
4. Repeat Until $K$ Clusters Are Formed: Continue bisecting clusters until the desired number of $K$ clusters is achieved.

Results are presented below.

![](images/cluster_TruncatedSVD_BisectingKMeans_CountVectorizer.png){#fig:bisecting-kmeans-count widh=80%}

![](images/cluster_TruncatedSVD_BisectingKMeans_TfidfVectorizer.png){#fig:bisecting-kmeans-tfidf widh=80%}

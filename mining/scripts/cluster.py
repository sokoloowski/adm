import gc

import matplotlib.pyplot as plt
from sklearn.calibration import LabelEncoder
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics import silhouette_score


def plot(X, y, labels, groundtruth, dec: str, alg: str, vect: str) -> None:
    plt.figure(figsize=(10, 6))
    plt.axis('off')
    plt.subplot(1, 2, 1)
    plt.scatter(X, y, c=labels)
    plt.title(f'Clustered {dec} of {alg} on {vect}')
    plt.subplot(1, 2, 2)
    plt.scatter(X, y, c=groundtruth)
    plt.title('Groundtruth')
    plt.show()


def analyze(algorithm, vectorizer, dataframe) -> None:
    gc.collect()
    le = LabelEncoder()
    y = le.fit_transform(dataframe['subreddit'])
    X = vectorizer.fit_transform(dataframe['body'])
    try:
        algorithm.fit(X)
    except:
        algorithm.fit(X.toarray())
    silhouette = silhouette_score(X, algorithm.labels_)
    print("Silhouette score:", silhouette)
    tsvd = TruncatedSVD(n_components=2)
    X_tsvd = tsvd.fit_transform(X)
    plot(X_tsvd[:, 0], X_tsvd[:, 1], algorithm.labels_, y,
         'Truncated SVD', algorithm.__class__.__name__,
         vectorizer.__class__.__name__)
    gc.collect()

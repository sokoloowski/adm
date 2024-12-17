import gc

import matplotlib.pyplot as plt
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from tqdm.auto import tqdm

from config import DATASET_SIZE
from scripts.colors import error, success


def setup(quiet: bool = True):
    tqdm.pandas()
    nltk_modules = ['brown', 'wordnet', 'punkt_tab', 'stopwords',
                    'universal_tagset', 'averaged_perceptron_tagger_eng']
    for module in nltk_modules:
        nltk.download(module, quiet=quiet)


def _plot_top_words(data: pd.Series, limit: int = 30, reverse: bool = False, **kwargs):
    vectorizer = CountVectorizer(**kwargs)
    X = vectorizer.fit_transform(data)
    words = vectorizer.get_feature_names_out()
    counts = X.sum(axis=0).A1
    freq_distribution = pd.Series(counts, index=words)
    ax = freq_distribution.sort_values(ascending=reverse)
    ax = ax.head(limit).plot(kind='barh', figsize=(16, 9))
    for container in ax.containers:
        ax.bar_label(container)
    plt.show()
    gc.collect()


def plot_most_popular(data: pd.Series, limit: int = 30, **kwargs):
    _plot_top_words(data, limit, False, **kwargs)


def plot_least_popular(data: pd.Series, limit: int = 30, **kwargs):
    _plot_top_words(data, limit, True, **kwargs)


def plot_length_histogram(data: pd.Series):
    data.progress_apply(len).hist(bins=100, figsize=(8, 5))
    plt.show()
    gc.collect()


def checkpoint(step: str, dataframe: pd.DataFrame = None):
    path = f"data/{step}-{DATASET_SIZE}.pkl"

    if dataframe is None:
        return pd.read_pickle(path)
    else:
        pd.to_pickle(dataframe, path)

    return dataframe


def diff(old: str, new: str):
    print("Original:", end=" ")
    error(old, critical=False)

    print("=" * 20)

    print("Modified:", end=" ")
    success(new)

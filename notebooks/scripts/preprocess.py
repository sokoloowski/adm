import re
from html import unescape

import nltk
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords, wordnet as wn


def detect_language(text: str):
    # inspiration: github.com/Priyanshuuu/Language-Detection
    # 1.75 ms ± 16.9 μs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
    # For comparison, `langdetect` takes 2.1 ms per loop
    words_set: set[str] = set(nltk.wordpunct_tokenize(text.lower()))
    occurences = {lang: len(words_set.intersection(stopwords.words(lang)))
                  for lang in stopwords.fileids() if lang != 'hinglish'}
    return max(occurences, key=occurences.get)


def preprocessing(text: str,
                  stop_words: list = stopwords.words('english'),
                  lemmatizer: WordNetLemmatizer = WordNetLemmatizer()) -> str:
    # Initial cleaning: lowercase, remove URLs, unescape HTML entities
    text = unescape(re.sub(r"http(s?)://\S+", '', text.lower()))

    # Remove stop words - first run
    text = ' '.join([word for word in text.split() if word not in stop_words])

    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    tokens = nltk.pos_tag(tokens, tagset='universal')

    result = []
    for token, pos in tokens:
        if token in stop_words:
            # Remove stop words - second run
            # Tokenization may reveal stop words, which were not removed in the first run
            continue
        pos = {'NOUN': 'n', 'VERB': 'v', 'ADJ': 'a', 'ADV': 'r'}.get(pos, 'n')

        # Lemmatize the token
        token = lemmatizer.lemmatize(token, pos)

        # Remove non-alphabetic characters
        token = re.sub(r"[^a-z]", ' ', token).strip()
        if token:
            result.append(token)

    # Remove stop words - third run
    # Replacing non-alphabetic characters may produce stop words: `he's` is not a stop word but `he` and `s` are
    return ' '.join([word for word in result if word not in stop_words])


def remove_nonwords(text: str, dictionary: set) -> str:
    return ' '.join([word for word in text.split() if word in dictionary])


def preprocessing_v2(text: str) -> str:
    # Initial cleaning: lowercase, remove URLs, unescape HTML entities
    text = unescape(re.sub(r"http(s?)://\S+", '', text.lower()))
    sw = stopwords.words('english')

    # Remove stop words - first run
    text = ' '.join([word for word in text.split() if word not in sw])

    # Tokenize the text
    tokens = nltk.word_tokenize(text)
    tokens = nltk.pos_tag(tokens, tagset='universal')

    result = []
    for token, pos in tokens:
        if token in sw:
            # Remove stop words - second run
            # Tokenization may reveal stop words, which were not removed in the first run
            continue
        pos = {'NOUN': 'n', 'VERB': 'v', 'ADJ': 'a', 'ADV': 'r'}.get(pos, 'n')
        synsets = wn.synsets(token, pos=pos)
        if synsets:
            # Lemmatize the token
            token = synsets[0].lemmas()[0].name().lower()

            # Remove non-alphabetic characters
            token = re.sub(r"[^a-z]", ' ', token).strip()
            if token:
                result.append(token)

    # Remove stop words - third run
    # Replacing non-alphabetic characters may produce stop words: `he's` is not a stop word but `he` and `s` are
    return ' '.join([word for word in result if word not in sw])
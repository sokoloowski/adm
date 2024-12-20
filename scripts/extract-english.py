
import pandas as pd
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 42


def detect_language(text):
    try:
        return detect(text)
    except:
        return 'error'


df = pd.read_pickle("./filtered.pkl")

# keep only english text
df = df[df['body'].apply(detect_language) == 'en']
# took 71m 14.3s

df.to_pickle("./filtered_en-full.pkl")

## Another approach to preprocessing

The methodology outlined in [@sec:preprocessing] effectively addresses the data cleansing issue, yet it is not a comprehensive solution. It was decided that a solution combining the advantages of the previously used ideas of removing non-word strings and retaining specialised vocabulary would be the optimal approach. To achieve this, we employed the use of WordNet, a large lexical database of English [@miller1995wordnet]. This necessitated a modification to the implementation of the function responsible for preprocessing (illustrated in [@lst:preprocessing]). Rather than utilising the pre-existing `WordNetLemmatizer` class, the text was processed manually using so-called synsets. This approach enabled the rejection of non-words, or words devoid of synonyms^[If the given string is a word, there is at least one synonym that is the same word as the given string.], at the level of lemmatisation. An attempt was made to stem the flow, but this proved unsuccessful.
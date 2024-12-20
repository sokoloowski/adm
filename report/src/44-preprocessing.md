## Another Approach to Preprocessing

The methodology described in [@sec:preprocessing] effectively addresses the data cleansing issue but does not provide a comprehensive solution. To enhance the preprocessing process, we sought a solution that combines the strengths of the previous approach—removing non-word strings—while retaining specialized vocabulary. To achieve this, we integrated **WordNet**, a large lexical database of the English language [@miller1995wordnet].

This required a modification to the preprocessing function (as shown in [@lst:preprocessing]). Instead of using the existing `WordNetLemmatizer` class, we manually processed the text with **synsets**. Synsets represent sets of synonyms that can provide richer linguistic context. By leveraging synsets, we could reject non-words—those words without any synonyms—during the lemmatization process. This method ensured that only valid words, with recognized meanings, were retained in the dataset.

Initially, an attempt was made to use stemming, but this approach was not successful in this context. Stemming often removes meaningful word parts and can distort the original word form, which was not suitable for the precise vocabulary required in our dataset. Therefore, we focused solely on lemmatization using WordNet synsets.

This refined approach allowed us to maintain meaningful words while filtering out non-lexical items, resulting in a cleaner and more relevant dataset for further analysis.

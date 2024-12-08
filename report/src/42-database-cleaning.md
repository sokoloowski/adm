## Reducing dataset size at the database level

Our initial plan was to remove all entries where either the author or the content was marked as deleted (indicated by `[deleted]`). However, we ultimately decided to preserve as much of the content as possible. As a result, we kept the rows with the deleted author, removing only the rows where the content itself was marked as deleted. This reduced our dataset by approximately 110 million rows, or around 8% of the total. Despite this, we still have a massive dataset that remains challenging to search without sufficient computing power.

![After removing rows with deleted content, our dataset did not change much.](images/comments_count_first_clean.png){#fig:first-clean width=80%}

We opted to significantly reduce the size of our dataset by retaining only the rows containing more than 1,000 characters of content. However, to avoid discarding valuable information, we chose not to apply this restriction too broadly. Consequently, we saved the selected records to a new table using a `SELECT INTO` query. The resulting table contained just under 27 million rows.

![Entries of more than 1,000 characters are a distinct minority, accounting for less than 2% of the total set of passed.](images/comments_count_second_clean.png){#fig:second-clean width=80%}

It is important to note that the restriction we imposed - requiring entries to exceed 1,000 characters - is relatively stringent, as shown in [@fig:second-clean]. In comparison, X (formerly Twitter) permits posts with a maximum length of 280 characters, with the majority of tweets being 34 characters long [@twitter2017]. Nonetheless, this limitation was chosen deliberately, as our dataset encompasses a highly diverse vocabulary. Our goal is to ensure that, even after the removal of stopwords, the underlying meaning of the posts remains intact.

Although not shown in [@fig:second-clean], the overall shape of the entry length graph is preserved. A comparison of the graphs, before and after data cleaning, is provided in [@fig:second-clean-distribution], with 100% representing the length of the longest entry. As depicted, despite the considerable reduction in the number of entries, the shape of the graph remained almost identical.

![Even after a comprehensive cleaning of the dataset, the overall structure of the chart was maintained.](images/comments_count_second_clean_compare.png){#fig:second-clean-distribution width=80%}

Due to constraints imposed by hardware limitations, we opted to focus on a subset of five subreddits for further analysis: `politics`, `programming`, `science`, `gaming`, and `technology`. This selection was guided by the prominence of these categories and their broad thematic diversity. As a result, we compiled a dataset comprising over 1.6 million entries, from which we randomly sampled 4,000 entries from each subreddit.

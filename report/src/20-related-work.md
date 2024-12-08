# State of the art and related work {#sec:related-work}

<!-- Opisać status API oraz istniejące biblioteki, wskazać limity API -->

Analyzing social media posts is a frequent topic in academic research. Users' posts often provide information about world events [@cheong2011social], as well as their emotions and opinions [@https://doi.org/10.1109/INFOP.2015.7489492]. Many academic papers focus on analyzing Twitter posts, but Reddit is also a popular source of data.

Reddit is one of the few social networks with such a large number of users, while having a free API. In addition, the platform is known for its high diversity of topics, which allows for analysis of different areas of life. Also important is the fact that Reddit's structure allows for categorization of posts, which relieves researchers of the need to manually label data.

To query the API, we wanted to use the PRAW^[Python Reddit API Wrapper] library [@praw2024]. It allows easy access to Reddit's APIs, as well as convenient data processing. In addition, PRAW allows you to handle authentication, which is essential for retrieving data from Reddit. Unfortunately, API limitations proved to be an obstacle during the initial development of the project. When querying to read posts and comments, we could retrieve a maximum of 100 results. Since we needed at least 5,000 posts to get a representative dataset, we had to find another source.

<!-- Opisać zebrany przez redditora dataset -->

Nearly 10 years ago, on July 3, 2015, Jason Baumgartner, under the nickname “u/Stuck_In_the_Matrix,” made a post in the “r/datasets” subreddit stating that he had collected all publicly available comments from Reddit, with the purpose of research [@datasets2015]. He collected about 250 GiB of data, which contains 1.7 billion posts and comments published on the platform from October 2007 to May 2015. The posts were grouped by month and year, and then saved in JSONL files^[The file format allows multiple JSON objects to be saved in a single file. One line is equivalent to one JSON document]. A day later, with the help of the community, the collection was made available as a torrent.

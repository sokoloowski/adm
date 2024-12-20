## Dataset Analysis {#sec:dataset-analysis}

The dataset contains Reddit comments, stored in JSON format. Each entry consists of 22 values that describe properties such as:

- the time of creation,
- the author,
- the author's role (e.g., moderator),
- the reply thread,
- the thematic thread,
- the content,
- the number of upvotes,
- the time of editing.

A cursory analysis reveals that some columns are not used at all: every value in the `ups` column is equal to the `score`, every value in the `downs` column is `0`, and every value in the `removal_reason` column is `null`.

Other columns provide information about:

- `parent_id` - the parent post ID,
- `created_utc` - the time when the post was added,
- `distinguished` - the author's role (e.g., moderator),
- `subreddit_id` - the subreddit identifier,
- `id` - the entry identifier,
- `archived` - whether the thread is archived,
- `link_id` - the reply thread identifier,
- `score_hidden` - whether the number of upvotes is hidden,
- `author_flair_text` - the text of the author's badge,
- `author_flair_css_class` - the CSS class for the author's badge,
- `name` - entry identifier in the `tX_<id>` format,
- `retrieved_on` - the time when the entry was retrieved,
- `edited` - whether and when the entry was edited.

This leaves the following useful columns:

- `controversiality` - whether the entry is considered controversial,
- `score` - the number of upvotes,
- `author` - the author of the entry,
- `body` - the content of the entry,
- `gilded` - the number of gold badges the author has received,
- `subreddit` - the topic or thread of discussion.

With an understanding of each column's meaning, we began the process of cleaning the dataset. We started by removing the redundant columns: `ups`, `downs`, and `removal_reason`.

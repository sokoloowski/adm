## Dataset analysis {#sec:dataset-analysis}

The dataset contains comments from Reddit, which are stored in a JSON format. Each entry contains 22 values that describe properties such as:

- the time of creation,
- the author,
- the author's distinguished function,
- the reply thread,
- the thematic thread,
- the content,
- the number of likes,
- the time of editing.

A cursory analysis shows that some columns are not used at all: every value from the `ups` column is equal to `score`, every value from the `downs` column is equal to `0`, and every value from the `removal_reason` column is equal to `null`.

Other columns include information about:

- `parent_id` - indicating the parent post,
- `created_utc` - the time when the post was added,
- `distinguished` - author function (e.g. moderator),
- `subreddit_id` - subject thread identifier,
- `id` - identifier of the entry,
- `archived` - whether the thread is archived,
- `link_id` - identifier of the reply thread,
- `score_hidden` - whether the number of likes is hidden,
- `author_flair_text` - the text of the author's badge,
- `author_flair_css_class` - CSS class of author badge,
- `name` - entry identifier in `tX_<id>` format,
- `retrieved_on` - the time when the entry was retrieved,
- `edited` - whether and when the entry was edited.

This leaves the following columns:

- `controversiality` - whether the entry is controversial,
- `score` - the number of likes,
- `author` - the author of the entry,
- `body` - the content of the entry,
- `gilded` - number of gold badges of the author,
- `subreddit` - topic thread.

With an idea of the meaning of each column, we can start cleaning the dataset. We started by removing the redundant 3 columns, that is, `ups`, `downs` and `removal_reason`.
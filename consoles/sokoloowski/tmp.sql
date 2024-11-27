SELECT count(*) FROM reddit;

CREATE DATABASE adm_backup WITH TEMPLATE adm OWNER postgres;

SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity
WHERE pg_stat_activity.datname = 'adm' AND client_addr = '10.10.10.2' AND pid <> pg_backend_pid();

SELECT DATE_TRUNC('month', created_utc) AS year_month, COUNT(id) AS row_count FROM cleared GROUP BY DATE_TRUNC('month', created_utc) ORDER BY year_month;

SELECT count(created_utc)
FROM reddit
WHERE created_utc <= '2014-12-31'
  AND length(body) > 1000;

SELECT *
INTO reddit_2011
FROM reddit
WHERE created_utc >= '2011-01-01'
  AND created_utc < '2012-01-01';

SELECT count(*)
FROM reddit_2007
WHERE body <> '[deleted]'
  AND subreddit <> 'reddit.com';

SELECT count(*)
FROM reddit_2011
WHERE downs <> 0;

SELECT *, age(state_change, query_start) AS duration, age(now(), query_start) AS from_start
FROM pg_stat_activity
WHERE datname = 'adm'
  AND application_name = 'psql';

SELECT * INTO cleared FROM reddit WHERE length(body) > 1000;

DELETE
FROM reddit_2007
WHERE body = '[deleted]';

SELECT pg_size_pretty(pg_database_size('adm')) as database_size;

-- count posts in each subreddit
SELECT subreddit, count(*) as count
FROM reddit_2009
WHERE length(body) > 100
GROUP BY subreddit
ORDER BY count DESC;

SELECT *
INTO filtered
FROM cleared
WHERE subreddit = 'politics'
    OR subreddit = 'programming'
    OR subreddit = 'science'
    OR subreddit = 'technology'
    OR subreddit = 'gaming';
# Potentially helpful queries
---

```SQL
SELECT author, COUNT(*) AS occurrence_count
FROM cleared_10
GROUP BY author
ORDER BY occurrence_count DESC;
```

```SQL
SELECT controversiality, COUNT(*) AS occurrence_count
FROM cleared_10
GROUP BY controversiality;
```
SELECT bk.book_id, bk.title, AVG(r.rating) AS avg_rating
FROM books bk, reviews r
WHERE bk.book_id = r.book_id
GROUP BY bk.book_id, bk.title
HAVING COUNT(r.rid) >= 2
ORDER BY avg_rating DESC
LIMIT 3;
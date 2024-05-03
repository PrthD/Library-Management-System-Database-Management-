SELECT bk.book_id, bk.title, bk.author, COUNT(b.bid), MAX(b.start_date)
FROM books bk LEFT OUTER JOIN borrowings b ON bk.book_id = b.book_id
WHERE bk.pyear > 2001
GROUP BY bk.book_id, bk.title, bk.author;
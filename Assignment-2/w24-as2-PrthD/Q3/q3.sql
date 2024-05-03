SELECT DISTINCT b.bid, b.member
FROM borrowings b
LEFT JOIN waitlists w ON b.book_id = w.book_id AND w.priority >= 5
WHERE (julianday(b.end_date) - julianday(b.start_date)) > 14
AND b.end_date IS NOT NULL
AND w.wid IS NULL;
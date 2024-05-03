CREATE VIEW book_info AS
SELECT bk.book_id, bk.title, 
    COUNT(r.rid) AS revcnt, 
    COALESCE(AVG(r.rating), 0.0) AS rating, 
    COALESCE(AVG(CASE WHEN strftime('%Y', r.rdate) = '2023' THEN r.rating ELSE NULL END), 0.0) AS rating23,
    (SELECT COUNT(*) FROM borrowings WHERE book_id = bk.book_id) + (SELECT COUNT(*) FROM waitlists WHERE book_id = bk.book_id) AS reqcnt
FROM books bk
LEFT JOIN reviews r ON bk.book_id = r.book_id
GROUP BY bk.book_id, bk.title;

SELECT * FROM book_info;
SELECT bk.book_id, bk.title, COUNT(b.bid) AS borrow_count
FROM books bk, borrowings b
WHERE bk.book_id = b.book_id AND bk.pyear <= 2015
GROUP BY bk.book_id, bk.title
HAVING borrow_count >= 1 AND borrow_count >= 2 * (
    SELECT COUNT(w.wid) FROM waitlists w WHERE w.book_id = bk.book_id
);
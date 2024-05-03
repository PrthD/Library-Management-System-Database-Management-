SELECT book_id, title, pyear
FROM (
    SELECT bk.book_id, bk.title, bk.pyear, RANK() OVER (ORDER BY COUNT(b.bid) DESC) AS rank
    FROM books bk
    JOIN borrowings b ON bk.book_id = b.book_id
    GROUP BY bk.book_id, bk.title, bk.pyear
) AS ranked_books
WHERE rank <= 3;
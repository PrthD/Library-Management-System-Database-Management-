SELECT DISTINCT b.member
FROM borrowings b
WHERE NOT EXISTS (
    SELECT * FROM book_info bi WHERE bi.book_id = b.book_id AND (bi.rating <= 3.5 OR bi.reqcnt <= (SELECT AVG(reqcnt) FROM book_info))
);
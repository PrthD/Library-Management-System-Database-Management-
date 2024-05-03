SELECT b.bid, b.member, b.end_date
FROM borrowings b, members m, books bk
WHERE b.member = m.email AND b.book_id = bk.book_id
AND m.faculty = 'CS' AND (LOWER(bk.author) LIKE '%john%' OR LOWER(bk.author) LIKE '%marry%');
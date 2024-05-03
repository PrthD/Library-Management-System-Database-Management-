SELECT DISTINCT m.name, m.email
FROM members m, waitlists w, borrowings b
WHERE m.email = w.member AND m.email = b.member AND w.book_id = b.book_id;
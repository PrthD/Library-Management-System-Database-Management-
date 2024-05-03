SELECT 
    members.email AS member, 
    COUNT(DISTINCT penalties.pid), 
    SUM(CASE WHEN penalties.paid_amount IS NOT NULL AND penalties.paid_amount >= penalties.amount THEN 1 ELSE 0 END),
    IFNULL(SUM(CASE WHEN penalties.paid_amount >= penalties.amount THEN penalties.paid_amount ELSE 0 END), 0)
FROM 
    members
    LEFT JOIN borrowings ON members.email = borrowings.member 
    LEFT JOIN penalties ON borrowings.bid = penalties.bid
GROUP BY 
    members.email
HAVING
    COUNT(DISTINCT penalties.pid) > 0;
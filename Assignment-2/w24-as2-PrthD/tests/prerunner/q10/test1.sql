PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE book_info(
  book_id INT,
  title TEXT,
  revcnt,
  rating,
  rating23,
  reqcnt
);
INSERT INTO book_info VALUES(1,'Book 1',0,0.0,0.0,2);
INSERT INTO book_info VALUES(2,'Book 2',2,3.5,4.0,2);
INSERT INTO book_info VALUES(3,'Book 3',1,4.0,4.0,5);
INSERT INTO book_info VALUES(4,'Book 4',0,0.0,0.0,4);
INSERT INTO book_info VALUES(5,'Book 5',0,0.0,0.0,1);
INSERT INTO book_info VALUES(6,'Book 6',0,0.0,0.0,0);
COMMIT;

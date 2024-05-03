INSERT INTO books values(1, 'Book 1', 'John', 2002);
INSERT INTO books values(2, 'Book 2', 'John', 2022);
INSERT INTO books values(3, 'Book 3', 'Marry', 2024);
INSERT INTO books values(4, 'Book 4', 'Mike', 2020);
INSERT INTO books values(5, 'Book 5', 'Rejwana', 2017);
INSERT INTO books values(6, 'Book 6', 'Marry', 2017);




INSERT INTO members values('dave@ualberta.ca', 'Dave', 1980, 'CS');
INSERT INTO members values('john@ualberta.ca', 'John', 1990, 'CS');
INSERT INTO members values('marry@ualberta.ca', 'Marry', 1995, 'CS');
INSERT INTO members values('mike@ualberta.ca', 'John', 1990, 'Math');
INSERT INTO members values('sarah@ualberta.ca', 'Sarah', 1990, 'Math');


INSERT INTO borrowings values(1, 'dave@ualberta.ca', 1, '2023-11-15', NULL);
INSERT INTO borrowings values(2, 'dave@ualberta.ca', 1, '2023-11-15', NULL);
INSERT INTO borrowings values(3, 'dave@ualberta.ca', 2, '2023-11-15', NULL);
INSERT INTO borrowings values(4, 'dave@ualberta.ca', 2, '2023-10-15', '2023-10-25');
INSERT INTO borrowings values(5, 'john@ualberta.ca', 3, '2023-10-15', '2023-10-25');
INSERT INTO borrowings values(6, 'john@ualberta.ca', 3, '2023-10-15', '2023-11-25');
INSERT INTO borrowings values(7, 'john@ualberta.ca', 3, '2023-10-15', '2023-11-25');
INSERT INTO borrowings values(8, 'john@ualberta.ca', 3, '2023-10-15', '2023-10-25');
INSERT INTO borrowings values(9, 'mike@ualberta.ca', 4, '2023-11-15', NULL);
INSERT INTO borrowings values(10, 'marry@ualberta.ca', 4, '2023-11-15', NULL);
INSERT INTO borrowings values(11, 'marry@ualberta.ca', 4, '2023-11-15', NULL);
INSERT INTO borrowings values(12, 'sarah@ualberta.ca', 5, '2023-11-15', NULL);



INSERT INTO waitlists values(1, 'dave@ualberta.ca', 3, 3, NULL);
INSERT INTO waitlists values(2, 'marry@ualberta.ca', 4, 6, '2023-12-15');



INSERT INTO penalties values(1, 1, 50, NULL);
INSERT INTO penalties values(2, 2, 50, 20);
INSERT INTO penalties values(3, 1, 50, 50);
INSERT INTO penalties values(4, 3, 60, 60);
INSERT INTO penalties values(5, 5, 90, 90);
INSERT INTO penalties values(6, 10, 50, NULL);
INSERT INTO penalties values(7, 12, 70, 70);


INSERT INTO reviews values(1, 2, 'dave@ualberta.ca', 4, '','2023-12-15');
INSERT INTO reviews values(2, 2, 'marry@ualberta.ca', 3, '','2022-12-15');
INSERT INTO reviews values(3, 3, 'dave@ualberta.ca', 4, '','2023-08-15');
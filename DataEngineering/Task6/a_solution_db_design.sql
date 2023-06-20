/*
Ticket Table:
    ticket_id (Primary Key)
    guest_name
    hotel_name

Comment Table:
    comment_id (Primary Key)
    ticket_id (Foreign Key referencing the Ticket table)
    author_id (Foreign Key referencing the Author table)
    comment_body
    creation_time

Author Table:
    author_id (Primary Key)
    author_name
    email_address
*/

CREATE TABLE Ticket (
  ticket_id INT PRIMARY KEY,
  guest_name VARCHAR(255),
  hotel_name VARCHAR(255)
);

CREATE TABLE Comment (
  comment_id INT PRIMARY KEY,
  ticket_id INT,
  author_id INT,
  comment_body TEXT,
  creation_time DATETIME,
  FOREIGN KEY (ticket_id) REFERENCES Ticket(ticket_id),
  FOREIGN KEY (author_id) REFERENCES Author(author_id)
);

CREATE TABLE Author (
  author_id INT PRIMARY KEY,
  author_name VARCHAR(255),
  email_address VARCHAR(255)
);


-- =========================================================
SELECT
    c.comment_id,
    c.comment_body,
    c.creation_time,
    a.author_name
FROM
    Comment c
    INNER JOIN Ticket t ON c.ticket_id = t.ticket_id
    INNER JOIN Author a ON c.author_id = a.author_id
WHERE
    t.ticket_id = <your_ticket_id>;

/*
Corresponding query in Django ORM

comments = Comment.objects
                .filter(ticket_id=<your_ticket_id>)
                .select_related('author')
                .values('id', 'comment_body', 'creation_time', 'author__author_name')
*/

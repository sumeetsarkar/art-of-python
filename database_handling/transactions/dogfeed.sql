INSERT INTO users (id, username, fname, lname, pin) VALUES
    (1, 'john', 'John', 'Rambo', 1234),
    (2, 'alice', 'Alice', 'Wonderland', 8890),
    (3, 'merkel', 'Merkel', 'Root', 5639);

INSERT INTO accounts (type, owner_id, balance) VALUES
    ('checking', 1, 250.0),
    ('savings', 1, 250.00),
    ('checking', 2, 250.0),
    ('savings', 2, 250.00),
    ('checking', 3, 250.0),
    ('savings', 3, 250.00);

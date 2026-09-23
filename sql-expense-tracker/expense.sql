 CREATE TABLE expenses (
    id INTEGER PRIMARY KEY,
    date TEXT,
    category TEXT,
    amount INTEGER,
    description TEXT
);

INSERT INTO expenses VALUES (1, '2026-09-23', 'Food', 150, 'Lunch');
INSERT INTO expenses VALUES (2, '2026-09-23', 'Travel', 50, 'Bus');

SELECT * FROM expenses;
SELECT category, SUM(amount) as total FROM expenses GROUP BY category;
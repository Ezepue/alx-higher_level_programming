-- Creates the table unique_id on your MySQL server.
-- Default id is 1
-- id must be unique
CREATE TABLE IF NOT EXISTS
unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);

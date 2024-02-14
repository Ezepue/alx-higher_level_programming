-- Creates the table force_name on your MySQL server.
-- name can not be NULL
CREATE TABLE IF NOT EXISTS
force_name (
	id INT,
	name VARCHAR(256) NOT NULL
);

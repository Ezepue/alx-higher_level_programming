-- Create a new user
CREATE USER 'wondahs'@'localhost' IDENTIFIED BY 'wondahs';

-- Grant all privileges on all databases to the new user
GRANT ALL PRIVILEGES ON *.* TO 'wondahs'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

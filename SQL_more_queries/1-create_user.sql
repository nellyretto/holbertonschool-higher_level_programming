-- creating a user with all permissions
CREATE IF NOT EXISTS USER 'user_0d_1'@localhost;
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2. 
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Crée l'utilisateur 'user_0d_2' s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- Modifie le mot de passe de l'utilisateur 'user_0d_1' pour le mettre à 'user_0d_1_pwd'
ALTER USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Accorde à 'user_0d_2' tous les privilèges sur toutes les bases de données et toutes les tables
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Actualise les privilèges pour s'assurer que les modifications prennent effet immédiatement
FLUSH PRIVILEGES;

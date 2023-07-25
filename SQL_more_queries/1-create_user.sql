-- Crée l'utilisateur 'user_0d_1' s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';

-- Modifie le mot de passe de l'utilisateur 'user_0d_1' pour le mettre à 'user_0d_1_pwd'
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorde à 'user_0d_1' tous les privilèges sur toutes les bases de données et toutes les tables, avec la possibilité de donner ces privilèges à d'autres utilisateurs
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Actualise les privilèges pour s'assurer que les modifications prennent effet immédiatement
FLUSH PRIVILEGES;

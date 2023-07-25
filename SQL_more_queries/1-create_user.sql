-- Crée l'utilisateur 'user_0d_1' s'il n'existe pas déjà
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';

-- Modifie le mot de passe de l'utilisateur 'user_0d_1' pour le mettre à 'user_0d_1_pwd'
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';


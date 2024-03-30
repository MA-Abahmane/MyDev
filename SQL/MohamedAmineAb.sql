--/ MOHAMED AMINE AB. \
--/   29/03/2024   \

-- | Examen de Fin de Module, Formation Initiale |



-- I) : Partie Théorique
-- 1) donnez la syntaxe de la requête de sélection avec les différentes clauses:

--  Select * from <table> where <condition> group by <column> having <condition> order by <column>


-- II) : Partie Pratique

-- Service (+Num_serv+, Nom_serv, Date_creation)
-- Employe (+Matricule+, Nom, Prenom, DateNaissance, Adresse, Salaire,Grade, Num_serv#)
-- Projet (+Num_prj+, Nom_prj, Lieu, nbr_limite_taches,Num_serv#)
-- Tache (+Num_tach+, Nom_tache, date_debut, date_fin, cout, Num_prj#)
-- Travaille (Matricule#,Num_tache#, Nombre_heure)


--- Créer la base de données (10pts):
-- 1. donner le script permettant de créer la base de données gestion_projet avec le schéma
--    relationne précédant.

CREATE DATABASE IF NOT EXISTS gestion_projet;
USE gestion_projet;


CREATE TABLE IF NOT EXISTS `Service` (
    Num_serv        INT auto_increment PRIMARY KEY,
    Nom_serv        VARCHAR(70),
    Date_creation   DATE
);

CREATE TABLE IF NOT EXISTS `Employe` (
    Matricule       INT auto_increment PRIMARY KEY,
    Nom             VARCHAR(70),
    Prenom          VARCHAR(70),
    DateNaissance   DATE,
    Adresse         VARCHAR(120),
    Salaire         INT,
    Grade           VARCHAR(50),
    Num_serv        INT,

    CONSTRAINT employeService FOREIGN KEY(Num_serv) REFERENCES `Service`(Num_serv)
);

CREATE TABLE IF NOT EXISTS `Projet` (
    Num_prj             INT auto_increment PRIMARY KEY,
    Nom_prj             VARCHAR(100),
    Lieu                VARCHAR(120),
    nbr_limite_taches   INT,
    Num_serv            INT,

    CONSTRAINT projetService FOREIGN KEY(Num_serv) REFERENCES `Service`(Num_serv)
);

CREATE TABLE IF NOT EXISTS `Tache` (
    Num_tach    INT auto_increment PRIMARY KEY,
    Nom_tache   VARCHAR(70),
    date_debut  DATE,
    date_fin    DATE,
    cout        INT,
    Num_prj     INT,

    CONSTRAINT CK_Tache_duree CHECK (date_fin - date_debut >= 3),
    CONSTRAINT CK_Tache_cout CHECK (cout >= (date_fin - date_debut) * 1000),
    CONSTRAINT tacheProjet FOREIGN KEY(Num_prj) REFERENCES Projet(Num_prj)
);

CREATE TABLE IF NOT EXISTS `Travaille` (
    Matricule       INT,
    Num_tache       INT,
    Nombre_heure    INT,

    CONSTRAINT travailleEmploye FOREIGN KEY(Matricule) REFERENCES Employe(Matricule),
    CONSTRAINT travailleTache FOREIGN KEY(Num_tache) REFERENCES Tache(Num_tach)
);


-- 2. ajouter le champ calculé âge à la table Employé.
SET SQL_SAFE_UPDATES = 0;

ALTER TABLE `Employe` ADD COLUMN age INT;
UPDATE `Employe` 
 SET age = YEAR(CURDATE()) - YEAR(DateNaissance)
WHERE age IS NULL;

ALTER TABLE `Employe` ADD CONSTRAINT CK_Employe_dateNaissance CHECK (age > 18);



--- B. Créer les requêtes de sélection

-- 1. afficher les employés dont le nom commence avec « El » et ne se termine pas par une lettre entre a et
--   f, trier la liste par date de naissance.
SELECT * 
FROM `Employe` 
WHERE Nom LIKE `El%`;

-- 2. afficher les noms des taches (en majuscule) qui prendrons fin ce mois ci.
SELECT UPPER(Nom_tache) 
FROM `Tache` 
WHERE YEAR(date_fin) = YEAR(CURDATE) 
AND MONTH(date_fin) = MONTH(CURDATE);

-- 3. compter le nombre de grades différents de l’entreprise.
SELECT COUNT(DISTINCT Grade) 
FROM `Employe`;

-- 4. afficher les employés qu’ont participé à un projet affecter à un service différent où il travaille.
SELECT DISTINCT e.Matricule, e.Nom
FROM Employe e
JOIN Travaille t ON e.Matricule = t.Matricule

-- 5. les projets avec une tache de durée inférieure à 30jours et une autre supérieure à 60jours
--   Durée d’une tache = Date de Fin – date de début
SELECT * FROM `Tache` WHERE  30 > DATEDIFF(date_fin, date_debut);
SELECT * FROM `Tache` WHERE  60 < DATEDIFF(date_fin, date_debut);

-- 6. afficher la masse horaire travaillée cette année (travaille débuter et terminer cette année) par projet.
--   Masse horaire = somme (nombre_heure)
SELECT p.Nom_prj SUM(tw.Nombre_heure)
FROM `Travaille` tw 
JOIN `Tache`  t ON tw.Num_tach = t.Num_tach
JOIN `Projet` p ON t.Num_prj = p.Num_prj
WHERE YEAR(t.date_debut) = YEAR(CURDATE())
AND YEAR(t.date_fin) = YEAR(CURDATE())
GROUP BY p.Num_prj;


-- 7. afficher le matricule et le nom des employés qui ont participé à la réalisation de plusieurs projets.
SELECT e.Matricule, e.Nom
FROM Employe e
JOIN Travaille tw ON e.Matricule = tw.Matricule
GROUP BY e.Matricule, e.Nom
HAVING COUNT(DISTINCT tw.Num_prj) > 1;

-- 8. afficher le matricule, le nom, la date d’anniversaire et l’adresse des employés qui vont fêter leur
--   anniversaire la semaine prochaine.
SELECT Matricule, Nom, DateNaissance, Adresse
FROM Employe
WHERE WEEK(DateNaissance, 1) = WEEK(CURDATE(), 1) + 1;

-- 9. afficher le(s) projet(s) qui se composent du plus grand nombre de taches.
SELECT p.*
FROM Projet p
JOIN (
 SELECT Num_prj, COUNT(*) AS nb_taches
 FROM Tache
 GROUP BY Num_prj
 ORDER BY COUNT(*) DESC
 LIMIT 1
) AS max_taches ON p.Num_prj = max_taches.Num_prj;

-- 10. afficher la durée de réalisation par projet :
--   La durée de réalisation d’un projet = la date de fin de la dernière tache de ce projet – la date de début
--   de la première tache du projet (utiliser Min et Max).
SELECT p.Nom_prj,
       DATEDIFF(MAX(t.date_fin), MIN(t.date_debut)) AS Duree_realisation
FROM Projet p
JOIN Tache t ON p.Num_prj = t.Num_prj
GROUP BY p.Num_prj, p.Nom_prj;



--- C. Créer les requêtes de mise à jour (3pts):

-- 1. modifier les salaires des employés selon la règle suivante (1pt5):
-- sans modification pour les employés âgés de moins de 58 ans,
-- augmentation de 0.5% pour les employés âgés entre 58 et 60 ans,
-- augmentation de 5% pour les employés âgés de plus que 60 ans.
UPDATE Employe
SET Salaire = CASE
 WHEN YEAR(CURDATE()) - YEAR(DateNaissance) < 58 THEN Salaire
 WHEN YEAR(CURDATE()) - YEAR(DateNaissance) BETWEEN 58 AND 60 THEN Salaire * 1.005
 ELSE Salaire * 1.05
END;

-- 2. supprimer les taches non réalisées (une tache non réalisée est une tache dont la date de fin est
-- dépassée sans qu’elle contienne un travail) (1pt5).
DELETE FROM Tache
WHERE date_fin < CURDATE()
AND Num_tach NOT IN (
 SELECT Num_tache
 FROM Travaille
);

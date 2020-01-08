-- badTaco

DROP TABLE IF EXISTS badTaco;
CREATE TABLE badTaco (
  id INTEGER PRIMARY KEY,
  shell VARCHAR(20),
  meat VARCHAR(20),
  topping VARCHAR(100),
  price DOUBLE
);

INSERT INTO badTaco VALUES(null, 'hard', 'beef', 'tomatoes, guacamole', 1);
INSERT INTO badTaco VALUES(null, 'soft', 'chicken', 'tomato and lettuce', 2.5);
INSERT INTO badTaco VALUES(null, 'corn', 'chiken', 'everything', 3.0);

-- SELECT * FROM badTaco;


DROP TABLE IF EXISTS taco;
CREATE TABLE taco (
  id INTEGER PRIMARY KEY,
  name VARCHAR(20),
  shellID INTEGER,
  price DOUBLE
);

INSERT INTO taco VALUES(null, 'beast', 1, 1);
INSERT INTO taco VALUES(null, 'yummy', 2, 1.5);
INSERT INTO taco VALUES(null, 'king', 2, 2.5);

-- SELECT * FROM taco;



DROP TABLE IF EXISTS shell;
CREATE TABLE shell (
  id INTEGER PRIMARY KEY,
  name VARCHAR(20)
);

INSERT INTO shell VALUES (null, 'hard');
INSERT INTO shell VALUES (null, 'soft');

-- SELECT * FROM shell;

-- SELECT * FROM shell, taco;

/*
SELECT
  taco.name as 'name',
  taco.shellID as 't.shellID',
  shell.id as 'shell.id',
  shell.name as 'shell'
FROM
  shell, taco;
  
SELECT
  taco.name AS 'name',
  shell.name AS 'shell'
FROM
  taco, shell
WHERE
  taco.shellID = shell.id;
*/

DROP VIEW IF EXISTS tacoShellView;
CREATE VIEW tacoShellView AS
  SELECT
    taco.name AS 'name',
    shell.name AS 'shell',
	taco.price AS 'price'
  FROM
    taco, shell
  WHERE
    taco.shellID = shell.id;

-- SELECT * from tacoShellView;

DROP TABLE IF EXISTS topping;
CREATE TABLE topping (
  id INTEGER PRIMARY KEY,
  name VARCHAR(20)
);

INSERT INTO topping VALUES(null, 'lettuce');
INSERT INTO topping VALUES(null, 'tomatoes');
INSERT INTO topping VALUES(null, 'guacamole');
INSERT INTO topping VALUES(null, 'cheese');
INSERT INTO topping VALUES(null, 'salsa');
INSERT INTO topping VALUES(null, 'sour cream');

-- SELECT * FROM topping;

DROP TABLE IF EXISTS taco_topping;
CREATE TABLE taco_topping (
  id INTEGER PRIMARY KEY,
  tacoID INTEGER,
  toppingID INTEGER
);

INSERT INTO taco_topping VALUES(null, 1, 1);
INSERT INTO taco_topping VALUES(null, 1, 2);
INSERT INTO taco_topping VALUES(null, 1, 3);
INSERT INTO taco_topping VALUES(null, 2, 4);
INSERT INTO taco_topping VALUES(null, 2, 5);
INSERT INTO taco_topping VALUES(null, 2, 6);
INSERT INTO taco_topping VALUES(null, 3, 1);
INSERT INTO taco_topping VALUES(null, 3, 2);
INSERT INTO taco_topping VALUES(null, 3, 3);
INSERT INTO taco_topping VALUES(null, 3, 4);
INSERT INTO taco_topping VALUES(null, 3, 5);
INSERT INTO taco_topping VALUES(null, 3, 6);

-- SELECT * FROM taco_topping;

DROP VIEW IF EXISTS toppingView;

CREATE VIEW toppingView AS
  SELECT
    taco.name AS 'taco',
    topping.name AS 'topping'
  FROM
    taco, topping, taco_topping
  WHERE
    taco.id = taco_topping.tacoID
  AND
    topping.id = taco_topping.toppingID;
	
-- SELECT * from toppingView;

SELECT * FROM tacoShellView WHERE name = 'yummy';
SELECT topping from toppingView WHERE taco = 'yummy';

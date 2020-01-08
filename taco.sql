DROP TABLE IF EXISTS taco;
CREATE TABLE taco (
  ID INTEGER PRIMARY KEY,
  shell VARCHAR(20),
  meat VARCHAR(20),
  toppings VARCHAR(20),
  price FLOAT
);

INSERT INTO taco VALUES(null, 'soft', 'chicken', 'lettuce', 1);
INSERT INTO taco VALUES(null, 'hard', 'meat', 'cheese', 1);
INSERT INTO taco VALUES(null, 'corn', 'steak', 'cheese, lettuce', 3);

SELECT * FROM taco;

UPDATE taco SET shell = 'flour' WHERE ID = 1;
SELECT * FROM taco;

DELETE FROM taco WHERE id = 2;
SELECT * FROM taco;

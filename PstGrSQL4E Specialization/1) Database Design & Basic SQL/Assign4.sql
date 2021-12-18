 CREATE TABLE make (
     id SERIAL,
     name VARCHAR(128) UNIQUE,
     PRIMARY KEY(id)
 );

 CREATE TABLE model (
   id SERIAL,
   name VARCHAR(128),
   make_id INTEGER REFERENCES make(id) ON DELETE CASCADE,
   PRIMARY KEY(id)
 );

 CREATE TABLE member (
  make_id INTEGER REFERENCES make(id) ON DELETE CASCADE,
  model_id INTEGER REFERENCES model(id) ON DELETE CASCADE,
  PRIMARY KEY (make_id, model_id)
 );

INSERT INTO make (name) VALUES ('Mercedes-Benz');
INSERT INTO make (name) VALUES ('Volvo');
INSERT INTO model (name) VALUES ('AMG SL65');
INSERT INTO model (name) VALUES ('AMG SLC43');
INSERT INTO model (name) VALUES ('AMG SLK55');
INSERT INTO model (name) VALUES ('S60');
INSERT INTO model (name) VALUES ('S60 AWD');


INSERT INTO model (name, make_id) VALUES ('AMG SL65', 1);
INSERT INTO model (name, make_id) VALUES ('AMG SLC43', 1);
INSERT INTO model (name, make_id) VALUES ('AMG SLK55', 1);
INSERT INTO model (name, make_id) VALUES ('S60', 2);
INSERT INTO model (name, make_id) VALUES ('S60 AWD', 2);


INSERT INTO member (make_id, model_id) VALUES (1, 1);
INSERT INTO member (make_id, model_id) VALUES (1, 2);
INSERT INTO member (make_id, model_id) VALUES (1, 3);
INSERT INTO member (make_id, model_id) VALUES (2, 4);
INSERT INTO member (make_id, model_id) VALUES (2, 5);

CREATE TABLE track_raw (
  title TEXT,
  artist TEXT,
  album TEXT,
  count INTEGER,
  rating INTEGER,
  len INTEGER
);

\copy track_raw(title,artist,album,count,rating,len) FROM 'library.csv' WITH DELIMITER ',' CSV;

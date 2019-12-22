.read fa19data.sql

CREATE TABLE obedience AS
  SELECT seven, instructor FROM students;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 2 ORDER BY smallest LIMIT 20;

CREATE TABLE matchmaker AS
  SELECT s1.pet,s1.song,s1.color,s2.color FROM students as s1, students as s2
         WHERE s1.time < s2.time and s1.pet=s2.pet and s1.song=s2.song;

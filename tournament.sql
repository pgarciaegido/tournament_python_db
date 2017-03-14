-- Table definitions for the tournament project.
CREATE DATABASE tournament;

-- Creates Players table
CREATE TABLE Players (
  name text,
  player_id serial PRIMARY KEY
);

-- Creates Matches table
CREATE TABLE Matches (
  winner int REFERENCES Players(player_id),
  loser int REFERENCES Players(player_id),
  match_id serial PRIMARY KEY
);

-- Creates Standings view
CREATE VIEW standings AS
SELECT p.player_id, p.name,
  (SELECT count(m.winner) FROM Matches as m WHERE p.player_id = m.winner) AS won,
  (SELECT count(m.match_id) FROM Matches as m WHERE p.player_id = m.winner OR p.player_id = m.loser) AS matches
FROM players AS p
ORDER BY won DESC, matches DESC;

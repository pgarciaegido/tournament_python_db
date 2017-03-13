-- Table definitions for the tournament project.
CREATE DATABASE tournament;

-- Creates Players table
CREATE TABLE players (
  name text,
  id serial primary key
);

-- Creates Matches table
CREATE TABLE matches (
  player1 int references players(id),
  player2 int references players(id),
  winner int references players(id),
  match_id serial primary key
)

-- Creates Results table
CREATE TABLE results (
  match_id int references matches,
  winner int references players(id),
  results_id serial primary key
)

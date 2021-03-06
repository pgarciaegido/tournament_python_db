#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    q = "DELETE FROM matches"

    conn = connect()
    c = conn.cursor()
    c.execute(q)
    conn.commit()
    conn.close()

    print('Matches deleted succesfully')


def deletePlayers():
    """Remove all the player records from the database."""

    q = "DELETE FROM players"

    conn = connect()
    c = conn.cursor()
    c.execute(q)
    conn.commit()
    conn.close()

    print('Players deleted succesfully')


def countPlayers():
    """Returns the number of players currently registered."""
    q = "SELECT COUNT (*) FROM players"

    conn = connect()
    c = conn.cursor()
    c.execute(q)
    num = c.fetchone()
    conn.close()

    print('There are %s players registered' % num)
    # It is a tuple
    return num[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    q = "INSERT INTO players VALUES (%s)"

    conn = connect()
    c = conn.cursor()
    c.execute(q, (name,))
    conn.commit()
    conn.close()

    print('New player %s added successfully' % name)


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    q = "SELECT * FROM standings"

    conn = connect()
    c = conn.cursor()
    c.execute(q)
    r = c.fetchall()
    conn.close()

    return r


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    q = "INSERT INTO matches VALUES (%s, %s)"

    conn = connect()
    c = conn.cursor()
    c.execute(q, (winner, loser))
    conn.commit()
    conn.close()

    print('New match recorded between %s and %s. The winner was %s'
          % (winner, loser, winner))


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    a = playerStandings()
    next_round = []
    for x in range(0, len(a), 2):
        pair = (a[x][0], a[x][1], a[x+1][0], a[x+1][1])
        next_round.append(pair)
    return next_round

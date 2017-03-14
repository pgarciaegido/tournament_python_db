# Swiss Tournament. SQL and Python.

Little program to create a game tournament, keep track of results and match opponents the [Swiss Way](https://en.wikipedia.org/wiki/Swiss-system_tournament).

## Instalation
To make the program run, you need to have a SQL DB running and Python. I've used a Virtual Machine thanks to Vagrant.

## Usage
First, run the _tournament.sql_ file in order to create the db and the necesary tables and views.

_tournament.py_ is where all the functions that run the program are hosted. The description of each function is detailed on the docs.

```Python
import tournament
tournament.countPlayers.__doc__

>>Returns the number of players currently registered.
```

You can try that works running tournament_test.py.

## Contributing
If you fancy, you can make a pull request if you want to improve the program. Any possible issues, you can report them [here](https://github.com/pgarciaegido/tournament_python_db/issues).

## Contact
You can contact me on pgarciaegido@gmail.com

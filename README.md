# Unix ASCII games

[![Build Status](https://travis-ci.org/ligurio/ttygames.svg?branch=master)](https://travis-ci.org/ligurio/ttygames)

This is a source of [https://bronevichok.ru/ttygames/](https://bronevichok.ru/ttygames/).
Feel free to submit pull requests to add new games and improve information about
those already in the database.

## How to contribute

Check `games.yaml` out. All information is inside, and you should more or less
understand what's going on by reading it. Sorting is alphabetical.

Simplest way to contribute: edit [games.yaml](/games.yaml), and then
your changes will be submitted as a pull request.

Use this template:

```
- name: hangman
  url: http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/man6/hangman.6?query=hangman&sec=6&arch=i386
  info: computer version of the game hangman
  screencast:
  play:
```

- `name`: Name of the game
- `url`: URL of main page
- `info`: free text with game description
- `screencast`: link to screencast (for example on asciinema)
- `play`: server hostname where game is available via telnet or ssh

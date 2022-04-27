#!/usr/bin/env python

import yaml
import re
from urllib.parse import urlparse

stream = open("games.yaml", "r")
ttygames = yaml.load(stream, Loader=yaml.FullLoader)
for entry in ttygames:
    name = str(entry['name'])
    header = "### %s" % name.strip()

    screencast = ""
    if 'screencast' in entry and entry['screencast']:
        u = urlparse(entry['screencast'])
        if u.hostname == 'asciinema.org':
            m = re.match(
                'https://asciinema.org/a/([0-9A-z]+)', entry['screencast'])
            if m:
                id = m.group(1)
                screencast = (
                    "[![asciicast](https://asciinema.org/a/%s.svg)](https://asciinema.org/a/%s)" % (id, id))
        else:
            header = header + " [Screencast](%s)" % entry['screencast']

    print(header, "\n")
    if screencast:
        print(screencast, "\n")

    if 'info' in entry:
        print("%s" % entry['info'])

    if 'url' in entry:
        print("\nWebsite: %s" % entry['url'])

    if 'wikipedia' in entry:
        print("\nWikipedia: %s" % entry['wikipedia'])

    if 'play' in entry:
        print("\n**Play**: ```%s```" % entry['play'])

    print()

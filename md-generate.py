#!/usr/bin/env python3

import yaml
import re
from urllib.parse import urlparse

stream = open("games.yaml", "r")
ttygames = yaml.load(stream, Loader=yaml.FullLoader)
for entry in ttygames:
    if 'url' in entry:
        header = "### [%s](%s)" % (entry['name'], entry['url'])
    else:
        header = "### %s" % entry['name']

    screencast = ""
    if 'screencast' in entry and entry['screencast']:
        u = urlparse(entry['screencast'])
        if u.hostname == 'asciinema.org':
            m = re.match(
                'https://asciinema.org/a/([0-9]+)', entry['screencast'])
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
        print("%s\n" % entry['info'])

    if 'wikipedia' in entry:
        print("See also [Wikipedia](%s).\n" % entry['wikipedia'])

    if 'play' in entry:
        print("\n**Play**: ```%s```\n" % entry['play'])

    print()

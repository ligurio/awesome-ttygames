#!/usr/bin/env python

import yaml
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


stream = open("games.yaml", "r")
ttygames = yaml.load(stream)
for entry in ttygames:

    if 'url' in entry:
        header = "### [%s](%s)" % (entry['name'], entry['url'])
    else:
        header = "### %s" % entry['name']

    if 'screencast' in entry:
        header = header + " [Screencast](%s)" % entry['screencast']

    print header, "\n"

    if 'info' in entry:
        print("%s\n" % entry['info'])

    if 'wikipedia' in entry:
        print("See also [Wikipedia](%s).\n" % entry['wikipedia'])

    if 'play' in entry:
        print("\n**Play**: ```%s```\n" % entry['play'])

    print

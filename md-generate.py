#!/usr/bin/env python

import os
import re
from urllib.parse import urlparse
import yaml

ASCIINEMA_TEMPLATE = "[![asciicast](https://asciinema.org/a/{}.svg)](https://asciinema.org/a/{})"
YOUTUBE_TEMPLATE = "[![IMAGE ALT TEXT](http://img.youtube.com/vi/{}/0.jpg)](http://www.youtube.com/watch?v={} \"Screencast\")"
YOUTUBE_ID_RE = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})'

def youtube_video_id(youtube_url):
    regex = re.compile(YOUTUBE_ID_RE)
    match = regex.match(youtube_url)
    return match.group('id')

stream = open("games.yaml", "r")
ttygames = yaml.load(stream, Loader=yaml.FullLoader)
for entry in ttygames:
    name = str(entry['name']).strip()
    header = "### {}".format(name)

    screencast = ""
    if 'screencast' in entry and entry['screencast']:
        u = urlparse(entry['screencast'])
        if u.hostname == 'asciinema.org':
            asciinema_id_re = re.match(
                'https://asciinema.org/a/([0-9A-z]+)', entry['screencast'])
            if asciinema_id_re:
                asciinema_id = asciinema_id_re.group(1)
                screencast = ASCIINEMA_TEMPLATE.format(asciinema_id, asciinema_id)
        elif u.hostname == 'www.youtube.com':
            youtube_id = youtube_video_id(entry['screencast'])
            if youtube_id:
                screencast = YOUTUBE_TEMPLATE.format(youtube_id, youtube_id)
        elif u.path is not None and screencast is not None:
            name, ext = os.path.splitext(u.path)
            if ext == ".gif":
                screencast = "![Alt Text]({})".format(entry['screencast'])
        else:
            header = "{} [Screencast]({})".format(header, entry['screencast'])

    print(header + "\n")
    if screencast:
        print("{}\n".format(screencast))

    if 'info' in entry:
        print(entry['info'])

    if 'url' in entry:
        print("\nWebsite: {}".format(entry['url']))

    if 'wikipedia' in entry:
        print("\nWikipedia: {}".format(entry['wikipedia']))

    if 'play' in entry:
        print("\n**Play**: `{}`".format(entry['play']))

    print()

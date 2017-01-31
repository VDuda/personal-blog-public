#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Vlad Duda'
SITENAME = 'My Blog'
SITEURL = 'http://Vlad-Duda.me'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/BigBostonGuy'),
          ('linkedin', 'http://www.linkedin.com/in/vduda'),
          ('github', 'https://github.com/VDuda'),
          ('stackoverflow', 'http://stackoverflow.com/users/3757609/vidalia', 'stack-overflow'))

DEFAULT_PAGINATION = 10

# Article settings
SUMMARY_MAX_LENGTH = 50
SLUGIFY_SOURCE = 'title'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = "pelican-themes/pelican-bootstrap3"

# Plugins
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ['i18n_subsites']

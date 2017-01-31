# Personal Pelican Based Static Site

## INSTALLATION
Pelican is a prerequisite for generating this site. 

### Packages
```
pip install pelican python-gettext jinja2
```

### Themes
I use the default pelican repo for managing themes. For usability sakes, I have not included this directory in the git repo and have explicitly ignored it in gitignore.
```
git clone https://github.com/getpelican/pelican-themes.git
# edit pelicanconf.py
```

### Plugins
```
https://github.com/getpelican/pelican-plugins
# edit pelicanconf.py
```

## USAGE
We deploy any new articles and edits up to the branch `gh-pages` on this repo. 

```
# perform edits
make github # Deploys to github branch gh-pages
```
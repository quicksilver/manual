# Quicksilver Manual Source #

These are the source files for the Quicksilver user manual. Use [MkDocs][] to build a site from these files.

## Working Locally ##

Editing this manual locally is relatively easy. You can just edit the files like you would any other Markdown without installing anything.

You can optionally install MkDocs to see a live preview of the site as you work. To use the latest release of Python and avoid installing packages system-wide, I recommend installing Python from [Homebrew][] and creating a virtual environment.

    $ brew install python3
    $ pip3 install virtualenv
    $ cd <your directory for projects>
    $ git clone <your fork of this repo>
    $ cd manual
    $ virtualenv -p python3 venv
    $ venv/bin/pip install -r requirements.txt
    $ venv/bin/mkdocs serve

This will run a web server at <http://localhost:8000/>. The site should reload automatically whenever you update content or configuration.

## Updating the Live Manual ##

The manual repository has been cloned into `/data/manual`.

MkDocs has been installed into a virtual environment in `/data/manual/venv`.

Publishing the latest version should be as simple as

    $ cd /data/manaul
    $ git pull
    $ venv/bin/mkdocs build

[MkDocs]: http://www.mkdocs.org/
[Homebrew]: https://brew.sh/

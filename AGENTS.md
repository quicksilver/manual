# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the source repository for the [Quicksilver User Manual](https://qsapp.com/manual/), a documentation site for the Quicksilver macOS application. It uses [MkDocs](https://www.mkdocs.org/) with the Material theme to build a static site from Markdown files.

## Development Commands

```bash
# Setup (one-time)
python3 -m venv venv
venv/bin/pip install -r requirements.txt

# Generate plugin documentation from qsapp.com API
venv/bin/python plugindocs.py
venv/bin/python plugindocs.py --fresh   # ignore local cache
venv/bin/python plugindocs.py --clear   # remove old plugin docs first

# Serve locally with live reload at http://localhost:8000/
venv/bin/mkdocs serve

# Build static site into site/
venv/bin/mkdocs build

# Build with PDF generation
BUILD_PDF=1 venv/bin/mkdocs build
```

## Architecture

### Content Structure

All manual content lives in `docs/` as Markdown files, organized into sections:

- `docs/getting-started/` — Installation, concepts, invoking Quicksilver
- `docs/features/` — Feature guides (files, contacts, mail, triggers, etc.)
- `docs/plugins/` — Auto-generated plugin documentation (see below)
- `docs/preferences/` — Preference pane walkthroughs
- `docs/appendix/` — FAQ, troubleshooting, style guide

Navigation structure is defined explicitly in `mkdocs.yml` under the `nav` key.

### Plugin Documentation Pipeline

Plugin docs are **auto-generated** — do not edit files in `docs/plugins/` directly (except `index.md`, which is manually maintained). The `.gitignore` excludes `docs/plugins/*` except `index.md`.

The pipeline works as follows:

1. `plugindocs.py` queries the qsapp.com API for plugin info across all `SUPPORTED_OS_VERSIONS`
2. Plugin HTML descriptions are transformed via XSLT and converted to Markdown with `html2text`
3. Generated `.md` files are written to `docs/plugins/`
4. The script updates the `nav` → `Plugins` section in `mkdocs.yml` and writes `manifest.json` for client-side plugin lookup
5. Cached API responses are stored in `_plugins/` (also gitignored)

When OS support changes, update `SUPPORTED_OS_VERSIONS` in `plugindocs.py`.

### Deployment

Pushes to `main` trigger a GitHub Actions workflow (`.github/workflows/deploy.yml`) that builds the site (with PDF) and deploys via rsync to the production server.

## Style Guide (Key Points)

The full style guide is in `docs/appendix/Style Guide.md`. Key formatting rules:

- Wrap each physical key in `<kbd>` tags: `<kbd>⌘</kbd><kbd>A</kbd>`, not `<kbd>⌘A</kbd>`
- Use unicode symbols for modifier keys in correct order: ⌃ ⌥ ⇧ ⌘
- Action names in **bold**
- File names, extensions, and code in backticks
- Display commands as: Direct Object ⇥ **Action** ⇥ Indirect Object
- Use bidirectional (smart/curly) quotes in prose
- Indent list items by two spaces before the marker
- Images go in `docs/images/` and should use the Bezel interface with default colors

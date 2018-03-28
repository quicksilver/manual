#!/usr/bin/env python3
"""
Import Documentation for Quicksilver plugins.

This script fetches plugin documentation from their respective repositories and
inserts them into the *plugins/* directory in *docs/*.
"""
import json
import logging
from os import makedirs
from pathlib import Path
import plistlib
import re
from shutil import copyfile
from subprocess import run
from urllib.request import urlopen

import yaml


CACHE_DIR = Path('_plugins')
CONFIG_PATH = Path(__file__).parent / 'mkdocs.yml'
DOCS_DIR = Path(__file__).parent / 'docs'
REPOS_URL = 'https://api.github.com/orgs/quicksilver/repos'


log = logging.getLogger(__name__)


def get_plugin_repositories(repos_url=REPOS_URL):
    """Get list of plugin repositories from github."""
    url = repos_url
    while True:
        log.debug('Querying %s for plugin repositories', url)
        with urlopen(url) as response:
            for repo in json.load(response):
                name = repo['name']
                if name.endswith('-qsplugin') and '-unused' not in name:
                    yield repo

            links = response.headers.get('Link')
            nextlink = re.search(r'<([^>]+)>; rel="next"', links)
            if nextlink:
                url = nextlink.group(1)
            else:
                break


def cache_code(repo_name, repo_url, cache_dir=CACHE_DIR):
    """Clone/update repo in cache_dir."""
    dest = cache_dir / repo_name
    if dest.is_dir():
        log.debug('Updating %s cache', repo_name)
        run(['git', 'pull', '--ff-only'], cwd=dest, check=True)
    else:
        log.debug('Caching %s from %s', repo_name, repo_url)
        run(['git', 'clone', repo_url, dest], check=True)

    return dest


class Project(object):
    """An mkdocs project."""

    def __init__(self, config_path=CONFIG_PATH, docs_dir=DOCS_DIR):
        """
        Create project object.

        :param config_path: Path to mkdocs.yml
        :param docs_dir: Path to docs/ subdirectory
        """
        self.config_path = config_path
        self.docs_dir = docs_dir
        self.pluginstoc = {}
        assert self.config_path.is_file()
        assert self.docs_dir.is_dir()

    def save(self):
        """Save project config."""
        log.debug('Saving config to %s', self.config_path)
        with open(self.config_path) as cfgfp:
            config = yaml.load(cfgfp)

        self._update_config(config)
        with open(self.config_path, 'w') as cfgfp:
            yaml.dump(config, cfgfp, default_flow_style=False)

    def _update_config(self, config):
        pagestoc = config.setdefault('pages', [])
        pluginstoc = [{k: v} for k, v in sorted(self.pluginstoc.items())]
        for section in pagestoc:
            if 'Plugins' in section:
                # Warning: Overwrites the whole section
                section['Plugins'] = pluginstoc
                break

        else:
            pagestoc.append({'Plugins': pluginstoc})

    def import_plugin_doc(self, source_dir):
        """Import doc file from plugin source_dir into project docs."""
        log.debug('Importing plugin %s', source_dir)
        name = source_dir.name[:-len('-qsplugin')]
        fname = name.lower()
        name = self._parse_info_plist(source_dir) or name
        dstfile = self.docs_dir / 'plugins' / f'{fname}.md'
        entry = f'plugins/{fname}.md'
        makedirs(dstfile.parent, exist_ok=True)
        for srcfile in Path(source_dir).iterdir():
            if re.match(r'Documentation.m((ar)?k)?d((ow)?n)?', srcfile.name):
                log.debug('Copying %s -> %s', srcfile, dstfile)
                copyfile(srcfile, dstfile)
                log.debug('Adding %s to page index', name)
                self.pluginstoc[name] = entry

    def _parse_info_plist(self, source_dir):
        try:
            with open(source_dir / 'Info.plist', 'rb') as infofp:
                info = plistlib.load(infofp)

        except OSError:
            return None
        else:
            name = info.get('CFBundleDisplayName')
            if not name or name.startswith('$'):
                name = info.get('CFBundleName')
                if not name or name.startswith('$'):
                    return None

            return name


def main():
    """Run script."""
    project = Project()
    for repo in get_plugin_repositories():
        source_dir = cache_code(repo['full_name'], repo['clone_url'])
    # for source_dir in Path('_plugins/quicksilver').iterdir():
        project.import_plugin_doc(source_dir)

    project.save()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()

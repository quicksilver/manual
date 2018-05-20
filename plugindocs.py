#!/usr/bin/env python3
"""
Import Documentation for Quicksilver plugins.

This script fetches plugin documentation from their respective repositories and
inserts them into the *plugins/* directory in *docs/*.
"""
import logging
import plistlib
from argparse import ArgumentParser
from os import makedirs
from pathlib import Path
from urllib.request import Request, urlopen

from html2text import html2text
import yaml


CACHE_DIR = Path('_plugins')
CONFIG_PATH = Path(__file__).parent / 'mkdocs.yml'
DOCS_DIR = Path(__file__).parent / 'docs'
CHECK_URL = 'https://qs0.qsapp.com/plugins/check.php'
INFO_URL = 'https://qs0.qsapp.com/plugins/info.php'
SUPPORTED_OS_VERSIONS = [
    (10, 11, 6),
    (10, 12, 6),
    (10, 13, 4),
]


log = logging.getLogger(__name__)


def get_latest_qsversion(osversion=None, check_url=CHECK_URL):
    """Query for the latest version of Quicksilver."""
    ua = 'manual/plugindocs'
    if osversion:
        ua += f' Mac OS X {osversion}'

    req = Request(check_url, headers={'User-Agent': ua})
    log.info('Querying %s for latest qs version', check_url)
    with urlopen(req) as response:
        hexbuild = response.read().decode()

    return int(hexbuild, 16)


def get_plugins_info(qsversion=None, osversion=None, fresh=False,
                     info_url=INFO_URL, cache_dir=CACHE_DIR):
    """Fetch plugin information list from qsapp."""
    if qsversion and osversion:
        cache_path = cache_dir / f'info_QS{qsversion}_OS{osversion}.plist'
    elif qsversion:
        cache_path = cache_dir / f'info_QS{qsversion}.plist'
    elif osversion:
        cache_path = cache_dir / f'info_OS{osversion}.plist'
    else:
        cache_path = cache_dir / 'info.plist'

    if cache_path.is_file() and not fresh:
        log.debug('Returning cached info from %s', cache_path)
        with open(cache_path, 'rb') as cachefp:
            info = plistlib.load(cachefp)

        return info['plugins']

    url = info_url
    if qsversion:
        url += f'?qsversion={qsversion}'

    ua = 'manual/plugindocs'
    if osversion:
        ua += f' Mac OS X {osversion}'

    req = Request(url, headers={'User-Agent': ua})
    log.info('Querying %s for plugins info', url)
    with urlopen(req) as response:
        log.debug('Caching response to %s', cache_path)
        makedirs(cache_dir, exist_ok=True)
        with open(cache_path, 'wb+') as cachefp:
            cachefp.write(response.read())
            cachefp.seek(0)
            info = plistlib.load(cachefp)

    return info['plugins']


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

    def clear(self):
        """Clear docs dir."""
        plugins_dir = self.docs_dir / 'plugins'
        log.warning('Clearing %s', plugins_dir)
        for file in plugins_dir.iterdir():
            if file.is_file():
                file.unlink()

    def save(self):
        """Save project config."""
        log.info('Saving config to %s', self.config_path)
        with open(self.config_path) as cfgfp:
            config = yaml.load(cfgfp)

        self._update_config(config)
        with open(self.config_path, 'w') as cfgfp:
            yaml.dump(config, cfgfp, default_flow_style=False)

    def _update_config(self, config):
        pagestoc = config.setdefault('pages', [])
        sortedpages = sorted(
            self.pluginstoc.items(),
            key=lambda i: tuple(map(str.lower, i)),
        )
        pluginstoc = [{k: v} for k, v in sortedpages]
        for section in pagestoc:
            if 'Plugins' in section:
                # Warning: Overwrites the whole section
                section['Plugins'] = pluginstoc
                break

        else:
            pagestoc.append({'Plugins': pluginstoc})

    def import_plugin_doc(self, plugin, skip_empty=True):
        """Import from plugin info into project docs."""
        name, fname = self._get_plugin_names(plugin)
        log.info('Importing plugin %s', name)
        source = plugin.get('QSPlugIn', {}).get('extendedDescription', '')
        output = html2text(source).strip()
        if not output and skip_empty:
            log.info('Skipping %s (no documentation)', name)
            return None

        dstfile = self.docs_dir / 'plugins' / f'{fname}.md'
        log.debug('Writing docs to %s', dstfile)
        makedirs(dstfile.parent, exist_ok=True)
        with open(dstfile, mode='w') as mdfile:
            summary = [
                f'# {name}\n\n',
                self._get_plugin_summary(plugin),
                '\n\n',
            ]
            mdfile.writelines(summary)
            if output:
                mdfile.write(output)
            else:
                log.debug('No documentation for %s', name)
                mdfile.write('No plugin documentation.')

        log.debug('Adding %s to page index', name)
        entry = f'plugins/{fname}.md'
        self.pluginstoc[name] = entry
        return name

    def _get_plugin_names(self, plugin):
        fname = plugin.get('CFBundleIdentifier').rsplit('.')[-1]
        if fname.startswith('QS'):
            fname = fname[2:]

        name = plugin.get('CFBundleDisplayName') or plugin.get('CFBundleName')
        if not name:
            name = fname

        if name.lower().endswith('plugin'):
            name = name[:-6].rstrip()

        fname = fname.lower()
        if fname.endswith('plugin'):
            fname = fname[:-6].rstrip()

        return name, fname

    def _get_plugin_summary(self, plugin):
        tpl = '\n'.join((
            '{desc}',
            '',
            ' Summary                    | {sp} ',
            '---------------------------:|:{hl:-^{width}}-',
            # '      Latest plugin version | {plv}',
            ' Available on macOS version | {osv}',
            '      for Quicksilver build | {qsv}',
            ''
        ))
        desc = plugin.get('QSPlugIn', {}).get('description', '')
        kw = {
            'desc': desc + '.' if desc and not desc.endswith('.') else desc,
            'sp': '&nbsp;',
            'hl': '-',
            # 'plv': plugin.get('CFBundleShortVersionString') or plugin.get('CFBundleVersion', ''),
            'osv': ', '.join('{}.{}'.format(*v) for v in sorted(plugin['_osversions'])),
            'qsv': ', '.join(format(v, 'x') for v in sorted(plugin['_qsversions'])),
        }
        kw['width'] = max(len(kw[s]) for s in kw.keys() if s != 'desc')
        return tpl.format(**kw)


def main():
    """Run script."""
    argp = ArgumentParser()
    logargs = argp.add_mutually_exclusive_group()
    logargs.add_argument('--debug', action='store_true', help='Turn on debug mesages')
    logargs.add_argument('--quiet', action='store_true',
                         help='Suppress output except for warnings and errors')
    argp.add_argument('--fresh', action='store_true', help='Ignore local info cache')
    argp.add_argument('--clear', action='store_true', help='Clear existing plugin docs')
    argp.add_argument('--keep-empty', action='store_false', dest='skip_empty',
                      help='Keep stub document for plugins without documentation')
    opts = argp.parse_args()

    if opts.debug:
        logging.getLogger().setLevel(logging.DEBUG)
    elif opts.quiet:
        logging.getLogger().setLevel(logging.WARNING)

    pluginmap = {}
    for major, minor, patch in sorted(SUPPORTED_OS_VERSIONS):
        # sorted takes care of later osversions go with later qsversions
        osversion = f'{major}_{minor}_{patch}'
        log.info('With osversion=%s:', osversion)
        qsversion = get_latest_qsversion(osversion=osversion)
        plugins = get_plugins_info(qsversion=qsversion, osversion=osversion, fresh=opts.fresh)
        for plugin in plugins:
            info = pluginmap.setdefault(plugin['CFBundleIdentifier'], plugin)
            info.setdefault('_osversions', set()).add((major, minor))
            info.setdefault('_qsversions', set()).add(qsversion)

    project = Project()
    if opts.clear:
        project.clear()

    for plugin in pluginmap.values():
        try:
            project.import_plugin_doc(plugin, skip_empty=opts.skip_empty)
        except Exception as exc:
            log.warning('Error importing %s: %s', plugin.get('CFBundleName'), exc)
            log.debug('Exception', exc_info=True)

    project.save()


if __name__ == '__main__':
    logging.basicConfig(
        format='%(message)s',
        level=logging.INFO,
    )
    try:
        main()
    except KeyboardInterrupt:
        log.critical('Aborting')

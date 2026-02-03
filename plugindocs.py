#!/usr/bin/env python3
"""
Import Documentation for Quicksilver plugins.

This script fetches plugin documentation from their respective repositories and
inserts them into the *plugins/* directory in *docs/*.
"""

import logging
import plistlib
from lxml import etree
from argparse import ArgumentParser
import json

from html2text import html2text
import yaml

from pathlib import Path
from urllib.request import Request, urlopen


CACHE_DIR = Path('_plugins')
CONFIG_PATH = Path(__file__).parent / 'mkdocs.yml'
DOCS_DIR = Path(__file__).parent / 'docs'
CHECK_URL = 'https://qs0.qsapp.com/plugins/check.php'
INFO_URL = 'https://qs0.qsapp.com/plugins/info.php'
SUPPORTED_OS_VERSIONS = [
    (10, 14, 6),
    (10, 15, 7),
    (11, 6, 7),
    (12, 4, 0),
    (13, 0, 0),
    (14, 0, 0),
    (15, 0, 0),
    (16, 0, 0),
]


log = logging.getLogger(__name__)


def get_latest_qsversion(osversion=None, check_url=CHECK_URL):
    """Query for the latest version of Quicksilver."""
    ua = 'manual/plugindocs'
    if osversion:
        ua += ' Mac OS X {osversion}'.format(**locals())

    req = Request(check_url, headers={'User-Agent': ua})
    log.info('Querying %s for latest qs version', check_url)
    with urlopen(req) as response:
        hexbuild = response.read().decode()

    return int(hexbuild, 16)


def get_plugins_info(qsversion=None, osversion=None, fresh=False,
                     info_url=INFO_URL, cache_dir=CACHE_DIR):
    """Fetch plugin information list from qsapp."""
    if qsversion and osversion:
        cache_path = cache_dir / 'info_QS{qsversion}_OS{osversion}.plist'.format(**locals())
    elif qsversion:
        cache_path = cache_dir / 'info_QS{qsversion}.plist'.format(**locals())
    elif osversion:
        cache_path = cache_dir / 'info_OS{osversion}.plist'.format(**locals())
    else:
        cache_path = cache_dir / 'info.plist'

    if cache_path.is_file() and not fresh:
        log.debug('Returning cached info from %s', cache_path)
        with cache_path.open('rb') as cachefp:
            info = plistlib.load(cachefp)

        return info['plugins']

    url = info_url
    if qsversion:
        url += '?qsversion={qsversion}'.format(**locals())

    ua = 'manual/plugindocs'
    if osversion:
        ua += ' Mac OS X {osversion}'.format(**locals())

    req = Request(url, headers={'User-Agent': ua})
    log.info('Querying %s for plugins info', url)
    with urlopen(req) as response:
        log.debug('Caching response to %s', cache_path)
        cache_dir.mkdir(parents=True, exist_ok=True)
        with cache_path.open('wb+') as cachefp:
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
        self.plugin_id_map = {}  # Maps bundle IDs to page slugs
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
        with self.config_path.open() as cfgfp:
            config = yaml.safe_load(cfgfp)

        self._update_config(config)
        with self.config_path.open('w') as cfgfp:
            yaml.dump(config, cfgfp, default_flow_style=False)
        
        # Save plugin ID mapping
        self._save_plugin_id_map()

    def _update_config(self, config):
        pagestoc = config.setdefault('nav', [])
        sortedpages = sorted(
            self.pluginstoc.items(),
            key=lambda i: tuple(s.lower() for s in i),
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
        plugin_id = plugin.get('CFBundleIdentifier')
        source = plugin.get('QSPlugIn', {}).get('extendedDescription', '').strip()

        if not source and skip_empty:
            log.info('Skipping %s (no documentation)', name)
            return None

        transform = etree.XSLT(etree.XML('''\
        <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:output method="html" indent="yes"/>
        <xsl:template match="node()|@*" name="identity">
            <xsl:copy>
                <xsl:apply-templates select="node()|@*"/>
            </xsl:copy>
        </xsl:template>

        <xsl:template match="//dl">
            <xsl:apply-templates />
        </xsl:template>

        <xsl:template match="//dl/dt">
            <h3><xsl:value-of select="text()" /></h3>
        </xsl:template>

        <xsl:template match="//dl/dd">
            <p><xsl:value-of select="text()" /></p>
        </xsl:template>
        </xsl:stylesheet>'''))
        xml = etree.HTML(source)
        source = str(transform(xml))

        output = html2text(source).strip()
        if not output and skip_empty:
            log.info('Skipping %s (no documentation)', name)
            return None

        dstfile = self.docs_dir / 'plugins' / '{fname}.md'.format(**locals())
        log.debug('Writing docs to %s', dstfile)
        dstfile.parent.mkdir(parents=True, exist_ok=True)
        with dstfile.open('w') as mdfile:
            summary = [
                '# {name}\n\n'.format(**locals()),
                self._get_plugin_summary(plugin),
                '\n\n',
                '<div id="plugin-docs" markdown="1">\n',
            ]
            mdfile.writelines(summary)
            if output:
                mdfile.write(output)
            else:
                log.debug('No documentation for %s', name)
                mdfile.write('No plugin documentation.')
            mdfile.write('\n</div>')
            
            # Add JavaScript for dynamic content loading
            mdfile.write('\n\n')
            mdfile.write(self._get_plugin_dynamic_loader(plugin_id))

        log.debug('Adding %s to page index', name)
        entry = 'plugins/{fname}.md'.format(**locals())
        # little py2 str hack to stop !!unicode appearing in yaml
        self.pluginstoc[str(name)] = str(entry)
        # Store mapping of plugin ID to page slug for lookup
        self.plugin_id_map[plugin_id] = fname
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

    def _get_plugin_dynamic_loader(self, plugin_id):
        """Generate JavaScript to dynamically load plugin info from API."""
        return '''
<script>
(function() {{
    const pluginId = '{}';
    const apiUrl = 'https://qs0.qsapp.com/api/plugin-info.php?id=' + encodeURIComponent(pluginId);
    const contentDiv = document.getElementById('plugin-docs');
    
    // Fetch and update plugin info from the API
    fetch(apiUrl)
        .then(response => {{
            if (!response.ok) throw new Error('Network response was not ok');
            return response.json();
        }})
        .then(data => {{
            if (data && data.pluginInfo && data.pluginInfo.extendedDescription) {{
                contentDiv.innerHTML = data.pluginInfo.extendedDescription;
            }}
        }})
        .catch(error => {{
            console.log('Could not fetch latest plugin info from API:', error);
            // Content above is static version, which is fine for offline access
        }});
    
    if (!contentDiv) return;
}})();
</script>
'''.format(plugin_id)

    def _save_plugin_id_map(self):
        """Save a lookup page embedding plugin IDs to page slugs."""
        redirect_file = self.docs_dir / 'plugins' / 's.md'
        log.debug('Creating plugin lookup redirect page at %s', redirect_file)
        with redirect_file.open('w') as f:
            f.write(self._get_plugin_lookup_page())

    def _get_plugin_lookup_page(self):
        """Generate a lookup page that redirects to the correct plugin page by ID."""
        manifest_json = json.dumps(self.plugin_id_map, indent=2, sort_keys=True)
        manifest_md = '''# Plugin Lookup

Redirecting...

<div id="plugin-lookup"></div>

<script id="plugin-manifest" type="application/json">
{manifest_json}
</script>
'''.format(manifest_json=manifest_json)
        return manifest_md + '''
<script>
(function() {
    // Get the plugin ID from query parameter
    const params = new URLSearchParams(window.location.search);
    const pluginId = params.get('id');
    
    const lookupDiv = document.getElementById('plugin-lookup');
    
    if (!pluginId) {
        window.location.href = '../../';
    }
    
    // Read the manifest embedded in the page
    let manifest = {};
    try {
        const manifestEl = document.getElementById('plugin-manifest');
        manifest = JSON.parse(manifestEl.textContent || '{}');
    } catch (error) {
        window.location.href = '../../';
        return;
    }

    const slug = manifest[pluginId];
    if (slug) {
        // Redirect to the plugin page
        window.location.href = '../' + slug + '/';
    } else {
        lookupDiv.innerHTML = '<p>Plugin not found: ' + escapeHtml(pluginId) + '</p>';
    }
    
    function escapeHtml(text) {
        if (!text) return '';
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, m => map[m]);
    }
})();
</script>
'''


def main():
    """Run script."""
    argp = ArgumentParser()
    logargs = argp.add_mutually_exclusive_group()
    logargs.add_argument('--debug', action='store_true', help='Turn on debug mesages')
    logargs.add_argument('--quiet', action='store_true',
                         help='Suppress output except for warnings and errors')
    argp.add_argument('--fresh', action='store_true', help='Ignore (& refresh) local info cache')
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
        osversion = '{major}_{minor}_{patch}'.format(**locals())
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

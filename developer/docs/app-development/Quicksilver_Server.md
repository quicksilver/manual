# Quicksilver Server Interaction

Quicksilver communicates with the servers at qsapp.com for the reasons
below. This page aims to document these interactions, which are for the
time being, mostly development plans.

# Objectives

The objective is to provide the most complete Quicksilver experience
with minimal user intervention, whilst maintain a user-configurable
level of stability.

Reasons to communicate with the server:

-   Self-update: check for new versions of quicksilver compatible with
    the user's OS, and download them
-   Plugin-list: *todo*: gather a list of compatible plugins and their
    related bundles to suggest relevant plugins to the user
-   Plugin download: *todo*: download the latest compatible version of a
    plugin by it's ID (for use with the qsinstall:// scheme and the
    plugin list)
-   Crash reports: *todo*: upload any crash reports concerning QS after
    obtaining user consent, and perhaps suggesting a fix if the report
    is recognised

# Currently existing

## Streams

-   Self-update:
    [QSUpdateController.h](https://github.com/quicksilver/Quicksilver/blob/master/Quicksilver/Code-App/QSUpdateController.h)
    -   Parameter `type` (from an integer `QSNewUpdateReleaseLevel`):
        `rel` or `pre` or `dev`
    -   Parameter `current` for QS version (from `kCFBundleVersionKey`)

The resulting text is read as a hexIntValue it then compares to the
`kCFBundleVersionKey`.

-   Plugin list:
    [QSPlugInManager.h](https://github.com/quicksilver/Quicksilver/blob/master/Quicksilver/Code-QuickStepCore/QSPlugInManager.h)
    -   Parameter `asOfDate` (NSDate of last update formatted as
        `%Y%m%d%H%M%S`)
    -   Parameter `qsversion` `[ [ NSApp buildVersion] hexIntValue]`
    -   Parameter `sids` a comma (and space ?) separated list of the
        identifiers of all installed plugins with `isSecret == 1`

When the self-update version reports a new version available,
Quicksilver attempts (and ignores on failure) to poll the plugin list.
In this case, the `qsversion` parameter is replaced by a `updateVersion`
parameter with the hexIntValue of the new QS version about to be
installed.

The result stream is an XML plist with a dictionary containing:

-   `fullIndex` boolean, if true, the list of known plugins in
    quicksilver is cleared before loading the updates
-   `plugins` an array of plugin info.plist-like entries. They are
    loaded into `[QSPlugIn plugInWithWebInfo:]` or updated with the
    `setData:` if the bundle id is known.
    -   The following keys are present from what I can tell
        `CFBundleIdentifier QSModifiedDate CFBundleName CFBundleVersion QSPlugIn QSRequirements CFBundleShortVersionString`

*NB:* The OS version is always sent in the HTTP headers: my user agent
is `Quicksilver/3842 CFNetwork/454.11.5 Darwin/10.6.0`
`(i386) (MacBookPro5%2C2)`

## QSRequirements

In the Info.plist of a plugin, the author can specify requirements for
the plugin to be installed. The `QSRequirements` key is a dictionary at
the root of the plist that can contain:

-   `bundles`: An array of dict. mapping bundle id to name. *[seems
    ignored](https://github.com/quicksilver/Quicksilver/blob/master/Quicksilver/Code-QuickStepCore/QSPlugIn.m#L512)*
-   `frameworks`: An array of dict
-   `paths`
-   `version` Quicksilver version (`versionCompare:`)
-   `feature` Integer feature level
-   `plugins` Array of dict. mapping plugin id to name

# Improvements

I'd like to address the following problems:

-   OS version is not checked before loading a plugin (that I could
    find)
-   It is inefficient to download quicksilver and plugin updates
    separately.
    -   If the plugin update fails, it might be dangerous to update QS
        anyway
    -   99% of polling will have nothing new to update, why ask twice ?
-   The plugin list uses system time to perform incremental updates, but
    this brings in computer time sync issues, and makes the url ever
    changing, thus difficult to cache.
-   It is difficult to gather community information on the stability of
    plugins
-   Users do not have a release level choice for plugins

Considerations (these are things we should make sure the new system will
keep possible, even they are not priorities today):

-   Including "breaks" or incompatibility data, such as negative
    QSRequirements. *Such plugin doesnt work if you have such an app
    installed*
-   Support for simultanous versions of plugins depending on the version
    of the OS/QS, and serve the right list
-   Make it easy to allow users to find help/report bugs per plugin, and
    use that data in plugin stability assessment
-   Secure the plugin system to ensure malware cannot be transmitted
    through this system (I'd vote for this to be a priority if it
    weren't so darn complicated, any volunteers ?), perhaps with an
    official RSA key pair, and require signatures to install a plugin
    (unless you compile quicksilver yourself)

Longer term:

-   Integrate data with the wiki so everyone can assist in maintaining
    it
-   Look for crash reports in the user's logs, ask his permission, and
    upload them to QSApp
-   Include a "community bounty" for plugin development =)

# Work plan

## Quicksilver.app

-   Add OS version check to plugins
-   Add release level for plugin list (+ UI ?)
-   Add `version` parameter to URL
-   Read a single URL, parse as XML plist, and:
    -   Store a `version` key value to provide in the URL at the next
        request
    -   Dispatch one key to app update, and the other to the plugin list
        update

## Server side

-   Implement OS + QS version parsing
-   Generate table of OS/QS/release level to QS update file
-   Generate table of OS/QS/version/release level to plugin update file
-   Concatenate and send
-   Generate table of OS/QS/bundle id/version to download url for qspkg

## Static data

I plan on using a template for
[1](https://github.com/ddlsmurf/qs-builder), a ruby project that parses
plugin files and runs templates out of that data.

The templates so far include:

-   `plist` template generates a compatible plugin list xml plist
-   `packager` builds qspkg files for each plugin
-   `basic` wiki documentation, `icon-maker` icons for the wiki

Override files are plists placed in folder and named with a plugins
bundle id. When such a file exists, it's contents is merged into the
existing plugin's info.plist. This mecanism lets us create a folder with
files for compatibility or stability data, as well as meta data such as
related tutorials.

What's missing:

-   A preliminary list of override files for each plugin
-   php table generation for picking compatible plugins
-   os/qs/etc version specific files
-   incremental update versions, which can be handled by adding updates
    to numerically sequential folders and only including those plugins
    for the incremental version, and all plugins for the full versions.
    Not sure how easy this will be to do, but it's not that important,
    using a hand specified integer constant will suffise to let proxies
    and caches do their jobs.
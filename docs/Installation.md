# Installation

## Requirements

* The latest version runs on OS X 10.9+
* Previous versions are available for older versions of OS X, including for PPC hardware.

## Installing Quicksilver

1. [Download Quicksilver](https://qsapp.com/download.php).
2. Open the `.dmg` file and drag Quicksilver to your Applications folder.
3. Drag the Quicksilver volume to the trash and delete the `.dmg` file.

On first launch, Quicksilver presents some setup options (it can be rerun later with the Run Setup button in the Application Preferences). Choose a shortcut that activates the Quicksilver command window, or just accept the default, <kbd>⌃</kbd><kbd>space</kbd>.  Quicksilver scans your computer for applications to recommend plugins to install. If the Contacts plugin is installed, the system will ask if you want to give Quicksilver access to your Contacts, click OK.

Initially, Quicksilver shows no windows when it is running. Activate Quicksilver using the shortcut <kbd>⌃</kbd><kbd>space</kbd> (if you accepted the default).

When Quicksilver starts it contacts qs0.qsapp.com to check for new versions. A security program like Little Snitch that monitors outgoing network connections might warn about this. It’s perfectly normal and benign.

## Support Files

The Quicksilver.app is usually installed in `/Applications/` or `~/Applications/`. Like most OS X applications Quicksilver stores its configuration information in the user's `~/Library` folder. As of 10.8, OS X hides this folder from the Finder by default. The Quicksilver action **Make Visible** from the File Attributes Plugin can be used to let the Finder show it. When first used, the following per user files and folders are created:

- `~/Library/Application Support/Quicksilver/`
    - `Actions.plist` - list of installed actions
    - `Catalog.plist` - the configured catalog sources
    - `Mnemonics.plist` - learned inputs, defaults and abbreviations
    - `PlugIns.plist` - the list of available plugins and how they are configured
    - `Triggers.plist` - the configured triggers
    - `PlugIns/` - installed plugins
    - `Shelves/` - where items on the Shelf and clipboards are stored
    - `Actions/` - add scripts here that implement actions
    - `Templates/` - not installed but create this folder to use with the Make New… action
- `~/Library/Preferences/com.blacktree.Quicksilver.plist` - various preferences and internal state
- `~/Library/Caches/Quicksilver/` - various state including indexes in binary files
- `~/Library/Caches/com.blacktree.Quicksilver/` - various state in binary files

It can also be useful to move or rename these while troubleshooting a problem. If plugins are not installing sometimes the permissions of `~/Library/Application Support/Quicksilver/` and the `PlugIns` folder inside it are wrong. If the owner is System, change it to your user account and restart Quicksilver.

## Uninstalling Quicksilver

Move the application file to the trash. This leaves the configuration files. If you reinstall Quicksilver, your configuration will be restored. To remove all remnants of Quicksilver, use the Uninstall Quicksilver button in the Quicksilver's preferences.


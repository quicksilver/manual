# Installation

## Requirements

The latest version runs on macOS 10.14 or later. [Previous versions](https://github.com/quicksilver/Quicksilver/releases) are available for older versions of macOS.

## Installing Quicksilver

From the Disc Image (.dmg) file:

  1. [Download Quicksilver](https://qsapp.com/download.php).
  2. Open the `.dmg` file and drag Quicksilver to your Applications folder.
  3. Unmount the Quicksilver volume and delete the `.dmg` file.

Using Homebrew:

[Homebrew is a package manager for OS X](https://brew.sh) for installs, updates and uninstalls of most OS X software:

Open Terminal, type `brew install --cask quicksilver`. You can `uninstall` just as easily.

## First Launch

On first launch, Quicksilver presents some setup options (it can be rerun later with the Run Setup button in the Application Preferences). Choose a shortcut that activates the Quicksilver command window, or just accept the default, <kbd>⌃</kbd><kbd>Space</kbd>. Quicksilver will recommend plugins based on applications you have installed and other criteria.

Initially, Quicksilver shows no windows when it is running. Activate Quicksilver using the shortcut <kbd>⌃</kbd><kbd>Space</kbd> (if you accepted the default).

When Quicksilver starts it contacts `qs0.qsapp.com` to check for new versions. A security program like Little Snitch that monitors outgoing network connections might warn about this. It's perfectly normal and benign.

## Support Files

Quicksilver is usually installed in `/Applications/` or `~/Applications/`.

Like most macOS applications, Quicksilver stores its configuration information in the user's `~/Library` folder. As of 10.8, macOS hides this folder from the Finder by default. The Quicksilver action **Make Visible** from the File Attributes Plugin can be used to let the Finder show it. When first used, the following per user files and folders are created:

  * `~/Library/Application Support/Quicksilver/`
      * `Actions.plist` - list of installed actions
      * `Catalog.plist` - the configured catalog sources
      * `Mnemonics.plist` - learned inputs, defaults and abbreviations
      * `PlugIns.plist` - the list of available plugins and how they are configured
      * `Triggers.plist` - the configured triggers
      * `PlugIns/` - installed plugins
      * `Shelves/` - where items on the Shelf and clipboards are stored
      * `Actions/` - add scripts here that implement actions
      * `Templates/` - not installed but create this folder to use with the **Make New…** action
  * `~/Library/Preferences/com.blacktree.Quicksilver.plist` - various preferences and internal state
  * `~/Library/Caches/Quicksilver/` - various state including indexes in binary files
  * `~/Library/Caches/com.blacktree.Quicksilver/` - various state in binary files

It can also be useful to move or rename these while troubleshooting a problem. If plugins are not installing sometimes the permissions of `~/Library/Application Support/Quicksilver/` and the `PlugIns` folder inside it are wrong. If the owner is System, change it to your user account and restart Quicksilver.

## Uninstalling Quicksilver

Move the application file to the trash. This leaves the configuration files. If you reinstall Quicksilver, your configuration will be restored. To remove all remnants of Quicksilver, use the Uninstall Quicksilver button in the Quicksilver's preferences.

# FAQ

## Quicksilver uses lots of memory, CPU, or hangs

Quicksilver keeps the entire index in memory and scans the catalog sources regularly. Usually when it uses too many resources it’s because the catalog is configured too large. The default `~/Documents` source is configured to a depth of 2. If you create a custom source of infinite depth, it will make the catalog large. Also, if you configure a source for your home directory, it will probably scan many unnecessary files (`~/Library`, etc.). This is also why your music and pictures aren’t in the global catalog and should be accessed via the iTunes and iPhoto plugins, which require you to type → to get into your music files and photos.

If you have network drives configured to be scanned, that can make the catalog large or take a while. Note the Find All Applications catalog source (in the Applications set) will scan your entire machine, including network drives for applications. A comfortable size for your catalog will vary based on the capabilities of your computer.

Also, if you have the Clipboard Module plugin installed and configured in the Clipboard Preferences to Capture History you might have large clippings in the history. This would cause Quicksilver to use lots of memory and perhaps lots of CPU at startup. The clipboard history is stored in the following file:

`~/Library/Application Support/Quicksilver/Shelves/QSPasteboardHistory.qsshelf`

You can check its size. To clear it you can use the clear button in the Clipboard History panel or, while Quicksilver is not running, delete the above file.

If you open the drawer for catalog sources, in the Contents tab you’ll find all the items found for that source. Clicking on the headings in this tab will sort the list. Large catalog sources (500 or more) will take a long time to sort and use lots of memory. If I accidentally sort my Documents with 2000 items I ultimately force quit Quicksilver since it uses 60-80% CPU and several hundred MB of real memory. Be careful as the sort order applies globally. If you sort a small source it works fine, if you then (even accidentally) click on a large source it will eat up resources. A Quicksilver restart resets the contents tab to be unsorted.

## Quicksilver doesn’t find my files

By default Quicksilver finds files on your Desktop and in your Documents folder but it doesn’t scan very far into those locations. It scans things on the Desktop but not inside folders on the Desktop, that is it scans the Desktop to a depth of 1. Quicksilver scans the `~/Documents` folder to a depth of 2.

To scan deeper, clone the source so it’s in the Custom set in the catalog and editable. To do this, select the Users set and the Documents source, open the drawer and select the Attributes tab. Click on Create Copy to create a new source in Custom named Documents. Select the new source and click on the button to show a drawer with three tabs. Select the Source Options tab and select the depth.

Do not just set it to infinite, the catalog will be too large and Quicksilver will slow to a crawl. See the Catalog section for some tips.

## Quicksilver always searches the entire catalog

After right-arrowing into something, if searching appears to start over from the entire catalog rather than searching the current context, you may have inadvertently changed the search mode using <kbd>⌘</kbd><kbd>→</kbd> or <kbd>⌘</kbd><kbd>←</kbd>.

After you right-arrow, click the gear at the top of the results list. You can change the search mode there. You can also use the keyboard shortcuts above to cycle though the search modes. “Filter Results” is probably what you want in most situations.

## Quicksilver crashes

When you see crashes, here are a few things to try.

  * Check the log in Console.app to see if there is some log message hinting at what might have gone wrong.
  * Try clearing the catalog cache by quitting Quicksilver and deleting `~/Library/Caches/Quicksilver`, then relaunch Quicksilver.
  * Try disabling plug-ins a few at a time to see if things improve. Repeat the process until you’ve identified the offending plug-in.
  * If Quicksilver crashes at startup, see if you have a `~/Library/Application Support/Quicksilver/Shelves/` folder. Quit  Quicksilver, move it out of the way and start Quicksilver again. Sometimes the shelf gets corrupted.

## Quicksilver won’t install any plugins or hangs when trying

This is usually a permissions problem. Check that your user account (and not root) owns `~/Library/Application Support/Quicksilver/` and the PlugIns folder beneath it. You can check and change this if needed by doing Get Info in the Finder and looking in the Ownership & Permission section. After making sure the folder exists and you own it and have permissions to write to it, restart Quicksilver.

The other cause is if you’re running Little Snitch which is a reverse firewall and prevents Quicksilver from contacting the server where the plugins are.

Another possibility is that the plugin is no longer supported by your system. See if the plugin was moved to `~/Library/Application Support/Quicksilver/PlugIns (disabled)`.

## Doesn’t Spotlight make Quicksilver unnecessary?

No, they do different things and are in fact complementary. Spotlight scans inside files (and their metadata) so you can search their contents. Quicksilver only looks at file names and inside some things like contacts and bookmarks and lets you do more than just open them (e.g., e-mail a file to a contact). Since Quicksilver’s index is smaller than Spotlight’s and because it learns from your previous searches Quicksilver often finds things faster than Spotlight.

## I don’t see feature X

Make sure you have the appropriate plugin(s) installed.

If it’s an action you don’t see, check in the Action Preferences that the action is enabled (checked).

If it’s something in the first pane you don’t see, make sure it’s enabled in the catalog and scanned (so that the catalog source has a number next to the checkbox). This manual tries to be very precise in describing how to enable each feature it describes.

## Why is X in my catalog?

If you see something unexpected or unwanted and you’re not sure how it ended up in your catalog, you can use the Show Source in Catalog action to see where it came from. The action will open Quicksilver’s preferences and select the source entry.

!!! note
    The Show Source in Catalog action needs to be enabled in Preferences → General → Actions

## Triggers don’t work after a restart of Quicksilver

You may create a trigger that works as expected until the next time Quicksilver is launched. If this happens, the trigger probably involves something that isn’t in the catalog. You may be able to find something and use it in a trigger while it’s in memory, but when Quicksilver restarts and sets up your triggers, only the objects in the catalog are available.

There are exceptions to this for objects that can be easily recreated in memory using their identifier, like text, files, and URLs.

## Catalog entries are missing on Mojave or later

This is known to affect Safari Bookmarks and Safari History.

Go to your [Privacy Preferences][privacy] and add Quicksilver to the “Full Disk Access” list.

## Actions fail on Mojave or later

In macOS Mojave, Apple began requiring user confirmation before allowing applications to interact with each other via AppleEvents (one of the technologies behind AppleScript). Quicksilver makes heavy use of AppleEvents to interact with your system.

If certain actions don’t seem to be doing anything, you may have accidentally denied access to Quicksilver, or you may have missed the dialog asking for permission, in which case it will default to denying access. (This is especially a problem as the dialog may appear *behind* the Quicksilver interface.)

If you find yourself in this situation, you can go to your [Privacy Preferences][privacy] and review the access given to Quicksilver.

Alternatively, you can reset the access in Terminal:

    tccutil reset AppleEvents

Unfortunately, that resets everything, so any application on your system using AppleEvents will have to be reauthorized.

[privacy]: x-apple.systempreferences:com.apple.preference.security?Privacy_Automation

## Adding symlinks to the Quicksilver catalog

Some users would like to add symlinks to files or directories to their
Quicksilver catalog *without* resolving the symlink. For example,
[`nix`](https://nixos.org/) users may want to add the contents of
`~/.nix-profile` to their catalog. `~/.nix-profile` is a symlink to a
directory whose target usually resides in `/nix/store` somewhere
(you can inspect with `/usr/bin/readlink -f ~/.nix-profile/`).

If one attempts to add this path to the Quicksilver catalog through the
graphical user interface (`Settings` ⇥ `Catalog` ⇥ `+` ⇥
`File & Folder Scanner`), a MacOS file picker
presents itself, and one can enter in the path either by pressing
<kbd>⌘</kbd><kbd>⇧</kbd><kbd>G</kbd> to type it in, or using
<kbd>⌘</kbd><kbd>⇧</kbd><kbd>.</kbd> to toggle showing hidden files and
folders. However, taking this approach, MacOS will resolve the path to the
symlink at the time of adding the path; if that symlink changes to point to a
different directory, the Quicksilver catalog entry will still point to the old
path that was resolved at the time of adding.

If this is not the desired behavior, one can add the symlink to the
Quicksilver catalog *without* resolving to its target by selecting the symlink
in Quicksilver's first pane (either by navigating or by entering text mode,
typing it in, then hitting <kbd>⎋</kbd>), then using the `Add To Catalog`
action:

![Adding a Symlink to the Catalog](images/add_symlink_to_catalog.png)

Please note that currently Quicksilver will not index the contents of a
symlinked directory, though it will index the content of a directory that is
within a symlinked directory. For example, adding `~/.nix-profile` to the
catalog will not index `~/.nix-profile/bin`. However, because
`~/.nix-profile/bin` is a directory (not a symlink), adding
`~/.nix-profile/bin` to your catalog can scan and add its contents such as
`~/.nix-profile/bin/nix`. Further, if you use the approach above to add it
without resolving its path, it should continue to update its contents over
time, even as the target of `~/.nix-profile` evolves.

For context and additional discussion, see
[Quicksilver/issues/2758](https://github.com/quicksilver/Quicksilver/issues/2758).

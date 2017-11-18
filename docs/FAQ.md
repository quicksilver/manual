# FAQ

## Quicksilver uses lots of memory, cpu or hangs:

Quicksilver keeps the entire index in memory and scans the catalog sources regularly. Usually when it uses too many resources it’s because the catalog is configured too large. The default ~/Documents/ source is configured to a depth of 2, if you create a custom source of infinite depth it will make the catalog large. Also if you configure a source for your home directory (~) it will probably scan many unnecessary files (~/Library, etc.). This is also why your music and pictures aren’t in the global catalog and should be accessed via the iTunes and iPhoto plugins which require you to type → to get into your music files and photos. 

Also if you have network drives configured to be scanned that can make the catalog large or take a while. Note the Find All Applications catalog source (in the Applications set) will scan your entire machine, including network drives for applications. A comfortable size for your catalog will vary based on the capabilities of your computer, I try to keep my catalog below 5000 items.

Also, if you have the Clipboard Module plugin installed and configured in the Clipboard Preferences to Capture History you might have large clippings in the history. This would cause Quicksilver to use lots of memory and perhaps lots of CPU at startup. The clipboard history is stored in the following file:

~/Library/Application Support/Quicksilver/Shelves/QSPasteboardHistory.qsshelf

you can check it’s size. I have my clipboard history set to 100 and the file is 512KB. To clear it you can use the clear button in the Clipboard History panel or while Quicksilver is not running, delete the above file.

If you open the drawer for catalog sources, in the Contents tab you’ll find all the items found for that source. Clicking on the headings in this tab will sort the list. Large catalog sources (500 or more) will take a long time to sort and use lots of memory. If I accidentally sort my Documents with 2000 items I ultimately force quit Quicksilver since it uses 60-80% CPU and several hundred MB of real memory. Be careful as the sort order applies globally. If you sort a small source it works fine, if you then (even accidentally) click on a large source it will eat up resources. A Quicksilver restart resets the contents tab to be unsorted.

## Quicksilver doesn’t find my files

By default Quicksilver finds files on your Desktop and in your Documents folder but it doesn’t scan very far into those locations. It scans things on the Desktop but not inside folders on the Desktop, that is it scans the Desktop to a depth of 1. Quicksilver scans the ~/Documents folder to a depth of 2. To scan deeper, clone the source so it’s in the Custom set in the catalog and editable. To do this, select the Users set and the Documents source, open the drawer and select the Attributes tab. Click on Create Copy to create a new source in Custom named Documents. Select the new source and click on the  button to show a drawer with three tabs. Select the Source Options tab and select the depth. Do not just set it to infinite, the catalog will be too large and Quicksilver will slow to a crawl. See the Catalog section for some tips.

## Quicksilver plays or shows notifications for the wrong iTunes track

Yes, unfortunately this is a problem in B51.

## Quicksilver crashes

A few plugin are destabilizing. In particular the Developer Module and Running Applications plugins. Try disabling them and see if things improve. TODO: Otherwise, check the log in Console.app to see if there is some log message hinting at what might have gone wrong. 

If Quicksilver crashes at startup, see if you have a `~/Library/Application Support/Quicksilver/Shelves/` folder. Quit  Quicksilver, move it out of the way and start Quicksilver again. Sometimes the shelf gets corrupted.

## Quicksilver won’t install any plugins and hangs when trying

This is usually a permissions problem and kGTD has been known to cause problems. Check that your user account (and not root) owns `~/Library/Application Support/Quicksilver/` and the PlugIns folder beneath it. You can check and change this if needed by doing Get Info in the Finder and looking in the Ownership & Permission section. After making sure the folder exists and you own it and have permissions to write to it, restart Quicksilver. 

The other cause is if you’re running Little Snitch which is a reverse firewall and prevents Quicksilver from contacting the server where the plugins are. TODO: I’m not sure if Little Snitch can be configured to to allow Quicksilver to work or if you have to disable it.

## Doesn’t Spotlight make Quicksilver unnecessary?

No, they do different things and are in fact complementary. Spotlight scans inside files (and their metadata) so you can search their contents. Quicksilver only looks at file names and inside some things like contacts and bookmarks and lets you do more than just open them (e.g., e-mail a file to a contact). Since Quicksilver’s index is smaller than Spotlight’s and because it learns from your previous searches Quicksilver often finds things faster than Spotlight. The Quicksilver Spotlight Module provides a Quicksilver interface to spotlight by adding 3 actions that work on a text subject.

## I don’t see feature X

Make sure you have the appropriate plugin(s) installed. If it’s an action you don’t see, check in the Action Preferences that the action is enabled (checked). If it’s something in the first pane you don’t see, make sure it’s enabled in the catalog and scanned (so that the catalog source has a number next to the checkbox). This manual tries to be very precise in describing how to enable each feature it describes.

## The Quicksilver .dmg doesn’t mount

If you downloaded it with Safari, look to see if the downloaded file’s name ends with `.bz2`. Rename the file in the Finder, removing the `.bz2` and then try opening the file.

## The third pane is empty

If the TextStart Ranker is installed, uninstall it and restart Quicksilver. It’s known to break selecting items in the third pane, e.g., when using the **Open With…** or **E-mail To…** actions. If you’re trying to get contacts, make sure the correct plugin is installed (e.g., Contacts) and check that they are enabled in the catalog (can you get to them in the first pane?).

## Triggers don’t save

TODO: There are usually 3 things that come up with triggers that don’t save.

1. So-called dynamic triggers don’t save. That is the something like Mail (**Get New Mail**) won’t save because the **Get New** action come from QS inspecting Mail.app (it’s not listed in the actions prefs). Or a trigger using the *Menu Bar Items...* action with the third pane filled in, won’t save.
2. Triggers are saved in `~/Library/Application Support/Quicksilver/Triggers.plist` if the permissions of that file or directory don’t allow you to write, then no trigger will be saved. There have also been reports of this file becoming corrupted.
3. If you have triggers using actions from some plugin and then uninstall that plugin, the triggers remain and QS can be confused. Sometimes a particular trigger doesn’t display, sometimes only one of many triggers appears in the prefs. To fix, reinstall the needed plugins, delete the related triggers, then remove the plugin.

## Leopard Specific Things

### Removing Time Machine items from Catalog

Uncheck the backup drive in Preferences → Catalog → Devices → Disks → Show Info → Contents. Then rescan the catalog by clicking the curved arrow button at the bottom of the catalog or by activating QS with <kbd>⌃</kbd><kbd>Space</kbd> (or <kbd>⌘</kbd><kbd>Space</kbd> or whatever you use) and then typing <kbd>⌘</kbd><kbd>R</kbd>. Also make sure Find All Applications is not checked in the catalog, that scans every connected drive.

### LockScreen in Extra Scripts doesn’t work

Start the screen saver and have 'Require password after ScreenSaver’ in your Security prefs

### iCal Plugin doesn’t give access to other calendars

### Show Menu Items doesn’t work for some applications

Fails: TextMate, NetNewsWire

Works: Colloquy

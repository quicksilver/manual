#User Interface

Access the menus and windows of running applications.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 2.2.1
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


## User Interface Plugin

This plugin adds the ability to search for and manipulate running applications
(processes), application windows, and application menu items from Quicksilver.

Access for assistive devices **must** be enabled in 'Universal Access' pane of
System Preferences to use this plugin.

### Processes

Processes represent applications which are currently running on your Mac. Any
application in Quicksilver's catalog can be used as a process if that app is
running. The following actions are available for processes:

  * **Show Menu Items** – Generates and displays a searchable list of the app's menu items.
  * **Show Windows** – Generates and displays a list of the app's windows, searchable by window title.
  * **Focused Window** – Fetches and displays the app's focused window – this is usually the most recently used window, and the window which would get keyboard input if you started typing.
  * **Current Document** – Fetches and displays the file which corresponds with the document open in the app's focused window.

Selecting these objects in the second pane causes the third pane to display
the results:

  * **Windows…** – Generates a list of the app's windows, searchable by window title. Pressing return on one of these windows is equivalent to using the Activate action on it.
  * **Menu Bar Items…** – Generates a searchable list of the app's menu items. Pressing return on one of these menu items is equivalent to using the Press action on it.

### Windows

Windows can also have several actions performed on them (you can view a full
list in the [Actions preferences](qs://preferences#QSActionsPrefPane) by
selecting 'Application Windows' from the dropdown types list). Several of the
actions also have alternate actions (which can be executed with ⌘↩), you can
see these in the same place in the Actions preferences:

  * **Select Application** \- shows the application for the selected window in Quicksilver
  * **Activate Window** – Focuses the window, then makes all windows belonging to the app appear in front of all other windows.
  * **Raise** – Makes the window appear in front of all other windows, without changing which app is focused.
  * **Close** – The same as pressing the red Close button in the window's title bar.
  * **Minimize Window** – The same as pressing the amber Minimize button in the window's title bar.
  * **Zoom** – The same as pressing the green Zoom button in the window's title bar.
  * **Show Menu Items & Menu Bar Items...** \- See above (Processes section). These actions work just the same as for processes, except they show the menu bar items for a specific window. Menu bar items may be different for each window, so this is useful for selecting items specific to one window.

_Note: The 'Close', 'Minimize' and 'Zoom' actions work with the comma trick,
allowing you to manage multiple windows at once_

### Menu Items

Menu Items only have one action available: **Press**. This has the same effect
as clicking the menu item. To better indicate where Menu Items have come from,
their details will show the full Menu path. For example: "Edit ▸ Find ▸ Find…"

### Triggers

When this plugin is installed, the following triggers are available in the UI
Access section of the Triggers preference pane:

  * **Show All Menus** – Generates and displays a searchable list of the menu items of all running apps, grouped by app.
  * **Show All Windows** – Generates and displays a list of the windows of all running apps, searchable by window title and app name.
  * **Current Application** – Fetches the current app, places it in the first pane of the command window, and selects the second pane of the command window.
  * **Current Focused Window** – Fetches the current app's focused window, places it in the first pane of the command window, and selects the second pane of the command window.
  * **Current Document** – Fetches the document open in the current app's focused window, places it in the first pane of the command window, and selects the second pane of the command window.

### Proxy Objects

When this plugin is installed, the following proxy objects are available in
the Proxy Objects source in the Quicksilver section of the Catalog preference
pane:

  * **Current Focused Window** – Represents the current app's focused window. The current app is whichever app currently has it's name in the menu bar. The focused window is usually the most recently used window, and the window which would get keyboard input if you started typing.
  * **Current Document** – Represents the file which corresponds with the document open in the current app's focused window.
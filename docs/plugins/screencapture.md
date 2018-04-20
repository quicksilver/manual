# Screen Capture

A set of actions that allow capturing the screen.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 1.7.0
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


## Screen Capture Plugin

This plugin adds support for using Grab.app to capture portions of your
display to image files, which can then be manipulated by Quicksilver. In order
to see the objects added by the Screen Capture Plugin (they are visible in
Quicksilver's first pane), you must enable the "Internal Commands" catalog
entry, found in the [Catalog Preferences](qs://preferences#QSCatalogPrefPane)
under the "Quicksilver" side tab.  

Note that all pictures captured with the Screen Capture Plugin are also saved
to your Desktop.

### Command Objects

**Capture Region**

This command object (run from Quicksilver's 1st pane) enables Grab.app in its
"Capture Selection" mode. A cross hair is displayed on screen allowing you to
drag a rectangle around what you want captured. Once complete the captured
region is returned to Quicksilver.

**Capture Window**

Similar to the 'Capture Region' command object, 'Capture Window' gives you
allows you to capture a whole window, and return the corresponding image to
Quicksilver

**Capture Screen**

The 'Capture Screen' command object takes a screenshot of your current screen
and returns it to Quicksilver.

### Trigger Events

Event Triggers can be run whenever an image is captured using this plug-in.
The "Event Trigger Object" will refer to the image's file.
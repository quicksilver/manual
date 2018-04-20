#Firefox

Bookmarks & History for Firefox.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 1.0.1
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


### Firefox Plugin

This plugin gives you access to your Firefox bookmarks and history for more
recent Firefox versions (3.0 and later). It also provides a "Current Web Page
(Firefox)" proxy object.

This plugin adds a "Firefox" catalog group, with "Firefox Bookmarks" and
"Firefox History" as subentries.

**Firefox Bookmarks** includes all the URLs you bookmarked, without any folder
structure or tags you might have applied.

**Firefox History** contains the last 200 URLs you visited.

This is disabled by default, but can be enabled easily in the catalog section
of the preferences.

The history is limited to the most recent 200 URLs, so the Quicksilver catalog
doesn't get too large. With too many items in the catalog, Quicksilver slows
down considerably.

If this isn't enough of your browsing history and Quicksilver still feels fast
enough, you can change this number. Currently there is no user interface for
it, but you can change it manually. Got to:

  * Go to `~/Library/Application Support/Quicksilver/PlugIns/`
  * find `com.blacktree.quicksilver.QSFirefoxPlugin.*.qsplugin`
  * right-click -> "Show Package Contents"
  * then open `Contents/Info.plist`
  * In there, find the entry `QSPresetAdditions -> Item 0 -> children -> Item 1 -> settings -> historySize`
  * change the number to something different.

After restarting Quicksilver and rescanning the catalog, the new settings will
be applied. Sorry for the inconvenience. Maybe there'll be a user interface
for that in the future.

**Current Web Page (Firefox)**

The plugin also adds a proxy object that contains the webpage you have
currently open in Firefox. It's called " **Current Web Page (Firefox)** " and
works just like the one for Safari. One limitation though: There might be a
slight delay. Firefox only updates this information every few seconds (every
15 seconds by default, I believe), and the proxy object only has access to
this delayed information. For me, this was rarely a problem. But if you really
need to reduce this delay, you can do this by changing a hidden preference in
Firefox. To do this:

  * type `about:config` in Firefox's address bar. (You'll get to a page where you can modify all kinds of weird options for Firefox. Don't mess with them, unless you know what you are doing!)
  * Now type `sessionstore.interval` in the filter-field.
  * The `browser.sessionstore.interval` value is in milliseconds. Change it to something smaller. But making it too small might slow down Firefox. So be careful!
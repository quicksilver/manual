# Catalog

The Catalog is the collection of items indexed by Quicksilver during its periodic scans. You  populate it by configuring catalog sources which Quicksilver periodically indexes. This is done in the Catalog panel. You can bring it up from the menu or by activating Quicksilver and typing <kbd>⌘</kbd><kbd>;</kbd>.

Catalog sources are configured into sets shown in the left panel. Many plugins (and Quicksilver itself) provide catalog presets. These are pre-configured catalog entries that you might find useful. Presets can’t be altered, but you can copy one, customize the copy, and disable the original. You can also manually add your own entries. Anything you add or copy from a preset will appear under Custom.

The checkbox enables or disables the entry. Enabled entries that have been indexed show the number of items found. Note that not all entries are enabled by default after plugins are installed.

At the bottom of the window you can configure how frequently Quicksilver rescans the catalog sources to find (and remove) items. The default is 10 minutes. This might seem too short, but give it a try before adjusting it. Quicksilver isn’t going to bog down your system with a full rescan every 10 minutes. Instead, it only asks the catalog source for each entry whether or not it _needs_ to be scanned again. The answer is almost always “no”, so very little ends up happening unless there’s a reason. For example, your Applications folder will only be scanned if its modification time is more recent that the last scan.

The Refresh button will manually rescan a selected catalog source. You can manually rescan the whole catalog with the Rescan Catalog command in the Quicksilver menu (only if you have the Dock icon visible) or more conveniently by typing <kbd>⌘</kbd><kbd>R</kbd> after activating Quicksilver. Some interfaces (e.g., Bezel) will show a spinner icon while rescanning the catalog. You can also configure the Task Viewer to show automatically during a catalog rescan. Show the Task Viewer by selecting it from the Window menu (if the Quicksilver Dock icon is enabled) or by typing <kbd>⌘</kbd>K after activating Quicksilver. The gear menu in the top right (which is there even if it’s not visible in some interfaces) will let you configure two options: Show Automatically and Resize Automatically. The Task Viewer isn’t all that useful as things usually just work. It could be used to notice when Quicksilver is doing rescans or perhaps to help troubleshoot a slow catalog source (if you’ve configured a file scan to be too deep).

With a source selected click on the ⓘ button to show a drawer with three tabs:

  * **Source Options** - Varies based on the kind of source. A file source allows you to configure depth of scan and file types to be included. See below for details.
  * **Contents** - The list of all items found by indexing this source. You can remove a specific item by unchecking it.
  * **Attributes** - Provides some info about the source and allows you to enable it and change the name. Include in Global Catalog is whether the source is enabled or not and is the same as the checkbox in the main Catalog panel. Presets have a Create Copy button that will duplicate the source to the Custom catalog set, allowing you to change the source options. 

To find out what catalog source an object comes from, bring up the object in the first pane and use the **Show Source in Catalog** action; the Catalog window will open with the source of the object selected. If the catalog contains unwanted items, this is a way to track down what sources you want to modify or remove. 

Using the + and - buttons in the Custom set you can add and remove additional catalog entries. The + button will show a drop down menu of various source types (aka scanners) which varies based on the plugins installed. Note that some plugins provide presets in the Plugins set and others provide new scanner types, while some provide both. When trying to determine what a new plugin does, remember to check both places (or read its documentation).

## Proxy Objects

Proxy objects are items in your catalog that refer to another object that could change at any time. They are one of Quicksilver’s more powerful features. Some examples will probably make it easier to understand than a description.

  * Current Web Page
  * Finder Selection
  * Latest Download
  * Currently Playing Track
  * Current Selection (text, files, tracks and playlists in iTunes, etc.)

Proxy objects allow you to do things like e-mail the selected files to a coworker, paste the URL of the page open in your browser, assign a rating to the currently playing track, or move the latest download to another folder. You can do all of that without switching apps, copying, selecting, dragging, etc.

If you’re now convinced that proxy objects are amazing, you probably want to know what other proxy objects are available. Open the Catalog, select the Quicksilver set and then select Proxy Objects source, click the ⓘ button at the bottom to open the drawer and look at the Contents tab. Note that some third party plugins might install additional proxy objects.

It’s obvious from the name what most of them do, but the usefulness of some might _not_ be so obvious.

The Quicksilver Selection might seem silly. If you already have something selected, why do you need a proxy for it? Some proxy objects, like this one, are really only useful (but extremely so) as part of [Triggers](triggers.md), which are discussed in a bit.

## Synonyms

Synonyms allow you to assign another name to an object in your catalog. Remember that you can only assign an abbreviation to something if those letters appear in the name. So you can’t use <kbd>I</kbd><kbd>R</kbd><kbd>C</kbd> to launch Colloquy, for instance. But you can create a synonym for Colloquy called “IRC Client” and search for that instead.

Some other examples:

  * Your muscle memory hasn’t adjusted since Apple renamed Address Book to Contacts, so you could create “Address Book” as a synonym for Contacts.
  * If you’re used to Windows and can never remember the name of that text editing app, create a synonym called “Notepad” that points to TextEdit.

Synonyms act just like the object they refer to, so they will have the same icon, the same children, and the same actions will be available in the second pane.

To create a synonym:

  1. Go to Preferences → Catalog
  2. Click the + button at the bottom of the window
  3. Choose “Synonym”
  4. In the panel that appears, type a name for your synonym and hit <kbd>↩</kbd>
  5. Click the search widget to search the catalog just like you would in Quicksilver’s main interface.
  6. Once the desired object is selected, you can close the Preferences window

## Preset Details

The **File & Folder Scanner** lets you add folders to scan into the catalog. You can also just drag folders into the main catalog pane to add a source.

A common thing to want to do is to scan the `~/Documents/` folder deeper than the depth of 2 the default source uses (in the User set). To do this, select the Users set and the Documents source, open the drawer and select the Attributes tab. Click on Create Copy to create a new source in Custom named Documents. The difference is that the Source Options tab of it is editable. Change the depth slider to what you want. Many people just select infinity but this is never recommended. Your indexes will take longer and your catalog will be huge which will slow Quicksilver down. Also if you have many extra items in your catalog your searches are more likely to contain useless noise. Remember that you can always navigate to any file in Quicksilver (see the [Files and Folders](../features/Files and Folders.md) section), so all you need in your catalog are your more commonly used files.

You probably don’t want to just index your entire home directory. `~/Library` alone has many preference and cache files that you don’t want indexed, and the Music and Pictures folders are better served by the iTunes and iPhoto plugins.

The File & Folder Scanner can also scan the _contents_ of files to add to the catalog. The scanner can recognize either HTML links or text lines depending on the setting of the Include Contents popup. Text lines are ["sniffed"](../features/Text.md#string-sniffing) to see if they can be converted into anything useful.

The Applications set has 4 sources defined. The Applications (User) source indexes `~/Applications/` to a depth of 3 but also only finds the applications, not the intervening folders. If you want those in the catalog so you can easily move an application into them (e.g., `~/Applications/Games/` and `~/Application/Browsers/`), the Types field in the Source Options tab is useful for this. If you type file extensions (e.g., `.txt`, `.c`, `.doc`, etc.) into it you can filter the kinds of files indexed. You can also enter Mac Type Codes surrounded by single quotes and type tab to have it interpreted.

So, to get applications entered as it is in the pre-configured source, enter `'APPL'` (including the single quotes). In this example, you want folders, so enter `'fold'` and type tab and it’s replaced with “folder”. You can choose a depth of 1 to include the Games and Browsers folders but not folders that some applications come with (or the Contents folders inside the `.app` packages).

Note that the Find All Applications source under the Applications set will search the whole system for application packages. It also indexes any external drives connected. Be aware that allowing Quicksilver to index things on an external drive might cause performance problems and other strange behavior.

The Spotlight object source allows you to add files to the catalog if they match a Spotlight query. See the Spotlight plugin’s documentation for a discussion of the syntax.

The Defaults Reader allows you to index some keys from Property List (`.plist`) files, though it’s a little flakey (doesn’t deal well with paths), is difficult to configure (you must manually specify each key) and doesn’t let you change the plist file.

The Group type is just a a folder for custom catalog sources to be able to group many custom sources in the catalog preferences to make them easier to read.

Additional catalog sources are described elsewhere in this manual.

## Plugin Catalog Sources

The types of items Quicksilver can add to its catalog can be extended through plugins. The table below shows a few (but not all) of the plugins that add new catalog sources.

![Adding a catalog source](../images/addcatalog.png)

| Plugin | Added Catalog Source | Description |
| --- | --- | --- |
| Built in | Synonym | Allows you to specify a new name for an item in Quicksilver's catalog by providing a synonym. E.g., you could create a synonym for "Sparrow.app" called "Mail" so that when you search for "Mail" you can select "Sparrow.app". |
| Web Searches Plugin | Web Search List | Allows Quicksilver to catalog Web Search URLs for searching websites. The URL you enter must contain `***` in place of the search string. E.g., for a Web Search on Google.com, the Search URL would be `http://google.com/search?q=***`. |
| Remote Hosts Plugin | Remote Hosts | Allows you to define a file which Quicksilver scans for "Remote Host" items. See the Remote Hosts documentation for more information. |
| Spotlight Plugin | Spotlight | Add files to the catalog based on a Spotlight search. You define the Spotlight query and limit the search to a specific folder. |

In the Quicksilver set there is a source called Quicksilver Catalog Entries. If enabled, an item is added to the catalog for each source configured. These items have names that end with “(Catalog)”. You can select one of these items in the first pane and then type <kbd>→</kbd> to navigate through just that source. If you want to do this often, create a trigger. E.g., the trigger Applications (Catalog) (**Show Contents**) lets you search through just the applications in your catalog (well those that are found via this catalog source). While you can often do this just by typing <kbd>→</kbd> into an object, if you have custom sources configured (say for files of a particular project) this can be very handy.


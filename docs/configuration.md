# Configuration

Quicksilver has a configuration window that provides access to the Guide, Preferences, Triggers, Catalog and Plugins. These can be accessed several ways:

1. The easiest is to activate Quicksilver (with <kbd>⌃</kbd><kbd>space</kbd>) and then use the standard shortcut <kbd>⌘</kbd><kbd>,</kbd> to bring up preferences or use one of these other shortcuts:

| Shortcut | Action |
| --- | --- |
| <kbd>⌘</kbd><kbd>?</kbd> | Open Guide |
| <kbd>⌘</kbd><kbd>,</kbd> | Open Preferences |
| <kbd>⌘</kbd><kbd>;</kbd> | Open Catalog |
| <kbd>⌘</kbd><kbd>’</kbd> | Open Triggers |
| <kbd>⌘</kbd><kbd>”</kbd> | Open Plugins |

2. In the main command window select one of the Internal Commands: Show Guide, Show Preferences, Show Trigger Preferences, QS Catalog Preferences, Show Plugin Preferences and use the Run action.

3. Click the Quicksilver dock icon and Quicksilver’s menu appears, look unde Quicksilver.

4. If the menu bar icon is enabled, a menu is available by clicking on it

5. Right-click the Quicksilver icon in the Dock.

The following sections describe these preferences. First global preferences that affect how Quicksilver is activated and appears and then sections on Plugins, the Catalog, Actions, Handlers, and Notifications. Triggers are a large topic and are covered in their own entire section immediately after this one.

Configuring new Quicksilver features is usually done by installing the relevant plugin. Sometimes there are additional things to configure such as enabling new catalog sources, new actions (under Preferences, Actions) or relevant Handlers (under Preferences, Handers). Finally some plugins add their own preference panels listed in the lower left area of the Preferences window.

# Preferences

Quicksilver’s Preferences are divided into sets at the left of the window. Those listed at the top are built-in to Quicksilver and those in the bottom section are enabled by installed plugins.

The Application Preferences control the most fundamental aspects of Quicksilver as an application. Once you’re hooked on Quicksilver you’ll want to enable “Start at login”. 

Quicksilver shows an icon in the Dock like most applications, but many people prefer to disable this. Uncheck the box to disable the Dock icon. The ⌽ symbol indicates Quicksilver must be restarted before the change will take affect. The easy way to restart is to activate Quicksilver (<kbd>⌃</kbd><kbd>space</kbd>) and then type <kbd>⌃</kbd><kbd>⌘</kbd><kbd>Q</kbd>

Without a Dock icon, Quicksilver runs as a background process. This means it won’t appear in the Dock or when switching apps with <kbd>⌘</kbd><kbd>tab</kbd> and the main Quicksilver menu will not appear while the preference window is open. I tend to keep it in the Dock so that it’s easy to restart if Quicksilver crashes (though this is less of a problem as of 1.0). 

The “Show icon in menu bar” preference puts an indicator in the top right part of the screen, some people like this, particularly if they don’t configure a Dock icon or have their Dock hidden. It provides a simplified menu to access the various configuration panes of Quicksilver. For access to the full menu options (via more sub-menus) set the option “Include access to all menu items from menu bar”. 

The next section controls if and how Quicksilver checks its website automatically for updates both for updates to Quicksilver and for all installed plugins. It can be configured to check on launch, daily, weekly or monthly. The Check Now button will, not surprisingly, check immediately for an update. 

The three buttons at the bottom will rerun the installation setup described in the [Installation](introduction#Installation) section, Reset Quicksilver’s preferences, and completely Uninstall Quicksilver.

The Appearance Preferences control how Quicksilver looks. 

The command window  supports various skins or themes, known as Interfaces and installed via plugins (all of which end with the word Interface). Select the Interface to use here via the popup list showing all installed Interfaces. See the Interface section below for details.

The default interface is Primer and it shows a little more context information than other interfaces so it’s recommended for new users. The other builtin interface is Bezel interface; it’s very popular and is shown throughout this manual. 

The Superfluous visual effects vary per interface but include the command window unzipping open and fading closed.

The Colors options allow further customization of the appearance of the interface and vary per interface. The column headers have tooltips showing what they represent: Background, Selection & Accents, and Text colors. Clicking on the nine colors in the grid will bring up a color picker.

The Command Preferences allows configuration of the command window’s behavior. 

The top of the pane affects how you activate Quicksilver. The Keyboard Activation is the basic way to activate Quicksilver. The default is to type <kbd>⌃</kbd><kbd>space</kbd>, though as shown a common alternative.

TODO: The shortcut is configurable in the Command Preferences Pane under Activation. Quicksilver defaulted to <kbd>⌘</kbd><kbd>space</kbd> for a long time and then in 10.4, Apple chose to use <kbd>⌘</kbd><kbd>space</kbd> for Spotllght. So Quicksilver changed its default to <kbd>⌃</kbd><kbd>space</kbd>. If you look at older posts on the Web you’ll often see <kbd>⌘</kbd><kbd>space</kbd> used to activate Quicksilver. Since I use Quicksilver a lot more often than Spotlight (and anything without <kbd>⌘</kbd> conflicts with Emacs), I use <kbd>⌘</kbd><kbd>space</kbd> for Quicksilver and <kbd>⌥</kbd><kbd>⌘</kbd><kbd>space</kbd> for Spotlight (set in the Spotlight System Preference pane of macOS). Another advantage is that many shortcuts used after activating Quicksilver use <kbd>⌘</kbd>, so using the same modifier key is easier. For example, <kbd>⌘</kbd><kbd>,</kbd> (that’s <kbd>⌘</kbd><kbd>comma</kbd>) will open up Quicksilver’s Preferences (as it will in most applications). I find it easier to type <kbd>⌘</kbd><kbd>space</kbd> <kbd>⌘</kbd><kbd>,</kbd> than <kbd>⌃</kbd><kbd>space</kbd> <kbd>⌘</kbd><kbd>,</kbd> because I don’t have to change modifier keys.

“Modifier-only Activation” allows you to activate Quicksilver by single or double presses of modifier keys such as <kbd>⌃</kbd>, <kbd>⌥</kbd>, <kbd>⇧</kbd>, <kbd>⌘</kbd> or even <kbd>fn</kbd> on a laptop. Some applications can call for secure text entry and this can interfere with modifier only activation. If you use Visor and a double shift modifier isn’t working for you, open Terminal.app and in the File menu enable “Secure Keyboard Entry”. There have also been reports that Quicken Scheduler app that runs in the background as a login item to do scheduled downloads can also interfere with modifier only activation.

“Hide if pressed when already visible” affects what happens if you activate Quicksilver when it’s already active. Regardless of the setting of this option, typing <kbd>⎋</kbd> will close the command window.

The “Alternative Services Menu Key” is how to change the shortcut assigned to the Quicksilver service Get Current Selection. The default value is <kbd>⌘</kbd><kbd>esc</kbd>, so you might want to change it if you use Front Row as described above in [Invoking Quicksilver](introduction#invoking-quicksilver).

The bottom of the Command Preferences pane affects how the results list window appears. You can specify the Row Height in pixels. A higher value will show a larger image on each row. A lower value will result in a single line per entry. The info displayed in the 2nd line for the selected entry will be shown in the bottom of the window.

Selecting “Show children split view” will split the results list vertically into two columns, the right one showing the contents of the selected item in the left one (much like the column view of the Finder). You must restart Quicksilver for changes to this setting to take effect. When first enabled you’ll only see one column, but notice the small dot in the middle of the right edge, you can click on and drag that to the left to reveal the second column.

“Show other matches” controls if the results list appears after you type into the command window immediately, after a short delay or not until you type <kbd>↓</kbd>. By virtue of Quicksilver’s matching algorithm, the spacebar isn’t particularly useful in the command window. The “Spacebar behavior” preference lets you reclaim that key to make Quicksilver a little faster to use. You can configure it to:

- Normal - literally type a space and include it in the search term
- Select Next Result - select the next result in the results list, like typing <kbd>↓</kbd>
- Jump to Argument List - change to the third pane
- Switch to Text Mode - change the current pane to text mode entry, like typing <kbd>.</kbd> or <kbd>‘</kbd>
- Show Item’s Contents - goes into the item, like typing <kbd>→</kbd> or <kbd>/</kbd>
- Quick Look - Show the selected file(s) using Quick Look
- Smart (default) - Select one of the above behaviors automatically based on context

The smart spacebar tries to be the best of all worlds and do what you probably want in any given situation. This is how it decides what to do:

- If in the second pane, select the first action that takes an argument in the third pane.
- If user is holding Shift, go to the parent (same as left arrow).
- If the object has children, show them (same as right arrow) unless it’s a text file.
- Jump to the third pane if the current action requires it. This is very useful for web searches.
- Quick Look if the object supports it.
- Switch to text mode.

Plug-ins can override the above where it makes sense. For example, iTunes tracks have children (genre, artist, and album). According to the above rules, spacebar would act like right arrow and show them, but the iTunes plug-in tells the smart spacebar to use Quick Look instead.

“Switch to text mode if no match is found” will allow you to save typing <kbd>.</kbd> or <kbd>‘</kbd> to enter text mode in a pane. “Reset search after” lets you configure how much of a pause in typing into the command will start a new search as opposed to appending to the existing search.

The Extras Preferences have some advanced options.

“Application Update Type” allows you to choose between Prerelease Candidates and Final Releases when Quicksilver checks for updates as configured in the Application Preferences. Sometimes after installation this is set to a blank value and that has been observed to cause problems, make sure it’s set to some value in the popup.

“Application reopen behavior” configures what happens if you use the Open action on an application that is already running. You can have it activate the application, show the front window or show all windows.

Since the matching algorithm is case-insensitive the shift key is available for some use in Quicksilver. If you check “Capitalize Key modifies action in command window“ then shifted letters are used to select the action, eliminating the need to tab to the second pane. Once moved to the action pane, unshifted letters don’t change the first pane, all typing counts for the second pane. If you also hold down the <kbd>⌘</kbd> key the action will be performed immediately, no need to type return. E.g., <kbd>⇧</kbd><kbd>I</kbd> selects the action for i (perhaps **IM**) while <kbd>⇧</kbd><kbd>⌘</kbd><kbd>I</kbd> performs the action for i. Use caution as it’s not always clear which action is invoked.

If you prefer concentrating on one thing at a time, check “Hide other applications when switching” so that Quicksilver will do a “Hide Others” after switching applications. You can prevent the hiding behavior by holding down the shift key when completing the command. There have been problems reported with this feature that applications no longer appear when doing <kbd>⌘</kbd><kbd>tab</kbd>.

Normally <kbd>⌘</kbd><kbd>G</kbd> will take the Finder’s selection and put it into Quicksilver. By checking the “Pull selection from front application instead of Finder” option, it will use the same mechanism as <kbd>⌘</kbd><kbd>esc</kbd> and will pull the selection from whatever the active application is. See more details at [Invoking Quicksilver](introduction#invoking-quicksilver).

Checking “Run tasks in background” will do just that. E.g., if you use the **Compress** action it does the compressing in the background allowing you to do other things with Quicksilver immediately. However as of B51 some have reported some instability from using this option. E.g., some have reported that running the **Compress** action via a trigger with this option checked causes Quicksilver to hang during the compression.

Quicksilver has a small window that shows current status known as the Task Viewer. You can bring it up by activating Quicksilver (<kbd>⌃</kbd><kbd>space</kbd>) and typing <kbd>⌘</kbd><kbd>K</kbd>. Most people don’t use it. You can also check the “Show Task Viewer Automatically” option to have it appear when Quicksilver is performing tasks such as refreshing the catalog. There’s an image of it in the Catalog section below.

If you enable “Disable Keyboard Triggers when Quicksilver is focused” then keyboard triggers will not work while Quicksilver is activated (i.e., the command window is open). I have no idea why you would want to enable this.

## Interfaces

Interface plugins change the look of Quicksilver’s command window. Install them just like other plugins from the Plugins Preferences. Then select one of the installed interfaces in the Appearance Preference pane using the Command Interface popup. If you use a program like VNC to connect to different machines, you might want to configure them with different interfaces or change the colors on the interface to distinguish them.

The following screenshots show each of the six interfaces at full size so for comparison purposes. These are all the official interfaces available from the Plugins Preferences. 

- **Primer** - The default interface is large and provides more info to help you learn 
- **Window** - Like Primer but smaller and with less info
- **Mini** - Like Primer and Window but even smaller
- **Bezel** - Grey, horizontal panes. Very popular (used in this manual at reduced size)
- **Flashlight** - Looks like Spotlight and appears in top left corner of the screen
- **Menu** -- Fills the macOS menu bar with input panes, doesn’t support the comma trick (TODO make this a link to comma trick).
- **Cube** - A single square pane that rotates as you tab between the panes. Shown above are the first and third sides of the cube on this one command. Note that the order of the command parts (object, action, argument) changes on each side. It’s very slick seeing it rotate.

## Plugins

Quicksilver is designed with a central core that implements some basic functionality but most of the features are implemented in plugins. You can pick and choose which plugin functionality you want, but must install the plugins before that functionality is available. Managing the plugins including finding, installing, enabling, and removing is done entirely from within Quicksilver in the Plugins Preferences (though additional configuration in Preferences or the Catalog may be useful or necessary). You can bring it up from the menu or by activating Quicksilver and typing <kbd>⌘</kbd><kbd>”</kbd>.

The plugins are shown in the right pane, with a checkbox showing if they are enabled, a column showing the version number (which follow no consistent pattern) and the date the plugin was last updated. The left panel shows sets of plugins:

- **Recommended** - recommended for you based on a scan of what applications are installed in the machine.
- **Installed Plugins** - those plugins that are installed in ~/Library/Application Support/Quicksilver/PlugIns/. Only those that are checked are enabled, those not checked are installed, but disabled.
- **All Plugins** - all available plugins from the quicksilver.blacktree.com server. Checked plugins are installed and enabled, unchecked plugins are not installed. <kbd>⌥</kbd>-click on this to show some hidden built-in plugins like Core Support and E-mail Support.
- **Categories** - shows plugins collected into relevant categories by feature. Plugins can be in more than one category. Otherwise behaves like All Plugins, checked plugins are installed and enabled, unchecked plugins are not installed.

Checking a plugin will enable it, downloading and installing it if necessary. Selecting a plugin and clicking the ⓘ button will open a drawer with (usually limited) information about what the plugin does. Selecting one or more plugins and clicking the + button opens a pop-up menu of things you can do to plugins including install, download, copy, and delete. Delete is the only one you’ll typically use from this menu. The last three items in the menu are options you can enable or not. The ↻ button will refresh the list of plugins from [qsapp.com](https://qsapp.com/plugins.php). 

To disable a plugin, uncheck it. Its features will no longer be available but its code will still be loaded into memory. To clean up this memory (possibly fixing stability issues), restart Quicksilver. The plugin is still installed on disk (so it will appear unchecked in the Installed Plugins view) until it is deleted. So, to uninstall a plugin, select it from the list and choose the Delete Selected Plugins option from the menu.

If you expect to see a plugin in the list and don’t, try refreshing the list of plugins. 

If you’re having problems installing plugins check the ownership and permissions on `~/Library/Application Support/Quicksilver/PlugIns/` and its parent directory. Use the Finder’s Get Info command (from the File menu) to see the Ownership & Permissions of a folder. It should be owned by you and you should have permission to read and write it. Usually quitting Quicksilver and removing (or moving) the PlugIns folder or its parent Quicksilver folder and restarting Quicksilver (allowing it to recreate the folder) will solve any problems. Of course removing the Quicksilver folder will remove any customizations you’ve made.

Some people have reported that using the Little Snitch network monitor interferes with Quicksilver’s ability to download plugins. If your plugin list is empty and you run Little Snitch, try disabling it.

## Catalog

The Catalog is the collection of items indexed by Quicksilver during its periodic scans. You  populate it by configuring catalog sources which Quicksilver periodically indexes. This is done in the Catalog panel. You can bring it up from the menu or by activating Quicksilver and typing <kbd>⌘</kbd><kbd>;</kbd>.

Catalog sources are configured into sets shown in the left panel. Most are pre-configured by various plugins and many plugins add sources to the Modules set. The checkbox enables or disables the source. Enabled sources that have been indexed show the number of items found. Note that not all sources are enabled by default after plugins are installed.

At the bottom of the window you can configure how frequently Quicksilver rescans the catalog sources to find (and remove) items. The default is 10 minutes. The ↻ button will manually rescan a selected catalog source. You can manually rescan the whole catalog with the Rescan Catalog command in the Quicksilver menu (only if you have the Dock icon visible) or more conveniently by typing <kbd>⌘</kbd><kbd>R</kbd> after activating Quicksilver. Some interfaces (e.g., Bezel) will show a progress icon while rescanning the catalog. You can also configure the Task Viewer to show automatically during a catalog rescan. Show the Task Viewer by selecting it from the Window menu (if the Quicksilver Dock icon is enabled) or by typing <kbd>⌘</kbd>K after activating Quicksilver. The gear menu in the top right (which is there even if it’s not visible in some interfaces) will let you configure two options: Show Automatically and Resize Automatically. The Task Viewer isn’t all that useful as things usually just work. It could be used to notice when Quicksilver is doing rescans or perhaps to help troubleshoot a slow catalog source (if you’ve configured a file scan to be too deep).

With a source selected click on the ⓘ button to show a drawer with three tabs. Shown below are the tabs for the Desktop source selected in the above image.:

- Source Options - varies based on the kind of source. A file source (shown) allows you to configure depth of scan and file types to be included, see below for details. This is shown greyed out since the Desktop source is not configurable.
- Contents - the list of all items found by indexing this source. You can remove a specific item by unchecking it
- Attributes - provides some info about the source and allows you to enable it and change the name. Include in Global Catalog is whether the source is enabled or not and is the same as the checkbox in the main Catalog panel. Predefined sources have a Create Copy button that will duplicate the source in the Custom catalog set, allowing you to change the source options. 

To find out what catalog source an object comes from, bring up the object in the first pane and use the **Show Source in Catalog** action; the Catalog window will open with the source of the object selected. If the catalog contains unwanted items, this is a way to track down what sources you want to modify or remove. 

Using the + and - buttons in the Custom set you can add and remove additional catalog sources. You can also create custom sources via the Create Copy button in the Attributes tab of pre-defined sources. The + button will show a drop down menu of various source types (aka scanners) which varies based on the plugins installed. Shown at the right are all available scanners. Note that some plugins install catalog sources in the Modules set and others install new scanner types. When trying to determine what a new plugin does, remember to check both places (or read this manual).

The File & Folder Scanner lets you add folders to scan into the catalog. You can also just drag folders into the main catalog pane to add a source. A common thing to want to do is to scan the `~/Documents/` folder deeper than the depth of 2 the default source uses (in the User set). To do this, select the Users set and the Documents source, open the drawer and select the Attributes tab. Click on Create Copy to create a new source in Custom named Documents. The difference is that the Source Options tab of it is editable. Change the depth slider to what you want, I have mine at 3. Many people just select infinity but that’s probably not what you want. Your indexes will take longer and your catalog will be huge which will slow Quicksilver down. Also if you have many extra items in your catalog your searches are more likely to have extraneous results. Remember that you can always navigate to any file in Quicksilver (see the [Files and Folders](Files and Folders.md) section) so all you need in your catalog are your more commonly used files. Also you probably don’t want to just index your entire home directory. `~/Library` has many preference and cache files that you don’t want indexed and the Music and Pictures folders are better served by the iTunes and iPhoto plugins and their catalog sources. The File & Folder Scanner can also scan the contents of files to add to the catalog. The scanner can recognize either HTML links or text lines depending on the setting of the Include Contents popup.

The Applications set has 4 sources defined. The Applications (User) source indexes `~/Applications/` to a depth of 3 but also only finds the applications, not the intervening folders. I want those in the catalog so that I can easily move an application into them (e.g., `~/Applications/Games/` and `~/Application/Browsers/`). The Types field in the Source Options tab is what’s useful for this. If you type file extensions (e.g., `.txt`, `.c`, `.doc`, etc.) into it you can filter the kinds of files indexed. You can also enter Mac Type Codes surrounded by single quotes and type tab to have it interpreted. So, to get applications entered as it is in the pre-configured source, enter <kbd>'APPL'</kbd> (including the single quotes). In this example I want folders, so I enter <kbd>‘fold’</kbd> and type tab and it’s replaced with “folder”. I choose a depth of 1 to include my Games and Browsers folders but not folders that some applications come with (or the Contents folders inside the .app packages) . TODO: Some Type Codes are listed here.

Note that the Find All Applications source under the Applications set will search the whole system for application packages. It also indexes any external drives connected. Some people complain that when connecting drives to their machine the drives spin up. To prevent Quicksilver from causing this, uncheck the Find All Applications catalog source.

The QSSpotlightObjectSource allows you to specify a Spotlight query to find items to add to the catalog. See Apple’s documentation for Spotlight’s Query Expression Syntax (TODO) and Common Metadata Attribute Keys (TODO). Unfortunately in B51 this is buggy. It’s difficult to get one of these sources to scan and it sometimes goes into a loop continuously rescanning and using lots of CPU.

The Defaults Reader allows you to index some keys from preferences files (.plist), though it’s a little flakey (doesn’t deal well with paths), is difficult to configure (you must manually specify each key) and doesn’t let you change the plist file, so it doesn’t seem useful.

The Group type is just a a folder for custom catalog sources to be able to group many custom sources in the catalog preferences to make them easier to read. 

QSBackpackPluginSource, Stikkits, Web Search List, and Social Bookmarks are described in other places in this manual. 

In the Quicksilver set there is a source called Quicksilver Catalog Entries. If enabled, an item is added to the catalog for each source configured. These items have names that end with “(Catalog)”. You can select one of these items in the first pane and then type <kbd>→</kbd> to navigate through just that source. If you want to do this often, create a trigger. E.g., the trigger Applications (Catalog) (**Show Contents**) lets you search through just the applications in your catalog (well those that are found via this catalog source). While you can often do this just by typing <kbd>→</kbd> into an object, if you have custom sources configured (say for files of a particular project) this can be very handy.

Above is a screenshot showing all the catalog sources installed under Modules with all plugins installed in B51.

## Actions

TODO

## Handlers

Quicksilver not only makes it easier to work with a variety of applications, it sometimes uses other applications to perform commands. These are configurable in the Handlers Preferences pane. The list of handlers varies based on which plugins are installed. Shown here are all the handlers available as of B51.

- **E-mail** - Mail program to use for E-mail actions (Mail, Gmail, Entourage, or Mailsmith).
- **Instant Messaging** - IM program to use for IM and chat actions (iChat or Adium).
- **Command Line Interface** - Terminal program to use (either Terminal or iTerm) for Terminal actions .
- **String Ranker** - The TextMate Ranker plugin installs a different matching algorithm that can be selected here. See the TextMate Ranker section for details. As of B51 it’s known to cause problems selecting things in the 3rd pane.
- **File System Browser** - The Path Finder plugin installs a handler that can be selected here to have Quicksilver use Path Finder instead of Finder for some file system actions like Reveal.
- **Missing Object Selector** - This is installed by the Constellation plugin. It should be set to Quicksilver and not Constellation Menus.
- **Notification** - Display notifications with Quicksilver, Console or Growl. See the next section.

## Notifications

Quicksilver supports 3 different notification events:

- iTunes Track Changes
- Calculator Results
- Plugin Installation

These are typically displayed using Quicksilver’s built-in notification system which pops up a small window (shown at left for an iTunes track). In Handlers preferences under Notifications you can change to have notifications sent to the Console. If you install the Growl Notifier plugin you can instead choose to have [Growl](http://growl.info/) handle notifications. One limitation is that iTunes notifications generated by Quicksilver and displayed via Growl will not show the track’s rating. Ratings are shown when using Quicksilver’s built-in notifications. 

The Notifications Hub plugin allows finer granularity in configuring notifications. It adds a new preference pane called Notification Hub. There you can configure a default notifier as well as configure specific notifiers for specific events. E.g., iTunes notifications go to the Quicksilver built-in notification notifier while Plugin Installation notifications go to Growl. You can even send the same notification to multiple handlers by adding multiple lines for the same Notification and with different Notifiers. As of B54, The plugin is Intel-only and will not work on a PowerPC Mac.

# Triggers

## Trigger Basics

Triggers allow you to execute Quicksilver commands without having to use the command window. Quicksilver supports executing triggers by typing a keyboard shortcut, clicking or dragging the mouse, or (if you have the Abracadabra plugin installed) making a mouse gesture. Triggers are available whenever Quicksilver is running and you do not have to activate Quicksilver (with <kbd>⌃</kbd><kbd>space</kbd>) to use them. Triggers make it easier to control iTunes, launch applications, perform web searches, or do anything else Quicksilver can do. You can create as many as you want but you probably want them only for the operations you do frequently.

Your trigger configuration is stored in `~/Library/Application Support/Quicksilver/Triggers.plist`. This is useful to know if you want to have the same configuration on several machines, just copy the file between the machines while Quicksilver is not running. 

You define triggers in the Triggers Preference pane. You can go to this pane directly by activating Quicksilver and typing <kbd>⌘</kbd><kbd>’</kbd>. You’ll see several sets in the left side of the preference pane. Some triggers are predefined by Quicksilver itself or various plugins, e.g., you’ll find several in iTunes, and two in Quicksilver. Triggers you create will be in the Custom Triggers set. 

Prior to B51 the Constellation plugin installed its own trigger set with three triggers defined, but it no longer does so.. 

Each trigger is shown by its name which is usually a combination of the object and action to be invoked. The checkbox shows if the trigger is active. The <kbd>⌘</kbd> column shows the type of trigger, in this case they are all activated by a shortcut which is shown in the Trigger column (some are not assigned to keys). If you select a trigger and click on the ⓘ button at the bottom a drawer is revealed with various settings for the trigger. The settings tab looks different for each type of trigger (Gesture, Keyboard, or Mouse). Shown here is the one for a shortcut. You set the shortcut by clicking the Edit button and then typing whatever key you want. You can change the name of the trigger in the top text field. There are various other options to tailor the keystroke to behave exactly the way you want. These are described below.

You can change some options by clicking in the main trigger window. If you click on the command name you can get an edit field to change the name of the trigger. If you click in the Trigger column you can set or change the shortcut. If you click on the icon in the <kbd>⌘</kbd> column you can add another means (Gesture, Mouse) to activate the trigger. Though once you create an additional way, there doesn’t seem to be a way to delete it without deleting the entire trigger.

You create a new trigger by clicking the + button at the bottom and selecting a trigger type from the pop-up menu (Gesture, Keyboard, or Mouse, depending on installed plugins). The Group option is just a way to collect triggers in a group or folder. They don’t perform any function other than helping you organize a lot of triggers. You can’t activate all the triggers in a group at once. Create a Group from the + menu and drag triggers into it. 

Regardless of which type you choose, a special command window appears (populated with the last command you performed) to let you define the command for the trigger. Enter the command and click Save. Then open the drawer to the Settings tab to assign a shortcut, mouse click, or gesture to use to activate the trigger. If you’re creating a keyboard trigger, just click in the Trigger column for this new trigger, the drawer will open and you can just type the shortcut as if you had clicked the Edit button.

By default, triggers are available whenever Quicksilver is running, regardless of what application is active. They can also be limited to function only when a certain application is active or when a certain application is not active. You do this by opening the drawer for a trigger and choosing the Scope tab. The default is “Enabled in all applications” but you can also choose from the popup “Enabled in selected applications” or “Disabled in selected applications”. For the latter two you can type the name of the application into the large box and type tab after the name to have it turn into a blue button. You can then enter another application if you choose. Unfortunately as of B51, you cannot drag and drop an application into the pane.

One place I use this is for a BlogThis bookmarklet in Safari. Like any bookmarklet it is javascript, which in this case opens a small browser window with a blog entry form and the current URL filled in. Since Safari treats it as a bookmark I can’t easily assign a shortcut to it. So I have a Quicksilver keyboard trigger which opens that bookmark (it’s in the Catalog with the other Safari bookmarks) and I have the scope set to work only when Safari is active because it’s not useful in any other application. This way if I accidentally type the shortcut, nothing will happen. You should be able to configure different commands on the same shortcut scoped to different applications but in B51 it doesn’t seem to work.

Note if you have triggers that use certain features, be cautious about deleting the plugins that supply those features. In particular if you have triggers using mouse gestures from Abracadabra (see below) and if you remove the Abracadabra plugin, the trigger panel may display oddly with some blank lines and missing icons. To correct this, reinstall the plugin (Abracadabra in this case), remove the triggers, and uninstall the plugin.

The following sections discuss each type of trigger with many examples. The commands used will come from many different plugins not covered here. If you want more information on them, look in the relevant sections in Part III of this manual. While you have a lot of freedom in defining triggers anyway you want, some commands are better suited to certain trigger types.

Keyboard Triggers are the most commonly used and are described first. Proxy objects make triggers far more powerful and are described next. Mouse triggers are covered next along with Abracadabra gestures. Related to using the mouse are Constellation menus and regular context menus, so they are described net. Finally using and saving command objects, and droplets is described.

## Keyboard Triggers

If you enter a complete command into the trigger, like choosing an application and the Open action, it will be run when you execute the trigger. If you choose just a partial command, like a web-search and the **Search For…** action, when you execute the trigger a command window will appear with as much filled in as your trigger defines. You can’t have gaps (e.g., you can’t leave the first pane blank and use the **Get Info** action). This is discussed more below. Triggers are given a default name based on the command they represent. Here are some examples:

### Safari (Open)

The most common simple trigger created is to open an application. Shown here is a trigger to open Safari, it’s just the Safari application in the first pane and the **Open** action in the second. The argument is blank. Notice that when the action is **Open** the default name for the trigger is Open followed by the application. Usually the default name is the object followed by the action in parenthesis. **Open** is special, probably because it’s so common. If in the Extras Preferences you have Application reopen behavior set to activates, then using this trigger when Safari is already running will make it the active application. 

You can obviously make similar triggers to open your favorite applications. Some people create other triggers like Safari (**Quit**) or Safari (**Hide Others**) and put them on the same keys but with different modifiers (e.g., <kbd>⌥</kbd> or <kbd>⇧</kbd>). Others just use the standard macOS shortcuts of <kbd>⌘</kbd>Q and <kbd>⌥</kbd><kbd>⌘</kbd><kbd>H</kbd> to run these on the current application.

### Shelf (Show Contents) and Clipboard History (Show Contents)

The Shelf and Clipboard History are enabled with the Shelf Module plugin and the Clipboard Module plugin respectively. Each enables a window that you typically access with the mouse (see Clipboard and Shelf for details). To get keyboard access to these, first enable the objects in the Catalog under Quicksilver and Shelf & Clipboard (check the box and click the rescan button). If you select these objects in the first pane, you can type <kbd>→</kbd> or <kbd>/</kbd> to open a new results list with their contents. The **Show Contents** action is the equivalent of this and since it’s an action, unlike using <kbd>→</kbd>, you can use it in a trigger. So this trigger will open the shelf in a results list, with the first item selected, and let you type to select any item on the shelf (or the Clipboard History if you use that object). You can also use the **Search Contents** action which is very similar but won’t select the first time and won’t show a results list at first. I prefer **Show Contents** because it has more feedback. You can also use this technique to create a trigger to anything you can type <kbd>→</kbd> into, such as Contacts, iTunes, your Documents folder, etc.

### Wikipedia Quicksearch (Search For…)

Some actions take an argument in the third pane and triggers can use these too. The **Search For…** action will search some web site for the text entered as an argument. See the Web Searches section for the details of using this action. A trigger for a commonly used web search, such as Wikipedia, is very useful. If you specified the argument in the trigger it would search for the same text each time it’s run. However, if you leave the third pane blank, then when the trigger is run, Quicksilver will open a command window with the first two panes filled in (in this case with Wikipedia Quicksearch and **Search For…**), and the third pane selected, ready for you to type the query. Quicksilver is also smart enough to realize that the **Search For...** action wants a text argument and puts the third pane in text mode for you. It even fills in the default text from the OSX Shared Find Clipboard (which you can set in many Cocoa applications with <kbd>⇧</kbd><kbd>⌘</kbd><kbd>E</kbd>). Note, if the third pane isn’t empty when you create the trigger and you want it to be, you can type <kbd>⌘</kbd><kbd>X</kbd> to cut out whatever is there.

I have this trigger configured on the shortcut <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd>. I type <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd>, the query and return and the browser opens with the search results. If I want to search for some text in a document, I can select the text, copy it with <kbd>⌘</kbd><kbd>C</kbd>, type <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd> and then paste the text with <kbd>⌘</kbd><kbd>V</kbd> and type return. That’s pretty easy, but in the next section you’ll see how a proxy objects reduce this to one step.

## Proxy Objects

For this section make sure Proxy Objects are enabled in the Catalog under Quicksilver. Proxy objects are a special kind of object that stands for (or proxies) something else that changes. Having an unchanging object represent something that changes allows you to use it when you don’t know what it will be ahead of time. Here are some more example triggers to make that clearer

### Current Web Page (Paste)

This example lets you paste the URL of the page Safari is displaying into any other application without switching applications and without having to do a copy step. I have it bound to <kbd>⌃</kbd><kbd>⌘</kbd><kbd>F</kbd> and use it all the time to paste an URL into mail messages, chats, documents, iCal events, etc. The magic is because of the Current Web Page proxy object used in the first pane. It acts like a placeholder for the URL Safari will be displaying when I use this command. When the command is run, this proxy object asks Safari what it’s currently displaying and uses that in the command. Proxy objects allow your triggers to be dynamic and are one of the most powerful features of Quicksilver.

Note the Current Web Page proxy object is poorly named. It should be called Current Safari Page because it doesn’t use the default browser but only Safari (it’s defined in the Safari Module plugin so install that if you don’t see it). If you use OmniWeb you can use the OmniWeb Active Page proxy object. Unfortunately as of B51 there are no equivalent proxy objects for other browsers.

### Current Selection (Find With…) Wikipedia Quicksearch

The Current Selection proxy object gets the selection from the frontmost application. It uses a service internally so it only works with Cocoa applications (e.g., Safari, Mail, Preview, iWork, etc.). That’s most modern Mac apps but the notable exceptions are MS Office and Firefox (try Camino instead). Still, it’s remarkably useful.

It should be possible to use this proxy object as the argument in the Wikipedia search trigger above, so that you could select text in some Cocoa application, invoke the trigger, and have the search run. However in B51 I can’t get Current Selection into the third pane (even with pasting). But the **Search For…** action has a complementary action called **Find With…** that takes the query text as the object and the search site as the argument. I have a trigger of the Current Selection proxy object with the  **Find With…** action and the Wikipedia Quicksearch argument bound to the shortcut <kbd>⇧</kbd><kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd>. 

It’s useful to assign triggers to shortcuts in some pattern so they are easier to remember. I use <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd> to search Wikipedia for text I enter, and I add <kbd>⇧</kbd> to the sequence to search for selected text. I have similar pairs of triggers for other quick searches such as Google (<kbd>⌃</kbd><kbd>⌘</kbd><kbd>G</kbd>), IMdB (<kbd>⌃</kbd><kbd>⌘</kbd><kbd>F</kbd>), and Amazon (<kbd>⌃</kbd><kbd>⌘</kbd><kbd>Z</kbd>). These triggers are some of the most frequent ways I use Quicksilver.

If you’re now convinced that proxy objects are amazing, you probably want to know what other proxy objects are available. Open the Catalog, select the Quicksilver set and then select Proxy Objects source, click the ⓘ button at the bottom to open the drawer and look at the contents tab. Or you can look at the table below which organizes them into similar categories. Note that some third party plugins might install additional proxy objects.

- iTunes
    - Album Now Playing
    - Artist Now Playing
    - Current Playlist
    - Current iTunes Selection
    - Selected Playlist
    - Track Now Playing
- Finder
    - Finder Selection
    - Mounted Disks
    - Network Disks
    - Removeable Disks
- iPhoto
    - Current iPhoto Selection
    - Selected iPhoto Album
- Quicksilver
    - Clipboard Contents
    - Current Selection
    - Current Web Page
    - Last Command
    - Last Object
    - Quicksilver Selection
- Mouse
    - Mouse Trigger
    - Dragged Object
    - Droplet Item
- Applications
    - Current Application
    - Previous Application
    - Hidden Applications
    - Visible Applications

It’s obvious from the name what most of them do, with a few exceptions. The Current Web Page proxy object really should be called Current Safari Page. The Mouse ones are covered below. The Quicksilver Selection proxy object represents what is in the object pane (aka first pane). This allows you to assign shortcuts to particular actions (or actions and arguments). E.g., create the trigger Quicksilver Selection (**Get Info**) and assign it to <kbd>⌃</kbd><kbd>⌘</kbd><kbd>I</kbd>. Now you can activate Quicksilver, select a file object in the catalog or navigate to one in the filesystem and type <kbd>⌃</kbd><kbd>⌘</kbd><kbd>I</kbd> to bring up the Finder’s Info pane of that file. You don’t even have to tab to the action pane. You might think you could scope this trigger to only work in Quicksilver but that’s probably not what you want. If you do so, the trigger will only work if Quicksilver is active and frontmost, with its menu bar displayed. When you activate it with <kbd>⌃</kbd><kbd>space</kbd>, this isn’t usually the case. If you’re in some other application and activate Quicksilver, that other application is still considered active so the trigger isn’t available. Therefore you probably don’t want the Get Info trigger on the Finder’s binding of <kbd>⌘</kbd><kbd>I</kbd> since that with interfere with every application which usually defines that for toggling italics.

Sometimes when creating triggers with proxy objects, the action you want doesn’t appear in the list. As you’ve probably noticed, Quicksilver normally narrows down the action list to only those that are relevant. Sometimes proxy objects confuse it because they represent something else. If this happens you can work around it with copy and paste. It’s not obvious but if you bring up a regular command window (with <kbd>⌃</kbd><kbd>space</kbd>), when you tab to the action pane you can type <kbd>⌘</kbd><kbd>C</kbd> to copy the action. You can then paste it into the second pane of the trigger definition window with <kbd>⌘</kbd><kbd>V</kbd>. You can also cut an item out with <kbd>⌘</kbd><kbd>X</kbd>. This is useful when creating commands that do a web search with the **Search For…** action and you want a blank third pane. There are many other proxy objects giving you access to interesting things to use in triggers such as Track Now Playing (in iTunes), Current Application, Previous Application, Finder Selection, etc. Experiment to see what you find useful.

## More on Triggers

The possibilities for triggers seem endless. Here are some triggers people have posted on the Quicksilver forums as their favorites:

- Documents (**Open**) - the Finder doesn’t have a shortcut for this
- Finder Selection (**Go To Directory in Terminal**)
- Finder Selection (**Rename…**) - Cocoa text editing bindings are available
- Finder Selection (**Scale Image…**) 400 
- Finder Selection (**Open With…**) TextMate
- Current Application (**Menu Bar...**)
- Current Application (**Menu Bar Items...**)
- Current Application (**Show Menu Items**)
- Current Application (**Relaunch**)
- Current Application (**Hide Others**) - though <kbd>⌥</kbd><kbd>⌘</kbd><kbd>H</kbd> already works in most every application
- Previous Application (**Open**) - go back to what you were doing last, toggle between two apps
- Artist Now Playing (**Show Contents**)
- Browse Albums (**Search Contents**)
- killall Dock (**Run Command in Shell**) - or any other frequent shell command
- pbpaste | pbcopy (**Run Command in Shell**) - copies the clipboard without formatting
- date (**Run Command in Shell**) - acts like a clock
- Current Web Page (**Open With…**) Camino - or any other browser
- Removeable Disks (**Eject**) - great to clean up mounted disk images
- Network Disks (**Eject**)

There are some limits to triggers that you can create. You can’t save a trigger with a dynamic action. Dynamic actions are those that ask the application at runtime for their content. So the Current Application (**Menu Bar…**) trigger above works, but you can’t do Current Application (**Menu Bar…**) Help. Also actions that appear only for particular applications can’t be saved as triggers, so you can’t do Mail (**Get New Mail**). For some of these you can physically create the trigger but they won’t save properly and will be broken on Quicksilver relaunch.

The Settings tab in the drawer lets you set various options for a keyboard trigger. “Shortcut” lets you set the key. “Activate” lets you determine if the trigger activates when the key is pressed or released, and lets you set it to repeat if the key is held down for a period of time (useful for a fast-forward script). With a “Delay” set, the trigger won’t activate until the key has been held down for the number of specified seconds. The “Display” “Show Window” option shows a command window when the trigger is activated which is useful to see feedback that a trigger has executed. 

A delay can be useful for some dangerous commands that you don’t want to execute if you accidentally type the key. E.g., if you had a shortcut to Run the Quit All Visible Applications script from the Extra Scripts plugin, you might configure it to only execute if you hold the key down for 2 seconds.

TODO: You can define combinations of triggers to do one operation on immediate press and a second on a press an hold. E.g., you can define <kbd>⌃</kbd><kbd>⌘</kbd><kbd>I</kbd> to open your Inbox and a second <kbd>⌃</kbd><kbd>⌘</kbd><kbd>I</kbd> trigger to Get New Mail if you hold it down for 2 seconds. (one key for mail, holding it checks for new mail and then opens it) You can also configure triggers that use two scripts, one on start, one on finish.

If you create a lot of keyboard triggers it’s probably best to use some system to remember them. Some people put applications on their function keys, others use mnemonic keys like <kbd>⌃</kbd><kbd>⌘</kbd><kbd>S</kbd> for Safari. In examples above <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd> did a Wikipedia search and adding a <kbd>⇧</kbd> to the shortcut did the same thing with the current selection. Someone posted on the forums a scheme using <kbd>⌥</kbd><kbd>⌘</kbd><kbd>*letter*</kbd> and <kbd>⌃</kbd><kbd>⌥</kbd><kbd>⌘</kbd><kbd>*letter*</kbd> for Applications, <kbd>⇧</kbd><kbd>⌥</kbd><kbd>⌘</kbd><kbd>*letter*</kbd> for Folders , <kbd>⇧</kbd><kbd>⌃</kbd><kbd>⌘</kbd><kbd>*letter*</kbd> for iChat buddies. The important thing is to find something that works for you. It can be difficult to work around keys used by applications you use (particularly if you use TextMate or Emacs), but it can be done. The next sections describe using triggers with the mouse instead of shortcuts.

# Using the Mouse

## Drag and Drop

While it does involve switching between keyboard and mouse, the Quicksilver command window can be a convenient drag & drop source or target. E.g., with an Open File dialog up from some application, rather than navigating in that window you can activate Quicksilver, type to select the file you want to open and then drag it from the first pane into the Open File dialog. To make this a little more seamless there is an [AppleScript Action](docs.blacktree.com/quicksilver/applescript_open_and_save_selection) you can download from the Quicksilver site that add an action to send the file to an open or save dialog, so you can avoid the dragging. To move a file from the desktop to a folder, activate Quicksilver and bring up the folder in the first pane; then just drag the file from the desktop to the folder in the first pane.

You can bring up an e-mail address and drag it into the To: or CC: field of a mail message. Mail.app doesn’t recognize nicknames in it’s matching so using Quicksilver for this might be convenient. Note you have to drag an e-mail address for this to work, not a contact. You can also drag a file into a message as an attachment.

If the application you’re dropping into doesn’t accept the item your dragging from Quicksilver you’ll probably get the name of the item dropped in. E.g., if you drag a file into a web form you’ll find the file name with its full path entered into the form. Do the same thing with a contact to make sure you get a difficult name spelled correctly. Drag a postal address from a contact into a document or a field in an online mapping service (note, the newlines might prevent a web field from getting more than the street address). With proxy objects you can drag the Current Web Page URL or the iTunes Track Now Playing.

## Mouse Triggers

With the Mouse Triggers plugin installed triggers can also be assigned to the Mouse. The Settings tab of the drawer for the trigger is different for a mouse trigger. You can assign triggers to a number of mouse clicks, with or without modifier keys. Note that the Anywhere button in the desktop drawing is actually a button. If you want a trigger to work if you <kbd>⌘</kbd>-right-click anywhere in the window you have to click the Anywhere button for it to work. Also as of B51 it seems the Anywhere checkbox at the bottom is always greyed out. 

You can also activate a trigger when the mouse enters or exits an edge or corner of the screen or if you drag something to an edge or corner of the screen. If you have multiple monitors connected to your Mac you can choose if the trigger will work on all displays or on a particular one. I have Current Application (**Hide**) set when I mouse to the lower left corner. It gives me an easy mouse-based way to hide an application.

Dragging triggers work well with the Mouse Trigger Dragged Object proxy object. E.g., configure these when dragging to a corner or edge for your commonly used application or folder:

- Mouse Trigger Dragged Object (**Open With…**) application
- Mouse Trigger Dragged Object (**Move to…**) folder

Here are some more advanced ones that might require additional plugins:

- Mouse Trigger Dragged Object (**E-mail to…(**Compose**)**)
- Mouse Trigger Dragged Object (**Compress (**Create Archive**)**)
- Mouse Trigger Dragged Object (**Set Desktop Picture**)
- Mouse Trigger Dragged Object (**Add Tags...**) tags
- Mouse Trigger Dragged Object (**Upload to Site...**) Transmit favorite

Note that if you configure a trigger to activate when mousing or dragging to an edge it might interfere with the shelf or clipboard windows if you have them on an edge. In such a case the trigger will win and you’ll need to use some other means like a key stroke to open the shelf or clipboard windows.

One thing might not be obvious, you can configure the same trigger to activate by multiple means. E.g., if you have an Open Safari trigger assigned to the shortcut <kbd>⌃</kbd><kbd>⌘</kbd>S you can also assign it to having the mouse enter the left edge of the screen, and both will work. You do this by clicking the icon of the type of trigger in the <kbd>⌘</kbd> column of the Triggers preference pane. A pop-up menu appears of the other choices and you can select another one and configure it. Now both work. This can be useful to have two ways to invoke a trigger, one when your hands are on the keyboard and another when one hand is on the mouse. I don’t see a way to remove only one method from a trigger. The - button at the bottom of the screen deletes the whole trigger. For a shortcut you can always change it to not be bound to a specific key by clicking the Edit button and then the delete key. For a mouse trigger you can achieve the same effect by choosing Mouse Entered and selecting no edge or corner.

Most useful on mouse triggers are the **Show Menu**, **Show Contents Menu**, and **Show Action Menu** actions. These bring up a context menu for the object. **Show Contents Menu** creates a menu for the items that would appear if you typed <kbd>→</kbd> to go into the object, it’s like **Show Contents** but in menu form. Items have sub-menus showing the actions you can perform on them and any children they have. **Show Action Menu** shows a menu of the actions you can perform on an object. **Show Menu** shows a menu that combines the contents and actions you can perform. Mouse triggers for Shelf (**Show Contents Menu**) or Clipboard History (**Show Contents Menu**) are very useful.

## Abracadabra Mouse Gestures

For this section install the Abracadabra Triggers plugin. This enables a new trigger type known as a Gesture to go along with Keyboard and Mouse triggers. It also installs an Abracadabra preference pane. 

Abracadabra lets you invoke a trigger by drawing a shape with the mouse. E.g., you can configure Quicksilver to activate the Open Safari trigger by drawing an S on the screen. You configure your shape by drawing with the mouse button down in the pane in the Settings tab of the trigger’s drawer. The “Show zooming trigger window” will show a bezel window that enlarges when a gesture trigger is recognized and executed (like the Display: Show Window option of a keyboard trigger).

In the Abracadabra Preference pane you configure how you invoke all gestures. That is what mouse button you hold down and/or what modifier key you hold down while drawing any gesture. If you have a mouse with extra buttons it’s probably most convenient to use one of them for this as you’ll only need one hand to invoke the gesture. You can also choose the colors used to draw the shape on the screen as you draw and after you finish for a recognized gesture and an unrecognized gesture, as well as sounds to play. 

There’s also an option to Enable LaserKey Support which is a virtual keyboard device made by Cellulon. With it you can make gestures with your finger. Wherever I say mouse gestures here, LaserKey gestures is implied if you’re one of the lucky few to have one of these devices.

Simple gestures are best as you’ll have an easier time remembering them and Quicksilver will have an easier time recognizing them. You can create a gesture for any Quicksilver command (that is trigger). E.g., skipping to the next track in iTunes by drawing a line from left to right. Try a gesture for the **Quit** or **Hide** actions using the Current Application proxy object.

Gestures also go well with limiting the scope of a trigger and using the **Menu Bar Items…** action. This way you can make a trigger to invoke Safari’s Back command or Mail’s Reply command. This usually works best for things that don’t need the keyboard, e.g., navigating in Safari. Using a gesture to bring up a Find dialog probably doesn’t make much sense since you’ll need to type the text to find. Expose actions work well with gestures.

An interesting idea is using the Current Application proxy object and the **Menu Bar Items…** action to invoke an action common in all applications, e.g., Undo or Close. The problem is that many applications dynamically update their menus (e.g., “Undo Typing”) or slightly rename these commands (e.g., Close Window and Close Tab) so the trigger won’t work in all applications. Also there’s no way to select a menu command that is generic and not specific to an application, so this isn’t possible.

## Constellation Radial Menus

Most menus on computers look pretty similar. You click on something and a rectangle appears with commands listed vertically. Move the mouse over the command you want and click and you’re done. The one inefficient part is that if you want to choose the last item you have to move the mouse much farther than if you want the first item. Radial menus take a different approach. They pop up a circle around the mouse and divide the circle into pie pieces, one for each command. In this configuration choosing any item is just a different direction to move the mouse, but not any extra distance. Of course Quicksilver can use radial menus, and they look very very pretty.

For this section check “Enable access for assistive devices” in the Universal Access System Preferences. In addition to Constellation you’ll need to install the Mouse Triggers and User Interface Access plugins. Note that the plugin installs a Missing Object Selector Handler (in Preferences, Handlers) that you can configure, but don’t do that, leave it set to Quicksilver (see note below when discussing the Constellation triggers). The Constellation plugin installs two actions, **Show Radial Menu** and **Show Radial Action Menu**. It also installs a preference pane called Constellation listed in General . Up until B51 it installed a new trigger set on the left of the Triggers preference pane with 3 triggers predefined.

Let’s start with the **Show Radial Action Menu** action. Activate Quicksilver and bring up a folder (these examples use the hard disk) and choose the **Show Radial Action Menu** action. You’ll see a menu appear around your mouse pointer with items for the actions you could choose, as if you had brought up the folder in the first pane and looked at the available actions in the second pane. Moving the mouse into one of the pie slices highlights it, click to perform the action.

In the center to the left is an x in a circle, clicking that will close the menu. To the right is a button with 3 horizontal lines, clicking it will bring up a traditional menu of the items shown in the radial menu. If there are more items to display than fit in the pie slices a down-arrow button appears at the bottom of the center circle. Clicking it or anywhere in the bottom half of the center icon will bring them up. On additional menus an up arrow is displayed and clicking it or anywhere in the top half of the icon will go back.

If you use the **Show Radial Menu** action for the same folder you’ll see not the actions you can do to it but rather the contents of the folder appear in the menu. By clicking the items you can navigate into the folders bringing up additional radial menus of the contents of the sub-folders. The little arrows at the center of the pie slices correspond to >’s in a results list, it shows that there are children. If you click on one without an arrow, a menu opens as if you had done **Show Radial Action Menu** on that object. If you control-click (or right-click) on an item with an arrow in it you will pop up an action menu for that item. If you double-click on an item you will perform the default action for that item immediately. So double-clicking on a folder will open a Finder window of that folder. 

The Constellation preference pane allows you to customize the look of the menu. You can set the size of the menu and the number of slices in the pie. The Edge Behavior setting controls how the menu is displayed when the mouse is too close to an edge to show the whole menu. You can crop the menu (Slice Edge), move the mouse (Slide Mouse), or move the whole screen temporarily (Slide Screen). There are also various options for showing the labels (the above image is using “Around Edge”) and whether submenus are shown when hovering.

TODO: The trigger set is not installed in B51, will it come back? Should I remove the following 3 paragraphs?

The Constellation plugin installs a trigger set called, Constellation. There are three pre-configured triggers: Show Radial Menu for iTunes (on <kbd>F6</kbd>), Show Menu Bar Contents (Change Helper) (on <kbd>F7</kbd>) and E-mail Dragged Items (on mouse drag and drop into the lower-right corner). The first shows choices as if you had typed <kbd>→</kbd> into iTunes (Recent Tracks, Browse Artists, Genres, Albums, etc.). It’s just the iTunes object with the **Show Radial Menu** action. You can click on these to open other radial menus to browse your music library. With album art showing it’s very pretty. Control-clicking brings up an action menu with Play and Party Shuffle actions.

The second pre-configured trigger pops up a menu that shows the current application’s menu items (like File, Edit, etc.). If you like the idea of radial menus you’ll like this. It’s somewhat special in that there seems to be no way to create this yourself. It’s like the **Show Menu Items** action but in a radial menu. Note: this trigger only works if the Missing Object Selection Handler is set to Constellation. The problem is that setting it to Constellation can (as of B51) cause Quicksilver to crash on some occasions (see Bug 1017). In particular I have problems when using Web Search triggers with a blank third pane. My understanding is that this handler was originally a hack and I suspect it will be removed in a future version of Quicksilver.

With the third pre-configured trigger you drag text or a file to the lower right corner and it pops up a radial menu of Contacts to send to. It’s populated the same as the results list in the third pane of a command with the **E-mail to…(Compose)** action so it’s a list of commonly used contacts. The trigger is the proxy object Mouse Trigger Dragged Object with the action **E-mail to…(Compose)** but it pops up this radial menu (which with pictures in your Contacts entries is very pretty).

Those are the basics. You can of course use radial menus for lots of things and create your own triggers for commonly used ones (these will be in the Custom trigger set, not the Constellation trigger set). If you create triggers you probably want them bound to the mouse or at least to shortcuts easily typed with your non-mouse hand. What I think works well for radial menus are things that don’t change position (which isn’t so easy to arrange for) so you can learn them and things with clearly differentiated icons so you can recognize them quickly.

Here are some examples of objects to use the **Show Radial Menu** action on. Many of these are proxy objects which you must enable in the catalog under Quicksilver, Proxy Objects.

- Visible Applications - this is a cool mouse-based alternative to the <kbd>⌘</kbd><kbd>tab</kbd> method of switching applications. (shown at right).
- Track Now Playing - Shows a four part menu of the album, artist, genre, and composer of the current track, ready for easy browsing.
- Artist Now Playing - this shows all the albums by this artist you have in iTunes (with album art)
- Clipboard History 
- Shelf
- Finder Sidebar Items 
- Desktop
- Comma trick - create a trigger collecting several things you use frequently via the comma trick and use **Show Radial Menu** to display them. Works well for contacts, bookmarks, playlists, presentation documents, etc.

I haven’t thought of any good uses of **Show Radial Action Menu** as a trigger.

Instead of using the comma trick you can collect useful things in a folder. Here’s a fun idea I got from the Quicksilver forums. Create a folder and call it something like iTunes Controls. Do a Get Info on it and on the iTunes.app. Copy the iTunes icon to the new folder. Now activate Quicksilver and bring up the Play.scpt that controls iTunes and use the **Reveal** action on it. This will open a finder window inside the iTunes Module.qsplugin showing the scripts. Now copy them to the iTunes Controls you created. Remove the ones you don’t want and rename the remaining ones putting number at the beginning of the name to order them as you want. Now bring up the iTunes Control folder and use the **Show Radial Menu** action to bring up the controls as shown. Save this as a trigger to make these controls easily accessible. If you want to be more creative you can add your own icons for the scripts that don’t have them. Jacob Rus has put some icons and extra scripts together you can download [here](hcs.harvard.edu/~jrus/site/itunes-control.zip).

## Command Objects and Droplets

Commands in Quicksilver can be represented as objects in Quicksilver. To create a command object, activate Quicksilver and enter a command as you normally do, but instead of typing return to execute it, instead type <kbd>⌃</kbd><kbd>return</kbd>. You’ll see a new command window appear in which the object is a new command object of the command you entered and a default action which is probably **Run**.

Other actions that work on commands include **Run**, **Run after Delay...**, and **Run at Time...**. The first, **Run**, is obvious and not particularly useful since just executing the command without creating a command object is easier. The other two are useful as alarms when used with actions like **Large Text** or **Display Dialog**. A delay period is entered as a decimal number followed by an h, m or s to indicate hours, minutes or seconds. E.g., 2h, 10m, 90s, or 1.5h. A number without a suffix is interpreted as minutes. You can combine these separated by spaces such as 2m 30s. You can also enter a time format such as minutes:seconds or hours:minutes:seconds. For example 9:35 or 2:11:30. I believe you can also enter decimal numbers with colons like 1.5:10:00 for 100 minutes but that is probably not useful.

Times for **Run at TIme...** are typically entered as a digital clock, hh:mm:ss although it uses macOS's natural language date parser so things like 3pm December 15, 2008 or next Tuesday at dinner are supposed to work.

There’s also an **Add Trigger** action but in B51 all it seems to do it open the Triggers preference pane. It actually does add a keyboard trigger representing the command but it doesn’t show up in the Triggers list until you restart Quicksilver. You can then assign a shortcut to it.

The **Save Command to File…** action takes a command object and saves it in a file. You enter a folder name as the argument and Quicksilver saves a file there with the extension .qscommand. If you open the resulting file (e.g., by double-clicking it), it will run the command. Quicksilver makes running commands simple and triggers make running command even easier. But for commands that you might run a few times but not enough to bother creating a trigger for, the **Save Command to File…** action can be useful. E.g., if your working on creating a document and you want to send several drafts to a group of people (using the comma trick) it’s easy to save this (complicated) command in a file to rerun.

With a saved command on your Desktop you might want to be able to drag a file onto the command and have it run on that file. This can be done, and this type of saved command is known as a Droplet. To create a droplet, use the Droplet Item proxy object in the command and save it using the **Save Command to File…** action. The command file will have a special icon and a .app extension. Unfortunately in B51 these don’t seem to always work and sometimes create running Droplet processes that have to be quit before you can delete the files.

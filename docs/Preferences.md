# Preferences

Quicksilver has a configuration window that provides access to the Guide, Preferences, Triggers, Catalog and Plugins. These can be accessed several ways. The easiest is to activate Quicksilver (with <kbd>⌃</kbd><kbd>Space</kbd>) and then use the standard shortcut <kbd>⌘</kbd><kbd>,</kbd> to bring up preferences. Other shortcuts are available to go directly to various sections of the preferences.

| Shortcut | Action |
| --- | --- |
| <kbd>⌘</kbd><kbd>,</kbd> | Open Preferences |
| <kbd>⌘</kbd><kbd>;</kbd> | Open Catalog |
| <kbd>⌘</kbd><kbd>'</kbd> | Open Triggers |
| <kbd>⌘</kbd><kbd>"</kbd> | Open Plugins |

Other ways to access preferences:

  1. In the main command window, select one of the Internal Commands: Show Guide, Show Preferences, Show Trigger Preferences, QS Catalog Preferences, Show Plugin Preferences and use the Run action.

  2. Click the Dock icon and Quicksilver’s menu appears, look under Quicksilver.

  3. If the menu bar icon is enabled, a menu is available by clicking on it

  4. Right-click the Quicksilver icon in the Dock.

The following sections describe these preferences. First, global preferences that affect how Quicksilver is activated and appears and then sections on Plugins, the Catalog, Actions, Handlers, and Notifications. Triggers are a large topic and are covered in their own entire section immediately after this one.

Configuring new Quicksilver features is usually done by installing the relevant plugin. Sometimes there are additional things to configure such as enabling new catalog sources, new actions (under Preferences, Actions) or relevant Handlers (under Preferences, Handers). Finally some plugins add their own preference panels listed in the lower left area of the Preferences window.

# General

Quicksilver’s Preferences are divided into sets at the left of the window. Those listed at the top are built-in to Quicksilver and those in the bottom section are enabled by installed plugins.

## Application

The Application Preferences control the most fundamental aspects of Quicksilver as an application. Once you’re hooked on Quicksilver you’ll want to enable **Start at login**.

Quicksilver shows an icon in the Dock like most applications, but many people prefer to disable this. Uncheck the box to disable the Dock icon. The ⌽ symbol indicates Quicksilver must be restarted before the change will take effect. An easy way to restart is to activate Quicksilver and then type <kbd>⌃</kbd><kbd>⌥</kbd><kbd>⌘</kbd><kbd>Q</kbd>.

Without a Dock icon, Quicksilver runs as a background process. This means it won’t appear in the Dock or when switching apps with <kbd>⌘</kbd><kbd>⇥</kbd> and the main Quicksilver menu will not appear while the preference window is open.

The **Show icon in menu bar** preference puts an indicator in the top right part of the screen. Some people like this, particularly if they don’t configure a Dock icon or have their Dock hidden. It provides a simplified menu to access the various configuration panes of Quicksilver. For access to the full menu options (via more sub-menus) set the option **Include access to all menu items from menu bar**. 

The next section controls if and how Quicksilver checks its website automatically for updates both for updates to Quicksilver and for all installed plugins. It can be configured to check on launch, daily, weekly or monthly. The Check Now button will, not surprisingly, check immediately for an update. 

The three buttons at the bottom will rerun the installation setup described in the [Installation](introduction#Installation) section, Reset Quicksilver’s preferences, and completely Uninstall Quicksilver.

The Appearance Preferences control how Quicksilver looks. 

The command window  supports various skins or themes, known as Interfaces and installed via plugins (all of which end with the word Interface). Select the Interface to use here via the popup list showing all installed Interfaces. See the Interface section below for details.

The default interface is Primer and it shows a little more context information than other interfaces so it’s recommended for new users. The other builtin interface is Bezel interface; it’s very popular and is shown throughout this manual. 

The Colors options allow further customization of the appearance of the interface and vary per interface. The column headers have tooltips showing what they represent: Background, Selection & Accents, and Text colors. Clicking on the nine colors in the grid will bring up a color picker.

## Command

The Command Preferences allows configuration of the command window’s behavior. 

### Activation Shortcuts

The top of the pane affects how you activate Quicksilver. The Keyboard Activation is the basic way to activate Quicksilver. The default is to type <kbd>⌃</kbd><kbd>Space</kbd>, though <kbd>⌘</kbd><kbd>Space</kbd> is a common alternative.

The shortcut is configurable in the Command Preferences Pane under Activation. Quicksilver defaulted to <kbd>⌘</kbd><kbd>Space</kbd> for a long time, but with 10.4, Apple chose to use <kbd>⌘</kbd><kbd>Space</kbd> for Spotlight. So Quicksilver changed its default to <kbd>⌃</kbd><kbd>Space</kbd>. If you look at older posts on the Web, or even current posts from long-time users, you’ll often see <kbd>⌘</kbd><kbd>Space</kbd> used to activate Quicksilver.

A common setup is to use <kbd>⌘</kbd><kbd>Space</kbd> for Quicksilver and <kbd>⌥</kbd><kbd>⌘</kbd><kbd>Space</kbd> for Spotlight (set in the Spotlight System Preference pane of macOS). An advantage is that many shortcuts used after activating Quicksilver use <kbd>⌘</kbd>, so using the same modifier key is easier. For example, <kbd>⌘</kbd><kbd>,</kbd> will open up Quicksilver’s Preferences.

**Modifier-only Activation** allows you to activate Quicksilver by single or double presses of modifier keys such as <kbd>⌃</kbd>, <kbd>⌥</kbd>, <kbd>⇧</kbd>, <kbd>⌘</kbd> or even <kbd>fn</kbd>. The activation is only triggered when you “tap” the chosen key and nothing else, so accidental activations are _far more rare_ than you might expect.

**When activated, switch keyboard to** allows you to force Quicksilver to use a different keyboard layout than the one you use for macOS in general. <!-- TODO: use case? -->

### Searching and Spacebar Behavior

Thanks to Quicksilver’s matching algorithm, the spacebar is completely unnecessary for searches in the command window. The **Spacebar behavior** preference lets you reclaim that easy-to-smack key and make Quicksilver a little faster to use. The options are:

  * **Normal** - Literally type a space and include it in the search term
  * **Select Next Result** - Select the next result in the results list, like typing <kbd>↓</kbd>
  * **Jump to Argument List** - Change to the third pane
  * **Switch to Text Mode** - Change the current pane to text mode entry, like typing <kbd>.</kbd> or <kbd>'</kbd>
  * **Show Item’s Contents** - Goes into the item, like typing <kbd>→</kbd> or <kbd>/</kbd>
  * **Quick Look** - Show the selected file(s) using Quick Look
  * **Smart** (default) - Select one of the above behaviors automatically based on context

The smart spacebar tries to be the best of all worlds and do what you probably want in any given situation. This is how it decides what to do:

  * If in the second pane, select the first action that takes an argument in the third pane.
  * If user is holding Shift, go to the parent (same as left arrow).
  * If the object has children, show them (same as right arrow) unless it’s a text file.
  * Jump to the third pane if the current action requires it. This is very useful for web searches.
  * Quick Look if the object supports it.
  * Switch to text mode.

Plug-ins can override the above where it makes sense. For example, iTunes tracks have children (genre, artist, and album). According to the above rules, spacebar would act like right arrow and show them, but the iTunes plug-in tells the smart spacebar to use Quick Look instead.

**Switch to text mode if no match is found** will allow you to save typing <kbd>.</kbd> or <kbd>'</kbd> to enter text mode in a pane.

**Reset search after** lets you start a new search without manually clearing the current search string.

**Wait before searching** can be tweaked to work with your typing speed. It tells Quicksilver not to start a potentially resource intensive search until you've finished typing.

### Results

The bottom of the Command Preferences pane affects how the results list window appears and how actions that return something to Quicksilver should behave.

**Focus action when displaying results** is designed to save time when performing multiple commands in sequence. For example, if you wanted to compress a folder, rename the resulting ZIP file, then copy it to another location. By default, each of those actions would show the resulting file in Quicksilver and select it, requiring you to hit <kbd>⇥</kbd> each time to choose the next action.

Selecting **Show children split view** will split the results list vertically into two columns, the right one showing the contents of the selected item in the left one (much like the column view of the Finder). You must restart Quicksilver for changes to this setting to take effect. When first enabled you’ll only see one column, but notice the small dot in the middle of the right edge, you can click on and drag that to the left to reveal the second column. **This feature will slow Quicksilver down tremendously (as it’s constantly loading children you probably don't care about) and should never be used.**

You can specify the Row Height in pixels. A higher value will show a larger image on each row. A lower value will result in a single line per entry (showing label, but not details). The details for the selected entry will be shown in the bottom of the window in that case.

**Show other results** controls if the results list appears after you type into the command window immediately, after a short delay, or not until you manually scroll with <kbd>↓</kbd>.

## Appearance

Interface plugins change the look of Quicksilver’s command window. Install them just like other plugins from the Plugins Preferences, then select one of the installed interfaces in the Appearance preference pane. If you use a remote control application to connect to different machines, you might want to configure them with different interfaces or change the colors on the interface to distinguish them.

Two interfaces are included with Quicksilver out of the box. Primer (the default) is intended for new users as it does a better job of labeling things and helping you understand what’s going on. Bezel is a nice looking interface that places emphasis on icons over text.

The Colors and Text sections can be used to adjust the look of the selected interface (and the results list) if that interface supports it. Some interfaces have a hard-coded look and will ignore these settings.

Some interfaces will offer a Customize button that provides additional adjustments specific to that interface.

## Actions

All of the actions available in Quicksilver are listed in this section of the preferences. It’s a good idea to scan through this list to get an idea what sort of things are possible.

### Viewing Actions

The default is to group actions by type. That is, clicking a type on the left will narrow the list of actions on the right to only those that work with that type. You can also view the actions by plug-in. Choosing a plug-in on the left will narrow the list of actions to only those provided by that plug-in.

You can also narrow the list of actions by name using the search field.

The list of actions will also show the alternate action if one exists. Alternate actions provide a quick way to do something slightly different from the selected action by hitting <kbd>⌘</kbd><kbd>↩</kbd> instead of just <kbd>↩</kbd>. For example, if you select a file and run the **Open** action, the file will open. Hitting <kbd>⌘</kbd><kbd>↩</kbd> instead will run the **Reveal** action instead, showing the file in Finder.

### Adjusting actions

The checkbox next to every action allows you to enable or disable it. You may want to disable some you think you’ll never use. Some of the more technically oriented or dangerous actions are disabled by default, but you can enable them here.

The most important use for the action preferences is to control the order in which they appear. The goal is for the actions you use most often to be selected by default so you’ll rarely need to go to the second pane and choose one manually. You can change the order by dragging and dropping.

When you select an object in Quicksilver’s first pane, the highest ranked applicable action will be the one selected by default in the second pane. The word “applicable” there is important and deserves some discussion: The second pane will only contain actions that can be used on whatever you select in the first pane. Because of this, _you will generally want to put more specific actions (those that only apply to one or two types) high up on the list, and the more general actions lower_. For example, dragging the **Open URL** action all the way to the top will not annoy you by constantly showing that action when you select files because it will only appear when you select a URL. On the other hand, an action like **Paste** can be used on any object, so placing it high on the list _will_ annoy you because you probably don’t want it to be the default for everything you select.

Quicksilver and its plug-ins ship with reasonable defaults for the action rankings, but you might want to make adjustments. It might take some experimentation with real-world use before you get things just right.

## Extras

The Extras Preferences have some advanced options.

**Show the Task Viewer automatically when tasks are created** will let you keep tabs on things Quicksilver does in the background. Unless you interact with it, the Task Viewer will hide itself again once all tasks are complete.

If you prefer concentrating on one thing at a time, check **Hide other applications when switching applications** so that Quicksilver will do a **Hide Others** after switching applications. You can prevent the hiding behavior by holding down the Shift key when completing the command.

**Run tasks and actions in the background** prevents longer-running commands from locking up Quicksilver’s interface until they finish. You should only disable this if something isn’t working as expected.

**Reopening the current application** configures what happens if you use the Open action on an application that is already running. You can have it activate the application, show the front window, or show all windows.

**Application Update Type** allows you to choose between Prerelease Candidates and Final Releases when Quicksilver checks for updates as configured in the Application Preferences. Sometimes after installation this is set to a blank value and that has been observed to cause problems, make sure it’s set to some value in the popup.

Since the matching algorithm is case-insensitive the Shift key is available for some use in Quicksilver. If you check **Allow capitalized keys to select the action** then shifted letters are used to select the action, eliminating the need to tab to the second pane. Once moved to the action pane, unshifted letters don’t change the first pane, all typing counts for the second pane. If you also hold down the <kbd>⌘</kbd> key the action will be performed immediately, no need to type return. E.g., <kbd>⇧</kbd><kbd>I</kbd> selects the action for “i” (perhaps **IM**) while <kbd>⇧</kbd><kbd>⌘</kbd><kbd>I</kbd> performs the action for “i”. Use caution, as it’s not always clear which action is invoked.

If you enable **Disable Keyboard Triggers when Quicksilver is focused** then keyboard triggers will not work while Quicksilver is activated (i.e., the command window is open). I have no idea why you would want to enable this. If you don’t want a particular trigger to work when Quicksilver is active, this can be configured in the individual trigger’s settings.

**Pressing the Delete key clears the whole search string** disables the default behavior of removing a single character at a time from the search string. With this enabled, you can immediately start a new search by hitting <kbd>⌫</kbd>, and clear the interface entirely with <kbd>⌫</kbd><kbd>⌫</kbd>.

## Handlers

Quicksilver not only makes it easier to work with a variety of applications, it sometimes uses other applications to perform commands. These are configurable in the Handlers Preferences pane.

  * **E-mail** - The e-mail client to use for Send/Compose actions
  * **Command Line Interface** - The terminal program to use for command-line actions
  * **String Ranker** - Choose either the default built-in ranker, or the TextStart Ranker, which uses a different matching algorithm. See the [TextStart Ranker](introduction/#textstart-ranker) section for details.
  * **File System Browser** - The application to use for file system actions like Reveal, Open, or Copy
  * **Missing Object Selector** - This is the interface Quicksiver will present if you need to select an object for the third pane.
  * **Notification** - How to display notifications. See the next section.

It’s important to understand that the choices here actually refer to Quicksilver plug-ins and not the applications themselves. So for example, you won’t see every e-mail client on your system listed. You will only see the ones for which a plug-in exists and has been installed.

### Notifications

The Notifications Hub plugin allows finer granularity in configuring notifications. It adds a new preference pane called Notification Hub. There you can configure a default notifier as well as configure specific notifiers for specific events. E.g., iTunes notifications go to the Quicksilver built-in notification notifier while Plugin Installation notifications go to Growl. You can even send the same notification to multiple handlers by adding multiple lines for the same Notification and with different notifiers.

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

The Quicksilver Selection might seem silly. If you already have something selected, why do you need a proxy for it? Some proxy objects, like this one, are really only useful (but extremely so) as part of [Triggers](#triggers), which are discussed in a bit.

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

A common thing to want to do is to scan the `~/Documents/` folder deeper than the depth of 2 the default source uses (in the User set). To do this, select the Users set and the Documents source, open the drawer and select the Attributes tab. Click on Create Copy to create a new source in Custom named Documents. The difference is that the Source Options tab of it is editable. Change the depth slider to what you want. Many people just select infinity but this is never recommended. Your indexes will take longer and your catalog will be huge which will slow Quicksilver down. Also if you have many extra items in your catalog your searches are more likely to contain useless noise. Remember that you can always navigate to any file in Quicksilver (see the [Files and Folders](Files and Folders.md) section), so all you need in your catalog are your more commonly used files.

You probably don’t want to just index your entire home directory. `~/Library` alone has many preference and cache files that you don’t want indexed, and the Music and Pictures folders are better served by the iTunes and iPhoto plugins.

The File & Folder Scanner can also scan the _contents_ of files to add to the catalog. The scanner can recognize either HTML links or text lines depending on the setting of the Include Contents popup. Text lines are [“sniffed”](Text.md#string-sniffing) to see if they can be converted into anything useful.

The Applications set has 4 sources defined. The Applications (User) source indexes `~/Applications/` to a depth of 3 but also only finds the applications, not the intervening folders. If you want those in the catalog so you can easily move an application into them (e.g., `~/Applications/Games/` and `~/Application/Browsers/`), the Types field in the Source Options tab is useful for this. If you type file extensions (e.g., `.txt`, `.c`, `.doc`, etc.) into it you can filter the kinds of files indexed. You can also enter Mac Type Codes surrounded by single quotes and type tab to have it interpreted.

So, to get applications entered as it is in the pre-configured source, enter `'APPL'` (including the single quotes). In this example, you want folders, so enter `'fold'` and type tab and it’s replaced with “folder”. You can choose a depth of 1 to include the Games and Browsers folders but not folders that some applications come with (or the Contents folders inside the `.app` packages).

Note that the Find All Applications source under the Applications set will search the whole system for application packages. It also indexes any external drives connected. Be aware that allowing Quicksilver to index things on an external drive might cause performance problems and other strange behavior.

The Spotlight object source allows you to add files to the catalog if they match a Spotlight query. See the Spotlight plugin’s documentation for a discussion of the syntax.

The Defaults Reader allows you to index some keys from Property List (`.plist`) files, though it’s a little flakey (doesn’t deal well with paths), is difficult to configure (you must manually specify each key) and doesn’t let you change the plist file.

The Group type is just a a folder for custom catalog sources to be able to group many custom sources in the catalog preferences to make them easier to read.

Additional catalog sources are described elsewhere in this manual. 

In the Quicksilver set there is a source called Quicksilver Catalog Entries. If enabled, an item is added to the catalog for each source configured. These items have names that end with “(Catalog)”. You can select one of these items in the first pane and then type <kbd>→</kbd> to navigate through just that source. If you want to do this often, create a trigger. E.g., the trigger Applications (Catalog) (**Show Contents**) lets you search through just the applications in your catalog (well those that are found via this catalog source). While you can often do this just by typing <kbd>→</kbd> into an object, if you have custom sources configured (say for files of a particular project) this can be very handy.

# Triggers

Triggers allow you to execute Quicksilver commands without having to use the command window. Quicksilver supports executing triggers based on

  * Keyboard shortcuts (built-in)
  * Mouse position and/or buttons (Mouse Triggers plugin)
  * System Events (Event Triggers plugin)
  * Gestures (Abracadabra Triggers plugin)

Triggers are available whenever Quicksilver is running and you do not have to invoke Quicksilver to use them. Triggers make it easier to control iTunes, launch applications, perform web searches, or do anything else Quicksilver can do. You can create as many as you want but you probably want them only for the operations you do frequently.

Your trigger configuration is stored in `~/Library/Application Support/Quicksilver/Triggers.plist`. This is useful to know if you want to have the same configuration on several machines, just copy the file between the machines while Quicksilver is not running. 

You define triggers in the Triggers Preference pane. You can go to this pane directly by activating Quicksilver and typing <kbd>⌘</kbd><kbd>'</kbd>. You’ll see several sets in the left side of the preference pane. Some triggers are predefined by Quicksilver itself or various plugins, e.g., you’ll find several in iTunes, and two in Quicksilver. Triggers you create will be in the Custom Triggers set. 

Each trigger is shown by its name which is usually a combination of the object and action to be invoked. The checkbox shows if the trigger is active. The <kbd>⌘</kbd> column shows the type of trigger, in this case they are all activated by a shortcut which is shown in the Trigger column (some are not assigned to keys). If you select a trigger and click on the ⓘ button at the bottom, a drawer is revealed with various settings for the trigger. The settings tab looks different for each type of trigger. You can change the name of the trigger in the top text field.

You can change some options by clicking in the main trigger window. If you click on the command name you can get an edit field to change the name of the trigger. If you click in the Trigger column you can set or change the shortcut. If you click on the icon in the <kbd>⌘</kbd> column you can add another means (Gesture, Mouse) to activate the trigger. Though once you create an additional way, there doesn’t seem to be a way to delete it without deleting the entire trigger.

You create a new trigger by clicking the + button at the bottom and selecting a trigger type from the pop-up menu (Gesture, Keyboard, or Mouse, depending on installed plugins). The Group option is just a way to collect triggers in a group or folder. They don’t perform any function other than helping you organize a lot of triggers. You can’t activate all the triggers in a group at once. Create a Group from the + menu and drag triggers into it. 

Regardless of which type you choose, a special command window appears (populated with the last command you performed) to let you define the command for the trigger. Enter the command and click Save. Then open the drawer to the Settings tab to assign a shortcut, mouse click, or gesture to use to activate the trigger. If you’re creating a keyboard trigger, just click in the Trigger column for this new trigger, the drawer will open and you can just type the shortcut as if you had clicked the Edit button.

By default, triggers are available whenever Quicksilver is running, regardless of what application is active. They can also be limited to function only when a certain application is active or when a certain application is not active. You do this by opening the drawer for a trigger and choosing the Scope tab. The default is “Enabled in all applications” but you can also choose from the popup “Enabled in selected applications” or “Disabled in selected applications”. For the latter two you can type the name of the application into the large box and type <kbd>⇥</kbd> or <kbd>,</kbd> after the name to have it turn into a blue button. You can then enter another application if you choose.

If you have triggers that use certain features, be cautious about deleting the plugins that supply those features. In particular if you have triggers using mouse gestures from Abracadabra (see below) and if you remove the Abracadabra plugin, the trigger panel may display oddly with some blank lines and missing icons. To correct this, reinstall the plugin (Abracadabra in this case), or remove the triggers.

The following sections discuss each type of trigger with some examples. The commands used will come from many different plugins not covered here. If you want more information on them, look in the relevant sections under Features. While you have a lot of freedom in defining triggers any way you want, some commands are better suited to certain trigger types.

## Keyboard Triggers

If you enter a complete command into the trigger, like choosing an application and the Open action, it will be run when you execute the trigger. If you choose just a partial command, like a web-search and the **Search For…** action, when you execute the trigger a command window will appear with as much filled in as your trigger defines. You can’t have gaps (e.g., you can’t leave the first pane blank and use the **Get Info** action). This is discussed more below. Triggers are given a default name based on the command they represent. Here are some examples:

### Open Safari

The most common simple trigger created is to open an application. Shown here is a trigger to open Safari, it’s just the Safari application in the first pane and the **Open** action in the second. The argument is blank. Notice that when the action is **Open** the default name for the trigger is Open followed by the application. Usually the default name is the object followed by the action in parenthesis. **Open** is special, probably because it’s so common. If in the Extras Preferences you have Reopening the current application set to “activates the application”, then using this trigger when Safari is already running will make it the active application.

You can obviously make similar triggers to open your favorite applications. Some people create other triggers like Safari (**Quit**) or Safari (**Hide Others**) and put them on the same keys but with different modifiers (e.g., <kbd>⌥</kbd> or <kbd>⇧</kbd>). Others just use the standard macOS shortcuts of <kbd>⌘</kbd>Q and <kbd>⌥</kbd><kbd>⌘</kbd><kbd>H</kbd> to run these on the current application.

### Show Shelf/Clipboard Contents

The Shelf and Clipboard History are enabled with the Shelf plugin and the Clipboard plugin respectively. Each enables a window that you typically access with the mouse (see [Clipboard and Shelf](Clipboard and Shelf.md) for details). To get keyboard access to these, first enable the objects in the Catalog under Quicksilver and Shelf & Clipboard (check the box and click the rescan button). If you select these objects in the first pane, you can type <kbd>→</kbd> or <kbd>/</kbd> to open a new results list with their contents. The **Show Contents** action is the equivalent of this, and since it’s an action, you can use it in a trigger.

So this trigger will open the shelf in a results list, with the first item selected, and let you type to select any item on the shelf (or the Clipboard History if you use that object). You can also use the **Search Contents** action which is very similar but won’t select the first time and won’t show a results list at first.

You can create triggers using **Show Contents** or **Search Contents** for anything you can right-arrow into, such as Contacts, iTunes, your Documents folder, etc.

### Search Wikipedia

Some actions take an argument in the third pane and triggers can use these too. The **Search For…** action will search some web site for the text entered as an argument. See the [Web Searches](Web.md#web-searches) section for the details of using this action.

A trigger for a commonly used web search, such as Wikipedia, is very useful. If you specified the argument in the trigger it would search for the same text each time it’s run. However, if you leave the third pane blank, then when the trigger is run, Quicksilver will open a command window with the first two panes filled in (in this case with Wikipedia and **Search For…**), and the third pane selected, ready for you to type the query.

Quicksilver is also smart enough to realize that the **Search For…** action wants a text argument and puts the third pane in text mode for you. It even fills in the default text from the macOS Shared Find Clipboard (which you can set in many Cocoa applications with <kbd>⌘</kbd><kbd>E</kbd>). Note, if the third pane isn’t empty when you create the trigger and you want it to be, type <kbd>⌘</kbd><kbd>X</kbd> to clear the selection.

If you have this trigger configured on the shortcut <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd>, you type <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd>, the query, and hit <kbd>↩</kbd> then the browser opens with the search results. If you want to search for some text in a document, you can select the text, copy it with <kbd>⌘</kbd><kbd>C</kbd>, type <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd> and then paste the text with <kbd>⌘</kbd><kbd>V</kbd> and type return.

That’s pretty easy, but believe it or not, this is the hard way. In the next section, you’ll see how proxy objects reduce this to one step.

### Paste the Current URL

This example lets you paste the URL of the page Safari is displaying into any other application without switching applications multiple times, and without having to select or copy anything. You can use this trigger to paste a URL into mail messages, chats, documents, Calendar events, etc. The magic is because of the Current Web Page proxy object used in the first pane. It acts like a placeholder for the URL Safari will be displaying when you use this command. When the command is run, this proxy object asks Safari what it’s currently displaying and uses that in the command.

If you aren’t using Safari or use more than one browser, every browser plugin currently available also provides a “Current Web Page” proxy object.

### Search Wikipedia for Selected Text

The Current Selection proxy object gets the selection from the frontmost application.

If your current selection is text, it should be possible to use this proxy object as the argument in the Wikipedia search trigger above, so that you could select text in some Cocoa application, invoke the trigger, and have the search run. The **Search For…** action has a complementary action called **Find With…** that takes the query text as the object, and the search site as the argument. You can set up a trigger of the Current Selection proxy object with the  **Find With…** action and the Wikipedia argument.

It’s useful to assign triggers to shortcuts in some pattern so they are easier to remember. For example, you could use <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd> to search Wikipedia for text you enter, and add <kbd>⇧</kbd> to the sequence to search for selected text. Pairs of triggers for other quick searches might look like this: Google (<kbd>⌃</kbd><kbd>⌘</kbd><kbd>G</kbd>), IMdB (<kbd>⌃</kbd><kbd>⌘</kbd><kbd>F</kbd>), and Amazon (<kbd>⌃</kbd><kbd>⌘</kbd><kbd>Z</kbd>).

Sometimes when creating triggers with proxy objects, the action you want doesn’t appear in the list. As you’ve probably noticed, Quicksilver normally narrows down the action list to only those that are relevant. Sometimes proxy objects confuse it because they represent something else. If this happens you can work around it with copy and paste. It’s not obvious but if you bring up a regular command window (with <kbd>⌃</kbd><kbd>Space</kbd>), when you tab to the action pane you can type <kbd>⌘</kbd><kbd>C</kbd> to copy the action. You can then paste it into the second pane of the trigger definition window with <kbd>⌘</kbd><kbd>V</kbd>. You can also cut an item out with <kbd>⌘</kbd><kbd>X</kbd>. This is useful when creating commands that do a web search with the **Search For…** action and you want a blank third pane. There are many other proxy objects giving you access to interesting things to use in triggers such as Track Now Playing (in iTunes), Current Application, Previous Application, Finder Selection, etc. Experiment to see what you find useful.

### Quicksilver Selection

The Quicksilver Selection proxy object represents what is in the first pane. This allows you to assign triggers to particular actions (or actions and arguments). For example, create the trigger Quicksilver Selection (**Get Info**) and assign it to <kbd>⌃</kbd><kbd>⌘</kbd><kbd>I</kbd>. Now you can activate Quicksilver, select a file object in the catalog or navigate to one in the filesystem and type <kbd>⌃</kbd><kbd>⌘</kbd><kbd>I</kbd> to bring up the Finder’s Info pane of that file. You don’t even have to tab to the action pane.

You could also create a trigger to open files in an application you frequently use that might not be the default when you run **Open** by using the **Open With…** action. For example, you could bind <kbd>⌥</kbd><kbd>⌘</kbd><kbd>T</kbd> to Quicksilver Selection ⇥ Open With… ⇥ TextMate.

You might want to scope these triggers to only work in Quicksilver. They aren’t really useful in other contexts and you don’t want to tie up those shortcuts in other applications that might do something useful with them.

## More on Triggers

The possibilities for triggers seem endless. Here are some triggers people have posted on the Quicksilver forums as their favorites:

  * Documents ⇥ **Open**
  * Finder Selection ⇥ **Go To Directory in Terminal**
  * Finder Selection ⇥ **Rename…**
  * Finder Selection ⇥ **Scale Image…** ⇥ 400 
  * Finder Selection ⇥ **Open With…** ⇥ TextMate
  * Current Application ⇥ **Menu Bar…**
  * Current Application ⇥ **Menu Bar Items…**
  * Current Application ⇥ **Show Menu Items**
  * Current Application ⇥ **Relaunch**
  * Current Application ⇥ **Hide Others** (though <kbd>⌥</kbd><kbd>⌘</kbd><kbd>H</kbd> already works in most every application)
  * Previous Application ⇥ **Open** (go back to what you were doing last, toggle between two apps, or restore focus if Quicksilver steals it)
  * Artist Now Playing ⇥ **Show Contents**
  * Browse Albums ⇥ **Search Contents**
  * killall Dock ⇥ **Run Command in Shell** (or any other frequent shell command)
  * `pbpaste | pbcopy` ⇥ **Run Command in Shell** (re-copies the clipboard contents without formatting)
  * `date` ⇥ **Run Command in Shell** (acts like a clock)
  * Current Web Page ⇥ **Open With…** ⇥ [Some Web Browser]
  * Removable Disks ⇥ **Eject** (great to clean up mounted disk images)
  * Network Disks ⇥ **Eject**

There are some limits to triggers that you can create. You can’t save a trigger for something that isn’t in your catalog. So the Current Application ⇥ **Menu Bar…** trigger above works, but you can’t do Current Application ⇥ **Menu Bar…** ⇥ Help because the “Help” item is created on demand. Also, actions that appear only for particular applications can’t be saved as triggers, so you can’t do Mail (**Get New Mail**). For most of these, you can physically create the trigger, but the objects involved will disappear when Quicksilver restarts, making it impossible to set up the trigger again.

## Trigger Settings

The Settings tab in the drawer lets you set various options for a keyboard trigger. “Shortcut” lets you set the key combination. “Activate” lets you determine if the trigger activates when the key is pressed or released, and lets you set it to repeat if the key is held down for a period of time (useful for something like “skip forward” or “volume down”). With a “Delay” set, the trigger won’t activate until the key has been held down for the number of specified seconds. The “Show Window” option shows a small window that quickly zooms out of the center of the screen, which is useful if you need some indication that the trigger was executed.

A delay can be useful for some dangerous commands that you don’t want to execute if you accidentally type the key. If you had a shortcut to run the Quit All Visible Applications script from the Extra Scripts plugin, you might configure it to only execute if you hold the key down for 2 seconds.

If you create a lot of keyboard triggers it’s probably best to use some system to remember them. Some people put applications on their function keys, others use mnemonic keys like <kbd>⌃</kbd><kbd>⌘</kbd><kbd>S</kbd> for Safari. In examples above <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd> did a Wikipedia search and adding a <kbd>⇧</kbd> to the shortcut did the same thing with the current selection.

The nice thing about keyboard triggers is that you can fire them off from any context, but a major downside is that you need to choose a key combination that doesn’t conflict with anything else (you care about) in any context, and never will for any application you ever install. Not an easy task. Limit the scope to applications where the trigger makes sense whenever possible, and keep in mind that doing things “the hard way” by just calling up Quicksilver and smacking a few keys is often preferable to the stress of coming up with a keystroke you’ll never use anywhere else, ever again.

Another possibility is to avoid keystrokes altogether. The next sections describes using triggers with the mouse instead.

# Using the Mouse

## Drag and Drop

While it does involve switching between keyboard and mouse, the Quicksilver command window can be a convenient Drag and Drop source or target. With an Open File dialog up from some application, rather than navigating in that window you can activate Quicksilver, type to select the file you want to open and then drag it from the first pane into the Open File dialog. To move a file from the Desktop to a folder, activate Quicksilver and bring up the folder in the first pane, then just drag the file from the Desktop to the folder in the first pane.

You can bring up an e-mail address and drag it into the To: or CC: field of a mail message. Mail doesn’t recognize nicknames in it’s matching so using Quicksilver for this might be convenient. Note you have to drag an e-mail address for this to work, not a contact. You can also drag a file into a message as an attachment.

If the application you’re dropping into doesn’t accept the item your dragging from Quicksilver you’ll probably get the name of the item dropped in. For example, if you drag a file into a web form, you’ll find the file name with its full path entered into the form. Do the same thing with a contact to make sure you get a difficult name spelled correctly. Drag a postal address from a contact into a document or a field in an online mapping service. With proxy objects, you can drag the Current Web Page, the Currently Playing Track, or the Latest Download.

## Mouse Triggers

With the Mouse Triggers plugin installed, triggers can also be assigned to the Mouse. The Settings tab of the drawer for the trigger is different for a mouse trigger. You can assign triggers to a number of mouse clicks, with or without modifier keys. Note that the Anywhere button in the desktop drawing is actually a button. If you want a trigger to work if you <kbd>⌘</kbd>-right-click anywhere in the window, you have to click the Anywhere button for it to work.

You can also activate a trigger when the mouse enters or exits an edge or corner of the screen, or if you drag something to an edge or corner of the screen. Maybe you’d like to hide the current application when you move the mouse pointer to the lower-left corner. If you have multiple monitors connected to your Mac you can choose if the trigger will work on all displays or on a particular one.

Dragging triggers work well with the Mouse Trigger Dragged Object proxy object. Configure these for a commonly used application or folder when dragging to a corner or edge:

  * Mouse Trigger Dragged Object ⇥ ****Open With…**** ⇥ [Application]
  * Mouse Trigger Dragged Object ⇥ ****Move to…**** ⇥ [Folder]

Here are some more advanced ones that might require additional plugins:

  * Mouse Trigger Dragged Object ⇥ **E-mail To… (Compose)**
  * Mouse Trigger Dragged Object ⇥ **Compress (Create Archive)**
  * Mouse Trigger Dragged Object ⇥ **Set Desktop Picture**
  * Mouse Trigger Dragged Object ⇥ **Add Tags…** ⇥ [Tag 1, Tag 2]
  * Mouse Trigger Dragged Object ⇥ **Upload to Site…**** ⇥ [Transmit Favorite]

Note that if you configure a trigger to activate when mousing or dragging to an edge, it might interfere with the shelf or clipboard windows if you have them docked to that edge. In such a case, the trigger will win and you’ll need to use some other means like a keystroke to open the shelf or clipboard windows.

One thing might not be obvious: You can configure the same trigger to activate by multiple means. E.g., if you have an Open Safari trigger assigned to the shortcut <kbd>⌃</kbd><kbd>⌘</kbd><kbd>S</kbd>, you can also assign it to having the mouse enter the left edge of the screen, and both will work. You do this by clicking the icon of the type of trigger in the <kbd>⌘</kbd> column of the Triggers preference pane. A pop-up menu appears of the other choices and you can select another one and configure it. Now both work. This can be useful to have two ways to invoke a trigger: one when your hands are on the keyboard, and another when one hand is on the mouse. There isn’t a way to remove one method from a trigger. The `-` button at the bottom of the screen deletes the whole trigger. For a keyboard trigger, you can always change it to not be bound to a specific key by clicking the Edit button and then the delete key. For a mouse trigger, you can achieve the same effect by choosing Mouse Entered and selecting no edge or corner. To avoid this sort of thing, you can also just create entirely separate triggers that do the same thing with different activations.

Most useful on mouse triggers are the **Show Menu**, **Show Contents Menu**, and **Show Action Menu** actions. These bring up a context menu for the object. **Show Contents Menu** creates a menu for the items that would appear if you typed <kbd>→</kbd> to go into the object. It’s like **Show Contents** but in menu form. Items have sub-menus showing the actions you can perform on them and any children they have. **Show Action Menu** shows a menu of the actions you can perform on an object. **Show Menu** shows a menu that combines the contents and actions you can perform. Mouse triggers for Shelf ⇥ **Show Contents Menu** or Clipboard History ⇥ **Show Contents Menu** are very useful.

## Event Triggers

While keyboard triggers let you do something with a single keystroke, event triggers allow you to do something with _no keystrokes_ (or clicks).

Like all triggers in Quicksilver, event triggers can run any command Quicksilver is capable of running, but instead of running in response to keyboard and mouse activity from the user, they run automatically in response to things happening on your computer. The list of events you can assign triggers to will depend on which Quicksilver plugins are installed, but there are quite a few simply built into the Event Triggers Plugin. As of this writing, there are 38 events you can potentially hook into.

Some examples will probably explain it better at this point. The plugin’s documentation lists the following:

  * When the screen saver activates, pause iTunes.
  * When the computer wakes from sleep, open Mail.
  * When the network changes, run a shell script.
  * When a disk named “Backup” is mounted, compress a specific folder and copy it to the disk.
  * When switching to the internal speakers (headphones disconnected), pause iTunes.

Here are some other ideas:

  * Turn off AirPlay (by switching to the “Computer” device) when headphones are plugged in
  * Switch to the appropriate equalizer preset in iTunes when an optical cable is plugged in
  * When Pages launches, quit Twitter
  * After compressing files or folders, move the archive to the desktop
  * When taking a screen shot, ask me who to e-mail it to
  * Append a message to a file when you lose Internet connectivity

## Abracadabra Mouse Gestures

For this section, install the Abracadabra Triggers plugin. This enables a new trigger type known as a Gesture to go along with Keyboard and Mouse triggers. It also installs an Abracadabra preference pane. 

Abracadabra lets you invoke a trigger by drawing a shape with the mouse. E.g., you can configure Quicksilver to activate the Open Safari trigger by drawing an S on the screen. You configure your shape by drawing with the mouse button down in the pane in the Settings tab of the trigger’s drawer. The “Show zooming trigger window” will show a bezel window that enlarges when a gesture trigger is recognized and executed (like the Display: Show Window option of a keyboard trigger).

In the Abracadabra Preference pane you configure how you invoke all gestures. That is, what mouse button you hold down and/or what modifier key you hold down while drawing any gesture. If you have a mouse with extra buttons it’s probably most convenient to use one of them for this as you’ll only need one hand to invoke the gesture. You can also choose the colors used to draw the shape on the screen as you draw and after you finish for a recognized gesture and an unrecognized gesture, as well as sounds to play. 

There’s also an option to Enable LaserKey Support which is a virtual keyboard device made by Cellulon. With it you can make gestures with your finger. Wherever I say mouse gestures here, LaserKey gestures is implied if you’re one of the lucky few to have one of these devices.

Simple gestures are best as you’ll have an easier time remembering them and Quicksilver will have an easier time recognizing them. You can create a gesture for any Quicksilver command (that is trigger). E.g., skipping to the next track in iTunes by drawing a line from left to right. Try a gesture for the **Quit** or **Hide** actions using the Current Application proxy object.

Gestures also go well with limiting the scope of a trigger and using the **Menu Bar Items…** action. This way you can make a trigger to invoke Safari’s Back command or Mail’s Reply command. This usually works best for things that don’t need the keyboard, e.g., navigating in Safari. Using a gesture to bring up a Find dialog probably doesn’t make much sense since you’ll need to type the text to find.

An interesting idea is using the Current Application proxy object and the **Menu Bar Items…** action to invoke an action common in all applications, e.g., Undo or Close. The problem is that many applications dynamically update their menus (e.g., “Undo Typing”) or slightly rename these commands (e.g., Close Window and Close Tab) so the trigger won’t work in all applications. Also there’s no way to select a menu command that is generic and not specific to an application, so this isn’t possible.

## Command Objects and Droplets

Entire commands in Quicksilver can be represented as a single object. To create a command object, activate Quicksilver and enter a command as you normally do, but instead of typing return to execute it, type <kbd>⌃</kbd><kbd>↩</kbd> to “encapsulate” the command. You’ll see a new command window appear in which the object is a new command object and the action (with default settings) is **Run**.

Actions that work on commands include **Run**, **Run after Delay…**, **Run at Time…**, **Add Trigger…**, and **Save Command to File…**. The first, **Run**, is obvious and not particularly useful since just executing the command without creating a command object is easier. The other two are useful as alarms when used with actions like **Large Text** or **Display Dialog**. A delay period is entered as a decimal number followed by an h, m or s to indicate hours, minutes or seconds. E.g., 2h, 10m, 90s, or 1.5h. A number without a suffix is interpreted as minutes. You can combine these separated by spaces such as 2m 30s. You can also enter a time format such as minutes:seconds or hours:minutes:seconds. For example 9:35 or 2:11:30. I believe you can also enter decimal numbers with colons like 1.5:10:00 for 100 minutes but that is probably not useful.

Times for **Run at Time…** are typically entered as a digital clock, hh:mm:ss although it uses macOS’s natural language date parser, so things like “3pm December 15, 2018” or “next Tuesday at dinner” are supposed to work.

There’s also an **Add Trigger…** action which will ask for the type of trigger in the third pane, then open the trigger preferences with most of your new trigger already configured.

The **Save Command to File…** action takes a command object and saves it in a file. You enter a folder name as the argument and Quicksilver saves a file there with the extension `.qscommand`. If you open the resulting file (e.g., by double-clicking it), it will run the command. Quicksilver makes running commands simple and triggers make running command even easier. But for commands that you might run a few times but not enough to bother creating a trigger for, the **Save Command to File…** action can be useful. E.g., if your working on creating a document and you want to send several drafts to a group of people (using the comma trick) it’s easy to save this (complicated) command in a file to rerun.

With a saved command on your Desktop you might want to be able to drag a file onto the command and have it run on that file. This type of saved command is known as a Droplet. To create a droplet, use the Droplet Item proxy object in the command and save it using the **Save Command to File…** action. The command file will have a special icon and a `.app` extension. Whatever you drop on the droplet application will take the place of the Droplet Item proxy when the command is executed.

# Plugins

Quicksilver is designed with a central core that implements some basic functionality, but most of the features are implemented in plugins. You can pick and choose which plugin functionality you want, but must install the plugins before that functionality is available. Managing the plugins including finding, installing, enabling, and removing is done entirely from within Quicksilver in the Plugins Preferences (though additional configuration in Preferences or the Catalog may be useful or necessary). You can bring it up from the menu, or by activating Quicksilver and typing <kbd>⌘</kbd><kbd>"</kbd>.

The plugins are shown in the right pane, with a checkbox showing if they are enabled, a column showing the version number, and the date the installed version was released. The left panel shows sets of plugins:

  * **Recommended** - Plugins can appear on this list based on the applications you have installed, files that might exist on your system, or because they’re considered generally useful. This is also the list Quicksilver presents during the initial setup process.
  * **Installed Plugins** - All installed plugins are listed here. Only those that are checked are enabled. Those not checked are installed, but disabled.
  * **Disabled** - Plugins you’ve installed, but disabled are shown here. These may be candidates for removal.
  * **Not Installed** - To quickly see if there are any potentially useful plugins you don’t yet have, you can see a list of ones you don’t have installed.
  * **All Plugins** - All available plugins from the update server are listed here. Checked plugins are installed and enabled, unchecked plugins are not installed. <kbd>⌥</kbd>-click on this to show some hidden plugins.

    This section can be expanded to show a list of categories. Plugins can be in more than one category.

Checking a plugin will enable it, downloading and installing it if necessary. Selecting a plugin and clicking the ⓘ button will open a drawer with additional details:

  * Author(s)
  * A short description
  * Installed version (if installed)
  * Latest version available from the update server (based on your version of Quicksilver and macOS)
  * Status, which normally shows “Loaded”. If a plugin fails to load for some reason, you might find a helpful message here.

Clicking the `?` button will open the plugin’s documentation in a new window. Reading this for any installed plugins is highly recommended. Some less obvious features and uses can be discovered in the docs.

Selecting one or more plugins and clicking the gear button opens a pop-up menu of things you can do to plugins including install, download, copy, and delete. Delete is the only one you’ll typically use from this menu. The last three items in the menu are options you can enable or not.

The Refresh button (circular arrow) will refresh the list of plugins from the update server.

To disable a plugin, uncheck it. Its features will no longer be available but its code will still be loaded into memory. To clean up this memory (possibly fixing stability issues), restart Quicksilver. The plugin is still installed on disk (so it will appear unchecked in the Installed Plugins view) until it is deleted.

If you expect to see a plugin in the list and don’t, try refreshing the list of plugins. 

If you’re having problems installing plugins check the ownership and permissions on `~/Library/Application Support/Quicksilver/PlugIns/` and its parent directory. Use the Finder’s Get Info command (from the File menu) to see the Ownership & Permissions of a folder. It should be owned by you and you should have permission to read and write it. Usually quitting Quicksilver and removing (or moving) the PlugIns folder or its parent Quicksilver folder and restarting Quicksilver (allowing it to recreate the folder) will solve any problems. Of course removing the Quicksilver folder will remove any customizations you’ve made.

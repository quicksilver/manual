# General

Quicksilver's Preferences are divided into sets at the left of the window. Those listed at the top are built-in to Quicksilver and those in the bottom section are enabled by installed plugins.

## Application

The Application Preferences control the most fundamental aspects of Quicksilver as an application. Once you're hooked on Quicksilver you'll want to enable **Start at login**.

Quicksilver shows an icon in the Dock like most applications, but many people prefer to disable this. Uncheck the box to disable the Dock icon. The ⌽ symbol indicates Quicksilver must be restarted before the change will take effect. An easy way to restart is to activate Quicksilver and then type <kbd>⌃</kbd><kbd>⌥</kbd><kbd>⌘</kbd><kbd>Q</kbd>.

Without a Dock icon, Quicksilver runs as a background process. This means it won't appear in the Dock or when switching apps with <kbd>⌘</kbd><kbd>⇥</kbd> and the main Quicksilver menu will not appear while the preference window is open.

The **Show icon in menu bar** preference puts an indicator in the top right part of the screen. Some people like this, particularly if they don't configure a Dock icon or have their Dock hidden. It provides a simplified menu to access the various configuration panes of Quicksilver. For access to the full menu options (via more sub-menus) set the option **Include access to all menu items from menu bar**.

The next section controls if and how Quicksilver checks its website automatically for updates both for updates to Quicksilver and for all installed plugins. It can be configured to check on launch, daily, weekly or monthly. The Check Now button will, not surprisingly, check immediately for an update.

The three buttons at the bottom will rerun the installation setup described in the [Installation](../getting-started/installation.md) section, Reset Quicksilver's preferences, and completely Uninstall Quicksilver.

The Appearance Preferences control how Quicksilver looks.

The command window  supports various skins or themes, known as Interfaces and installed via plugins (all of which end with the word Interface). Select the Interface to use here via the popup list showing all installed Interfaces. See the Interface section below for details.

The default interface is Primer and it shows a little more context information than other interfaces so it's recommended for new users. The other builtin interface is Bezel interface; it's very popular and is shown throughout this manual.

The Colors options allow further customization of the appearance of the interface and vary per interface. The column headers have tooltips showing what they represent: Background, Selection & Accents, and Text colors. Clicking on the nine colors in the grid will bring up a color picker.

## Command

The Command Preferences allows configuration of the command window's behavior.

### Activation Shortcuts

The top of the pane affects how you activate Quicksilver. The Keyboard Activation is the basic way to activate Quicksilver. The default is to type <kbd>⌃</kbd><kbd>Space</kbd>, though <kbd>⌘</kbd><kbd>Space</kbd> is a common alternative.

The shortcut is configurable in the Command Preferences Pane under Activation. Quicksilver defaulted to <kbd>⌘</kbd><kbd>Space</kbd> for a long time, but with 10.4, Apple chose to use <kbd>⌘</kbd><kbd>Space</kbd> for Spotlight. So Quicksilver changed its default to <kbd>⌃</kbd><kbd>Space</kbd>. If you look at older posts on the Web, or even current posts from long-time users, you'll often see <kbd>⌘</kbd><kbd>Space</kbd> used to activate Quicksilver.

A common setup is to use <kbd>⌘</kbd><kbd>Space</kbd> for Quicksilver and <kbd>⌥</kbd><kbd>⌘</kbd><kbd>Space</kbd> for Spotlight (set in the Spotlight System Preference pane of macOS). An advantage is that many shortcuts used after activating Quicksilver use <kbd>⌘</kbd>, so using the same modifier key is easier. For example, <kbd>⌘</kbd><kbd>,</kbd> will open up Quicksilver's Preferences.

**Modifier-only Activation** allows you to activate Quicksilver by single or double presses of modifier keys such as <kbd>⌃</kbd>, <kbd>⌥</kbd>, <kbd>⇧</kbd>, <kbd>⌘</kbd> or even <kbd>fn</kbd>. The activation is only triggered when you "tap" the chosen key and nothing else, so accidental activations are _far more rare_ than you might expect.

**When activated, switch keyboard to** allows you to force Quicksilver to use a different keyboard layout than the one you use for macOS in general. <!-- TODO: use case? -->

### Searching and Spacebar Behavior

Thanks to Quicksilver's matching algorithm, the spacebar is completely unnecessary for searches in the command window. The **Spacebar behavior** preference lets you reclaim that easy-to-smack key and make Quicksilver a little faster to use. The options are:

  * **Normal** - Literally type a space and include it in the search term
  * **Select Next Result** - Select the next result in the results list, like typing <kbd>↓</kbd>
  * **Jump to Argument List** - Change to the third pane
  * **Switch to Text Mode** - Change the current pane to text mode entry, like typing <kbd>.</kbd> or <kbd>'</kbd>
  * **Show Item's Contents** - Goes into the item, like typing <kbd>→</kbd> or <kbd>/</kbd>
  * **Quick Look** - Show the selected file(s) using Quick Look
  * **Smart** (default) - Select one of the above behaviors automatically based on context

The smart spacebar tries to be the best of all worlds and do what you probably want in any given situation. This is how it decides what to do:

  * If in the second pane, select the first action that takes an argument in the third pane.
  * If user is holding Shift, go to the parent (same as left arrow).
  * If the object has children, show them (same as right arrow) unless it's a text file.
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

Selecting **Show children split view** will split the results list vertically into two columns, the right one showing the contents of the selected item in the left one (much like the column view of the Finder). You must restart Quicksilver for changes to this setting to take effect. When first enabled you'll only see one column, but notice the small dot in the middle of the right edge, you can click on and drag that to the left to reveal the second column. **This feature will slow Quicksilver down tremendously (as it's constantly loading children you probably don't care about) and should never be used.**

You can specify the Row Height in pixels. A higher value will show a larger image on each row. A lower value will result in a single line per entry (showing label, but not details). The details for the selected entry will be shown in the bottom of the window in that case.

**Show other results** controls if the results list appears after you type into the command window immediately, after a short delay, or not until you manually scroll with <kbd>↓</kbd>.

## Appearance

Interface plugins change the look of Quicksilver's command window. Install them just like other plugins from the Plugins Preferences, then select one of the installed interfaces in the Appearance preference pane. If you use a remote control application to connect to different machines, you might want to configure them with different interfaces or change the colors on the interface to distinguish them.

Two interfaces are included with Quicksilver out of the box. Primer (the default) is intended for new users as it does a better job of labeling things and helping you understand what's going on. Bezel is a nice looking interface that places emphasis on icons over text.

The Colors and Text sections can be used to adjust the look of the selected interface (and the results list) if that interface supports it. Some interfaces have a hard-coded look and will ignore these settings.

Some interfaces will offer a Customize button that provides additional adjustments specific to that interface.

## Actions

All of the actions available in Quicksilver are listed in this section of the preferences. It's a good idea to scan through this list to get an idea what sort of things are possible.

### Viewing Actions

The default is to group actions by type. That is, clicking a type on the left will narrow the list of actions on the right to only those that work with that type. You can also view the actions by plug-in. Choosing a plug-in on the left will narrow the list of actions to only those provided by that plug-in.

You can also narrow the list of actions by name using the search field.

The list of actions will also show the alternate action if one exists. Alternate actions provide a quick way to do something slightly different from the selected action by hitting <kbd>⌘</kbd><kbd>↩</kbd> instead of just <kbd>↩</kbd>. For example, if you select a file and run the **Open** action, the file will open. Hitting <kbd>⌘</kbd><kbd>↩</kbd> instead will run the **Reveal** action instead, showing the file in Finder.

### Adjusting actions

The checkbox next to every action allows you to enable or disable it. You may want to disable some you think you'll never use. Some of the more technically oriented or dangerous actions are disabled by default, but you can enable them here.

The most important use for the action preferences is to control the order in which they appear. The goal is for the actions you use most often to be selected by default so you'll rarely need to go to the second pane and choose one manually. You can change the order by dragging and dropping.

When you select an object in Quicksilver's first pane, the highest ranked applicable action will be the one selected by default in the second pane. The word "applicable" there is important and deserves some discussion: The second pane will only contain actions that can be used on whatever you select in the first pane. Because of this, _you will generally want to put more specific actions (those that only apply to one or two types) high up on the list, and the more general actions lower_. For example, dragging the **Open URL** action all the way to the top will not annoy you by constantly showing that action when you select files because it will only appear when you select a URL. On the other hand, an action like **Paste** can be used on any object, so placing it high on the list _will_ annoy you because you probably don't want it to be the default for everything you select.

Quicksilver and its plug-ins ship with reasonable defaults for the action rankings, but you might want to make adjustments. It might take some experimentation with real-world use before you get things just right.

## Extras

The Extras Preferences have some advanced options.

**Show the Task Viewer automatically when tasks are created** will let you keep tabs on things Quicksilver does in the background. Unless you interact with it, the Task Viewer will hide itself again once all tasks are complete.

If you prefer concentrating on one thing at a time, check **Hide other applications when switching applications** so that Quicksilver will do a **Hide Others** after switching applications. You can prevent the hiding behavior by holding down the Shift key when completing the command.

**Run tasks and actions in the background** prevents longer-running commands from locking up Quicksilver's interface until they finish. You should only disable this if something isn't working as expected.

**Reopening the current application** configures what happens if you use the Open action on an application that is already running. You can have it activate the application, show the front window, or show all windows.

**Application Update Type** allows you to choose between Prerelease Candidates and Final Releases when Quicksilver checks for updates as configured in the Application Preferences. Sometimes after installation this is set to a blank value and that has been observed to cause problems, make sure it's set to some value in the popup.

Since the matching algorithm is case-insensitive the Shift key is available for some use in Quicksilver. If you check **Allow capitalized keys to select the action** then shifted letters are used to select the action, eliminating the need to tab to the second pane. Once moved to the action pane, unshifted letters don't change the first pane, all typing counts for the second pane. If you also hold down the <kbd>⌘</kbd> key the action will be performed immediately, no need to type return. E.g., <kbd>⇧</kbd><kbd>I</kbd> selects the action for "i" (perhaps **IM**) while <kbd>⇧</kbd><kbd>⌘</kbd><kbd>I</kbd> performs the action for "i". Use caution, as it's not always clear which action is invoked.

If you enable **Disable Keyboard Triggers when Quicksilver is focused** then keyboard triggers will not work while Quicksilver is activated (i.e., the command window is open). I have no idea why you would want to enable this. If you don't want a particular trigger to work when Quicksilver is active, this can be configured in the individual trigger's settings.

**Pressing the Delete key clears the whole search string** disables the default behavior of removing a single character at a time from the search string. With this enabled, you can immediately start a new search by hitting <kbd>⌫</kbd>, and clear the interface entirely with <kbd>⌫</kbd><kbd>⌫</kbd>.

## Handlers

Quicksilver not only makes it easier to work with a variety of applications, it sometimes uses other applications to perform commands. These are configurable in the Handlers Preferences pane.

  * **E-mail** - The e-mail client to use for Send/Compose actions
  * **Command Line Interface** - The terminal program to use for command-line actions
  * **String Ranker** - Choose either the default built-in ranker, or the TextStart Ranker, which uses a different matching algorithm. See the [TextStart Ranker](../getting-started/invoking-quicksilver.md#textstart-ranker) section for details.
  * **File System Browser** - The application to use for file system actions like Reveal, Open, or Copy
  * **Missing Object Selector** - This is the interface Quicksiver will present if you need to select an object for the third pane.
  * **Notification** - How to display notifications. See the next section.

It's important to understand that the choices here actually refer to Quicksilver plug-ins and not the applications themselves. So for example, you won't see every e-mail client on your system listed. You will only see the ones for which a plug-in exists and has been installed.

### Notifications

The Notifications Hub plugin allows finer granularity in configuring notifications. It adds a new preference pane called Notification Hub. There you can configure a default notifier as well as configure specific notifiers for specific events. E.g., iTunes notifications go to the Quicksilver built-in notification notifier while Plugin Installation notifications go to Growl. You can even send the same notification to multiple handlers by adding multiple lines for the same Notification and with different notifiers.

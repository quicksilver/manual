# Tips

A collection of tips for Quicksilver, originally posted on the @LoveQuicksilver Twitter account.

## Browsing and Navigation

  * Pressing <kbd>⌫</kbd> while typing resets the search text without removing the Object in pane 1. Press it again to clear pane 1.
  * Dismissed Quicksilver and want to search the last object's folder again? Activate QS, press <kbd>←</kbd> then <kbd>→</kbd> and it's ready to search.
  * Instead of using <kbd>→</kbd> and <kbd>←</kbd> to browse in Quicksilver, try <kbd>/</kbd> and <kbd>?</kbd>.
  * <kbd>⌥</kbd><kbd>→</kbd> into folders when browsing in Quicksilver to see hidden files and folders. Also allows you to directly get into packages (e.g., `.app`, `.pages`, `.rtfd`).
  * Paste a path like `~/Downloads` directly into pane 1. Quicksilver will change it to a file. Or type it in; its icon will show when QS finds a matching path.
  * Get the last Quicksilver object by invoking QS and hitting <kbd>⌘</kbd><kbd>[</kbd> (Last Object Proxy). Useful if the 1st pane is wiped accidentally.

## Actions and Execution

  * Hit <kbd>⌘</kbd><kbd>⇧</kbd>(letter) in Quicksilver to launch the default Action for <kbd>⇧</kbd>(letter). For example, <kbd>⌘</kbd><kbd>⇧</kbd><kbd>O</kbd> executes **Open** (if it's the default for "O").
  * **Reveal in Finder** instead of **Open**: With a file in the 1st pane, <kbd>⇥</kbd>, <kbd>⌘</kbd><kbd>↩</kbd> to use the "alternate" Action. Check it out with other Actions!
  * Enable "Capitalized keys modify action in command window" in Preferences → Extras to avoid having to tab to alter the Action.
  * Right-click on an Object in pane 1 to see its alphabetical list of available Actions. Great for an overview.
  * Hold a key for a tad longer in Quicksilver to avoid having to press <kbd>↩</kbd>. Try it: Press and hold "a", and the default for "a" is acted upon.
  * If you press <kbd>⌃</kbd><kbd>↩</kbd> instead of <kbd>↩</kbd>, Quicksilver combines the panes so you can choose **Run after Delay** in pane 2, and enter a time period in pane 3. Cool for Triggers!

## Triggers

  * Make a Trigger for Downloads ⇥ **Show Contents**. Instant results without putting the contents in the Catalog or waiting for a rescan.
  * Make a Trigger for Airport ⇥ **Show Contents** to get a list of available networks. Instant access.
  * If you've installed the iTunes module for Quicksilver, check out the iTunes-specific triggers, e.g., "Show Playing Track".
  * Can't find an Action when making a Trigger? Try <kbd>⌘</kbd><kbd>C</kbd> from pane 2 of Quicksilver in normal use, then <kbd>⌘</kbd><kbd>V</kbd> into pane 2 of Trigger creation.
  * Launch and hide your most common applications with Triggers in Quicksilver: Set up a Trigger: (application(s)) ⇥ **Toggle Application**.

## Catalog

  * Quicksilver as Launchpad: Make a Trigger for Applications (Catalog) ⇥ **Show Contents**. Fully searchable!
  * To search by file extension, make sure Quicksilver's Search Mode is set to "Filter Results".
  * Make a custom Catalog entry for `/Volumes` (<kbd>⌥</kbd><kbd>→</kbd> into `/`) with a depth of 1. Quick access to any connected storage from Quicksilver.
  * To add to the custom Catalog, don't use the "+" button at the bottom — drag a file/folder from Quicksilver's interface into the list.
  * Bump results up the list by clicking the dot beside the entry to "Set as Default". Or use the **Assign Abbreviation** Action.
  * Plugins labelled with a "(+)" need "Enable advanced features" in Quicksilver's Preferences → Application pane to work.

## Clipboard and Shelf

  * Use the Shelf/Clipboard to store/paste special characters. Make Shelf ⇥ **Show Contents** into a trigger.
  * Navigate folders from Quicksilver's Shelf. Find them with a Shelf ⇥ **Show Contents** Trigger.
  * Add a color to Quicksilver's Shelf from the Color Picker, then paste it onto selected text to change its color.
  * Remove clipboard text formatting/make plain text in Quicksilver. Set up a Trigger with: `pbpaste | pbcopy` (**Run Command in Shell**).

## Interface and Preferences

  * Alter Quicksilver's command window colours in Preferences → Appearance. You can enable/disable glass/shadows and alter colours.
  * Open the Quicksilver interface with a single key by enabling the "Modifier-only Activation" setting in Preferences → Command.
  * Set up Quicksilver to activate with a single or double tap of either <kbd>⌘</kbd>, <kbd>⌥</kbd>, <kbd>⌃</kbd>, <kbd>⇪</kbd> or <kbd>fn</kbd> in Preferences → Command.
  * Set the spacebar behavior to "Jump to Argument Field" in Preferences → Command. Space gets the first Command using pane 3. Default: **Open**, space: **Open With...**
  * Make Quicksilver even faster! Try setting "Show other matches" to "Never" or "Delayed" in the Preferences → Command.
  * Show results in Quicksilver's 1st pane more quickly by reducing the "Wait before searching" time in Preferences → Command. Try 0.00s.
  * View more results in the drop-down Results List by altering the Row Height in Preferences → Command. Try setting it to 26.

## Miscellaneous

  * Pipe files to Quicksilver from Terminal by installing the Command Line Tool plugin. Usage: `qs file` or put on the Shelf using `qs -s file`.
  * Get selected text into Quicksilver: check "Send to Quicksilver" in Keyboard System Preferences.
  * Type <kbd>=</kbd> in the 1st pane to enter Quicksilver's Calculator mode. Simple math only, and requires the Calculator Module.
  * Use plain text files as snippet libraries searchable from pane 1: make a Trigger for (plain text file) ⇥ **Show Contents**.
  * Quit and Relaunch multiple applications with the comma trick. Invoke Quicksilver, type your applications (comma separated) <kbd>⇥</kbd> **Quit** or **Relaunch**, <kbd>↩</kbd> — done.
  * Use the first pane to locate files and then drag and drop, e.g., for attachments.
  * Relaunch Quicksilver easily by activating the interface and holding <kbd>⌘</kbd><kbd>⌃</kbd><kbd>Q</kbd>.

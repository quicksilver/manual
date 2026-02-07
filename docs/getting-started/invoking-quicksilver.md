# Invoking Quicksilver

macOS uses the term "activate" to mean switching to an application (starting it if necessary). In fact there's a Quicksilver action called Activate that does just that. The menu bar shows the menus of the active application. But if you hide its Dock icon (as most users do) Quicksilver runs in the background and unless it's Preferences are open, it's not the active application. Invoking Quicksilver, that is calling it forward and making it ready to use, is typically done by using the keyboard shortcut (by default <kbd>⌃</kbd><kbd>Space</kbd>) to bring up the command window. The first pane is selected and ready to find something in the Catalog via typing.

## Selecting Items

With Quicksilver activated and the first pane selected, type some characters and an object will appear. To bring up a Contacts entry for Abraham Lincoln (doesn't everyone have him in their address book?), type <kbd>A</kbd><kbd>B</kbd><kbd>R</kbd><kbd>A</kbd><kbd>H</kbd><kbd>A</kbd><kbd>M</kbd>, <kbd>A</kbd><kbd>B</kbd><kbd>R</kbd><kbd>A</kbd><kbd>H</kbd>, <kbd>A</kbd><kbd>B</kbd>, or maybe just <kbd>A</kbd><kbd>L</kbd> to select it. The trick is to keep typing the name of item until it appears in the first pane (and at the top of the results list).

If it doesn't quite make to the top of the results list, scroll through the list and find the item and click it to select it. This can happen if there are several objects with the same name, for example a Contacts entry for Abraham Lincoln and a Finder folder named the same thing.

Quicksilver remembers what's been typed and what's been selected and learns to
guess better as its used. If I type <kbd>A</kbd> and pick Abraham Lincoln's
Contacts entry, Quicksilver will start to guess it more often instead of the
folder of the same name or "AirPort Utility" or "Adium" or other things that
begin with "A".

The matching algorithm that Quicksilver uses for selecting objects and how you can help it learn more efficiently are discussed below.

By default Quicksilver shows the results list after a short delay. This behavior can be changed to Immediately or Manually in the Command Preferences under "Show other matches". There is also a choice to configure the spacebar to behave like <kbd>↓</kbd> or <kbd>→</kbd>.

## Navigation

Quicksilver includes a lot of things in its Catalog, but to keep things fast, it doesn't include everything on the system and (unlike Spotlight) it doesn't index the contents of objects, just their names. Lincoln's Contact entry may have his phone number and e-mail address, but typing them in the first pane won't match the Contact. Quicksilver can navigate an iTunes music collection, but doesn't include all songs and artists in the Catalog.

That's not to say Quicksilver can't use and manipulate these things. Once a parent object (in these examples, a contact or the iTunes app) is selected, typing <kbd>→</kbd> will move into the object and the results list will show its children (the contact fields or music collection). The results list displays items with children by showing a &gt; at the far right. Navigating like this is often referred to as "right-arrowing into an object". Similarly <kbd>←</kbd> will go "up" and select the parent object. Quicksilver can navigate files and folders this way too. So while every file might not be indexed in the Catalog, the entire filesystem can be navigated using the arrow keys in Quicksilver. Since right-arrowing into folders is so common, the <kbd>/</kbd> key does the same thing as <kbd>→</kbd>, while <kbd>⇧</kbd><kbd>/</kbd> is equivalent to <kbd>←</kbd>. (That key was chosen because `/` is used as the separator between folders and files in a path. It's also easier to reach on most keyboards.)

## Alternate Keystrokes

A mouse or trackpad can be used to navigate the results list, but Quicksilver can do virtually anything from the keyboard. The <kbd>↓</kbd> and <kbd>↑</kbd> keys will move the selection in the results list down and up one item. For touch typists, the keystrokes <kbd>⌃</kbd><kbd>N</kbd> (next) and <kbd>⌃</kbd><kbd>P</kbd> (previous) will do the same thing and <kbd>⌃</kbd><kbd>V</kbd> and <kbd>⌥</kbd><kbd>V</kbd> will scroll the results list down or up one whole screen.

For Vim users, <kbd>⌃</kbd><kbd>H</kbd>, <kbd>⌃</kbd><kbd>J</kbd>, <kbd>⌃</kbd><kbd>K</kbd>, and <kbd>⌃</kbd><kbd>L</kbd> can also be used in place of the arrow keys.

## Dealing with Typos

By default as of Quicksilver 1.5.1, the <kbd>⌫</kbd> key will remove a single character from your search string. If the search string is empty, typing will begin a new search (even if the previous selection is still shown), while hitting <kbd>⌫</kbd> again will clear the current selection.

New users should find the ability to remove a single character more intuitive, but for many years (prior to 1.5.1), there was no way to delete just a letter or two. The delete key <kbd>⌫</kbd> would clear the entire search, allowing you to immediately start a new one.

As you become more experienced, you may realize that simply starting over is much faster than correcting a mistake in the current search. For example, if you've built up years of muscle memory typing <kbd>G</kbd><kbd>R</kbd><kbd>L</kbd><kbd>I</kbd> to find your grocery list, but you accidentally type <kbd>G</kbd><kbd>R</kbd><kbd>I</kbd><kbd>L</kbd> one day, wiping the search with a single press of <kbd>⌫</kbd> and letting your fingers do what they're used to is much easier than trying to figure out what you did wrong, how many characters you need to erase, what you need to then type to fix it, etc. The old behavior can be restored under Preferences → General → Extras.

The interface can be cleared entirely by pressing <kbd>⌫</kbd> with an empty search string, or by pressing <kbd>⌃</kbd><kbd>U</kbd> or <kbd>⌘</kbd><kbd>X</kbd> at any time. (The latter will copy the object to the clipboard.) If a Quicksilver pane is in text mode these behave slightly differently, as shown below.

| Shortcut | Regular Mode | Text Mode |
| --- | ------------ | --------- |
| <kbd>⌫</kbd> | removes one character from the search, or clears the selection | deletes one character |
| <kbd>⎋</kbd> | closes results list if open, or dismisses Quicksilver | leaves text mode |
| <kbd>⌃</kbd><kbd>U</kbd> | empties window, dismisses results list, back to top | nothing |
| <kbd>⌘</kbd><kbd>X</kbd> | empties window, dismisses results list, back to top, copies object to clipboard | deletes selection, copies selection to clipboard |

The Command Preferences has an option, "Reset search after" time. This is how long between keystrokes Quicksilver waits before reseting the search. So if it's set to .85 seconds and it's been 1 second since a key has been typed, typing another one will start a new search in the current context.

## Combining Activation and Selection

There are faster ways to use Quicksilver too. You can activate it and put something in one or more panes at the same time. Triggers let you define key sequences, mouse clicks, and mouse gestures that will activate Quicksilver and fill in some panes and even execute commands immediately. These are discussed in more detail later but it's worth describing two triggers now.

In the Triggers Preferences under Quicksilver are two predefined triggers: **Command Window with Selection** and **Command Window in Text Mode**. The first opens a command window with the current application's selection in the first pane. This is typically text, though for the Finder this is one or more selected files or folders. Some other applications like iTunes also allow their non-text selection to be brought into Quicksilver. The second trigger will bring the selection into the first pane but will put that pane into text-mode so you can edit it.

Quicksilver installs a service available in other applications (look in the application's menu under Services and you'll see Quicksilver). The service is called **Get Current Selection**. It activates Quicksilver and puts the application's current selection (typically text) into the first pane.

You can use this service from anywhere by selecting something and hitting <kbd>⌘</kbd><kbd>⎋</kbd>. You can change this shortcut in Preferences → Triggers → Quicksilver. If <kbd>⌘</kbd><kbd>⎋</kbd> isn't working for you, check in the Catalog under Quicksilver that Internal Commands is enabled.

Yet another way to put the selection into the object pane is to activate Quicksilver and then type <kbd>⌘</kbd><kbd>G</kbd> (for "grab"). This is slower than the other methods since you have to activate Quicksilver first, but since I learned it first, it's in my fingers, so I use it a lot.

If Quicksilver is already running, clicking on its Dock icon will bring up the command window. If you drag and drop something onto the icon it will be selected in the first pane. This is convenient if Quicksilver is in your Dock, but people also put it in the Finder's sidebar or toolbar. This is particularly useful if you hide your Dock and use Finder windows often. (I find the more I use Quicksilver, the less I use the Finder).

There are other, less obvious ways to select something in a Quicksilver command window pane. As discussed above you can type <kbd>⌘</kbd><kbd>G</kbd> to grab the selection of the frontmost application. You can also paste something into the pane with the standard key binding <kbd>⌘</kbd><kbd>V</kbd>, and you can drag and drop something into a pane as well.

## History

The Catalog has two built-in presets for Recent Objects and Recent Commands. If Recent Objects is enabled, you can quickly navigate and act on your history.

  | Shortcut                              | Purpose                          |
  | --------------------------------------| -------------------------------- |
  | <kbd>⌘</kbd><kbd>[</kbd>             | go back in history               |
  | <kbd>⌘</kbd><kbd>]</kbd>             | go forward in history            |
  | <kbd>⌃</kbd><kbd>⌘</kbd><kbd>[</kbd> | show history in the results list |

Showing the history in the results list allows you to search for something using Quicksilver's matching algorithm.

Recent commands can be searched for by name in the main Catalog, or if the Quicksilver Catalog Entries preset is enabled, you can search for and right-arrow into "Recent Commands (Catalog)".

History is discarded when Quicksilver quits. To clear history without restarting, search for "Clear Quicksilver History" in the Catalog and run it.

## Immediate Execution

You can create triggers that perform an entire command, like open an application or file. Triggers are great but they require you to pre-configure them. You can also perform a command by holding down the key you use to select a subject or action. For example, if you type <kbd>A</kbd><kbd>D</kbd> to select Adium.app and hold down the <kbd>D</kbd> then Quicksilver will execute the default action which should be **Open**. As described above, for me typing <kbd>A</kbd> will default to the Contacts contact for my friend Ashish. I can activate Quicksilver and hold down <kbd>A</kbd> to open an e-mail message (the default action for a contact) addressed to her.

This trick also works for actions. If you hold down the last key you type to select an action it will execute it. So I can select Ashish in the first pane, tab to the second and hold down <kbd>E</kbd> to use the **Edit Contact** action. This method is a little risky if you don't know what the action will be, but if you do it's a little faster and there's no trigger configuration needed.

To make it faster you can type the letter that matches an action with the <kbd>⇧</kbd><kbd>⌘</kbd> modifiers while still in the first pane. So to edit Ashish's contact entry I would activate Quicksilver, type <kbd>A</kbd> to bring up her entry and then type <kbd>⇧</kbd><kbd>⌘</kbd><kbd>E</kbd> to have Quicksilver execute the command. This only allows you to use one letter to identify the action and has the same risk that you have to know what action will be run, but if you do, it can be convenient.

Holding down <kbd>⇥</kbd> for a while will execute the command, if for some reason you'd rather do that than hit <kbd>↩.</kbd>

## The Comma Trick

A non-obvious feature is known as the **_comma trick_**. The <kbd>,</kbd> key allows multiple items to be selected in first or third pane, and then a single action can operate on all of them with one command. This can move several files to the same place or address an e-mail to multiple people.

Activate Quicksilver, select an item, type <kbd>,</kbd> and then select another item. A collection of smaller icons accumulate at the bottom or left of the object pane depending on the interface used (the menu interface does not support the comma trick). Any number of items can be selected, after which <kbd>⇥</kbd> to the action pane and continue as normal.

Another way to select multiple items is with <kbd>⌘</kbd><kbd>A</kbd>. It will select all the items in the results list as if the comma trick had been used individually for all of them. If the results list is long this can take a long time. It's most useful to operate on all the items in a small folder (e.g., deleting, moving, or tagging them all).

Collections can be browsed using <kbd>⌃</kbd><kbd>[</kbd> and <kbd>⌃</kbd><kbd>]</kbd>. The currently selected object can be removed from the collection with the <kbd>⌫</kbd> key. <kbd>⌥</kbd><kbd>,</kbd> will remove the most recent item added to the collection, no matter what you have selected.

## Filtering the Results List

The default behavior of Quicksilver is to **_filter_** the results list when searching. As keys are entered, things that don't match are removed from the results and the remaining items are sorted based on how well they match what was entered.

There's an often overlooked gear menu at the top right of the results list. It can change the search mode of the results list. Instead of filtering the results list can be set to snap to a match. The items remain sorted and as keys are typed the selected item is changed (and the list scrolled) but non-matching items aren't removed from the list.

Sometimes these behaviors are known as **_narrowing_** (filtering) and **_selection_** (snapping).

  * **_Filter Results_** - Filters the current results list.
  * **_Filter Catalog_** - Filters, but also includes the entire contents of the top-level catalog. Lasts until you type <kbd>⎋</kbd> or activate Quicksilver again.
  * **_Snap to Best_** - scrolls the results list to the best match but doesn't remove non-matching items.

## Helping the Matching Algorithm

Quicksilver learns what you do (and makes that easier to do) because of its matching algorithm. It remembers what commands you execute and what you did to call them up. Do them a few times and they get easier to call up because those objects and actions appear higher in the results. However if you do things that are similarly named it confuses Quicksilver and it won't guess as quickly as it could. Fortunately you can teach it. Triggers, described above, are the fastest way to do things in Quicksilver, but there are only so many keystrokes you can remember. Here are some other techniques you can use.

If you activate Quicksilver and start typing into the object pane you'll see a results list appear of items that match what you've typed. The order of the items is known as their **_rank_**. The first item is ranked 1 the second is ranked 2, etc. For objects, the rank is determined based on the score of the items. **_Score_** is computed based on how well an item matches what you typed.

Theoretically, items move to second place rank the first time they are used to match some input. The second time they are used they get ranked first. The circle to the left of the item indicates how well the item matches the typed input. The darker the circle, the stronger the match (i.e., the higher the score).

You can manually adjust the score of an item by <kbd>⌃</kbd>-clicking on it to bring up a menu of choices. If you choose "Set as Default for…" then the selected item will match if you type the same abbreviation again. You can undo an abbreviation by choosing Decrease Score in the menu.

Setting a default works for what you've typed, but say you want to set as a default something that is mid-way in a very long list that you don't want to scroll through. As an example say you want "Z" to bring up your Amazon bookmark and that if you type <kbd>Z</kbd>, Amazon is further down the list than you want to look. In that case, use the **Assign Abbreviation** action. Bring up the object you want in the first pane (www.amazon.com), choose **Assign Abbreviation** as the action, and in the third pane enter the abbreviation you want via text mode (<kbd>Z</kbd>). Now if you type that abbreviation in either the first or third pane, your choice will be ranked first. This happens because exactly matching an abbreviation causes the item to have a very high score.

!!! note
    Abbreviations will only work if they match the input string in some way. You can't set <kbd>I</kbd><kbd>R</kbd><kbd>C</kbd> to be an abbreviation for `Colloquy.app` because if you typed <kbd>I</kbd><kbd>R</kbd><kbd>C</kbd>, Colloquy would not appear in the results list. Say you don't use Activity Monitor often and when you want it you can never remember its name but you think of the word "processes". Searching for "proc" won't work since those letters don't appear in "Activity Monitor". [Synonyms](#synonyms) were created for situations like this.

Actions in the second pane work a little differently. When they initially appear, their rank is statically determined by their order in the Actions Preferences. You can manually change the order in Preferences by dragging and dropping them. You can save time by making sure the action you use most often is automatically selected. Once you start typing in the second pane though, the order of actions is determined by the matching algorithm.

## Synonyms

Continuing with the example above, where you naturally think of "processes" when looking for Activity Monitor, you can use **_synonyms_** to create an identical copy of something with a different name. In this case, you could create a synonym called "Processes" that refers to Activity Monitor. From then on, you can find it by searching for "proc".

Details on setting up synonyms can be found in the Preferences section.

## TextStart Ranker

A slightly different matching algorithm can be installed using the TextStart Ranker plugin and selecting it as the String Ranker handler in Preferences. In general it works better matching acronyms over continuous letters in the name of something. Specifically, it makes two changes to the algorithm.

The first is that it favors letters at the beginning of words more. E.g., if the input is <kbd>A</kbd><kbd>M</kbd> it will match "Activity Monitor" over "Amazon" since two beginning of word letters are matched instead of just one. The second difference is that it favors input that matches a higher percentage of the words. So the input <kbd>A</kbd><kbd>M</kbd> will favor "Activity Monitor" over "Audio MIDI Setup" since all the words are matched (2 out of 2) instead of two thirds of them (2 out of 3).

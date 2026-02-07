# Concepts and Terminology

Quicksilver is a modular application. This manual is organized around the things that Quicksilver can manipulate such as files, text, music, etc. Various Quicksilver concepts and facilities are introduced here so that the explanations in each following section can make use of them. A term introduced and defined is written like **_this_**.

These are the modifier key abbreviations used:

  * <kbd>⌘</kbd> Command
  * <kbd>⌥</kbd> Option
  * <kbd>⌃</kbd> Control
  * <kbd>⇧</kbd> Shift

Combinations are achieved by holding down one or more modifier keys and typing another key, such as a letter, number, or punctuation character. E.g., <kbd>⌘</kbd><kbd>;</kbd>, <kbd>⌥</kbd><kbd>⌘</kbd><kbd>S</kbd>, etc. The arrow keys are shown as <kbd>→</kbd>, <kbd>←</kbd>, <kbd>↑</kbd>, and <kbd>↓</kbd>.

The Quicksilver application runs in the background. By default there is a Dock icon, but no menu, menu bar icon, or other indication of Quicksilver on screen until it is **_activated_** with the shortcut <kbd>⌃</kbd><kbd>Space</kbd>. Though there are preferences to control the presence of Quicksilver in the Dock and menu bar. Preferences are available by typing <kbd>⌘</kbd><kbd>,</kbd> when Quicksilver has focus. (This is the Mac standard shortcut for opening Preferences).

## The Interface

![Command Window Terms](../images/command_window_terms.png)

Quicksilver commands are entered via two or three panes containing respectively an **_object_**, an **_action_**, and if a third pane is needed, an **_argument_**. These are the terms used in this manual, but unfortunately other terms are used in some places in Quicksilver and in discussions online. The Primer Interface labels the panes Subject, Action, and Object. Some forum posts use Subject, Verb, and Object; and others use Direct Object, Verb, and Indirect Object. Much of the built-in plugin documentation refers to objects in the first and third panes as "items". This manual uses the terms in the diagram above.

When typing in one of the panes, Quicksilver determines what items **_match_**, puts the top choice in the pane, and additional lower ranked matching items are shown in the **_results list_**. This happens for each pane, so the results list will contain objects, actions, or arguments depending on which pane is selected. The results list above is showing the possible arguments that match the entered text <kbd>Q</kbd><kbd>U</kbd><kbd>I</kbd>. The term **_item_** is used for something appearing in the results list, regardless of whether they are objects, actions or arguments.

## Plugins

**_Plugins_** are optional modules that are installed which can add objects, actions, or other capabilities to Quicksilver. Plugins are managed entirely from within Quicksilver's Preferences including finding, installing, updating, enabling, configuring and removing them.

Plugins can be viewed and downloaded from [qsapp.com](https://qsapp.com/plugins.php), but the in-app system is recommended. The website will always show the latest version of the plugin, while the in-app preferences will take into account your version of Quicksilver and macOS and only show you plugins that will actually work.

## The Catalog

The **_Catalog_** is the collection of objects that can be selected in Quicksilver's first pane. Quicksilver populates the catalog by scanning **_catalog entries_** that are configured in the Catalog Preferences.

For example, there is a source for Safari which indexes bookmarks and history into the catalog. Each bookmark is an object in Quicksilver. So are files and folders in the home directory, contacts in Contacts, all the apps in the Applications directory, the playlists in iTunes, and many other things (provided the appropriate plugins are installed). Note that some plugins (such as Remember the Milk) allow Quicksilver to index things stored on web servers and not merely things on the hard drive.

Scanning to keep the Catalog up-to-date is done in the background at regular intervals (every 10 minutes by default).

!!! note "Relax"
    Many new users worry about a performance hit from frequent scanning. *Don't.* The first part of the scanning process for any catalog entry is to ask "Has anything changed?" and the answer is almost always "No". In general, only things that have been touched since that last scan will get scanned again.

## Actions

A Preference pane shows all of the available **_actions_**. All actions work on objects, and actions are available based on the **_type_** of object selected. E.g., the **Open URL** action is only available for objects that are URLs. Actions that require an argument typically end in "…" and arguments are expected to be of a certain type. E.g., the **E-mail To…** actions expect the argument to be an e-mail address or contact. Actions with optional arguments usually end in "[…]".

Some actions have a complementary action that reverse the object and argument ordering. Consider these two commands:

> file, **E-mail To… (Compose)**, address

> address, **E-mail Item… (Compose)**, file

Notice the names of the actions are slightly different (**To** vs **Item**). Many (but not all) action names hint at the type of argument they take. **E-mail To…** wants an address to follow. **E-mail Item…** wants some kind of item to send (like text, or a file). These e-mail actions are similarly named and many people don't notice they are two different actions. In other cases actions are so differently named people might not notice they are related. For example, to perform a web search on a site like Google the two possible commands are:

> site, **Search For…**, query

> query, **Find With…**, site

There are also unfortunately some actions like **Make New…** which have no complement and don't hint at what their argument type is. Explaining these actions is one of the reasons this manual exists.

## Interfaces

**_Interfaces_** are configurable themes that change the appearance of the command window. They are installed as plugins and can be configured from the Appearance Preference pane. There are two built-in interfaces: Primer and Bezel. Primer (the default) is meant for new users as it labels a few things explicitly. Bezel is what has been shown so far and is used predominantly in this manual.

## Matching

Objects, actions, and arguments are selected by typing. As each letter is typed the choices are filtered down from all possible choices to only those that match the input, and those objects are shown in the results list. You won't see a typical "Search" input box that displays what you type. (If you're doing it right, what you type will probably be unreadable garbage anyway.) Instead, you will see the characters you typed underlined in the top match.

The matching method is one of the strengths of Quicksilver. Matches can be by the beginning of the name (e.g., <kbd>D</kbd><kbd>E</kbd><kbd>S</kbd><kbd>K</kbd> for "Desktop"), or by initials (e.g., <kbd>B</kbd><kbd>A</kbd> for "Browse Artists" which is an iTunes object), or some combination of those. As long as the letters you type appear _somewhere_ in an object's name in the order you type them, **not necessarily next to each other**, the object will match.

The more items (objects and actions) are used, the higher they appear in the list of results. After typing <kbd>D</kbd><kbd>E</kbd><kbd>S</kbd> a few times, Quicksilver will start guessing "Desktop", and if done often enough, it will start matching after just <kbd>D</kbd>.

!!! note "Always think in terms of abbreviations!"
    Much of the value of using Quicksilver is that, unlike other systems, you don't need to type <kbd>Q</kbd><kbd>U</kbd><kbd>I</kbd><kbd>C</kbd><kbd>K</kbd><kbd>T</kbd><kbd>I</kbd><kbd>M</kbd><kbd>E</kbd><kbd>Space</kbd><kbd>P</kbd><kbd>L</kbd><kbd>A</kbd>, etc. to find QuickTime Player. Just type <kbd>Q</kbd><kbd>T</kbd><kbd>P</kbd><kbd>L</kbd> or even just <kbd>Q</kbd><kbd>T</kbd>. Quicksilver will quickly learn which abbreviations refer to which things in your head.

## Children

Some items have **_Children_**, e.g., folders have files, contacts have phone numbers and addresses, musical artists have albums, etc. When an item has children there is a &gt; to the right of the item in the results list. View the children (e.g., go into a folder) by typing <kbd>→</kbd> or <kbd>/</kbd>. The selected object then changes to the top child, and the results list shows the other children. Navigate these by using the <kbd>↑</kbd> and <kbd>↓</kbd> arrows, or better yet, by typing to match against this list. This is an easy way to navigate folder hierarchies, or any other hierarchies.

## Triggers

Quicksilver's matching algorithm makes finding something specific very efficient, and its ability to perform many different actions on objects makes it powerful. The main interface is efficient, but there are even faster ways to perform commands.

**_Triggers_** can be invoked at anytime, without having to first activate Quicksilver with <kbd>⌃</kbd><kbd>Space</kbd>. There are a few built-in triggers, and plugins sometimes add more, but you can add your own for common tasks.

Triggers can be configured to start or complete a frequently used command. Quicksilver comes with the ability to assign triggers to shortcut keys, but plugins are available to run triggers based on mouse events, gestures (drawing shapes on screen), and system events (like "Switched to Battery Power").

## Proxy Objects

**_Proxy objects_** work especially well with triggers. These are special objects which represent something on the system such as the currently selected text (which may be sent to a search engine) or the last downloaded file (which may be opened or moved) or the URL of the current page in Safari (which may be pasted into an e-mail message).

## Collections

**_Collections_** are groups of objects built up either by using [the comma trick](#the-comma-trick), selecting all results with <kbd>⌘</kbd><kbd>A</kbd>, or grabbing multiple selected items from another application. You can use a collection to act on multiple objects at once. (e.g., copy multiple files, send an e-mail to multiple contacts, add multiple tags to a file, etc.)

#Spotlight

Spotlight actions and integration.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 2.1.2
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


## Spotlight Plugin

This adds Spotlight integration to Quicksilver. It allows you to add files to
your catalog based on Spotlight queries, tag files, and perform searches
directly from Quicksilver.

### Tagging

Users on OS X 10.9 or later are strongly encouraged to use the tagging
features from the File Attribute Plugin. It offers all of the same features
without the compromises by taking advantage of OS X's native tagging system.
Tagging related actions and catalog presets are disabled by default, but can
be activated in the preferences.

To distinguish between the two systems, the type of tags offered by this plug-
in are now referred to as "comment tags".

Comment tags are all prefixed with one or more characters to make them stand
out from regular text. By default, tags will be prefixed with `#`, but you can
change this (to `@` or `tag:`) in the preferences. You should choose a prefix
prior to tagging any files and stick with it. If you change it later, you'll
have to go update all existing tags manually.

Tags and comments are both stored in a file's "Spotlight Comments" field, but
they don't interfere with each other. In other words, manipulating tags will
not erase an existing comment, and setting a comment will not alter any tags.

### Catalog

#### Presets

There are two catalog presets added by this plug-in.

  * **Smart Folders** \- Automtically adds any Smart Folders you've created and saved. Presently, all you can do is open them in Finder.
  * **Comment Tags** \- If you've added any tags (using Quicksilver's tag prefix) to your files' Spotlight Comments, this will add them directly to the catalog. Using → or / on a tag will show all files matching that tag.

#### Custom Entries

You can create custom catalog entries to add files based on a Spotlight
search. (See the Syntax section.) From the catalog preferences, click the "+"
and choose "Spotlight". You'll be able to define the query, limit the search
to a specific folder, and ignore removable disks via the entry's info panel.

### Actions

#### Get Spotlight Results

Searches for text and shows the results in Quicksilver.

#### Show Spotlight Results in Finder

Uses search text to create and display a Smart Folder.

#### Spotlight in Window

Opens a Finder window with the search text pre-populated. The main advantage
to this action is that it allows you to use the search syntax most users are
familiar with.

#### Spotlight Contents…

Perform a Spotlight search inside the selected folder and display the results
in Quicksilver. Enter search text in the third pane.

#### Spotlight Contents in Finder…

Perform a Spotlight search inside the selected folder and display the results
in Finder. Enter search text in the third pane.

#### Spotlight Filenames Matching…

Search only filenames inside the selected folder and display the results in
Quicksilver. Enter search text in the third pane.

#### Show Files Matching Comment Tag

Create and display a Smart Folder containing files matching the selected
comment tag.

#### Show Comment Tags

Show any comment tags for the selected file or folder.

#### Add Comment Tags…

Add comment tags to the selected file or folder. Enter the new tags separated
by a single space in the third pane. Existing tags and comments will be
preserved.

#### Remove Comment Tags…

Remove comment tags from the selected file or folder. Enter the tags to remove
separated by a single space in the third pane.

#### Set Comment Tags…

Replace any comment tags with the ones specified. Enter the tags separated by
a single space in the third pane. Existing comments will be preserved.

#### Set Comment…

Set the file's Spotlight comment to the text entered in the third pane. Tags
in the comments (if any) will be preserved.

### Syntax

To search for basic terms like "vacation", you can just search for the word.
For more complicated searches (by type, etc.) this plugin is unfortunately not
able to support the familiar Spotlight syntax like `kind:movie`, so you might
have to get your hands dirty to set up a search. The syntax for most searches
is poorly documented by Apple in
[two](https://developer.apple.com/library/mac/#documentation/Carbon/Conceptual/SpotlightQuery/Concepts/QueryFormat.html#//apple_ref/doc/uid/TP40001849-CJBEJBHH)
[places](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/Predicates/Articles/pSyntax.html#//apple_ref/doc/uid/TP40001795-SW1).
It's really only worth the trouble if you're adding a custom catalog entry
based on Spotlight, but it also works with most of the actions.

Some examples might be helpful.

To search for movies related to "vacation", you might do something like this:

    
    
    kMDItemKind LIKE '*movie' && (kMDItemDisplayName LIKE[cd] '*vaction*' || kMDItemTextContent LIKE[cd] '*vaction*')
    

To replace the default "Applications" preset in your catalog with one that
finds _all_ applications, you could add a new entry with this query:

    
    
    kMDItemKind == 'Application'
    

A good way to see what attributes are available and what the values look like
is to examine a file in Terminal using `mdls`.

    
    
    mdls ~/Movies/Beach.mov
    

To make things worse, Smart Folders use a different syntax so if you're trying
to do a complicated search with the "Show Spotlight Results in Finder" action,
you'll need to use that, which is also
[documented](https://developer.apple.com/library/mac/#documentation/Carbon/Conceptual/SpotlightQuery/Concepts/QueryFormat.html#//apple_ref/doc/uid/TP40001849).
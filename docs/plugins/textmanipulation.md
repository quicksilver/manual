#Text Manipulation

Actions for manipulating text lines in files.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 1.2.0
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


## Overview

This plugin gives Quicksilver the ability to edit text files by appending text
lines to the end of a file, prepending text or changing or deleting lines
within a file. The plugin allows manipulation of `.txt`, `.rtf`, `.rtfd`,
`.doc` and `.TEXT` files.

Note that Quicksilver has the ability to enter into text files (using → or /)
and list the contents of the file, which can be used in conjunction with this
plugin for increased flexibility.

### Actions

Append Text… and Append To…

    

Append some text to the selected text file. You can append text to a text
file, or to a line within a text file (if you have entered a text file with →
or /). This action is reversible. You can:

  * [Some File] ⇥ Append Text… ⇥ [Some Text]
  * [Some Text] ⇥ Append To… ⇥ [Some File]

You should note that these actions can use Quicksilver's “smart” ability to
place any item, object or file inside a text file. If you append an image to a
text file, the path of the image is added, or similarly for web addresses
(URLs). When entering a text file (→ or /), these lines are automatically
resolved by Quicksilver into the original file, URL etc.

This gives you a convenient way to store and retrieve any file or piece of
information within a text file, using nothing but Quicksilver.

Prepend Text… and Prepend To…

    

This action works in a similar manner to the 'Append' actions, but puts a line
of text at the start of the file. The action is also reversible.

Change To…

    

The Change to… action is available for lines within a text file. To view
lines, press → or / to enter into a text file. It allows for the modification
of a specific line within a file.

Delete Line

    

As with the Change To… action, the Delete Line action is available for lines
within a text file. It can be used to remove certain lines from within a given
file.

#### Timestamps

All of the Append/Prepend actions have alternates that will include a
timestamp at the beginning of the line. The timestamp's format is taken from
the “Short” format for Date and Time in System Preferences, so you can
customize it there.
# Using the Mouse

## Drag and Drop

While it does involve switching between keyboard and mouse, the Quicksilver command window can be a convenient Drag and Drop source or target. With an Open File dialog up from some application, rather than navigating in that window you can activate Quicksilver, type to select the file you want to open and then drag it from the first pane into the Open File dialog. To move a file from the Desktop to a folder, activate Quicksilver and bring up the folder in the first pane, then just drag the file from the Desktop to the folder in the first pane.

You can bring up an e-mail address and drag it into the To: or CC: field of a mail message. Mail doesn’t recognize nicknames in it’s matching so using Quicksilver for this might be convenient. Note you have to drag an e-mail address for this to work, not a contact. You can also drag a file into a message as an attachment.

If the application you’re dropping into doesn’t accept the item your dragging from Quicksilver you’ll probably get the name of the item dropped in. For example, if you drag a file into a web form, you’ll find the file name with its full path entered into the form. Do the same thing with a contact to make sure you get a difficult name spelled correctly. Drag a postal address from a contact into a document or a field in an online mapping service. With proxy objects, you can drag the Current Web Page, the Currently Playing Track, or the Latest Download.

## Grab 'n Drop

The <kbd>⌥</kbd><kbd>⌘</kbd><kbd>G</kbd> shortcut lets you combine a Finder selection with whatever is already in Quicksilver's first pane, automatically choosing an appropriate action.

  * **Open With...** -- Select a file (or files) in Finder, activate Quicksilver, and choose the application you want to use in the first pane. Instead of tabbing to the action pane, type <kbd>⌥</kbd><kbd>⌘</kbd><kbd>G</kbd>. The command window rearranges so the file is in the first pane, the action is **Open With...**, and the application is in the third pane.
  * **Move to...** -- Select the file or files to move in Finder, activate Quicksilver, and bring up the destination folder in the first pane. Type <kbd>⌥</kbd><kbd>⌘</kbd><kbd>G</kbd>. The command window rearranges so the files are in the first pane, the action is **Move to...**, and the destination folder is the argument. Press <kbd>↩</kbd> to execute.

In general, if an application is in the first pane when you type <kbd>⌥</kbd><kbd>⌘</kbd><kbd>G</kbd>, the Finder selection becomes the object and the application becomes the **Open With...** target. If a directory is in the first pane, the Finder selection becomes the object and the directory becomes the **Move to...** target.

## Command Objects and Droplets

Entire commands in Quicksilver can be represented as a single object. To create a command object, activate Quicksilver and enter a command as you normally do, but instead of typing return to execute it, type <kbd>⌃</kbd><kbd>↩</kbd> to “encapsulate” the command. You’ll see a new command window appear in which the object is a new command object and the action (with default settings) is **Run**.

Actions that work on commands include **Run**, **Run after Delay…**, **Run at Time…**, **Add Trigger…**, and **Save Command to File…**. The first, **Run**, is obvious and not particularly useful since just executing the command without creating a command object is easier. The other two are useful as alarms when used with actions like **Large Text** or **Display Dialog**. A delay period is entered as a decimal number followed by an h, m or s to indicate hours, minutes or seconds. E.g., 2h, 10m, 90s, or 1.5h. A number without a suffix is interpreted as minutes. You can combine these separated by spaces such as 2m 30s. You can also enter a time format such as minutes:seconds or hours:minutes:seconds. For example 9:35 or 2:11:30. I believe you can also enter decimal numbers with colons like 1.5:10:00 for 100 minutes but that is probably not useful.

Times for **Run at Time…** are typically entered as a digital clock, hh:mm:ss although it uses macOS’s natural language date parser, so things like “3pm December 15, 2018” or “next Tuesday at dinner” are supposed to work.

There’s also an **Add Trigger…** action which will ask for the type of trigger in the third pane, then open the trigger preferences with most of your new trigger already configured.

The **Save Command to File…** action takes a command object and saves it in a file. You enter a folder name as the argument and Quicksilver saves a file there with the extension `.qscommand`. If you open the resulting file (e.g., by double-clicking it), it will run the command. Quicksilver makes running commands simple and triggers make running command even easier. But for commands that you might run a few times but not enough to bother creating a trigger for, the **Save Command to File…** action can be useful. E.g., if your working on creating a document and you want to send several drafts to a group of people (using the comma trick) it’s easy to save this (complicated) command in a file to rerun.

With a saved command on your Desktop you might want to be able to drag a file onto the command and have it run on that file. This type of saved command is known as a Droplet. To create a droplet, use the Droplet Item proxy object in the command and save it using the **Save Command to File…** action. The command file will have a special icon and a `.app` extension. Whatever you drop on the droplet application will take the place of the Droplet Item proxy when the command is executed.


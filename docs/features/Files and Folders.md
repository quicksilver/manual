# Files and Folders

The most commonly used items on your computer are files and folders. Any file or folder can be selected as an object in Quicksilver. If you were working on a file called `Résumé.pages` in your Documents folder, since `~/Documents` is in the catalog, you can select the file in the first pane by just typing its name. As you type <kbd>R</kbd><kbd>E</kbd><kbd>S</kbd>, it appears with the default action of **Open**. If you type <kbd>↩</kbd>, Pages will open the file. You can select the Documents folder itself by typing “documents” (or as much of it as you need to match it) and since it’s really a folder, the default action is **Open**.

Quicksilver isn’t limited to only what’s in the catalog. If a folder is in the object pane, use <kbd>→</kbd> to show its contents. Since it’s common to separate folders with `/`, typing <kbd>/</kbd> is equivalent to <kbd>→</kbd> when navigating. Pressing <kbd>⌥</kbd><kbd>→</kbd> or <kbd>⌥</kbd><kbd>/</kbd> when navigating will include hidden files in the results list. This also enables browsing into packages (like the Finder’s Show Package Contents command).

Quicksilver also understands the tilde (<kbd>~</kbd>) as the Unix shortcut for the home directory. Since the Desktop is just a folder in the home directory, I could navigate to this manual’s file (at `~/Desktop/Quicksilver.md`) by typing <kbd>~</kbd><kbd>/</kbd><kbd>D</kbd><kbd>E</kbd><kbd>/</kbd><kbd>Q</kbd><kbd>S</kbd>. Quicksilver also interprets a backquote (<kbd>`</kbd>) as a tilde. (On US keyboards the tilde is a shifted backquote.) Back up a folder hierarchy by typing <kbd>←</kbd> or <kbd>?</kbd> (a shifted slash on a US keyboard). This can backup all the way to the root directory. Type <kbd>/</kbd> and hold it down for a second to select the root directory immediately. Disks are also included in the catalog so type their name to select them.

Several common folders are included in the the catalog by default. Under the User set are catalog entries for the Home, Documents, and Desktop folders. Under Dock are entries for Dock Files & Folders and under Recent Items is an entry for Recent Documents, Favorites, and Recent Folders (Open & Save).

Since there are a lot of files on your machine, to avoid using a lot of memory and CPU, Quicksilver doesn’t scan them all into the catalog. Instead, folders are only scanned to a configured depth. The default Home entry is only indexed one level down and the default Documents entry only 2 levels. These entries are not configurable themselves, but an editable copy can be made. See the Catalog section for instructions on doing this.

Do not just create copies of the sources that scan to infinite depth. This will cause Quicksilver to use a lot of memory, slow down all of your searches, and waste a large percentage of the CPU to scan the entire drive every few minutes. Instead, only scan the folders that are really used. Don’t scan the Home folder more than one level down. `~/Library/` will probably just clog the Catalog with many unused items, and `~/Music/` and `~/Pictures/` are better scanned with the iTunes and iPhoto plugins.

## Basic File Actions

The default file action **Open**, opens a file in its default application; the same as double-clicking on the file’s icon. The default action for a folder is also **Open**, and just like double-clicking on its icon, it opens the folder in a Finder window. There are also other actions available. Use **Open With…** to open the file with a different application specified in the third pane. The third pane will have a results list of applications to choose from. If the desired application is not there, navigate to it starting with <kbd>/</kbd> or <kbd>~</kbd> or by selecting the application in the Finder and using <kbd>⌘</kbd><kbd>G</kbd>. If the third pane is in text-mode, exit text mode by typing <kbd>⎋</kbd> and navigate to the desired application.

Another way to use **Open With…** is to select the file (or files) in the Finder, then activate Quicksilver and select the application to use in the first pane. Then, instead of tabbing to the action pane, just type <kbd>⌥</kbd><kbd>⌘</kbd><kbd>G</kbd>. The command window will change so that the Finder selection is in the first pane, the action is **Open With…**, and the application is in the third pane. It’s a little convoluted but it’s quick.

The default action for a file object is **Open**. For scripts however this could be unclear. Should they be opened in an editor or executed? Quicksilver solves this by having the **Open** action open them in an editor and having several **Run** actions. More about them in the section on the Terminal, but as an example, the Extra Scripts plugin includes an Empty Trash script (in the Catalog under Plugins → Scripts) to be used with the **Run** action.

It might be more common to use with an application, but the **Open at Login** action can also set a file to open automatically at login time. The item is added to the list in the Account System Preferences under the Login Items tab. All items listed in that pane are started at login, the checkbox only indicates if they are hidden when started. The **Do Not Open at Login** action removes something from the list. (Both of these actions are disabled by default.)

The **Reveal** action opens the containing folder and selects the item. This is a very easy way to find what folder an item is in, particularly when finding the item directly via the catalog instead of navigating down to it. I do this often to find applications (which are in my catalog) and might be in `/Applications` or `~/Applications` or a couple of levels down. In fact, it's so useful Quicksilver uses this as the [alternate](../preferences/general.md#actions) for **Open**. (With a file in the first pane and the action set to **Open**, typing <kbd>⌘</kbd><kbd>↩</kbd> performs the **Reveal** action.)

Quicksilver includes several methods that take a file and return a form of the file’s path.

  Action | Behavior
  ------ | ----------------------------------------------------------------
  Get Path          | Returns a unix-style path using `~` to represent your home directory (if applicable)
  Get Absolute Path | Returns a unix-style absolute path
  Get File URL      | Returns a `file://` URL to the file
  Get File Location | Returns an HFS+ path (with colons)

All of the actions show the path in Quicksilver’s command window. From there, you can copy and paste a file’s path somewhere. The Terminal section describes using the **Go To Directory in Terminal** and **Go To Directory in iTerm** actions to open a terminal shell in the folder specified in the first pane as the current working directory.

The actions **Rename…**, **Copy to…**, and **Move to…** are very commonly used. For all of them, the third pane opens so you can select the new name or location.

The <kbd>⌥</kbd><kbd>⌘</kbd><kbd>G</kbd> trick also works with the **Move to…** action. In the Finder, select the file(s) to move, activate Quicksilver, and bring up the destination folder in the first pane. Then instead of tabbing to the action pane, just type <kbd>⌥</kbd><kbd>⌘</kbd><kbd>G</kbd>. The command window will change so that the files are in the first pane, the action is **Move to…** and the destination folder is the argument. Type <kbd>↩</kbd> to execute the command. Mouse users might prefer to just drag the file from the Finder to the folder when it’s in the first pane.

!!! warning
    The **Move to…** action can be confusing. The name assumes the destination folder is on the same volume. If the destination is on another volume, the file is _copied_ instead. In other words, it behaves exactly like dragging a file in Finder without holding any modifier keys.

Since moving something to the trash is so common, there’s an action called **Move to Trash**. There’s also a **Delete (Erase)** action which skips the Trash and actually removes the file. Since that action can’t be undone, it’s disabled by default.

The **Make Alias in…** action creates a macOS alias for a file in the folder specified in the third pane. The **Make Link in…** and **Make Hard Link in…** actions do the same for unix-style links for those that know the difference. (Since many don’t, they are disabled by default.)

The **Make New…** action requires a little configuration. Create the folder `~/Library/Application Support/Quicksilver/Templates/`. Now put some template files in there. E.g., an empty `untitled.txt` file or a `Letter.doc` with a return address filled in or a `Letter.pages` with the return address created by Pages cleaned up (e.g., removing URLs and phone numbers). Now activate Quicksilver, select a folder as the object, the **Make New…** action, and in the third pane choose a template. Executing the command copies the template to the object folder and a new Quicksilver command window appears with the new file in the first pane and a default action (probably **Open**) which can be changed. It’s a bit like the Finder’s Stationery Pad functionality integrated into Quicksilver. Place folder hierarchies in the Templates folder and the **Make New…** action will create them; this is useful for creating new projects.

The **Get Info** action shows the Finder’s info panel for the object, just like selecting a file in the Finder and choosing the Get Info from the File menu or typing <kbd>⌘</kbd><kbd>I</kbd>. The File Attributes Actions plugin adds several actions that will modify information in the info panel. **Set Icon…** changes the file’s icon to one specified in the third pane. Spotlight users can add metadata to files with the **Set Comment…** action. This opens a third pane to enter text which will become the Spotlight comment (visible in the Get Info panel of the Finder). It doesn’t add to the comment but replaces whatever the current comment is with the new text. 

The **Set Label…** action opens a third pane to choose a color label. The **Lock File** and **Unlock File** actions do the obvious. The **Make Invisible (hide)** and **Make Visible (Show)** actions change the visibility attribute of files. To find invisible files use the Finder’s Find command (<kbd>⌘</kbd><kbd>F</kbd>) and from the search attributes pop-up menu choose Other and then Visibility, then pick the desired value (Visible, Invisible, or either). The **Always Open Type With…** action will tell macOS to always open files of that type with the specified application, same as the “Change All…” button in the info panel.

There are many file and folder actions, but realize they work with Quicksilver's other capabilities. By using [the comma trick](../getting-started/invoking-quicksilver.md#the-comma-trick) an action can be used on multiple files at once. E.g., move several files to the Trash or a folder, upload them to a server, add a label or tag to several files, send multiple attachments to multiple recipients in a single e-mail message, etc. 

See the [Text Files](Text.md#text-files) section for actions that modify the contents of a text files.

## Previewing A File With QuickLook

To preview a file using QuickLook, type <kbd>⌘</kbd><kbd>Y</kbd>. To preview full-screen, use <kbd>⌥</kbd><kbd>⌘</kbd><kbd>Y</kbd> (these are the same shortcuts as in the Finder). QuickLook is also the default behavior of <kbd>Space</kbd> for some file types if “Spacebar behavior” is set to “Smart” or “QuickLook” in the Command section of the General preferences pane.

## File Tagging

The File Attributes plugin allows Quicksilver to tag files and search for files based on one or more tags.

Three of the tag actions are used to modify tags on files: **Set Tags…**, **Add Tags…**, and **Remove Tags…**. All three actions take files or folders as objects and use the third pane to select existing tags or create new ones via text mode. **Set Tags…** replaces any existing tags and **Add Tags…** will append more tags leaving the current ones in place.

To see the tags assigned to just one file, bring up that file in the first pane and use the **Show Tags** action. This brings up a new command window with a results list of tags.

With a tag in the first pane, just type <kbd>→</kbd> to see a list of all files with that tag. All additional tags for the matching files will appear at the bottom of the list. Selecting one of those tags and hitting <kbd>→</kbd> again will reveal all files that match _both_ tags. You can repeat this for as many tags as you see to quickly narrow the list of files.

## File Compression

The File Compression Module plugin installs three additional file actions: **Decompress**, **Compress (Create Archive)**, and **Compress Using…**. The first works on an archive object (`zip`, `cpio`, or `cpgz`) and decompresses it (or you can use the **Open** action which will also decompress the archive). The **Compress (Create Archive)** action will zip the object, creating a new ZIP archive in the same folder (the original item remains), and a new command window appears with the new ZIP archive as the object allowing additional actions such as **Move to…**, **E-mail To…** or whatever. The **Compress Using…** action opens a third pane to select a compression format to use such as TGZ, CPIO, CPGZ, ZIP, or TBZ. Executing the **Compress Using…** action in the ZIP format when using the comma trick or dragging multiple files into the first pane will result in an error and a ding sound.

## Sending Files

The E-mail Support plugin adds the three varieties of the **E-mail To…** action. They  all send files specified in the first pane as an e-mail attachment to a contact or address specified in the third pane. For details on the differences between the **Compose**, **Send** and **Send Directly** varieties see the the [Mail](Mail.md) section below. 

Send a file to a printer with the **Open With…** action and then choose a printer as the argument in the third pane. The third pane is pre-populated with applications and printers.

## Path Finder

Path Finder is a popular Finder alternative from Cocoatech. The Path Finder plugin allows Quicksilver to use it when appropriate. After installing the plugin, go to the Handler’s preference pane and under File System Browser choose Path Finder. This causes the **Open**, **Reveal**, and **Get Info** actions to use Path Finder. <kbd>⌘</kbd><kbd>G</kbd> will bring the Path Finder selection into the first or third pane. The plugin also installs under Plugins → Path Finder two catalog objects called Path Finder Recent Files and Path Finder Recent Folders. There is also a Path Finder Selection proxy object that can be used instead of the Finder Selection proxy object.

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


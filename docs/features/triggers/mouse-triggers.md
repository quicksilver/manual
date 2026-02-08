# Mouse Triggers

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


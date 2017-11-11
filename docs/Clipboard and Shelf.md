# Clipboard and Shelf

## Clipboard History

For this section you’ll need the Clipboard Module plugin installed. It doesn’t install any actions but does add several catalog objects in the Quicksilver set. Inside Shelf & Clipboard you’ll find two items, Shelf, and Clipboard History. Make sure the latter is enabled for this section. (You may need to install the Shelf Module plugin to see the Shelf & Clipboard catalog source and click refresh after checking it.) Under Internal Commands you’ll find several related objects, some of which behave like actions but are scripts (such as Clip Store Copy 2) that you use with the **Run** action. Also under Proxy Objects there’s a Clipboard Contents proxy object.

One limitation of copy and paste on the Mac is that the clipboard only remembers the last thing you copied. With Quicksilver’s Clipboard Module you can extend this to remember the last several items you’ve copied. In the Clipboard Preference pane you can configure the number of items to be saved in the clipboard. 

A large number like 100 is useful to  be able to remember things you copied several days ago but it uses more memory. If you put large images on the clipboard consider a number a like 10.

You can bring up a window showing the Clipboard History by activating Quicksilver and typing the built-in shortcut <kbd>⌘</kbd> <kbd>L</kbd>. You can also choose the Clipboard History object and the Show action. This action is actually a toggle and will close it if it’s visible. If you use it often you can create a trigger. Note that some have reported that having the TextExtras Input Manager installed breaks the <kbd>⌘</kbd><kbd>L</kbd> shortcut.

If a clipboard item is text, the first few words are included in the list to help you identify the correct item. If the item is an image, the icon (usually) shows a thumbnail of it. Personally I use Clipboard History with the **Show Contents** action as a trigger on <kbd>⌃</kbd><kbd>⌘</kbd><kbd>C</kbd> so that I get a new results list that I can use the matching algorithm to search through. However this doesn’t work too well for image items, you have to scroll to see them.

<kbd>⌘</kbd><kbd>L</kbd> is a toggle, so typing it again will make the window disappear. In the Clipboard preference pane you can enable the “Hide after pasting” option. If you position the window with one side on an edge of the screen then it will always disappear when idle (even if “Hide after pasting” is unchecked). You can then bring it back by moving the mouse to that same edge of the screen and it will appear again. This is similar to using the screen corners in the Dashboard & Expose System Preference. 

For the first 10 items in the history you can paste them into the current application by typing the number of the item while the Clipboard History window is open. For other items you’ll need to double-click on them to paste them. 

Items remain in the Clipboard History until it fills up, in which case the oldest items are removed when new items are added (i.e., FIFO). The Clipboard History survives Quicksilver restarts and system reboots. The clear button at the bottom of the Clipboard History window will remove all but the most recent item from the history. You can remove a single item from the history by selecting it with single click and then typing the delete key. You can’t delete the first (number 0) item. Instead copy something else onto the history to move it down and then delete it.

The Clipboard Contents proxy object represents the 0’th or most recent item in the history. Using it with the **Paste** action is the same as using Paste in whatever application you are using.  It will include the formating of the text, use the **Type Text** action to paste without the original formating, matching the style of the destination. However you can use it with other actions such as **Open URL…**, **Look Up in Dictionary…**, **Email To…**, etc. I find it easier to use <kbd>⌘</kbd><kbd>⎋</kbd> to bring the selection into the object pane but if your item is already on the clipboard this could be useful.

There have been some reports of pasting from the clipboard not working or crashing Quicksilver B51 when a non-US keyboard is in use. To solve this, you don’t have to switch to a US keyboard, but  you do have to enable the “U.S.” keyboard in the Input Menu tab of the International System Preferences. That is, the U.S. keyboard doesn’t need to be in use, just enabled.

TODO: Show Clipboard Cache (pNew) and Show Clipboard Cache (pOld)

## Clipboard Storage

Since cut and copy are such common operations on your Mac, items in the Clipboard History change frequently. If you want to save something for longer you can use an alternate clipboard called Clipboard Storage. The contents only last as long as Quicksilver is running. If you restart Quicksilver (or obviously if you logout or reboot) the Clipboard Storage will be lost. The Clipboard Storage is also installed with the Clipboard Module plugin and is accessed via the same window. You can toggle the window between showing the Clipboard Storage and the Clipboard History by using the drop down in the top of the window. You can also show the Clipboard Storage by using the Show Clipboard Storage object with the **Run** action. That’s something you may want to create a trigger for.

Unfortunately showing the Clipboard Storage seems to toggle the state of the window but there’s no way to toggle it back to showing the Clipboard History without using the mouse to choose it from the drop down in the top right of the window. The command Show Clipboard, Run will just bring up the window in its last state. The command Clipboard History, **Show** behaves the same way. However the trigger I use, Clipboard History (**Show Contents**), continues to show the history in the results list regardless of what the window is showing.

You use the Clipboard Storage the same way you use the Clipboard History. Double-clicking or typing a digit will paste that item into the current application. The Storage always has 10 numbered slots regardless of the number of history items you have configured. The only way to put an item into the Clipboard Storage is to drag it into a slot. You can use any slot regardless if higher slots are filled or not. Dragging an item into an already filled slot will replace the item in that slot. You can remove an item by selecting it and typing the delete key. The clear button will remove all items from the Storage, it doesn’t leave the latest item as it does in History. There are objects of the form Clip Store Copy # and Clip Store Paste # which would seem very useful for frequent access to non-temporary items but they don’t seem to work in B51.

## Shelf

For this section you’ll need the Shelf Module plugin installed. The Shelf is in the catalog under Quicksilver under Shelf & Clipboard. Make sure it’s enabled (in B51 it’s not by default) by selecting Shelf & Clipboard, typing the ⓘ button to open the drawer, going to the Contents tab and checking the Shelf object. You might need to run the command Shelf & Clipboard (Catalog), **Rescan Catalog Entry**, after the first time you add something to shelf to have it scanned by Quicksilver. The plugin installs two actions **Put on Shelf** and **Show**. The **Put on Shelf** action is not enabled by default, so find it in the Actions Preferences and check it.

The shelf is a place for long term storage frequently used items. It’s like the Clipboard Storage described above but it lasts across Quicksilver sessions. People use it for: email addresses, images, code fragments and templates, favorite hex colors, lorem ipsum text, passwords (though this isn’t secure), etc.. You can also put documents, folders and, applications on it and treat it like an alternate Dock.

When Quicksilver is activated, you can use the built-in shortcut <kbd>⌥</kbd><kbd>⌘</kbd><kbd>S</kbd> to toggle the shelf. The Shelf object with the **Show** action will also toggle the shelf. If you use it frequently consider creating a trigger for this, it will work faster than <kbd>⌥</kbd><kbd>⌘</kbd><kbd>S</kbd> since you won’t first have to activate Quicksilver. Just like with the Clipboard, if you position the shelf window with one side on an edge of the screen then it will disappear when idle. You can then bring it back by moving the mouse to that same edge of the screen and it will appear again. This is similar to using the screen corners in the Dashboard & Expose System Preference. 

The typical way to add something to the shelf is using the **Put on Shelf** action. It adds items to the top of the shelf as if it were a stack. You can also drag items to the shelf, into any contiguous location. The Current Selection proxy object with the **Put on Shelf** action makes a good trigger. You can also use <kbd>⌘</kbd><kbd>V</kbd> to paste things onto the shelf. If nothing in the shelf is selected the item will be pasted to the top, otherwise it’s added above the selected shelf object.

You can bring up the shelf in the object pane and then type <kbd>→</kbd> to bring its contents into a results list. You can also drag and drop from the shelf with the mouse. Unlike the Clipboard, there are no numbers to select items with. While the shelf otherwise behaves as a stack, there’s no easy way (such as a Pop From action or an analog for the Clipboard Contents proxy object) to get the first item into the object pane.

You can delete an item by selecting it with the mouse and then typing <kbd>⌫</kbd>. Like on a stack, the lower items move up. There’s no clear button to empty the shelf, but just select the top item and type <kbd>⌫</kbd> repeatedly for each item on the shelf.

I use the shelf as follows. I have it on the edge of the screen so if I am using a mouse I can conveniently drag things to or from it. I have a trigger for the Shelf with the **Show Contents** action so I can quickly call up items using just the keyboard.

TODO: Right click shelf items to show a menu.

## Comparing Clipboard History, Storage and Shelf

|  | History | Storage | Shelf |
| ---: | --- | --- | --- |
| **Window** | Shared with Storage | Shared with History | Separate |
| **Max Items** | Configurable in Preferences | Unlimited? | Unlimited |
| **Items Added** | On top with every Cut or Copy | Anywhere | On top or above selected item with <kbd>⌘</kbd><kbd>V</kbd> |
| **Items Accessed** | Number keys, Results list, mouse | Number keys, mouse | Results list, mouse |
| **Persistence** | Survives system restarts but oldest items removed when full | Empties when Quicksilver restarts | Permanent until removed, survives restarts |
| **Right Click Menu** | No | No | Yes |

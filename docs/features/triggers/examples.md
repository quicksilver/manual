# Example Triggers

### Open Safari

The most common simple trigger created is to open an application. Shown here is a trigger to open Safari, it’s just the Safari application in the first pane and the **Open** action in the second. The argument is blank. Notice that when the action is **Open** the default name for the trigger is Open followed by the application. Usually the default name is the object followed by the action in parenthesis. **Open** is special, probably because it’s so common. If in the Extras Preferences you have Reopening the current application set to “activates the application”, then using this trigger when Safari is already running will make it the active application.

You can obviously make similar triggers to open your favorite applications. Some people create other triggers like Safari (**Quit**) or Safari (**Hide Others**) and put them on the same keys but with different modifiers (e.g., <kbd>⌥</kbd> or <kbd>⇧</kbd>). Others just use the standard macOS shortcuts of <kbd>⌘</kbd>Q and <kbd>⌥</kbd><kbd>⌘</kbd><kbd>H</kbd> to run these on the current application.

### Show Shelf/Clipboard Contents

The Shelf and Clipboard History are enabled with the Shelf plugin and the Clipboard plugin respectively. Each enables a window that you typically access with the mouse (see [Clipboard and Shelf](../features/Clipboard and Shelf.md) for details). To get keyboard access to these, first enable the objects in the Catalog under Quicksilver and Shelf & Clipboard (check the box and click the rescan button). If you select these objects in the first pane, you can type <kbd>→</kbd> or <kbd>/</kbd> to open a new results list with their contents. The **Show Contents** action is the equivalent of this, and since it's an action, you can use it in a trigger.

So this trigger will open the shelf in a results list, with the first item selected, and let you type to select any item on the shelf (or the Clipboard History if you use that object). You can also use the **Search Contents** action which is very similar but won’t select the first time and won’t show a results list at first.

You can create triggers using **Show Contents** or **Search Contents** for anything you can right-arrow into, such as Contacts, iTunes, your Documents folder, etc.

### Search Wikipedia

Some actions take an argument in the third pane and triggers can use these too. The **Search For…** action will search some web site for the text entered as an argument. See the [Web Searches](../features/Web.md#web-searches) section for the details of using this action.

A trigger for a commonly used web search, such as Wikipedia, is very useful. If you specified the argument in the trigger it would search for the same text each time it’s run. However, if you leave the third pane blank, then when the trigger is run, Quicksilver will open a command window with the first two panes filled in (in this case with Wikipedia and **Search For…**), and the third pane selected, ready for you to type the query.

Quicksilver is also smart enough to realize that the **Search For…** action wants a text argument and puts the third pane in text mode for you. It even fills in the default text from the macOS Shared Find Clipboard (which you can set in many Cocoa applications with <kbd>⌘</kbd><kbd>E</kbd>). Note, if the third pane isn’t empty when you create the trigger and you want it to be, type <kbd>⌘</kbd><kbd>X</kbd> to clear the selection.

If you have this trigger configured on the shortcut <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd>, you type <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd>, the query, and hit <kbd>↩</kbd> then the browser opens with the search results. If you want to search for some text in a document, you can select the text, copy it with <kbd>⌘</kbd><kbd>C</kbd>, type <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd> and then paste the text with <kbd>⌘</kbd><kbd>V</kbd> and type return.

That’s pretty easy, but believe it or not, this is the hard way. In the next section, you’ll see how proxy objects reduce this to one step.

### Paste the Current URL

This example lets you paste the URL of the page Safari is displaying into any other application without switching applications multiple times, and without having to select or copy anything. You can use this trigger to paste a URL into mail messages, chats, documents, Calendar events, etc. The magic is because of the Current Web Page proxy object used in the first pane. It acts like a placeholder for the URL Safari will be displaying when you use this command. When the command is run, this proxy object asks Safari what it’s currently displaying and uses that in the command.

If you aren’t using Safari or use more than one browser, every browser plugin currently available also provides a “Current Web Page” proxy object.

### Search Wikipedia for Selected Text

The Current Selection proxy object gets the selection from the frontmost application.

If your current selection is text, it should be possible to use this proxy object as the argument in the Wikipedia search trigger above, so that you could select text in some Cocoa application, invoke the trigger, and have the search run. The **Search For…** action has a complementary action called **Find With…** that takes the query text as the object, and the search site as the argument. You can set up a trigger of the Current Selection proxy object with the  **Find With…** action and the Wikipedia argument.

It’s useful to assign triggers to shortcuts in some pattern so they are easier to remember. For example, you could use <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd> to search Wikipedia for text you enter, and add <kbd>⇧</kbd> to the sequence to search for selected text. Pairs of triggers for other quick searches might look like this: Google (<kbd>⌃</kbd><kbd>⌘</kbd><kbd>G</kbd>), IMdB (<kbd>⌃</kbd><kbd>⌘</kbd><kbd>F</kbd>), and Amazon (<kbd>⌃</kbd><kbd>⌘</kbd><kbd>Z</kbd>).

Sometimes when creating triggers with proxy objects, the action you want doesn’t appear in the list. As you’ve probably noticed, Quicksilver normally narrows down the action list to only those that are relevant. Sometimes proxy objects confuse it because they represent something else. If this happens you can work around it with copy and paste. It’s not obvious but if you bring up a regular command window (with <kbd>⌃</kbd><kbd>Space</kbd>), when you tab to the action pane you can type <kbd>⌘</kbd><kbd>C</kbd> to copy the action. You can then paste it into the second pane of the trigger definition window with <kbd>⌘</kbd><kbd>V</kbd>. You can also cut an item out with <kbd>⌘</kbd><kbd>X</kbd>. This is useful when creating commands that do a web search with the **Search For…** action and you want a blank third pane. There are many other proxy objects giving you access to interesting things to use in triggers such as Track Now Playing (in iTunes), Current Application, Previous Application, Finder Selection, etc. Experiment to see what you find useful.

### Quicksilver Selection

The Quicksilver Selection proxy object represents what is in the first pane. This allows you to assign triggers to particular actions (or actions and arguments). For example, create the trigger Quicksilver Selection (**Get Info**) and assign it to <kbd>⌃</kbd><kbd>⌘</kbd><kbd>I</kbd>. Now you can activate Quicksilver, select a file object in the catalog or navigate to one in the filesystem and type <kbd>⌃</kbd><kbd>⌘</kbd><kbd>I</kbd> to bring up the Finder’s Info pane of that file. You don’t even have to tab to the action pane.

You could also create a trigger to open files in an application you frequently use that might not be the default when you run **Open** by using the **Open With…** action. For example, you could bind <kbd>⌥</kbd><kbd>⌘</kbd><kbd>T</kbd> to Quicksilver Selection ⇥ Open With… ⇥ TextMate.

You might want to scope these triggers to only work in Quicksilver. They aren’t really useful in other contexts and you don’t want to tie up those shortcuts in other applications that might do something useful with them.


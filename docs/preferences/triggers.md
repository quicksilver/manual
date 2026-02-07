# Triggers

Triggers allow you to execute Quicksilver commands without having to use the command window. Quicksilver supports executing triggers based on

  * Keyboard shortcuts (built-in)
  * Mouse position and/or buttons (Mouse Triggers plugin)
  * System Events (Event Triggers plugin)
  * Gestures (Abracadabra Triggers plugin)

Triggers are available whenever Quicksilver is running and you do not have to invoke Quicksilver to use them. Triggers make it easier to control iTunes, launch applications, perform web searches, or do anything else Quicksilver can do. You can create as many as you want but you probably want them only for the operations you do frequently.

Your trigger configuration is stored in `~/Library/Application Support/Quicksilver/Triggers.plist`. This is useful to know if you want to have the same configuration on several machines, just copy the file between the machines while Quicksilver is not running. 

You define triggers in the Triggers Preference pane. You can go to this pane directly by activating Quicksilver and typing <kbd>⌘</kbd><kbd>'</kbd>. You’ll see several sets in the left side of the preference pane. Some triggers are predefined by Quicksilver itself or various plugins, e.g., you’ll find several in iTunes, and two in Quicksilver. Triggers you create will be in the Custom Triggers set. 

Each trigger is shown by its name which is usually a combination of the object and action to be invoked. The checkbox shows if the trigger is active. The <kbd>⌘</kbd> column shows the type of trigger, in this case they are all activated by a shortcut which is shown in the Trigger column (some are not assigned to keys). If you select a trigger and click on the ⓘ button at the bottom, a drawer is revealed with various settings for the trigger. The settings tab looks different for each type of trigger. You can change the name of the trigger in the top text field.

You can change some options by clicking in the main trigger window. If you click on the command name you can get an edit field to change the name of the trigger. If you click in the Trigger column you can set or change the shortcut. If you click on the icon in the <kbd>⌘</kbd> column you can add another means (Gesture, Mouse) to activate the trigger. Though once you create an additional way, there doesn’t seem to be a way to delete it without deleting the entire trigger.

You create a new trigger by clicking the + button at the bottom and selecting a trigger type from the pop-up menu (Gesture, Keyboard, or Mouse, depending on installed plugins). The Group option is just a way to collect triggers in a group or folder. They don’t perform any function other than helping you organize a lot of triggers. You can’t activate all the triggers in a group at once. Create a Group from the + menu and drag triggers into it. 

Regardless of which type you choose, a special command window appears (populated with the last command you performed) to let you define the command for the trigger. Enter the command and click Save. Then open the drawer to the Settings tab to assign a shortcut, mouse click, or gesture to use to activate the trigger. If you’re creating a keyboard trigger, just click in the Trigger column for this new trigger, the drawer will open and you can just type the shortcut as if you had clicked the Edit button.

By default, triggers are available whenever Quicksilver is running, regardless of what application is active. They can also be limited to function only when a certain application is active or when a certain application is not active. You do this by opening the drawer for a trigger and choosing the Scope tab. The default is “Enabled in all applications” but you can also choose from the popup “Enabled in selected applications” or “Disabled in selected applications”. For the latter two you can type the name of the application into the large box and type <kbd>⇥</kbd> or <kbd>,</kbd> after the name to have it turn into a blue button. You can then enter another application if you choose.

If you have triggers that use certain features, be cautious about deleting the plugins that supply those features. In particular if you have triggers using mouse gestures from Abracadabra (see below) and if you remove the Abracadabra plugin, the trigger panel may display oddly with some blank lines and missing icons. To correct this, reinstall the plugin (Abracadabra in this case), or remove the triggers.

The following sections discuss each type of trigger with some examples. The commands used will come from many different plugins not covered here. If you want more information on them, look in the relevant sections under Features. While you have a lot of freedom in defining triggers any way you want, some commands are better suited to certain trigger types.

## Keyboard Triggers

If you enter a complete command into the trigger, like choosing an application and the Open action, it will be run when you execute the trigger. If you choose just a partial command, like a web-search and the **Search For…** action, when you execute the trigger a command window will appear with as much filled in as your trigger defines. You can’t have gaps (e.g., you can’t leave the first pane blank and use the **Get Info** action). This is discussed more below. Triggers are given a default name based on the command they represent. Here are some examples:

### Open Safari

The most common simple trigger created is to open an application. Shown here is a trigger to open Safari, it’s just the Safari application in the first pane and the **Open** action in the second. The argument is blank. Notice that when the action is **Open** the default name for the trigger is Open followed by the application. Usually the default name is the object followed by the action in parenthesis. **Open** is special, probably because it’s so common. If in the Extras Preferences you have Reopening the current application set to “activates the application”, then using this trigger when Safari is already running will make it the active application.

You can obviously make similar triggers to open your favorite applications. Some people create other triggers like Safari (**Quit**) or Safari (**Hide Others**) and put them on the same keys but with different modifiers (e.g., <kbd>⌥</kbd> or <kbd>⇧</kbd>). Others just use the standard macOS shortcuts of <kbd>⌘</kbd>Q and <kbd>⌥</kbd><kbd>⌘</kbd><kbd>H</kbd> to run these on the current application.

### Show Shelf/Clipboard Contents

The Shelf and Clipboard History are enabled with the Shelf plugin and the Clipboard plugin respectively. Each enables a window that you typically access with the mouse (see [Clipboard and Shelf](../Clipboard and Shelf.md) for details). To get keyboard access to these, first enable the objects in the Catalog under Quicksilver and Shelf & Clipboard (check the box and click the rescan button). If you select these objects in the first pane, you can type <kbd>→</kbd> or <kbd>/</kbd> to open a new results list with their contents. The **Show Contents** action is the equivalent of this, and since it's an action, you can use it in a trigger.

So this trigger will open the shelf in a results list, with the first item selected, and let you type to select any item on the shelf (or the Clipboard History if you use that object). You can also use the **Search Contents** action which is very similar but won’t select the first time and won’t show a results list at first.

You can create triggers using **Show Contents** or **Search Contents** for anything you can right-arrow into, such as Contacts, iTunes, your Documents folder, etc.

### Search Wikipedia

Some actions take an argument in the third pane and triggers can use these too. The **Search For…** action will search some web site for the text entered as an argument. See the [Web Searches](../Web.md#web-searches) section for the details of using this action.

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

## More on Triggers

The possibilities for triggers seem endless. Here are some triggers people have posted on the Quicksilver forums as their favorites:

  * Documents ⇥ **Open**
  * Finder Selection ⇥ **Go To Directory in Terminal**
  * Finder Selection ⇥ **Rename…**
  * Finder Selection ⇥ **Scale Image…** ⇥ 400 
  * Finder Selection ⇥ **Open With…** ⇥ TextMate
  * Current Application ⇥ **Menu Bar…**
  * Current Application ⇥ **Menu Bar Items…**
  * Current Application ⇥ **Show Menu Items**
  * Current Application ⇥ **Relaunch**
  * Current Application ⇥ **Hide Others** (though <kbd>⌥</kbd><kbd>⌘</kbd><kbd>H</kbd> already works in most every application)
  * Previous Application ⇥ **Open** (go back to what you were doing last, toggle between two apps, or restore focus if Quicksilver steals it)
  * Artist Now Playing ⇥ **Show Contents**
  * Browse Albums ⇥ **Search Contents**
  * killall Dock ⇥ **Run Command in Shell** (or any other frequent shell command)
  * `pbpaste | pbcopy` ⇥ **Run Command in Shell** (re-copies the clipboard contents without formatting)
  * `date` ⇥ **Run Command in Shell** (acts like a clock)
  * Current Web Page ⇥ **Open With…** ⇥ [Some Web Browser]
  * Removable Disks ⇥ **Eject** (great to clean up mounted disk images)
  * Network Disks ⇥ **Eject**

There are some limits to triggers that you can create. You can’t save a trigger for something that isn’t in your catalog. So the Current Application ⇥ **Menu Bar…** trigger above works, but you can’t do Current Application ⇥ **Menu Bar…** ⇥ Help because the “Help” item is created on demand. Also, actions that appear only for particular applications can’t be saved as triggers, so you can’t do Mail (**Get New Mail**). For most of these, you can physically create the trigger, but the objects involved will disappear when Quicksilver restarts, making it impossible to set up the trigger again.

## Trigger Settings

The Settings tab in the drawer lets you set various options for a keyboard trigger. “Shortcut” lets you set the key combination. “Activate” lets you determine if the trigger activates when the key is pressed or released, and lets you set it to repeat if the key is held down for a period of time (useful for something like “skip forward” or “volume down”). With a “Delay” set, the trigger won’t activate until the key has been held down for the number of specified seconds. The “Show Window” option shows a small window that quickly zooms out of the center of the screen, which is useful if you need some indication that the trigger was executed.

A delay can be useful for some dangerous commands that you don’t want to execute if you accidentally type the key. If you had a shortcut to run the Quit All Visible Applications script from the Extra Scripts plugin, you might configure it to only execute if you hold the key down for 2 seconds.

If you create a lot of keyboard triggers it’s probably best to use some system to remember them. Some people put applications on their function keys, others use mnemonic keys like <kbd>⌃</kbd><kbd>⌘</kbd><kbd>S</kbd> for Safari. In examples above <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd> did a Wikipedia search and adding a <kbd>⇧</kbd> to the shortcut did the same thing with the current selection.

The nice thing about keyboard triggers is that you can fire them off from any context, but a major downside is that you need to choose a key combination that doesn’t conflict with anything else (you care about) in any context, and never will for any application you ever install. Not an easy task. Limit the scope to applications where the trigger makes sense whenever possible, and keep in mind that doing things “the hard way” by just calling up Quicksilver and smacking a few keys is often preferable to the stress of coming up with a keystroke you’ll never use anywhere else, ever again.

Another possibility is to avoid keystrokes altogether. The next sections describes using triggers with the mouse instead.


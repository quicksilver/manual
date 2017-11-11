# System

Quicksilver deals not just with your data, but with your computer too. Here are the ways it can interact with your hardware and its configuration.

## Devices

In the catalog under System and Devices you’ll find Disks and Printers. If you install the Displays Module plugin you’ll also see Displays. If you install the AirPort Module plugin you’ll also see AirPort Networks. 

Installed Disks can be called up in the object pane by name. You can also hold down the <kbd>/</kbd> (slash) key to select the root drive. In addition there is an object called Network in the catalog for `/Network` on your system which without Quicksilver is typically opened from the top of the Finder’s sidebar. If you mount network volumes (typically using the Finder’s Connect to Server command) they will also appear, as well as two items for the automounter: Servers for `/automount/Servers` and static for `/automount/static`. There are also three proxy objects related to disks: Network Disks, Mounted Disks, and Removable Disks There are no special actions for these objects, you merely navigate through them as you do any other folder. There doesn’t seem to be a way to mount network drives but you can **Eject** them, in fact Network Disks (**Eject**) makes a nice trigger.

With the Displays Module installed the Catalog also includes all displays connected to the computer. It is a little flaky though. I have a PowerBook running in an English locale and yet in version 48 of the plugin my display appears in the catalog as “Écran à cristaux liquides couleur” which is French for “LCD Screen”. Still I can select it and then use one of the actions: **Set Refresh Rate…**, **Set Color Depth…**, or **Set Resolution…**. All three let you choose an argument from a list of available options and also have some very pretty icons.

The Displays Module also installs a **Find With…** action but it doesn’t do anything and shouldn’t be used.

Quicksilver scans the folder `~/Library/Printers/` to find all installed printers (they end with `.app`) and add them to the catalog. You can print a file by selecting it as the object, using the **Open With…** action and then choosing a printer as the argument. You can’t choose the printer directly in the third pane, you have to navigate to `~/Library/Printers/` to select it. A little easier is the reverse action **Open File…**. Choose the printer as the object, which you can do just by typing it and use the **Open File…** action and then choose the file as the argument. Since the first two panes are fixed, this form is better as a trigger. Select your primary printer, the **Open File…** action and leave the third pane blank, to be filled in when you use the trigger, perhaps by using <kbd>⌘</kbd><kbd>G</kbd> to choose the Finder’s selection. Note that selecting a file and using **Move To…** or **Copy To…** a printer will not print the file but will put it inside the printer’s .app package.

## Networking

With the AirPort Module plugin installed you’ll see any available wireless networks as objects. There is one action installed with the plugin. For a wireless network object you can choose **Select Network** to join that network (provided the configuration allows). If you need to switch to another network, this is a very convenient way. If you manual switch networks often, a useful trigger is AirPort Networks (Catalog) with the **Show Contents** action. You can then choose the network and use the **Select Network** action. 

In the Catalog under Quicksilver, Internal Commands are the Turn AirPort On and Turn AirPort Off objects. Use the **Run** action with them. 

With the Network Location Module plugin the locations you’ve configured in the Network System Preference pane are available in the Catalog (under System, Configuration, Network Locations). If you select one in the object pane you can use the **Switch to Location** action to use it. If you select the Network Locations (Catalog) object you can type <kbd>→</kbd> to get a results list of all configured network locations.

There are several OS X utilities that come in handy when dealing with networking that are easily accessed with Quicksilver. The Applications catalog source includes indexing in `/Applications` down 3 levels so by default you can get to AirPort Admin Utility, AirPort Setup Assistant and Internet Connect. The default action for any of these applications should be **Open**. The Network Preference Pane is available in the catalog under System, Configuration, Preference Panes, System Preferences (System).

## Configuration

Quicksilver includes the OS X System Preferences in the Catalog under System, Configuration. It will find preference panes in `/System/Library/PreferencePanes/`, `/Library/PreferencePanes/` and `~/Library/PreferencePanes/` and you can include or exclude these in the Catalog as groups if you want. The individual preferences panes are in the catalog, so you can bring them up directly. You can also select the Preference Panes (Catalog) object or the System Preferences.app as the object and type <kbd>→</kbd> to see a list of all preference panes in a results list. With a preference pane as the object, you’ll most likely want to use the **Open** action to bring up the preference pane, but they are treated like files and many other actions are available. 

With the User Accounts Module plugin installed the user accounts on your system are in the Catalog (under System, Configuration, User Accounts) and there is a **Switch to User** action. This invokes OS X’s fast user switching technology. If you select User Accounts(Catalog) object and type <kbd>→</kbd> you get a results list of all user accounts on the system. There’s also a Fast Logout.sh object installed with the Extra Scripts plugin. If you use the **Run […]** action from the Terminal Module plugin with it you will use fast user logout which basically just locks the screen but leaves everything in your session running as if you had done fast user switching. If you do this often create a trigger for it.

With the Keychain Module plugin installed your Keychains are available in the Catalog. They appear in the Catalog under Modules, Keychains. If you select one of your keychains as the object, you can type <kbd>→</kbd> to see the individual items in a results list. With a keychain item as the object you have three primary actions you’ll want to use: **Copy Password**, **Paste Password**, and **Get Password**. All three will open a Confirm Access to Keychain prompt, I always choose Allow Once. The first will copy the password to the clipboard, the second will paste it directly into the current application and the third will open a new command window with the password as the text object so you can choose any action you want. Accessing passwords using these actions should be more secure than keeping them as text in triggers, the shelf or clipboard, though if you use **Copy Password** you’re copying them to the clipboard anyway. **Paste Password** (unlike **Paste**) does not put a copy on the clipboard. If you use **Get Password** and then **Type Text** (instead of **Paste**) you will also avoid making copies on the clipboard. 

## Exposé

The System Hotkey Commands plugin creates Catalog entries for Dashboard and Exposé commands. For those commands configured on function keys (<kbd>F1</kbd>-<kbd>F13</kbd> with or without modifiers) in the Dashboard and Exposé System Preference pane, you’ll find Catalog entries in Modules, Exposé Commands as shown in the following table.

| Exposé Command | Quicksilver Catalog Item |
| --- | --- |
| All windows | Exposé All Windows
| Application Windows | Exposé Application Windows |
| Desktop | Exposé Desktop |
| Dashboard | Show Dashboard |

While there are other actions available I can’t imagine wanting to use anything other than **Run**. If you are annoyed that OS X doesn’t allow you to bind these to more keys, configure a trigger to access these any way you want.

## Extra Scripts

The Extra Scripts plugin is really just a catch-all of various scripts, but most have to do with controlling the computer so they are described here. Depending on the script you’ll use these with the Run action for applescripts or one of the **Run** actions from the Terminal module, The default action should be correct. If you use these often, they all make good candidates for triggers. For some of them like Shut Down, if you make a keyboard trigger for them, you might want to set a Delay on the trigger so you can’t accidentally type it.

- System
	- Sleep - same as <kbd>⌥</kbd><kbd>⌘</kbd><kbd>⏏</kbd>
	- Restart - same as <kbd>⌃</kbd><kbd>⌘</kbd><kbd>⏏</kbd>
	- Force Restart - same as <kbd>⌃</kbd><kbd>⌘</kbd>-power, warning: doesn’t offer to save files
	- Shut Down - same as <kbd>⌃</kbd><kbd>⌥</kbd><kbd>⌘</kbd><kbd>⏏</kbd>
	- Force Shutdown 
	- Empty Trash 
	- Eject
	- Close Disk Tray
- System Volume:
	- Mute Volume - sets volume to 0, not a toggle, don’t confuse with iTunes Module “Mute” script
	- Min Volume (20%) - sets volume to 1
	- Mid Volume (40%) - sets volume to 4
	- Max Volume (60%) - sets volume to 7
	- Toggle Audio Input - toggles between input devices in the Sound System Preference
	- Toggle Audio Output - toggles between output devices in the Sound System Preference
- Networking:
	- Get IP - shows the result in Large Type
	- Get External IP - shows the result in Large Type
- Processes:
	- Hide Others - most OS X applications have this as a shortcut on <kbd>⌥</kbd><kbd>⌘</kbd><kbd>H</kbd>
	- Show All
	- Quit Visible Apps
	- LockScreen - runs the screen saver and makes you type a password to get back
	- Logout - same as <kbd>⇧</kbd><kbd>⌘</kbd><kbd>Q</kbd> (or is it <kbd>⌥</kbd><kbd>⇧</kbd><kbd>⌘</kbd><kbd>Q</kbd>?)
	- Fast Logout - leaves you logged in, but goes to a login window (OSX’s Fast User Switching)
	- Switch To Root
	- Classic Shutdown
	- top 10 - use Run in Terminal… as it outputs 10 lines of text for the 10 busiest applications
- Miscellaneous:
	- Show Character Palette - Often <kbd>⌥</kbd><kbd>⌘</kbd><kbd>T</kbd> but not in all applications
	- Show Keyboard Viewer
	- Sync Now - runs synchronize in iSync
	- Type Clipboard 
	- Zoom Front Window - This is like clicking the green button in the top left of a window

# Finder Selection

A useful shortcut for working with active files in Quicksilver is the "Current Selection" trigger that opens the Quicksilver command window with the files currently selected in Finder.app.

Unfortunately, Apple's implementation for this has had issues in recent versions of macOS, but there are workarounds.

Also see [Using the Mouse](using-the-mouse.md) for the Grab 'n Drop feature.

## Proxy Object

There are two proxy objects that can grab the current Finder selection: "Finder Selection" and "Current Selection".

![Current Selection proxy object](../images/Current_selection.png)

"Current Selection" also works on other kinds of selections, like a URL highlighted in a text editor. You'll probably want to use "Current Selection" unless you're making a trigger that should only work on a file/folder, or need to get the Finder Selection while another program is in focus.

Quicksilver includes a default trigger for this, called "Command Window with Selection" (under Preferences → Triggers → Quicksilver).

## Send to Quicksilver (Service)

[Services](http://www.macworld.com/article/1163996/how_to_use_services_in_mac_os_x.html) can be a bit tricky. Any macOS application can register a "service" which is available from the application menu under "Services". You can assign shortcuts to them and use them much like you would use a Quicksilver trigger.

Quicksilver has a built-in service called "Send to Quicksilver", functioning similarly to the "Current Selection" proxy object.

![Send to Quicksilver Service in System Preferences](../images/Send_to_Quicksilver_Service.png)

This service has the keyboard shortcut <kbd>⌘</kbd><kbd>⎋</kbd>, which is the same as the "Command Window with Selection" trigger built into Quicksilver. If you wish to use the service separately from the trigger, you should change the keyboard shortcut for the trigger in the Trigger preferences.

## Tradeoffs

| Behaviour                                                                   | Proxy Object                   | Send to Quicksilver |
|-----------------------------------------------------------------------------|--------------------------------|---------------------|
| Always returns the correct selection from Finder                            | No                             | Yes                 |
| Works in Finder with a file/folder selected                                 | Yes                            | Yes                 |
| Works in Finder if there is no file/folder selected (returns current folder)| Yes                            | No                  |
| Works in Finder with column mode                                            | Yes                            | No                  |
| Works on selections in other programs                                       | Yes (Use "Current Selection")  | Yes                 |
| Can be used with triggers                                                   | Yes                            | No                  |
| No proxy resolution delay                                                   | No                             | Yes                 |
| Not cached for 3.0s                                                         | No (same for all proxy objects)| Yes                 |
| Does not change application focus to Quicksilver.app                        | Yes                            | No                  |

(The table is organized so that all "good" behaviour is "Yes" and all "bad" behaviour is "No".)

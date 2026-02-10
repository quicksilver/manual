# Event Triggers

While keyboard triggers let you do something with a single keystroke, event triggers allow you to do something with _no keystrokes_ (or clicks).

Like all triggers in Quicksilver, event triggers can run any command Quicksilver is capable of running, but instead of running in response to keyboard and mouse activity from the user, they run automatically in response to things happening on your computer. The list of events you can assign triggers to will depend on which Quicksilver plugins are installed, but there are quite a few simply built into the Event Triggers Plugin. As of this writing, there are 38 events you can potentially hook into.

Some examples will probably explain it better at this point. The plugin’s documentation lists the following:

  * When the screen saver activates, pause iTunes.
  * When the computer wakes from sleep, open Mail.
  * When the network changes, run a shell script.
  * When a disk named “Backup” is mounted, compress a specific folder and copy it to the disk.
  * When switching to the internal speakers (headphones disconnected), pause iTunes.

Here are some other ideas:

  * Turn off AirPlay (by switching to the "Computer" device) when headphones are plugged in
  * Switch to the appropriate equalizer preset in iTunes when an optical cable is plugged in
  * When Pages launches, quit Twitter
  * After compressing files or folders, move the archive to the desktop
  * When taking a screen shot, ask me who to e-mail it to
  * Append a message to a file when you lose Internet connectivity

## Event Trigger Object

The plugin provides a proxy object called **Event Trigger Object**. This proxy resolves to whatever object triggered the event, allowing the action to operate on it directly. For example, if you set an event trigger to fire whenever the track in iTunes changes and set the action to **Event Trigger Object** → **Large Type**, the name of the track will appear on screen whenever the track changes.

## Setup

To use event triggers, enable the following items in Preferences (<kbd>⌘</kbd><kbd>,</kbd>). Activate items from left to right.

| Triggers | Catalog |
| --- | --- |
| Adds "Event" triggers that are similar to ordinary triggers, but activated due to system changes. | Quicksilver → Proxy Objects → **Event Trigger Object** |


# Keyboard Triggers

Keyboard triggers are the most common type of trigger in Quicksilver. They let you execute any Quicksilver command with a simple keyboard shortcut, without having to activate Quicksilver first.

## How Keyboard Triggers Work

If you enter a complete command into the trigger, like choosing an application and the **Open** action, it will be run when you execute the trigger. If you choose just a partial command, like a web-search and the **Search For…** action, when you execute the trigger a command window will appear with as much filled in as your trigger defines. You can't have gaps (e.g., you can't leave the first pane blank and use the **Get Info** action).

Triggers are given a default name based on the command they represent. When the action is **Open**, the default name is "Open" followed by the application. Usually the default name is the object followed by the action in parenthesis. **Open** is special, probably because it's so common.

## Keyboard Trigger Settings

The Settings tab in the drawer lets you set various options for a keyboard trigger:

- **Shortcut** - The key combination that activates this trigger
- **Activate** - Whether the trigger activates when the key is pressed or released, and whether it repeats if the key is held down (useful for something like "skip forward" or "volume down")
- **Delay** - The trigger won't activate until the key has been held down for the specified number of seconds
- **Show Window** - Shows a small window that quickly zooms out of the center of the screen, providing visual feedback that the trigger was executed

A delay can be useful for dangerous commands that you don't want to execute accidentally. If you had a shortcut to run the Quit All Visible Applications script from the Extra Scripts plugin, you might configure it to only execute if you hold the key down for 2 seconds.

## Choosing Shortcuts

If you create a lot of keyboard triggers, it's best to use some system to remember them. Some people put applications on their function keys, others use mnemonic keys like <kbd>⌃</kbd><kbd>⌘</kbd><kbd>S</kbd> for Safari. You could use <kbd>⌃</kbd><kbd>⌘</kbd><kbd>W</kbd> for a Wikipedia search and add a <kbd>⇧</kbd> to the shortcut to do the same thing with the current selection.

The nice thing about keyboard triggers is that you can fire them off from any context, but a major downside is that you need to choose a key combination that doesn't conflict with anything else (you care about) in any context, and never will for any application you ever install. Not an easy task. Limit the scope to applications where the trigger makes sense whenever possible, and keep in mind that doing things "the hard way" by just calling up Quicksilver and typing a few keys is often preferable to the stress of coming up with a keystroke you'll never use anywhere else, ever again.

## Multiple Activation Methods

One thing might not be obvious: You can configure the same trigger to activate by multiple means. For example, if you have an Open Safari trigger assigned to the shortcut <kbd>⌃</kbd><kbd>⌘</kbd><kbd>S</kbd>, you can also assign it to a mouse gesture or mouse position, and both will work. You do this by clicking the icon of the type of trigger in the <kbd>⌘</kbd> column of the Triggers preference pane. A pop-up menu appears of the other choices and you can select another one and configure it. This can be useful to have two ways to invoke a trigger: one when your hands are on the keyboard, and another when one hand is on the mouse.

There isn't a way to remove one method from a trigger without deleting the entire trigger. The `-` button at the bottom of the screen deletes the whole trigger. For a keyboard trigger, you can always change it to not be bound to a specific key by clicking the Edit button and then the delete key. To avoid this issue, you can also just create entirely separate triggers that do the same thing with different activations.

## See Also

For examples of useful keyboard triggers, see the [Example Triggers](examples.md) section.

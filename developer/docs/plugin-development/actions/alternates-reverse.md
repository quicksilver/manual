# Alternate Actions

Alternate actions are a very powerful feature of Quicksilver. When a user selects an action in the second pane, they can hit ↩ to run it, or they can hit ⌘↩ to run an alternate (if one is defined). Generally an alternate action will be similar to the main action, but modified in some way.

You create alternate actions just like any other action by adding a section for it in `Info.plist` and adding code in `BlahAction.m` for it. The main thing to note is that an action doesn't need to be active (checked in the preferences) to work as an alternate. You can define which of the actions in your plug-in are enabled or disabled by default, so an alternate could be something you never intend for the user to see/use directly or it could be one of the "normal" actions that you want to be conveniently accessible. Users can, of course, enable or disable actions themselves after your plug-in is installed.

Alternate actions should be able to take the same number of arguments as the main action. You can't define an alternate that requires something in the third pane for an action that doesn't use the third pane.

To define an alternate for an action, add an item named `alternateAction` to your action's properties in `Info.plist`. The value for `alternateAction` should be the identifier of another action.

# Reverse Actions

Some actions are reversible. For instance, web searches can be either

    Search Engine → Search For… → [search terms]

or

    [search terms] → Find With… → Search Engine

Reverse actions are added to the plist just like any other action. They should be more or less identical to the "forward" version of the action, with a couple of key changes:

  1. The identifier for the action should be different.
  2. The name of the action should be different.
  3. There should be a boolean called `reverseArguments` set to `YES`

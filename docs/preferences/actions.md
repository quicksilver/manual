# Actions

The Actions preference pane shows every action Quicksilver can perform. Open it by activating Quicksilver, typing <kbd>⌘</kbd><kbd>,</kbd>, and selecting the Actions tab. From here you can enable or disable individual actions, reorder their priority, and see which object types each action supports.

![The Actions preference pane](../images/Quicksilver_actions_preferences.png)

## How Actions Work

Executing an action in Quicksilver is known as a "command." Commands are entered via two or three panes containing, respectively, an Object, an Action, and (if a third pane is needed) an Argument. Actions appear in Quicksilver\u2019s second pane.

![A Quicksilver command is composed of an Object, an Action, and optionally an Argument](../images/Command_diagram.png)

All actions work on an object, and the available actions depend on the type of object selected. For example, the **Open URL** action is only available when the object is a URL. Actions that require an argument typically end in "\u2026" and the argument is expected to be of a certain type. For instance, the **Email To\u2026** action expects the argument to be an email address or contact.

## Reordering and Disabling Actions

Uncheck an action\u2019s checkbox to remove it from use. To change the order in which actions appear in the results list, select the "Rank" column header and drag actions to the desired position.

![Drag actions to reorder them by rank](../images/Actions_Rank.png)

The ranking determines which action appears first in the second pane after you select an object. Higher-ranked actions are matched sooner when you begin typing.

## Actions Are Grouped by Object Type

Actions are also grouped by the type of object in the first pane. This means that even though you set a global ranking, the actions you see depend on what kind of object is selected. A file object will surface file-related actions, while a URL object will surface URL-related actions.

![Actions grouped by object type](../images/Actions_by_object.jpg)

## Complementary Actions

Some actions have a complementary action that reverses the object and argument types. This lets Quicksilver adapt to however you prefer to think about a command.

  * **Email To\u2026 (Compose)** expects a file as the object and an address as the argument, while **Email Item\u2026 (Compose)** expects an address as the object and a file as the argument.
  * **Search For\u2026** expects a site as the object and a query as the argument, while **Find With\u2026** expects a query as the object and a site as the argument.

Many (but not all) action names hint at the type of argument they take. Some complementary pairs are so similarly named you might not notice they are different; others are so differently named you might not realize they are related.

![Examples of complementary action pairs](../images/Complimentary_actions.png)

## User-Installed Actions

Actions can be added by plugins or by the user. User-installed actions are placed in:

`~/Library/Application Support/Quicksilver/Actions`

User-installed actions generally require a text or file object in the first pane. Plugins are optional modules that can also add objects or other capabilities to Quicksilver.

## The \u201cCapitalize Key\u201d Preference

If you enable \u201cCapitalize Key modifies Action in Command window\u201d in Preferences \u2192 Extras, shifted letters typed in the first pane will select an action in the second pane, eliminating the need to press <kbd>⇥</kbd> first. Once focus moves to the action pane, unshifted letters continue to refine the action.

If you also hold <kbd>⌘</kbd>, the action will execute immediately\u2014no need to press <kbd>↩</kbd>. For example, <kbd>⇧</kbd><kbd>I</kbd> selects the action for \u201cI\u201d (perhaps **Get Info**), while <kbd>⇧</kbd><kbd>⌘</kbd><kbd>I</kbd> performs it. Use with caution, as it is not always clear which action will be invoked.

## Alternate Actions

Alternate actions provide a quick way to modify the action without re-typing it. Press <kbd>⌘</kbd><kbd>↩</kbd> instead of <kbd>↩</kbd> to run the alternate for the current action.

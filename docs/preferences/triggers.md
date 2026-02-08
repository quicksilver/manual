# Triggers

You define triggers in the Triggers Preference pane. You can go to this pane directly by activating Quicksilver and typing <kbd>⌘</kbd><kbd>'</kbd>. You'll see several sets in the left side of the preference pane. Some triggers are predefined by Quicksilver itself or various plugins, e.g., you'll find several in iTunes, and two in Quicksilver. Triggers you create will be in the Custom Triggers set.

## The Triggers Interface

Each trigger is shown by its name which is usually a combination of the object and action to be invoked. The checkbox shows if the trigger is active. The <kbd>⌘</kbd> column shows the type of trigger, in this case they are all activated by a shortcut which is shown in the Trigger column (some are not assigned to keys). If you select a trigger and click on the ⓘ button at the bottom, a drawer is revealed with various settings for the trigger. The settings tab looks different for each type of trigger. You can change the name of the trigger in the top text field.

## Editing Triggers

You can change some options by clicking in the main trigger window. If you click on the command name you can get an edit field to change the name of the trigger. If you click in the Trigger column you can set or change the shortcut. If you click on the icon in the <kbd>⌘</kbd> column you can add another means (Gesture, Mouse) to activate the trigger. Though once you create an additional way, there doesn't seem to be a way to delete it without deleting the entire trigger.

## Creating New Triggers

You create a new trigger by clicking the + button at the bottom and selecting a trigger type from the pop-up menu (Gesture, Keyboard, or Mouse, depending on installed plugins). The Group option is just a way to collect triggers in a group or folder. They don't perform any function other than helping you organize a lot of triggers. You can't activate all the triggers in a group at once. Create a Group from the + menu and drag triggers into it.

Regardless of which type you choose, a special command window appears (populated with the last command you performed) to let you define the command for the trigger. Enter the command and click Save. Then open the drawer to the Settings tab to assign a shortcut, mouse click, or gesture to use to activate the trigger. If you're creating a keyboard trigger, just click in the Trigger column for this new trigger, the drawer will open and you can just type the shortcut as if you had clicked the Edit button.

## Settings and Scope

By default, triggers are available whenever Quicksilver is running, regardless of what application is active. They can also be limited to function only when a certain application is active or when a certain application is not active. You do this by opening the drawer for a trigger and choosing the Scope tab. The default is "Enabled in all applications" but you can also choose from the popup "Enabled in selected applications" or "Disabled in selected applications". For the latter two you can type the name of the application into the large box and type <kbd>⇥</kbd> or <kbd>,</kbd> after the name to have it turn into a blue button. You can then enter another application if you choose.

If you have triggers that use certain features, be cautious about deleting the plugins that supply those features. In particular if you have triggers using mouse gestures from Abracadabra (see the [Gestures](../features/triggers/gestures.md) section) and if you remove the Abracadabra plugin, the trigger panel may display oddly with some blank lines and missing icons. To correct this, reinstall the plugin (Abracadabra in this case), or remove the triggers.

## Tips

Your trigger configuration is stored in `~/Library/Application Support/Quicksilver/Triggers.plist`. This is useful to know if you want to have the same configuration on several machines, just copy the file between the machines while Quicksilver is not running.

For more information on using triggers, see the [Triggers](../features/triggers/index.md) feature section.

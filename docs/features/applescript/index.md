# AppleScript

Quicksilver can be called from AppleScript. Quicksilver can also call AppleScripts and you can attach triggers to these scripts as well. This page provides an overview of the ways you can use AppleScript with Quicksilver along with some useful AppleScripts that users have created.

## Calling Quicksilver from AppleScript

You can open an object in Quicksilver by setting its selection property in AppleScript. Quicksilver will try to automatically determine what kind of object the text actually represents to show the appropriate actions. Some examples:

```applescript
tell application "Quicksilver" to set selection to "text"
tell application "Quicksilver" to set selection to "/"
tell application "Quicksilver" to set selection to "http://google.com"
```

## Pane 1 AppleScripts

These AppleScripts are selected in Quicksilver's first pane. Simply select any `.scpt` file in the first pane and then the **Run** action.

You can also use AppleScript Editor to save a script as an "Application". Like any application they can then be selected in the first pane and run using the **Open** action.

### Adding Pane 1 AppleScripts to the Catalog

You can add scripts to your Catalog to quickly find and **Run** them. Quicksilver by default adds the scripts it finds in `~/Library/Scripts` and `/Library/Scripts`. You can add more locations by adding a "File & Folder Scanner".

### Using Text Action AppleScripts in Pane 1

Any Text Action AppleScript (see below) can also be used in the first pane. When you select a Text Action AppleScript in the first pane instead of getting the **Run** action you will get the **Process Text...** action and be prompted for the text in the third pane. This can be very useful for making Triggers for Text Action AppleScripts.

You may also want to consider adding a `~/Library/Application Support/Quicksilver/Actions/` File & Folder Scanner to your catalog so that Text Action AppleScripts can be quickly selected.

### Example Pane 1 Scripts

These simple scripts take no arguments. Copy them into AppleScript Editor and then save them as `.scpt` files.

  * [Open AirDrop](open-airdrop.md)
  * [Color Picker](color-picker.md) — displays the color picker from any app

## Pane 2 AppleScript Actions

Action AppleScripts are actions you can select in Quicksilver's second pane for certain first pane types (the script determines what types).

To install a script, save it in `~/Library/Application Support/Quicksilver/Actions/MyActionName.scpt` where MyActionName is the name the action will have in the second pane, and `~` is your user's home folder. Then **relaunch Quicksilver**. Create the `Actions` folder if it doesn't exist.

See the [Custom Actions](custom-actions.md) page for information on writing your own actions. For convenience, you can start using one of the [AppleScript Action templates](templates.md).

### File Action AppleScripts

  * [Paste file path](paste-file-path.md) — pastes the file path of the file in the first pane

### Three-Pane AppleScripts

  * [Run command in shell with arguments](run-shell-command.md) — runs a text command entered in the first pane using the file or text arguments entered in the third pane
  * [Convert Units To...](convert-units.md) — takes a value with units in the first pane, and converts it to the units entered in the third pane

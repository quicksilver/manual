# AppleScript Actions

It's possible to define actions that exist only as AppleScript and not as Objective-C. These actions will look a little bit different in your `Info.plist`.

  1. `actionClass` should be set to "QSAppleScriptActions".
  2. `actionScript` should be set to the name of an AppleScript file, like "Blah.scpt". This script will need to be copied into your plug-in's `Resources` folder. A single AppleScript file can handle multiple actions (by using different `actionHandler`s).
  3. `actionHandler` should be the name of a function in the script, like "do_this_thing" (assuming the script has something like this in it).
     
        on do_this_thing(objectFromQuicksilver)
            tell application "XYZ" to lick the face of objectFromQuicksilver
        end do_this_thing

You'd omit the `actionSelector` for AppleScript actions.

I'm not sure what happens if you send multiple objects (via the comma trick) to an AppleScript action.

# Application Actions

*Applications Actions* are actions that only appear in the list of actions when a specific application if selected in the first pane of Quicksilver. Examples of this are the actions "Next Song", "Play - Pause", "Previous Song" that are provided by the iTunes plugin and only appear if iTunes is selected in the first pane. Or the "Get New Mail" and "Open New Mail" actions for Mail.app.

These actions are defined in the `Info.plist` of the plugin, in `QSRegistration` → `QSApplicationActions` → bundle identifier → action identifier. The same pattern can be used as in the normal actions (inside `QSActions`) **OR** a `QSCommand`. For an example of how `QSApplicationActions` are defined, see [the Info.plist of the Apple Mail Plugin](https://github.com/quicksilver/com.apple.Mail-qsplugin/blob/master/Info.plist).

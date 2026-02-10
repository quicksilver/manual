# Open AirDrop

This script allows you to open AirDrop using Quicksilver.

Save this script somewhere that Quicksilver can find it, such as `~/Library/Scripts`, then bring it up in the first pane and use the **Run** action.

If you want to get fancy, you can apply the AirDrop icon to the script file. To do so: (1) right click on AirDrop in the Finder sidebar and select Get Info from the contextual menu, (2) similarly open the Info window of your `Open AirDrop.scpt` file, then (3) click on the AirDrop icon in the first Info window, press <kbd>⌘</kbd><kbd>C</kbd> to copy it, and finally (4) click on the generic script icon in the other Info window and press <kbd>⌘</kbd><kbd>V</kbd> to paste the new icon.

## Code

```applescript
tell application "Finder"
    if exists window "AirDrop" then
        tell application "System Events" to ¬
            tell application process "Finder" to ¬
                perform action "AXRaise" of ¬
                    (windows whose title is "AirDrop")
    else if (count Finder windows) > 0 then
        make new Finder window
        tell application "System Events" to ¬
            click menu item "AirDrop" of menu 1 of menu bar item ¬
                "Go" of menu bar 1 of application process "Finder"
    else
        tell application "System Events" to ¬
            click menu item "AirDrop" of menu 1 of menu bar item ¬
                "Go" of menu bar 1 of application process "Finder"
    end if
    activate
end tell
```

# Color Picker

Save as an Application in AppleScript Editor. This script opens the system color picker from any application.

```applescript
tell application "System Events" to set _frontMostApp to (name of processes whose frontmost is true)
set _frontMostApp to item 1 of _frontMostApp
tell application _frontMostApp to activate
choose color
```

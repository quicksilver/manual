Pastes the file location of the file that's in the first pane. So the
folder 'Application Support' will be pasted as 'MacBook
HD:Users:username:Library:Application Support:'

Useful if writing AppleScripts!

``` applescript
using terms from application "Quicksilver"
    on open _file
        try
            set _atid to AppleScript's text item delimiters

            set _homePath to path to home folder
            set _homePath to POSIX path of _homePath

            set _path to POSIX path of (item 1 of _file)
            set AppleScript's text item delimiters to _homePath
            set _path to "~/" & (text items 2 thru -1 of _path) as text

            set AppleScript's text item delimiters to _atid

            set the clipboard to _path
            delay 0.5

            tell application "System Events" to keystroke "v" using command down
        on error a number b
            set AppleScript's text item delimiters to _atid
            set selection to a
        end try
    end open
end using terms from
```
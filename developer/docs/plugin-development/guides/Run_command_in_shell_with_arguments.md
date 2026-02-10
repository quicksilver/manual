# Run\_command\_in\_shell\_with\_arguments

The following AppleScript code should be saved as a standard AppleScript .scpt file in \~/Library/Application Support/Quicksilver/Actions.

## Usage

Enter a text command in Quicksilver's first pane and then either enter a string of text in its third pane or select one or more files in the third pane.

By default, the POSIX paths of the files selected in the third pane (or the string of text entered in it) will be appended to the end of the command entered in the first pane.

Optionally, the command entered in the first pane can specify where arguments from the third pane should be substituted in. There are two methods to do so:

1\. Use $@ to indicate where all the arguments should go in one glob. Example:

&#x20;      `somecommand -i $@ --switches`         `will place all third pane arguments between -i and --switches`       &#x20;

2\. Use $1, $2, etc., to place specific arguments at specific points in the command. If an argument number is called for, but there are not enough arguments supplied in the third pane, this action will abort with an error message. If more arguments are supplied than there are argument numbers called for, the remaining arguments will be appended to the end of the command. It is possible to skip numbers in this sequence (e.g. $1, $3).

## Code

```applescript
property shouldVerify : true --change to false to skip verification dialog. Not recommended.

using terms from application "Quicksilver"
    on process text command with args --command is text, args can be text or (depending on the version of Quicksilver) either a list of POSIX paths of passed files or a list of HFS aliases to the passed files

        --Get POSIX paths of any files in the third pane.
        set args to args as list
        repeat with i from 1 to count args
            try
                if class of item i of args is alias then
                    set item i of args to quoted form of POSIX path of item i of args
                else if class of item i of args is text and item i of args begins with "/" then
                    set item i of args to quoted form of item i of args
                end if
            end try
        end repeat
        --


        if command contains "$@" then
            set args to my concatenateList(space, args)
            set command to my findReplace("$@", args, command)
        else if command contains "$" then
            repeat with i from (count args) to 1 by -1
                if command contains "$" & i then
                    set command to my findReplace("$" & i, item i of args, command)
                else
                    set command to my concatenateList(space, {command, item i of args})
                end if
            end repeat
            if command contains "$" & (count args + 1) then
                tell application "Quicksilver"
                    activate
                    display dialog "Argument count mismatch: Nothing supplied for $" & (count args + 1) buttons {"Cancel"}
                end tell
            end if
        else
            set args to my concatenateList(space, args)
            set command to my concatenateList(space, {command, args})
        end if

        if shouldVerify then
            activate
            display dialog "Please verify that the following command is correct." default answer command buttons {"Cancel", "Run"} default button "Run"
        end if

        do shell script command
        return result

    end process text

    on get argument count
        return 2
    end get argument count

    on get direct types
        return {"NSStringPboardType"}
    end get direct types

    on get indirect types
        return {"NSStringPboardType", "NSFilenamesPboardType"}
    end get indirect types
end using terms from

on findReplace(findText, replaceText, sourceText)
    set ASTID to AppleScript's text item delimiters
    set AppleScript's text item delimiters to findText
    set sourceText to text items of sourceText
    set AppleScript's text item delimiters to replaceText
    set sourceText to sourceText as text
    set AppleScript's text item delimiters to ASTID
    return sourceText
end findReplace

on concatenateList(delims, sourceText)
    set ASTID to AppleScript's text item delimiters
    set AppleScript's text item delimiters to delims
    set sourceText to sourceText as text
    set AppleScript's text item delimiters to ASTID
    return sourceText
end concatenateList
```

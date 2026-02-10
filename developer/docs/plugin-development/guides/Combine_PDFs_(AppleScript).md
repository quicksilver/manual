Combines PDFs selected in the first pane into a single document (leaving
the originals alone, of course). The output file goes in the same
location as the originals (if they're all in the same folder), or the
script asks where to put it (if they're in a number of places). It then
also returns the merged file to QS for further actions.

I *think* if you have something that's not a PDF in pane 1 it just gets
ignored. The shell script that actually does the merging probably
complains on stdout or stderr, but it doesn't fail.

**NEW: Updated for QS B72 with \`on open files\`.** Behavior is the
same—I wasn't sure what, if anything, to use pane 3 for. But pane 1 is
now limited to files, at least.

``` applescript
using terms from application "Quicksilver"

    on get direct types
        return {"NSFilenamesPboardType"}
    end get direct types

    on open files thePDFs
        tell application "Finder"
            set outputFolder to missing value
            set baseDir to container of first item of thePDFs
            repeat with p in items 2 through end of thePDFs
                if container of p is not equal to baseDir then
                    set outputFolder to (choose folder with prompt ¬
                        "Your PDFs are all over the place. Where do you want the merged file?" default location path to desktop folder)
                    exit repeat
                end if
            end repeat
            if outputFolder is missing value then set outputFolder to baseDir as alias
        end tell

        set outputFile to (outputFolder as text) & "Combined PDFs (" & (count of thePDFs) & ").pdf"
        set pdfArgs to ""
        repeat with p in thePDFs
            set pdfArgs to pdfArgs & " " & quoted form of POSIX path of p
        end repeat
        do shell script "\"/System/Library/Automator/Combine PDF Pages.action/Contents/Resources/join.py\" -o " & quoted form of POSIX path of outputFile & pdfArgs
        return outputFile as alias
    end open files

end using terms from
```
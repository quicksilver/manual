# Troubleshooting

http://docs.blacktree.com/quicksilver/support

Is the required plugin installed?

Is the catalog source, action, trigger enabled?

Check Console

Applications and system processes often write useful debugging information to log files. Different things write to different log files, but you can use /Applications/Utilities/Console.app to read all of them. Start Console.app and you’ll see the console.log displayed, most applications write their information to this log. If there isn’t a left hand pane in the window click the Logs button in the toolbar to make it appear (or use the Show Log List command from the View menu). Make sure the console.log is selected, that’s where Quicksilver writes all its information. Since so many things write to the console.log it’s useful to filter the display to just what you’re looking for, in this case type “Quicksilver” into the Filter box in the top right. Now you can see the Quicksilver log messages. Note that all the messages are preceded with a date and time to make finding relevant messages easier. Sometimes non-Quicksilver messages are relevant to diagnosing a problem, so after finding when something started failing you might unfilter the results and see if anything is reporting problems at the same time.



Task viewer (<kbd>⌘</kbd><kbd>K</kbd>) - gear menu invisible in Cube

where’s the verbose debugging info you’re seeing? you hold down option while starting up and it starts spitting out lots of info to console

Some things (oddly) require being administrator to work correctly

For Crashes, look in Console to find path to crash log, usually it is `~/Library/Logs/CrashReporter/Quicksilver.crash.log`

Find what catalog source is finding and item with **Show Source in Catalog**. e.g., to find what’s scanning an external drive.

The following files and folders should be owned by you and be readable and writable by you. You can check this by using the Finder’s Get Info command or opening Terminal.app and using the command line `ls -ld file`.

    drwxr-xr-x	~/Library/Application Support/Quicksilver/
    -rw-------	~/Library/Preferences/com.blacktree.Quicksilver.plist
    drwxr-xr-x	~/Library/Caches/Quicksilver/


## Program Interactions

Little Snitch prevents showing of plugin list 

kGTD might screw up the permissions of `~/Library/Application Support/Quicksilver/`

Stoplight prevents Quicksilver from starting

FileVault breaks stuff

Check that what’s in the panes is actually what you think is there. Some things look similar but are not the same, e.g., a link to google.com vs a google web search with *** in the URL or the actions. Can check with Show Source in Catalog.

## Reporting problems

I got an error but don’t mention what the error is. It’s like saying “Doctor it hurts when I do something”

Describing what you did so vaguely that others can’t reproduce or help. It’s like saying “I drove to Chicago but when I stopped I wasn’t there”

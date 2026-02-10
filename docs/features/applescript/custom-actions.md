# Custom AppleScript Actions

See [AppleScript](index.md) for a general overview of using AppleScript with Quicksilver.

## Overview

AppleScript Actions are used from Quicksilver's second pane and they behave exactly like any normal Quicksilver Action.

AppleScript Actions give you the ability to manipulate anything in Quicksilver's catalog. Most AppleScript Actions can use the comma trick, and Quicksilver's 3rd pane.

## Creating AppleScript Actions

The AppleScript format for a Quicksilver action is as follows:

```applescript
using terms from application "Quicksilver"
    on HANDLER_NAME

    end HANDLER_NAME
end using terms
```

`HANDLER_NAME` is the important bit. There are several potential handlers.

## Open Handlers

Each script should have one "open" or "process" handler. The open or process handler is what Quicksilver will call to do the actual work (i.e. it's what is called when you activate the Quicksilver action).

| Handler Name | Description |
|---|---|
| `open files _items_` | Receives direct objects from Quicksilver. Use this handler if you want an AppleScript Action to accept files from Quicksilver's 1st pane. |
| `open files _items_ with _indirect_items_` | Receives direct objects and indirect objects from Quicksilver. Use this handler if you want an Action to accept files from Quicksilver's 1st pane and also take an item from Quicksilver's 3rd pane (requires the `get argument count` handler). |
| `process text _text_` | Receives text from Quicksilver's 1st pane to process in the AppleScript. |
| `open _items_` | An old handler for sending files to Quicksilver. Should not be used; replaced by the `open files _items_` handler. |

### Returning Items to Quicksilver

At the end of an AppleScript, you can return items to Quicksilver by using `return xxx` in any of the Open Handlers in the table above.

At the moment, you can only return strings, URLs or an array (of strings or URLs), but Quicksilver can inspect these strings and work out what they might be. For example if you return a valid file path, Quicksilver will turn the string into a file object. If you return an email address, Quicksilver will turn it into an email.

An example:

```applescript
using terms from application "Quicksilver"
    on open files _items_
        -- do something with the _items_
        return "AppleScript complete!" -- return a string
    end open files
end using terms
```

## Argument Handlers

Argument handlers tell Quicksilver what the script expects. Quicksilver calls them when it starts up. It then uses that info to decide what types of objects to show the script for and if it should show the third pane.

| Handler Name | Description |
|---|---|
| `get argument count` | Specify whether the AppleScript action uses the 3rd pane or not. If this handler is not present, the value defaults to 1. If you would like to always use the 3rd pane with your Action then `return 2` in this handler. If you would like the third pane to be optional, use `return 3`. |
| `get direct types` | Specify the types of 1st pane objects for which the action displays. |
| `get indirect types` | Specify the types of objects that display in Quicksilver's 3rd pane. Only used if `get argument count` returns `2` or `3`. |

## Customising the Action Icon

To customise the icon of the action, change the AppleScript file's icon. Find the file in Finder, choose "Get Info" (by right clicking or pressing <kbd>⌘</kbd><kbd>I</kbd>), then paste your preferred icon over the icon in the Get Info window.

## Adding Script Actions to Quicksilver

Save your AppleScript file in `~/Library/Application Support/Quicksilver/Actions/My AppleScript Action.scpt` (where `~` is your Home folder) and relaunch Quicksilver.

Once saved, you can search for your action in Quicksilver's 2nd pane, based on the name of the AppleScript file.

## Examples

For examples on how to use these handlers, see the [AppleScript](index.md) page. Also see the [AppleScript Action Templates](templates.md).

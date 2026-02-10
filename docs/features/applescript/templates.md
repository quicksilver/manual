# AppleScript Action Templates

Several templates for AppleScript actions are given here. To learn what they mean and how to use them, see [Custom AppleScript Actions](custom-actions.md).

Note that Quicksilver is fully backwards-compatible with AppleScript actions written using obsolete templates, so those will still work with the latest version of Quicksilver, but they will not benefit from the new features available using the current templates.

## Process files or folders in Quicksilver's first pane

```applescript
using terms from application "Quicksilver"

  on open files direct_objects

  (* Your script goes here *)

  end open files

  --This handler may be omitted if the action accepts all direct object types.
  on get direct types
    return {"NSFilenamesPboardType"}
  end get direct types

end using terms from
```

## Process files or folders with indirect objects (third pane)

```applescript
using terms from application "Quicksilver"

  on open files direct_objects with indirect_objects

  (* Your script goes here *)

  end open files

  on get argument count
    (* Use "return 1" (or omit this entire handler) to never show the third pane.
       Use "return 2" to force the third pane to show.
       Use "return 3" to make the third pane optional. *)
    return 2
  end get argument count

  --This handler may be omitted if the action accepts all direct object types.
  on get direct types
    return {"NSFilenamesPboardType"}
  end get direct types

  --This handler may be omitted if the action accepts all indirect object types.
  on get indirect types
    return {"NSFilenamesPboardType", "NSStringPboardType"}
  end get indirect types

end using terms from
```

## Process text in Quicksilver's first pane

```applescript
using terms from application "Quicksilver"

  on process text direct_object

  (* Your script goes here *)

  end process text

  --This handler may be omitted if the action accepts all direct object types.
  on get direct types
    return {"NSStringPboardType", "Apple URL pasteboard type"}
  end get direct types

end using terms from
```

## Process text with indirect objects (third pane)

```applescript
using terms from application "Quicksilver"

  on process text direct_object with indirect_objects

  (* Your script goes here *)

  end process text

  on get argument count
    (* Use "return 1" (or omit this entire handler) to never show the third pane.
       Use "return 2" to force the third pane to show.
       Use "return 3" to make the third pane optional. *)
    return 2
  end get argument count

  --This handler may be omitted if the action accepts all direct object types.
  on get direct types
    return {"NSStringPboardType", "Apple URL pasteboard type"}
  end get direct types

  --This handler may be omitted if the action accepts all indirect object types.
  on get indirect types
    return {"NSFilenamesPboardType", "NSStringPboardType"}
  end get indirect types

end using terms from
```

## Supported Types

The following type strings can be used with `get direct types` and `get indirect types`:

| Type String | Description |
|---|---|
| `NSFilenamesPboardType` | Files and folders |
| `NSStringPboardType` | Text |
| `Apple URL pasteboard type` | URLs |
| `QSFormulaType` | Formulas |
| `qs.process` | Processes |
| `qs.command` | Commands |
| `QSRemoteHostsType` | Remote hosts |
| `com.apple.itunes.track` | iTunes tracks |

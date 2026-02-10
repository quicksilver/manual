# Property List Overview

Throughout this document are numerous references to things that go in a plug-in's property list. Refer back here if you want to see it all in one place.

## `QSPlugIn`

`author` (string)
: Put your name(s) here.

`description` (string)
: A one-line description of your plug-in's purpose.

`extendedDescription` (string)
: This is what the user will see when they click the Help (?) button in the Plugins section of the preferences. It can be text or HTML (recommended).

`icon` (string)
: This can be anything recognized by `-[QSResourceManager imageNamed:]`, which generally includes full paths, bundle IDs, or resources defined in various property lists. Other occurrences of `icon` in the property list follow this same convention.

`categories` (array)
: This is a list of categories you'd like the plug-in to be listed under. The full list of existing categories can be found under "All Plug-ins" in the Preferences.

`hidden` (boolean)
: This is generally only used by internal plug-ins bundled with Quicksilver. It's a boolean that tells whether or not your plug-in should show up on the list in the preferences.

`relatedBundles` (array)
: This is a list of bundle IDs for applications or plug-ins that are related. If a related bundle is present on the system, the plug-in will be listed in the "Recommended" section of the preferences.

`relatedPaths` (array)
: This is a list of paths for files or folders that might be related to your plug-in. This is useful for plug-ins based on some command-line tool(s) with no associated bundle. The path can be absolute, or use things like `~` to refer to the user's home directory. If a related file or folder is present on the system, the plug-in will be listed in the "Recommended" section of the preferences.

`recommended` (boolean)
: If a plug-in is likely to appeal to nearly everyone (such as Web Search), you can unconditionally add it to the "Recommended" section by setting this to `YES`.

`webIcon` (string)
: You can provide a URL that points to an image here.

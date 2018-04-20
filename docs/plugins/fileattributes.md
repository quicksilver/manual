# File Attribute

File tagging, locking, and visibility.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 2.0.6
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


# File Attribute Plugin

The File Attribute Actions plugin adds actions to Quicksilver that enable you
to alter the attributes of system files on your computer. This includes
tagging, altering the visibility of files and folders, locking files and
folders, and setting icons of files.

The tagging features provide an interface for adding and removing tags on
files, as well as browsing tags and finding all files with a certain tag or
tags.

## Actions

Add Tags…

    Add tags to the selected file(s).
Add to File…

    Apply the selected tag to one or more files in the third pane.
Set Tags…

    Apply tags to the selected file(s), replacing any existing tags.
Remove Tags…

    Remove specific tags from the selected file(s).
Show Tags

    Show a list of tags currently assigned to the selected file(s).
Clear Tags

    Remove all tags from the selected file(s).
Lock/Unlock File

    These actions lock or unlock the file(s) in Quicksilver's 1st pane. Locking a file is equivalent to ticking the 'Lock' checkbox in the 'Get Info' panel of a file, and makes the file or folder read only.
Make Visible (show) & Make Invisible (hide)

    These actions alter the display of files or folders within Finder. Making an item invisible means it does not display in Finder. An example of an invisible folder is the `~/Library` folder.
Set Icon…

    Allows you to alter the icon that is displayed by Finder for the file or folder. To un-set an icon, open the file in Finder and select 'Get Info' (⌘I). From here you can 'delete' the icon.
Clear Custom Icon

    Clears the custom icon set for the selected file(s).

## Catalog

The plugin adds all of the user’s tags to Quicksilver’s catalog. A tag in
Quicksilver is treated like a folder: its children are its contents, accessed
by drilling down into the tag with → or /. A tag’s contents consist of all
files tagged with it, plus every other tag belonging to these files.

### Custom Entries

You can add files to the catalog if they match one or more tags.

  1. Add a new custom catalog entry using the `+` at the bottom of the Catalog preferences.
  2. Select “Tagged Files” from the pop-up menu.
  3. Enter one or more tags in the token field.
  4. Optionally, change the name of the entry in the list.

Files matching all listed tags will be included in the global catalog.

## Search

Use Quicksilver to search for files by tag. Drill down into a tag (with → or
/) to see an alphabetical listing of all files so tagged. At the end of this
list is a list of the other tags for these files. Refine your search by
drilling down into one of these tags and filter even further. With this
mechanism you can arbitrarily extend a query to involve any number of tags.

For example, to see all files tagged with the tag “foo,” bring up the “foo”
tag and drill down into it. Say some of these files are also tagged with
“bar,” and still others, “baz”; these two will be listed at the bottom, after
the list of files. Drilling down into one will further filter the results to
only show files with _both_ tags (files tagged with “foo” and “bar” or files
tagged with “foo” and “baz”). Drilling up out of these results reverts to
showing all files tagged with just “foo”.

When performing such a compound tag query, you can keep track of the current
search by looking at a possible tag’s value: filtering files tagged with “foo”
and then “bar” will show the second tag as “foo + bar” in the command window.
(Note: If your Quicksilver catalog contains Recent Objects, these compound tag
lists will be included, and this may not be the browsing behavior you desire.)

## Working with Tags

All of the expected tagging actions are made available by the plugin. Users
can add tags to files, remove tags from files, set the tags of files to a
different set, clear all tags from files, and show the tags of files. These
actions can be performed on a single file or multiple files, thanks to
Quicksilver’s multiple selection support using the comma key. Tags can be
added to or removed from multiple files at a time, and the user can show all
the tags that a group of files has in common. Showing the tags for a file or
files will bring up a list of the tags in the Quicksilver’s direct object
pane, ready to be explored. A similar interface is used for removing tags from
files, presenting a list of that file’s current tags (or shared tags for
multiple files).

In addition to operating on multiple files, you can use multiple tags in an
operation. A list of appropriate tags should appear in the third pane. You can
enter a new tag by switching to text-entry mode. Multiple tags can be selected
with the comma trick or entered in text-entry mode by separating them with
commas.

Tags can contain almost anything other than comma.

## Event Triggers

If the Event Triggers plug-in is installed, you can configure actions to run
when tags are modified or cleared via Quicksilver. The Event Trigger Object
proxy will refer to the file(s) affected.
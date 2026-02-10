# Documentation and `bltrversion`

Before we get into the technical stuff, make sure you **provide adequate documentation** with any plug-in you create. This also goes for existing plug-ins that you're updating or fixing. Quicksilver plug-ins are notoriously light on documentation and as a result, people don't discover some of their best features for years. If you're not afraid to screw with the code, don't be afraid to screw with the documentation as well.

The best place to document your plug-in is in the `Info.plist` by adding an `extendedDescription` to the `QSPlugIn` section. This should be a string in HTML format.

Keeping documentation up to date is as simple as editing (or creating) `Documentation.mdown` at the root of your project's repository (wherever `$SRCROOT` refers to). This is a Markdown file that should be much easier to deal with than raw HTML in Property List Editor.

It's processed using [Python-Markdown][pymd] with the [extra extension][mdex] enabled, so you can use the usual Markdown syntax, as well as tables, definition lists, etc.

If you need to refer to a Unix command, be aware of OS X's `x-man-page://` URL scheme. For example, linking to `x-man-page://ls` will open the man page for `ls` in a special Terminal window.

### bltrversion

This script is called every time you build your project. A short explanation of what it does and the implications is in order. Every time you build, it will:

  1. Increment the Bundle version in `Info.plist`
  2. Convert `Documentation.mdown` to HTML and insert it into the `extendedDescription`

There are a couple of things to keep in mind.

  * It will not change the "short" version number that the user sees. You'll need to manage that manually.
  * The script unfortunately runs *after* the build, so if you want to update the version or documentation, you need to build, commit, then build again (and most likely revert the additional version bump that will result). This ensures that the built product matches what another developer will find in the repository.
  * Git will almost always show this file as having changed. Don't commit the change unless it's actually what you want.
  * You may have built the thing 250 times since the last commit, but do you really want the build number to jump that far when you were probably just testing some small changes? No. So either manually revert it to the last committed value, or increment it to something reasonable.
  * You can normally install an updated plug-in by double-clicking it in Finder, but it will only replace the old one if it has a higher build number. If you lowered the number recently in order to commit something more reasonable, you might have to manually remove the old version (with a higher build number) before you can install the latest.
  * Python and Objective-C programs unnecessarily escape quotes in property lists, while Property List Editor does not. So if you build to update the documentation, then commit, then make a small change via Property List Editor, you will see a large number of meaningless changes to `Info.plist`. One option is to just build again, reverting the HTML to the previous format.

[pymd]: http://packages.python.org/Markdown/
[mdex]: http://packages.python.org/Markdown/extensions/extra.html

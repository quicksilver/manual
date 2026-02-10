# Scripting Bridge

If you plan to use the Scripting Bridge in your plug-in, here are some tips.

In addition to the steps from [Getting Started](intro.md#getting-started), you'll need two more things in your project:

  1. The Scripting Bridge framework
  2. A header file describing the capabilities of the application you want to script

The framework is included with OS X and can be added like any other. For the header file, there are two ways to proceed: Generate the file and add it to the project, or have the file generated automatically when you build the plug-in.

The automatic way means you'll always have the latest header if something changes, but it's more complicated to set up, it makes searching the project more difficult, and you may get changes you didn't want.

Both methods are described here. Choose only one.

## Adding the Header Manually

To create the header file, you'll want to run `sdef` on the application in question, then pipe its output to `sdp` and define a base name for all the classes. (The base name is usually the application's name with no whitespace.)

For example, to create a header for scripting Safari:

    sdef /Applications/Safari.app  | sdp -fh --basename Safari

This will create `Safari.h` in the current directory. Add that file to your plug-in project in Xcode, and you'll be able to import it from any one of your files.

## Generating the Header During Build

  1. Drag the application(s) you want scripting support for into your project. Don't let it copy the files.
  2. Use the Utilities panel to change the location for each application to "Absolute Path".
  3. Select the project on the left, then select the target (under TARGETS) on the right.
  4. Open the "Build Phases" tab.
  5. Drag the application(s) to the "Compile Sources" section and make sure it's the first thing on the list.
  6. Go to the "Build Rules" tab.
  7. Add a new build rule, set Process to "Source files with names matching" and enter `*.app`
  8. Select "Custom script" and enter this command:
  
        sdef "$INPUT_FILE_PATH" | sdp -fh -o "$DERIVED_FILES_DIR" --basename "$INPUT_FILE_BASE"	--bundleid `defaults read "$INPUT_FILE_PATH/Contents/Info" CFBundleIdentifier`
  
  9. Add an output file with the path `$(DERIVED_FILES_DIR)/$(INPUT_FILE_BASE).h`
  10. Add a line to import the resulting header file to the appropriate header files in your project. For example, if you added Safari, you'd enter:
  
        #import "Safari.h"
        
      This file won't exist until you build for the first time.

## Overview

Scripting Bridge is typically an excellent way to get information from an application, but a terrible way to control it. Unfortunately, for Quicksilver you basically need the opposite.

Keep in mind at all times that in order to interact with an application via Scripting Bridge, the application must be running. As a result, you should not use it to add objects to the catalog. Users will not appreciate applications launching seemingly at random (when Quicksilver updates the catalog entry). You need to find another way to get the same info (typically by parsing files on disk somewhere).

The type of objects Scripting Bridge is appropriate for is real-time items from an application, like "currently playing track", or "all open tabs". In most cases such as this, you should check `[appname isRunning]` before trying to get the information.

When defining actions on the other hand, it's generally OK to blindly interact with the application. For instance, if the user wants to play a track, it makes sense to open iTunes if it isn't already running.

## Performance

I won't try to repeat what's in the [official documentation][sbdoc], but you should look it over. It's not very long. In particular, see the sections on Using Element Arrays and improving performance. The general rule is: Minimize the number of Apple Events.

Having said that, there are exceptions I've run across, so you might have to get creative.

## Weirdness

There are some strange things you're going to run across. Here are some known examples.

### get

You generally don't need to call `get` on an `SBObject` or `SBElementArray`… except when you do. My advice is to avoid it unless something that seems like it should work just isn't working. Then add a call to `get`. One known example is when trying to use FourCharCodes in an `NSPredicate`. This should work, but doesn't:

    NSArray *iTunesDJplaylists = [[library playlists] filteredArrayUsingPredicate:[NSPredicate predicateWithFormat:@"specialKind == %i", iTunesESpKPartyShuffle]];

This works:

    NSArray *iTunesDJplaylists = [[[library playlists] get] filteredArrayUsingPredicate:[NSPredicate predicateWithFormat:@"specialKind == %i", iTunesESpKPartyShuffle]];

If the predicate just uses strings, it seems to work fine without `get`. Huh?

### SBElementArray

An `SBElementArray` (according to the documentation) is just an `NSMutableArray` and can be treated like one… except when it can't (which of course is *not* documented). In my experience, you can remove all objects or remove specific ones, but adding objects is problematic. It almost never works, but when it does, it seems to require something like

    [array insertObject:newThing atIndex:0];

My only advice is to start searching the web for answers when you get into this situation.

[sbdoc]: http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptingBridgeConcepts/Introduction/Introduction.html

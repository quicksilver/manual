# Troubleshooting

If things aren't working as expected, here are some things to try.

## Console.app

This should be your first stop. If the plug-in failed to load, it will tell you why.

## Debugging

If you're running Quicksilver from Xcode (see [Getting Started](intro.md#getting-started)), you can set breakpoints in your code. They should work. If they don't, make sure "Load Symbols Lazily" is unchecked in Quicksilver's Build Settings.

## Wrong Version

If your changes aren't showing up, you might be running the wrong version of the plug-in.

  1. Quit Quicksilver
  2. Clean your target in Xcode (Product → Clean)
  3. Go to `~/Library/Application Support/Quicksilver/PlugIns`
  4. Move any copies of your plug-in to the Trash
  5. Build and Run from Xcode

## Build Clean

If you're getting weird errors about headers not being found, or syntax errors in files you haven't touched, or linking errors, do a clean build. 

If that doesn't work, go to the Organizer and delete the Derived Data for the project.

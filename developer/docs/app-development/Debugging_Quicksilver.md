# Debugging Quicksilver

### Disabling the Catalog

If you want to run Quicksilver with the catalog disabled, hold down the
SHIFT key whilst starting Quicksilver. This will give you an NSLog in
the console saying 'Catalog Disabled'

### Testing an Old Version of Quicksilver

The oldest commit that is *easily* build-able, is commit
[33022115](https://github.com/quicksilver/Quicksilver/tree/33022115be10ddb169e33fef6e0a8d351305e4c9).
In order to build this version of Quicksilver, there are a few tasks you
must first complete.

-   First, checkout the commit using

<!-- -->

    git checkout -f 33022115be10ddb169e33fef6e0a8d351305e4c9

-   Download these six files (easiest if you right click -\> 'Save
    linked file as...'):
    [1](http://google-toolbox-for-mac.googlecode.com/svn/trunk/AppKit/GTMCarbonEvent.h),
    [2](http://google-toolbox-for-mac.googlecode.com/svn-history/r307/trunk/AppKit/GTMCarbonEvent.m),
    [3](http://google-toolbox-for-mac.googlecode.com/svn/trunk/GTMDefines.h),
    [4](http://google-toolbox-for-mac.googlecode.com/svn-history/r205/trunk/Foundation/GTMObjectSingleton.h),
    [5](http://google-toolbox-for-mac.googlecode.com/svn-history/r100/trunk/DebugUtils/GTMDebugSelectorValidation.h),
    [6](http://google-toolbox-for-mac.googlecode.com/svn-history/r400/trunk/DebugUtils/GTMTypeCasting.h),
    and place them in:

<!-- -->

    QS_ROOT/Code-External/GMTClasses/

-   Within XCode, search for \`QSKeyMap...\` and delete the two .h and
    .m files in red
-   Again, within XCode, search for \`QSModifierKeyHandler...\` and
    delete the two .h and .m files in red
-   Open up GMTDebugSelectorValidation.h and delete lines 31, 93, 99
    (related to \#if DEBUG)
-   Open up GMTCarbonEvent.h and delete lines 399-413
-   Clean the targets
-   Build the \`Quicksilver Distribution\` target in the Debug state.

You can now test an ancient version of Quicksilver, and use

    git bisect

**But be warned: Make sure you keep a copy of the GMTClasses folder when
changing commits so you don't have to do all of this all over again**

Commits older than this will be more difficult to build, since they use
.nib files instead of .xib files, and it would involve either converting
all the .xibs back to .nibs or downloading all the original .nibs.

## Debugging Plugins

Debugging Quicksilver plugins requires a little more work than just
clicking "Build and Debug" in XCode. There are step-by-step instructions
in the [Plugin Development
Reference](https://github.com/quicksilver/PluginDevelopmentReference/blob/master/QuicksilverPlug-inReference.md#debugging-plug-ins)
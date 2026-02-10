# Building Quicksilver

1.  Clone the repository from GitHub with
    `git clone --recursive `[`https://github.com/quicksilver/Quicksilver.git`](https://github.com/quicksilver/Quicksilver.git)
2.  Change to the newly created 'Quicksilver' folder by typing
    `cd Quicksilver`
3.  Pull in the submodules with
    `git submodule init; git submodule update`
4.  Open the project in Xcode
5.  Select the “Quicksilver Distribution → My Mac 64-bit” scheme in the
    upper left corner (next to the Stop button) if it’s not selected by
    default.
6.  Run Product \> Build or hit ⌘B

Everything you build should end up in `/tmp/QS/build/`.

### Running/Debugging in Xcode

1.  First of all let's make sure Xcode is setup to properly run
    Quicksilver
    1.  Choose Product \>\> Schme \>\> Edit Scheme...
    2.  Click on Run on the left
    3.  Then for the Executable select "Quicksilver.app"
    4.  The result should look like this:
        <img src="XcodeEditScheme.png" title="XcodeEditScheme.png" width="200"
        alt="XcodeEditScheme.png" />
2.  Next click Product \>\> Run to run Quicksilver

If using “Run” with the Release configuration, you might end up with an
unresponsive app. This is likely to happen under the following
conditions:

1.  Quicksilver is configured to hide its Dock icon
2.  You’re building for the the first time (or after doing a Clean)

If the “Stop” button in Xcode is grayed out, that’s a clue that
something went wrong. Use Activity Monitor to quit the Quicksilver
process then “Run” again. It should work for this and all subsequent
builds until you start fresh again.

You’re better off using the Debug configuration when doing “Run”, as it
knows not to relaunch the app.

### Avoiding Repetitive Permissions Popups

Normally, every time you build QS, you will have deal with a pop-up requesting permissions for things like your contacts, calendars, full-disk access, etc.
This is in part because every time the code changes, the resulting binary also changes, and so Xcode and Apple's codesigning treat it as potentially untrusted and a potential security risk.
This becomes really tedious when doing development work; as a workaround, one can run a script to set up a local self-signed certificate and use this for signing, which remembers the permissions across different builds:

```bash
bash Quicksilver/Tools/codesign/setup_cert.sh
```

Every once in a while (perhaps after Xcode or macos updates), this process may break or give errors such as:

```
XXXX: no identity found
Command CodeSign failed with a nonzero exit code
```

In this case, you may be able to get things working again by:

1. Re-run the `setup_cert.sh` step from above
1. `clean` the project within Xcode 
1. Remove the QS temporary directory: `rm -rf /tmp/QS`
1. Try building again

For debugging, one can view the known certificates with:

```bash
security find-identity -p codesigning
```

The one named `Local Self-Signed` is the one produced by the script above.

### Signing for Gatekeeper

Signing an application for Gatekeeper requires setting the Code Signing
Identity in the project's build settings. For security reasons we do not
share the Code Signing Identity, but instead set it with an environment
variable.

A build script located in `Quicksilver/Tools/qsrelease` manages the
release build process.

This script will

1.  Run all unit tests (this requires `xctool` to be installed on your
    system)
2.  Set the Code Signing Identity
3.  Choose the correct configuration and scheme
4.  Clean files from previous builds
5.  Build Quicksilver
6.  Verify that Gatekeeper accepts the resulting application
7.  Create a DMG containing the application
8.  Open the target folder in Finder to show the results of the build

### Macports

You can also install Quicksilver via
[Macports](http://www.macports.org/), a package management system for OS
X. You'll need to install the Xcode package and [Macports
itself](http://www.macports.org/install.php), but then you can build and
install Quicksilver from source just by running

`sudo port install quicksilver`

You can use this as a sanity check to be sure that your environment is
able to build Quicksilver. You can also inspect what Macports is doing
by adding a `-d` debug flag to the command or by running
`port edit quicksilver` to view the Portfile (Macports configuration
file).

**Please note:** This method is no longer supported for Quicksilver as
it does not deal with `git submodules`

### Layperson's Guide

For all the non-coding QS users out there, here's a further breakdown of
building the latest QS.

1.  Install Xcode from the Mac App Store.
2.  Make sure there's no other Quicksilver apps on the system by zipping
    older versions and deleting the apps the zips originated from, then
    emptying the Trash.
3.  See
    <http://qsapp.com/wiki/Github#Adding_the_Quicksilver_Remote_Repository>
    for info about downloading the latest QS build project.
4.  Open the Quicksilver.xcodeproj with XCode.
5.  Using the Scheme drop-down at the top of the window, choose
    'Quicksilver Distribution → My Mac 64-bit' and click ‘Build’ (or hit
    ⌘B).
6.  Quit your normal copy of Quicksilver.
7.  In Xcode, click 'Run' in the toolbar.

A ‘Product -\> Clean’ (or ⇧⌘K) should be performed if you're
experiencing crashes or problems. Also try deleting the folder `/tmp/QS`
before building again.

If the build still crashes regularly, move all of these paths before
trying a new build:

-   \~/Library/Application Support/Quicksilver/Plugins
-   \~/Library/Preferences/com.blacktree.Quicksilver.plist
-   \~/Library/Caches/com.blacktree.Quicksilver/
-   \~/Library/Caches/Quicksilver/

then move them back one at a time before trying again. When a replaced
folder causes a crash, repeat the process for the contained folders, and
so on.

If Quicksilver seems stable, and to get the full benefits of the app:

1.  “Clean”
2.  In the “Edit Scheme…” menu item on the Product menu, change the
    Build Configuration to “Release”
3.  Build as before.
4.  Copy the app in `/tmp/QS/build/Release` to `/Applications`
5.  Run as a normal app from `/Applications`

This process will overwrite any Quicksilver app you (shouldn't) have in
`/Applications`.
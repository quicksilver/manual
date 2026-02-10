When releasing a new version of Quicksilver, the following steps should
be taken.

## All Releases

-   Make final decision what's going in the new version (discuss it in
    the Dev groups)
-   Update any pulled .strings files in the Xcode proj (See
    [Localization](../app-development/Localization.md) for more info)
-   Make sure you have pulled the latest changes from upstream
    (`git pull --rebase origin main`)
-   Update the Quicksilver version in `Developer.xcconfig`
-   Commit any final changes (e.g.
    `git commit -am "Version bump for release 2.2.0`)
-   Add a tag for the release (e.g.
    `git tag -a "v2.2.0" -m "Version 2.2.0 of Quicksilver, for full list of changes, see: `[`https://github.com/quicksilver/Quicksilver/releases/`](https://github.com/quicksilver/Quicksilver/releases/)`"`
-   Push the code and to main `git push origin main` and
    `git push origin TAG_NAME`
-   Wait for GitHub actions to build a signed build and create a
    release: [1](https://github.com/quicksilver/Quicksilver/releases/)
-   Download this newly built Quicksilver and ensure it runs as you
    expect (works correctly, version numbers correct etc.)
-   Edit the 'Release' automatically created by github to add any additional release notes
-   Upload the .dmg to /qs0/plugins/admin/add.php along with the
    Info.plist (the Info.plist comes from within Quicksilver.app)
    **NOTE: Make sure to tick the 'Application update' checkbox!**

## Final Releases

-   Alter the app's 'release type' in the Plugins Admin page
-   Announce on users list and Twitter
-   Promote new release (e.g. inform mac news sites: Macrumors, Life
    Hacker, Mac Update, I Use This, Twitter, Mac Apper, Soft Pedia,
    upgradeosx, TUAW, makeuseof, Macworld, appleinsider, cultofmac.com,
    mashable.com, mactrast, gigaom, mac.appstorm, theNextWeb, MacNN, All
    Things D, [Slashdot](http://apple.slashdot.org/))
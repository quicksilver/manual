# Hidden Defaults

Quicksilver contains many hidden preferences which can be edited by entering a command with the following format into Terminal.app. Alter the "Setting Name" and "Value" parts of the command depending on the preference you would like to change:

    defaults write com.blacktree.Quicksilver "Setting Name" Value

An example:

    defaults write com.blacktree.Quicksilver "QSLoadImagePreviews" NO

Some settings take an array. For example, to enable previews only for images, video, and audio files:

    defaults write com.blacktree.Quicksilver QSFilePreviewTypes -array public.image \
    public.movie public.audio com.adobe.pdf

## Available Settings

| Setting Name                                   | Value                   | Description                                                                                                                                                                                                                                                  |
|------------------------------------------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Delay Before Quitting`                        | YES or NO               | Enable the "Hold <kbd>⌘</kbd><kbd>Q</kbd> to quit" dialogue (YES) or disable it (NO)                                                                                                                                                                         |
| `QSLoadImagePreviews`                          | YES or NO               | Enable the loading of icon previews (YES) or disable it (NO)                                                                                                                                                                                                 |
| `QSFilePreviewTypes`                           | an array of UTI strings | Fine-tune which file types get previews for aesthetic or performance reasons. Only applies if `QSLoadImagePreviews` is enabled.                                                                                                                              |
| `Show Release Notes on Upgrade`                | YES or NO               | Show the release notes when Quicksilver is updated (YES)                                                                                                                                                                                                     |
| `QSUpdateWithoutAsking`                        | YES or NO               | Allow Quicksilver to install app updates and plugin updates automatically, and restart without asking the user (YES) or to ask the user always (NO)                                                                                                          |
| `QSIgnorePlugInBundleRequirements`             | YES or NO               | Ignore bundle, application, path, framework, Quicksilver version, and OS version requirements when loading plug-ins. (This is not recommended.) Architecture incompatibilities and dependencies on other plug-ins will still prevent a plug-in from loading. |
| `QSRestartAutomaticallyWithoutCrashReporter`   | YES or NO               | Sets whether the crash reporter is shown when Quicksilver restarts after a crash. Set it to YES to hide the crash reporter.                                                                                                                                  |
| `QSPasteboardHistoryIsVisible`                 | YES or NO               | Display the Clipboard History window when Quicksilver is launched (YES) or hide it (NO).                                                                                                                                                                     |

You can also adjust many of the YES/NO settings by installing the [Secrets](http://secrets.blacktree.com) preference pane.

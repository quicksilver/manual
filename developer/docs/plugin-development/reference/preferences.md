# Preferences

This is a rough outline of what you need to do to add a preference pane for your plug-in.

  * add a new user interface file with a single window
  * uncheck Visible At Launch in the Attributes inspector
  * uncheck Release When Closed in the Attributes inspector
  * add a class to your project such as `QSBlahPrefPane` that inherits from `QSPreferencePane`
  * set File's Owner to be `QSBlahPrefPane`
  * connect the window to `_window` on File's Owner
  * add something like this to the plist under `QSRegistration`:
  
        <key>QSPreferencePanes</key>
        <dict>
            <key>QSBlahPrefPane</key>
              <dict>
                  <key>class</key>
                  <string>QSBlahPrefPane</string>
                  <key>name</key>
                  <string>Blah Blah Blah</string>
                  <key>description</key>
                  <string>Preferences</string>
                  <key>icon</key>
                  <string>QSBlahImage</string>
              </dict>
        </dict>
  
  * add your controls to the window and bind them to the right preferences (Shared Preferences Controller → values → QSBlahSetting)

   **Note:** You can create clickable href-links to your preference pane using the format `qs://<MyPreferencePaneClass>` that link directly to your preference pane. E.g. if your preference pane class is called `QSBlahPrefPane`, the link `qs://QSBlahPrefPane` will take you directly to your preference pane. This can be useful for linking users to the preference pane from websites, or opening the preference pane from within your plugin using `[[NSWorkspace sharedWorkspace] openURL:[NSURL UrlWithPath:@"qs://QSBlahPrefPane"]];`

# Object Source Preferences

  * add a new user interface file with a single view
  * uncheck Use Auto Layout in the File inspector
  * set File's Owner to `QSBlahSource`
  * bind File's Owner `settingsView` to the new view
  * create controls and bind them to outlets/actions in File's Owner
  * add a strings file to the project called `QSObjectSource.name.strings` (or set the name as the key under `QSObjectSources` if it won't be localized)

You'll need to add at these methods to `QSBlahSource`.

Make this source appear on the drop-down for adding new catalog entries:

    - (BOOL)isVisibleSource
    {
        return YES;
    }

Return the icon that will appear next to the source name in the drop-down and next to custom entries:

    - (NSImage *) iconForEntry:(NSDictionary *)theEntry
    {
        // this can be smarter based on theEntry - up to you
        return [QSResourceManager imageNamed:@"GenericDocument"];
    }

Load your custom view:

    - (NSView *)settingsView
    {
        if (![super settingsView]) {
            [NSBundle loadNibNamed:NSStringFromClass([self class]) owner:self];
        }
        return [super settingsView];
    }

Update the view every time the selection changes:

    - (void)populateFields
    {
        NSMutableDictionary *settings = [[self currentEntry] objectForKey:kItemSettings];
        // set values for controls in the view based on settings
    }

To customize the name of the source in the drop-down, add something like this to the `strings` file:

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
    	<key>QSBlahSource</key>
    	<string>Blah Source</string>
    </dict>
    </plist>

And of course you need to make sure you update or create the catalog entry when changes are made in the interface. See `QSFileSystemObjectSource` for an example.

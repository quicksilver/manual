# Trigger Presets

Your plug-in can provide pre-defined triggers. These go under `QSTriggerAdditions` and look something like this:

    <key>ID</key>
    <string>QSiTunesNextSongTrigger</string>
    <key>command</key>
    <string>QSiTunesNextSongCommand</string>
    <key>defaults</key>
    <dict>
      <key>characters</key>
      <string></string>
      <key>keyCode</key>
      <integer>124</integer>
      <key>modifiers</key>
      <integer>9961768</integer>
      <key>type</key>
      <string>QSHotKeyTrigger</string>
    </dict>
    <key>name</key>
    <string>Next Song</string>
    <key>set</key>
    <string>iTunes</string>

Only the type is required under `defaults` if you don't want to specify a shortcut. The `set` refers to the name of a group in the Trigger preferences. To create a new group for your plug-in's triggers, add something like this under `QSRegistration` → `QSTriggerSets`:

    <key>QSBlah</key>
    <dict>
      <key>icon</key>
      <string>GenericDocument</string>
      <key>name</key>
      <string>Blah</string>
    </dict>

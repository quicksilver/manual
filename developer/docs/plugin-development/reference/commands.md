# Commands

A `QSCommand` is something that contains a direct object, an action, and an indirect object. In other words, it encapsulates something you would normally put together in Quicksilver's interface.

Commands can be created by users (using the ⌃↩ "encapsulate" keystroke), by code (using methods from the `QSCommand` class), and in a plug-ins `Info.plist` (Under `QSRegistration` → `QSCommands`). Triggers refer to commands for obvious reasons.

One thing to note is that commands don't require either a direct or indirect object. For example, the iTunes plug-in comes with a number of predefined triggers like "Play", "Increase Volume", "Increase Rating", etc. These always do the same thing. There's no need to specify an object for them to act on. As a result, the commands these triggers refer to contain only an action.

When defining commands in the property list, the contents will vary greatly depending on the `actionID`. The `actionID` can refer to any action, but there are only a few that make sense. Below are examples of three common types.

For commands that call an Objective-C method somewhere, use "QSObjCSendMessageAction":

    <key>QSiTunesMute</key>
    <dict>
      <key>command</key>
      <dict>
        <key>actionID</key>
        <string>QSObjCSendMessageAction</string>
        <key>directArchive</key>
        <dict>
          <key>data</key>
          <dict>
            <key>qs.action</key>
            <dict>
              <key>actionClass</key>
              <string>QSiTunesControlProvider</string>
              <key>actionSelector</key>
              <string>volumeMute</string>
              <key>icon</key>
              <string>iTunesIcon</string>
              <key>name</key>
              <string>Mute</string>
            </dict>
          </dict>
        </dict>
        <key>directID</key>
        <string>QSiTunesVolumeMute</string>
      </dict>
    </dict>

**Be sure the key and `directID` are not the same.**

For commands that should invoke Quicksilver, and allow searching a specific subset of objects, use "QSObjectSearchChildrenAction":

    <key>QSiTunesSearchArtists</key>
    <dict>
      <key>command</key>
      <dict>
        <key>actionID</key>
        <string>QSObjectSearchChildrenAction</string>
        <key>directArchive</key>
        <dict>
          <key>data</key>
          <dict>
            <key>com.apple.itunes.qsbrowsercriteria</key>
            <dict>
              <key>Result</key>
              <string>Artist</string>
              <key>Type</key>
              <string>Artist</string>
            </dict>
          </dict>
        </dict>
      </dict>
      <key>name</key>
      <string>Search Artists</string>
    </dict>

For commands that are handled by an AppleScript file somewhere, use "AppleScriptRunAction":

    <key>QSiTunesMute</key>
    <dict>
      <key>command</key>
      <dict>
        <key>actionID</key>
        <string>AppleScriptRunAction</string>
        <key>directResource</key>
        <dict>
          <key>bundle</key>
          <string>com.blacktree.Quicksilver.QSiTunesPlugIn</string>
          <key>path</key>
          <string>Contents/Resources/Scripts/Mute.scpt</string>
        </dict>
      </dict>
    </dict>

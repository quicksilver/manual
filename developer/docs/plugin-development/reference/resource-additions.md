# QSResourceAdditions

You can define short names here to use with `QSResourceManager`. This is most useful to refer to icons buried inside a bundle somewhere (including your own plug-in's bundle). It can also be used to refer to the absolute path of an image file. For example:

    <key>QSResourceAdditions</key>
    <dict>
      <key>QSBlahImage</key>
      <dict>
        <key>bundle</key>
        <string>com.qsapp.QSBlah</string>
        <key>resource</key>
        <string>SomeImage.png</string>
      </dict>
      <key>QSBlahAnotherImage</key>
      <string>/Absolute/Path/to/an/Image.png</string>
    </dict>

Since icons have a history of moving around or disappearing with various OS X updates, you also have the ability to assign "fall back" values for each resource. Instead of referring directly to a dictionary or a string, refer to an array of them. You can mix strings and dictionaries. For example:

    <key>QSResourceAdditions</key>
    <dict>
      <key>QSBlahImage</key>
      <array>
        <dict>
          <key>bundle</key>
          <string>com.qsapp.QSBlah</string>
          <key>resource</key>
          <string>SomeImage.png</string>
        </dict>
        <string>/Absolute/Path/to/an/Image.png</string>
      </array>
    </dict>

The identifier for a resource defined here can be used as the value for any `icon` in the plist, and it can be used in code:

    [object setIcon:[QSResourceManager imageNamed:@"QSBlahImage"]];

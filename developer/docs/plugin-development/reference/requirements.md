# QSRequirements

You can define prerequisites and other restrictions for your plug-in. Most of these, if not met, will prevent an installed plug-in from loading, but many of them should tell the on-line update system not to even *offer* the plug-in in the user's list for installation.

minHostVersion (string)
  : The minimum version (build number) of Quicksilver required by this plug-in. Note: this replaces the now obsolete 'version (string)' key

maxHostVersion (string)
  : The maximum version (build number) of Quicksilver this plug-in will work with.

osRequired (string)
  : The minimum version of OS X required to use the plug-in. Use this to prevent the plug-in from loading on an older OS. You can write the version as `10.x.x` or just `10.x`.

    If you use this, you should also require Quicksilver build 4005 or higher, as older versions of Quicksilver will not respect the OS version restrictions.

osUnsupported (string)
  : The version of OS X at which this plug-in will stop working. Use this to prevent the plug-in from loading on a newer OS. You can write the version as `10.x.x` or just `10.x`.

    If you use this, you should also require Quicksilver build 4005 or higher, as older versions of Quicksilver will not respect the OS version restrictions.

plugins (array)
  : A list of dictionaries describing other plug-ins required by this one. For example:

        <key>plugins</key>
        <array>
          <dict>
            <key>id</key>
            <string>com.blacktree.Quicksilver.QSChatSupport</string>
            <key>name</key>
            <string>Chat Support</string>
          </dict>
        </array>

    These plug-ins will be installed automatically to support your plug-in.

bundles (array)
  : A more general list of things that must be installed before this plug-in will load. You can also require a minimum version of the bundle. For example:

        <key>bundles</key>
        <array>
          <dict>
            <key>id</key>
            <string>ch.sudo.cyberduck</string>
            <key>name</key>
            <string>Cyberduck</string>
            <key>version</key>
            <string>3.8</string>
          </dict>
        </array>

paths (array)
  : A list of strings defining files or folders that must exist for this plug-in to load.

frameworks (array)
  : Require specific frameworks and versions. For example:

        <key>frameworks</key>
        <array>
          <dict>
            <key>id</key>
            <string>com.skype.skypeframework</string>
            <key>name</key>
            <string>Skype Framework</string>
            <key>resource</key>
            <dict>
              <key>bundle</key>
              <string>com.skype.skype</string>
              <key>path</key>
              <string>/Contents/Frameworks/Skype.framework</string>
            </dict>
            <key>version</key>
            <string>0.1</string>
          </dict>
        </array>

obsoletes (array)
  : An array of bundle identifiers (strings) for plug-ins that are made obsolete by this one. For example:

        <key>obsoletes</key>
        <array>
          <string>com.blacktree.Quicksilver.QSAirPortPlugIn</string>
          <string>com.blacktree.Quicksilver.QSNetworkLocationPlugIn</string>
        </array>

    The update system will alert users with the obsolete plug-ins that your plug-in is available (and what it replaces). You could also use the `obsoletes` key to change the bundle identifier for an existing plug-in, but care should be taken in using it for this purpose.
  
    To use the `obsoletes` key, you should also require Quicksilver version 3926 or higher.

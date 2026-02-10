# `QSRegistration`

This section gives Quicksilver additional information about your plug-in.

## `QSTypeDefinitions`

This allows your custom type(s) to appear in the Actions section of the preferences. Any new types provided by your plug-in should be described here. The key is the name of a type as defined in your code. Each entry should have two children: `name` and `icon`.

An optional key available starting in Quicksilver build 4012 is `smartspace`. The value for `smartspace` should be an integer from 1 to 6. (Set the type to "Number".) You only need to define this if the default smart spacebar behavior is undesirable for this type of object.

What is the default behavior?

  * If in the second pane, select the first action that takes an argument in the third pane
  * If user is holding Shift, go to the parent (same as left arrow)
  * If the object has children, show them (unless it's a text file)
  * Jump to the third pane if the current action requires it
  * Quick Look if the object supports it
  * Switch to text mode

The available override values and their behaviors are:

  * 1 - type a space
  * 2 - next result (act like down arrow or ⌃J)
  * 3 - jump to argument field (third pane)
  * 4 - switch to text-entry mode
  * 5 - show children (act like right arrow or slash)
  * 6 - Quick Look

## `QSBundleChildHandlers`

This lists bundles that should have children provided by your plug-in. (Generally this is used to allow right-arrowing into an existing application like Mail or Address Book.) The key should be the bundle ID, and the value should be the name of a class that contains a `loadChildrenForObject:` method.

## `QSApplicationActions`

These are actions that only appear when a specific application is in the first pane. The key should be the bundle ID of the application. Under this is a dictionary of actions. See the iTunes module for an example.

## `QSProxies`

This defines proxy objects provided by the plug-in. Example:

    <key>QSProxies</key>
    <dict>
      <key>QSBlahProxyObject</key>
      <dict>
        <key>icon</key>
        <string>GenericDocument</string>
        <key>name</key>
        <string>Current Blah Thing</string>
        <key>providerClass</key>
        <string>QSBlahSource</string>
        <key>types</key>
        <array>
          <string>NSStringPboardType</string>
        </array>
      </dict>
    </dict>

Omitting the icon or setting its value to "ProxyIcon" will cause the proxy object to take on the icon of the resolved object.

## `QSTriggerEvents`

Your plug-in can post notifications that can be used to signal an event trigger. In order to add these notifications to the Event Triggers pop-up menu, you need to define them here. `QSTriggerEvents` is a dictionary. Each key is the name of a notification. The value is another dictionary with these keys:

`name`
  : The name that will appear in the pop-up menu.

    For events generated exclusively by Quicksilver, you should add `☿` after the name. For example, the "File Tagged" event will not be detected when files are tagged in Finder; only when the tags are modified by a Quicksilver action. So the name is shown as "File Tagged ☿".

`type`
  : The category or group that this "event" will be under in the menu.

`icon`
  : The icon that will appear next to the item in the pop-up menu.

`provider`
  : The name of the class that posts the notification.

`allowMatching`
  : Whether or not the match/ignore controls for triggers using this event should be enabled. If you plan on passing something specific as the Event Trigger Object, this should probably be `YES`.

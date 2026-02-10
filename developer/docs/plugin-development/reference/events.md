# Event Triggers

Any plug-in can define additional "events" to be monitored by the Event Triggers plug-in. There are a couple of reasons you might post a notification from a plug-in:

  1. Your plug-in does something that takes a long time. Particularly if it does it in the background.
  2. The result of some command might be useful in a follow-up command. (More on the Event Trigger Object later.)
  3. Your plug-in does something atypical *automatically* in the background.

To set this up correctly, you need an entry in `Info.plist` and some code to post the notification. A typical property list entry looks like this:

    <key>QSBlahThingHappened</key>
    <dict>
    	<key>name</key>
    	<string>Operation Finished ☿</string>
    	<key>icon</key>
    	<string>IconName</string>
    	<key>provider</key>
    	<string>QSBlahSource</string>
    	<key>type</key>
    	<string>Blah</string>
    </dict>

See [QSTriggerEvents](registration.md#qstriggerevents) for details.

Posting the notification should look something like this:

    NSDictionary *info = @{@"object": someQSObject};
    [[NSNotificationCenter defaultCenter] postNotificationName:@"QSEventNotification" object:@"QSBlahThingHappened" userInfo:info];

The object passed with the notification should be a string matching the key name defined in the property list.

`userInfo` can be `nil`, but if you pass anything, it should be a dictionary containing a `QSObject` for the key "object". The Event Triggers plug-in includes a proxy object called "Event Trigger Object". You can use that in an event trigger to refer to the `QSObject` included in `userInfo`. This potentially allows for powerful combinations of commands.

If you don't pass anything, the Event Trigger Object will just be a string object based on the event's name.

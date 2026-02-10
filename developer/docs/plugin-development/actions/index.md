# Actions Overview

To add an action, there are two basic steps:

  1. Define the action in `Info.plist`
  2. Write the action's code

You'll define your actions in the [`QSActions` section](properties.md) of the property list.

    <key>QSActions</key>
    <dict>
        <key>someExmapleAction</key>
        <dict>
            <key>actionClass</key>
            <string>QSBlahActionProvider</string>
            <key>actionSelector</key>
            <string>performActionOnObject:</string>
            <key>directTypes</key>
            <array>
                <string>QSBlahType</string>
            </array>
            <key>name</key>
            <string>Blah Example Action</string>
        </dict>
    </dict>

That's the bare minimum. There are several additional keys described in the [Action Properties](properties.md).

For the code, you'll have something like this:

    - (QSObject *)performActionOnObject:(QSObject *)dObject
    {
        NSLog(@"I'm doing something with %@", [dObject stringValue]);
        id theMeat = [dObject objectForType:QSBlahType];
        return nil;
    }

An action that expects and object in the third pane will have an `actionSelector` like `performActionOnObject:withObject:` and the code will look more like this:

    - (QSObject *)performActionOnObject:(QSObject *)dObject withObject:(QSObject *)iObject
    {
        NSLog(@"Sending %@ to %@", [dObject stringValue], [iObject stringValue]);
        return nil;
    }

An action should **always** be defined to return a `QSObject`, even if it never needs to return anything. A `(void)` action will crash Quicksilver. Actions aren't typically defined in your action provider's header file, but they can be if it makes you more comfortable.

## Direct and Indirect Objects

You may see references to direct and indirect objects. Basically, direct objects are the things in the first pane of Quicksilver's interface and indirect objects are the thing in the third pane.

If you're looking at existing code, these are usually referred to as `dObject` and `iObject`. You don't have to use these names, but it will save you some typing if you plan to copy and paste a lot from examples.

## Displaying Results

Something to note about the `displaysResult` option in `Info.plist`: This only means that Quicksilver will pop the interface back up *if* your action returns a `QSObject` to it. If you have an action that may or may not return something to the interface, it appears to be safe to enable this.

Also note that if your action returns a `QSObject` to Quicksilver, that *will* become the thing in the first pane, whether the UI is re-displayed or not. If not, the user will see the object you returned the next time he invokes Quicksilver.

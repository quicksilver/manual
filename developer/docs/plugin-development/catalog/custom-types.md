# Custom Types

You may want to add a new type of thing to Quicksilver's catalog that doesn't conform to the existing types Quicksilver knows about. The main reason you'd want to do this is to make your actions apply only to relevant entries. For instance, you may want "SSH to host" as the default for remote hosts. Though hostnames and FQDNs are just strings and can be added to Quicksilver easily, simply adding them to the catalog as strings would cause the default action to be "Open URL" or "Large Type" in most cases. You would either have to choose the SSH action manually every time, or move it up in priority making it the default for all text and URLs, which probably isn't what you want.

## Source

To use a custom type when adding objects to the catalog, the first thing to do is add something like this to one of your header files:

    #define QSBlahType @"blah.specific.type"

You'll probably want to use this in your action code too, so many plug-ins define things like this in a dedicated file, rather than in the object source.

Then, in your `objectsForEntry:` method in `BlahSource.m`, you would do something like this on each QSObject before adding it to the array:

    [myObject setObject:someValue forType:QSBlahType];

Now, when you're adding actions to the `Info.plist`, they can use "blah.specific.type" as a value under `directTypes` or `indirectTypes`. You will almost certainly want to assign other types in addition to the one you've created. See "Types" in the [QSObject](../reference/qsobject.md) section for details.

## Actions

Speaking of actions, if your action(s) need to refer to your custom type, you should include the header where the type is defined, then in the various action methods in `BlahAction.m`, you can test for objects of that type with something like this:

    if ([dObject containsType:QSBlahType]) {}

This allows you to use code completion and reduce the chance for typing errors. Unfortunately, whenever you refer to the types in your property list, you need to use the actual string the type refers to.

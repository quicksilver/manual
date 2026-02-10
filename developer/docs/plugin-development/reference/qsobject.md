# QSObject

Your plug-in will communicate with Quicksilver pretty much entirely through `QSObject` objects. That is, Quicksilver will send `QSObject`s to your methods, and if you need to send something back to Quicksilver, you'll return either a single `QSObject` or an array of them. Here are some details on creating them and using those previously created.

## Creating

You'll need to create `QSObject`s if adding things to the catalog and also if your action needs to send something back to Quicksilver (to end up in the first pane of the UI). This section is largely written with adding to the catalog in mind, but the information should be useful for returning objects for display as well (because it's so dead simple by comparison). There are several methods for creating new `QSObject`s. Here are some of the most common.

  * objectWithString
  * objectWithName
  * makeObjectWithIdentifier
  * objectWithURL
  * fileObjectWithPath

`objectWithName:` simply creates an empty object and stores the name in the object's dictionary of metadata. `objectWithString:` will use the string to set the name, but it also sets the type to `QSTextType` and then does some fancy analysis (using QSObject (StringHandling)'s `sniffString` method) to figure out if the string should be treated differently in any way. This is how strings can be turned into URL objects or file objects automagically. Also of note: The Mac OS X spell checker has no problem with "automagically".)

Most of the time, you probably want to take advantage of Quicksilver's "smarts" and use `objectWithString:` but if for some reason you just want it to take your string and not mess with it, use `objectWithName:`.

In my experience, you don't need to do anything more than the above to create a usable object, but you will probably want to add more details such as…

### Identifier

An identifier for your `QSObject` isn't required, but I recommend always setting one. In any case, it's important to understand how they're used. You set one like this:

    [myObject setIdentifier:someString];

In addition to actually storing the identifier string in your object, this causes Quicksilver to add the object to an internal registry.

If you choose an identifier that is already in use, you will **replace the existing object** with your new one in the registry. This has a couple of implications. First, you should obviously pick a unique string to use as an identifier. Second, if you end up "recreating" various objects (either to appear in the third pane, or to act as children for another object) be careful what you do with them. Here are some tips:

  1. For objects that just serve some temporary purpose in the UI, add a prefix to the identifier, or don't even set one.
  2. Wherever possible, use existing objects instead of recreating identical ones.
  3. If you want to use an existing object, but modify it in some way, create a new empty `QSObject` and assign it attributes from the existing object as needed.

### Name

If you've created an object using one of QSObject's more 'basic' methods such as `objectWithIdentifier:` or even `[[QSObject alloc] init]` it is important to set the object's name using the `setName:@"some name"` method.

This is the most prominent string in the UI (unless you set a label), and Quicksilver matches against it when a user is typing.

### Label

This is optional, but if you want the text that appears most prominently in the user interface to be something other than the name, you can set this using `setLabel:@"some string"`.

This is also the string that Quicksilver matches against when a user is typing, so keep that in mind. You can make things easier for users to find in the catalog by messing with the label. (The name will still be searchable as well, and will appear instead when matched.)

If you set name and label to the same thing, the value will be set as the name and the label will be removed automatically.

### Type

To set a type for an object, do something like this:

    [myObject setObject:someObject forType:QSBlahType];

A `QSObject` can have multiple types, so you can call this method multiple times, each with a different type, if you want. That deserves some further discussion. Most actions in Quicksilver only work with certain types. You will probably want to make built-in actions or actions defined in other plug-ins do something useful with your objects, which may be of a new type Quicksilver has never heard of. The "Paste" and "Large Type" actions are prime examples. You can't very well expect various other plug-ins (or Quicksilver itself) to add support for your new type. This is where you want to use an existing type to get things working.

Hopefully, by now, you've figured out what the object is supposed to be for each type you assign. It will be something that actions supporting that type can make use of. (See the warning on arrays below.) I'll use "Paste" as an example. The "Paste" action works with a few types I'm sure, but the simplest one is `QSTextType`. The thing you want to paste in that case will be a string. Your `QSObject` probably has many strings (name, label, details, etc.) so how can you tell Quicksilver which to spit out when running the "Paste" action? Like this:

    [myObject setObject:thisString forType:QSTextType];

Now, when a user selects this object and uses an action that works with `QSTextType`, it will use `thisString`.

If you set multiple types, you should also set one as primary.

    [myObject setPrimaryType:QSBlahType];

Don't use `setPrimaryType:` alone. You must also call `setObject:forType:` using the same type at some point.

Here are all the types Quicksilver declares in `QSTypes.h`. Examples of their creation and use are available in existing code.

    QSFilePathType
    QSTextType
    QSAliasDataType
    QSAliasFilePathType
    QSURLType
    QSEmailAddressType
    QSContactEmailType
    QSContactPhoneType
    QSContactAddressType
    QSFormulaType
    QSActionType
    QSProcessType
    QSMachineAddressType
    QSABPersonType
    QSNumericType
    QSIMAccountType
    QSIMMultiAccountType
    QSPasteboardDataType
    QSCommandType
    QSHandledType

A warning on arrays: If you call `[object setObject:someArray forType:QSBlahType]` then call `[object objectForType:QSBlahType]`, you will only get the array's last object. To get the original array back, call `[object arrayForType:QSBlahType]` instead.

### Details

The "details" string is the text that appears smaller underneath the label in most Quicksilver interfaces. Set it using `setDetails:@"some string"`.

Setting this explicitly is optional but if you don't, Quicksilver will pick something. In some cases, it uses the identifier. Keep this in mind if your identifiers aren't very nice to look at.

### Icon

You can set an icon (as an `NSImage`) for a `QSObject` using the `setIcon:` method. Quicksilver makes it easy go get various images with `QSResourceManager`. Just do something like this:

    [myObject setIcon:[QSResourceManager imageNamed:@"GenericNetworkIcon"]];

I don't recommend using the `setIcon:` method when adding things to the catalog. (See the note on `setQuickIconForObject:` for an explanation.) However, using this method directly from one of your actions does work if you want to set the icon temporarily for something you're sending back to the Quicksilver UI. (That too will go away, but this is only an issue if the user leaves the object you return up in the first pane.)

FYI, if you want to use one of the standard system icons for something, many can be found in `/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources`. You can refer to them using only the file's name (no path and no ".icns" extension). To use the icon for an application, use its bundle identifier, like `com.apple.Mail`. Finally, you can also provide the full path to an image file. Here are some examples:

    [QSResourceManager imageNamed:@"com.apple.Mail"]
    [QSResourceManager imageNamed:@"/Users/me/Pictures/Some.icns"]

You can also use `QSResourceManager` to get specific icons from inside a bundle's Resources folder, but that requires a bit of extra work. For example, to use the bookmark menu icon in Safari's bundle, you need to define a section in the property list called `QSResourceAdditions`, then define different icons under it.

Finally, if you want to use the icon for a particular file type, here's one method using the extension.

    NSImage *pdfIcon = [[NSWorkspace sharedWorkspace] iconForFileType:@"pdf"];
    [myObject setIcon:pdfIcon];

### Children

Usually, you'll load and set children on-the-fly using `loadChildrenForObject:`, but it does seem to be possible to set them when an object is first created as well. Assuming you have created an array of other `QSObject`s called "children", you can set them like this:

    [myObject setChildren:children];

These child objects will appear in the UI if a user select your object and hits → or /.

### Parent

If you have set children for an object so you can right arrow into them, these children should also know about their parent object. This builds a proper hierarchy and helps QS to figure out what to do when you arrow back out of the list of children objects (using ←).

So, before using `[myObject setChildren:children]` to set children for an object, for each of the children `QSObject`s, you should set the parent ID to the identifier of the parent `QSObject`. For example by doing the following for each `QSObject` in the `children` array:

    [childObject setParentID:[myObject identifier]];

Then, once the user arrows back out of the list of children, the correct object will be selected in the main QS pane and also be highlighted in the result list.

### Arbitrary Metadata

In addition to the standard things like name, label, icon, and type, `QSObject`s provide a metadata dictionary. You can store just about anything in here, so the possibilities for your plug-in get really interesting with this. If your objects are files, perhaps you want to store their size here. Perhaps you want to store width, height, and resolution for an image. Maybe you want to store a thumbnail image for the object. (It doesn't have to be a string.) Perhaps you just like to waste memory on other people's computers and want to store the lyrics to your favorite song.

To add your custom metadata to the object, you would do something like:

    [myObject setObject:value forMeta:@"key name"];

The key name is just a string you'll use to refer to this thing in the dictionary later. The value can by any type of object.

There'll be more on this in the next section. As a real-world example, one use I found for this was customizing icons for things in the catalog. As mentioned elsewhere, using `setIcon:` when things are added to the catalog is the wrong approach. You could probably store the icon as metadata, and move the logic that uses that data over to the `setQuickIconForObject:` method.

## Using

When Quicksilver passes `QSObject`s to your methods, here are some of the ways to get information out of them.

### String Values

To get a quick string representation of an object for whatever reason:

    NSString *blah = [dObject stringValue];

This is probably best for objects you didn't create and don't know the contents of. The `stringValue` method tries do do some smart things, but if none that pans out, it will call `displayName`. The `displayName` method will return the label if set, otherwise it returns the name.

If you're familiar with what an object contains and you want to get the name or label specifically, you can use `[dObject name]` or `[dObject label]`.

### Metadata

To retrieve metadata that you may have set when adding objects to the catalog:

    id value = [dObject objectForMeta:@"key name"];

Of course you if you know the type of object, you can be more specific than `id`.

This metadata has many possibilities, but two of the more obvious are:

  1. Checking to see which actions will work on this object (using `validActionsForDirectObject`)
  2. Directing the behavior of your actions

### Combined Objects

If a user sends multiple things to your action using the comma trick, then `[dObject stringValue]` will return "combined objects". I give examples of how to loop through one of these combined objects in the Actions section.

### Getting Specific Objects by ID

The `objectWithIdentifier:` method will return an existing `QSObject` if you know what it's ID was set to (probably because you set it yourself). It's a class method, so you don't call it on any particular object.

    QSObject *thisGuy = [QSObject objectWithIdentifier:uuid];

If building plug-ins for build 4008 or higher, you should get objects from `QSLibrarian` instead.

    QSObject *thisGuy = [QSLib objectWithIdentifier:uuid];

As a general rule, this will only work for objects that have been added to the catalog. It might work for other objects if they were recently used and are still in memory.

### Getting Specific Objects by Type

You can use `QSLibrarian` to retrieve objects from Quicksilver's catalog by type. The most common uses for this are to restrict the objects that appear in the third pane, and to build up a list of children for another object.

To simply get everything of a certain type, call this:

    NSArray *objects = [QSLib arrayForType:@"QSBlahType"];

To get the same list but sort by rank (typically determined by how often a user accesses the object):

    NSArray *objects = [QSLib scoredArrayForType:@"QSBlahType"];

### Respecting Disabled Objects

Users have the ability to remove individual objects from the catalog by unchecking them in the source entry's preferences. When providing a list of children or objects in the third pane, it's generally appropriate to respect these disabled objects and prevent them from appearing.

If you pull existing objects from the catalog by type as described above, the objects should already be omitted in build 4008 or later. If you're using an older build, getting a list by calling `objectForEntry:`, or generating objects on-the-fly somehow, you'll need to omit these items from the results yourself.

Here's one possible way to do it:

    // unfilteredResults is the array you start from
    NSIndexSet *enabled = [unfilteredResults indexesOfObjectsWithOptions:NSEnumerationConcurrent passingTest:^BOOL(QSObject *obj, NSUInteger idx, BOOL *stop) {
        return ![QSLib itemIsOmitted:obj];
    }];
    NSArray *filteredResults = [unfilteredResults objectsAtIndexes:enabled];

## More Information

A lot can be figured out by looking through `QSObject.m`. If you really want to track down *everything* `QSObject` provides, search for "@implementation QSObject" in the Quicksilver source and stare in horror at the number of results.

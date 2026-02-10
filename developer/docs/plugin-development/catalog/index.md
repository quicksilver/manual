# Adding to the Catalog

## Info.plist

There are two sections in `Info.plist` you should know about.

[`QSPresetAdditions`](../reference/registration.md#qspresetadditions) is where you can list catalog entries that should be present by default when your plug-in is loaded. (These are the things you see in the "Modules" section of the Catalog.) These can be normal existing sources, like "QSFileSystemObjectSource" (a.k.a. File & Folder Scanner), or they can refer to a new source you define yourself.

If you want to see what these look like, open `~/Library/Application Support/Quicksilver/Catalog.plist` and look at the `customEntries` section. In fact, one easy way to create a catalog preset for your plug-in is to create it as a custom entry in Quicksilver, then copy/paste it from `Catalog.plist`. The only thing you may want to add by hand is an `icon`. You'd also change `sources` to something like `QSBlahSource` if you're defining your own.

The other important section in the `Info.plist` is `QSRegistration`. If you're creating your own source instead of using one of the built-ins, you'll need to add it here so Quicksilver will use it. You'll want to make sure there's a dictionary called `QSObjectSources`. Create an item under this and set both the name and value to the name of the class in `BlahSource.m` that provides the source, such as `QSBlahSource`.

Also under `QSRegistration` are some settings you'll need if you want users to be able to "right arrow" into things (which can also be done with '/'). You can use `QSBundleChildHandlers` to allow right arrowing into bundles and you use `QSObjectHandlers` to allow arrowing into objects created by plug-ins.

The thing you use `QSBundleChildHandlers` for is generally some application that's already on the system and related to your plug-in, but has no direct knowledge of, or support for Quicksilver. The left hand side should be a bundle identifier, like `com.apple.Finder` and the right hand side should be the name of a class in your plug-in that contains a `loadChildrenForObject:` method.

By default, Quicksilver will show an application's recent documents when right-arrowing. Don't override this without good reason.

`QSObjectHandlers` tells Quicksilver where to go for more information about a particular type. This is typically a type that you've defined, but doesn't have to be. On the left should be a type of object in Quicksilver and on the right should be the name of a class in your plug-in that contains methods like `loadChildrenForObject:`, `setQuickIconForObject:`, etc. It might look like this:

    <key>QSObjectHandlers</key>
    <dict>
        <key>QSBlahType</key>
        <string>QSBlahSource</string>
        <key>QSBlahAnotherType</key>
        <string>QSBlahSource</string>
    </dict>

Note that you can use the same "source" class for all types, or create a separate class for each one. If you use the same source, the methods will just have to figure out what type of object they have before proceeding.

## Code

There are some methods you'll want to define in `BlahSource.m` and Quicksilver will call them at the appropriate time. This is not a complete list of available methods, but the common ones are covered. You can look at existing plug-ins for some example code. Note that many of these methods are only called by Quicksilver if you define something for `QSObjectHandlers` in `Info.plist`.

The information for an entry (from `Info.plist`) can be pulled in like this:

    NSMutableDictionary *settings = [theEntry objectForKey:kItemSettings];

Again, existing plug-ins can give you some examples of how to use this info since the dictionary contents can vary widely from one source to another.

### objectsForEntry

Example: `- (NSArray *)objectsForEntry:(NSDictionary *)theEntry`

This method does the work of adding your objects to the catalog. It can do whatever you want it to do (parse files, get information over the network, query a database, etc.) as long as it returns an array of `QSObject`s.

There are several ways to create a `QSObject`. Here are a couple:

    QSObject *myObject = [QSObject objectWithString:string];
    QSObject *myObject = [QSObject objectWithName:name];
    QSObject *myObject = [QSObject URLObjectWithURL:url];

There is a full list of all the methods available for creating objects in the [Creating](../reference/qsobject.md#creating) section of this reference.

There are also things you may want to do to your objects prior to adding them to the array to be returned, like `setIdentifier:`, `setLabel:`, `setDetails:`, `setName:`, `setObject:forType:` etc. There's a whole section in this document on `QSObject` that provides more details.

### indexIsValidFromDate

Example `- (BOOL)indexIsValidFromDate:(NSDate *)indexDate forEntry:(NSDictionary *)theEntry`

Quicksilver runs this during scheduled catalog updates (every 10 minutes by default) to ask "Is this catalog entry still up to date?" How you determine the answer to this question is up to you. If this method returns `YES`, Quicksilver moves along without doing anything. If this method returns `NO`, Quicksilver will attempt to update the entry by calling the `objectsForEntry:` method.

You can have this method do nothing but return `YES` or `NO` unconditionally, and that's exactly what it does for many plug-ins. Just keep in mind that this will either cause your source to never get updated (except manually) or cause it to get updated on every single rescan (which may be a performance concern, depending on what it does).

`indexDate` and `theEntry` are passed in by Quicksilver. The `indexDate` tells you when the entry was last updated in the catalog. `theEntry` contains information about the entry that you might need (file paths, URLs, etc.).

**NOTE**: This method is not consulted when your plug-in is first installed or when a user selects the entry in the catalog and hits the "rescan" button manually. In other words, if you're checking for errors with your source here to avoid unnecessary rescans, that's good, but you still need to check for errors in `objectsForEntry:` as well, because it will be called at least once.

To rescan your entry when a file has changed been changed since the last scan:

    - (BOOL)indexIsValidFromDate:(NSDate *)indexDate forEntry:(NSDictionary *)theEntry
    {
        // use the plist settings to determine which file to check
        NSMutableDictionary *settings = [theEntry objectForKey:kItemSettings];
        NSString *sourceFile = [self fullPathForSettings:settings];
        // get the last modified date on the source file
        NSFileManager *manager = [NSFileManager defaultManager];
        if (![manager fileExistsAtPath:sourceFile isDirectory:NULL]) return YES;
        NSDate *modDate = [[manager attributesOfItemAtPath:sourceFile error:NULL] fileModificationDate];
        // compare dates and return whether or not the entry should be rescanned
        if ([modDate compare:indexDate] == NSOrderedDescending) return NO;
        // if we fall through to this point, don't rescan by default
        return YES;
    }

To scan the entry once when Quicksilver starts, but never again:

    - (BOOL)indexIsValidFromDate:(NSDate *)indexDate forEntry:(NSDictionary *)theEntry {
        // rescan only if the indexDate is prior to the last launch
        NSDate *launched = [[NSRunningApplication currentApplication] launchDate];
        if (launched) {
            return ([launched compare:indexDate] == NSOrderedAscending);
        } else {
            // Quicksilver wasn't launched by LaunchServices - date unknown - rescan to be safe
            return NO;
        }
    }

In the above example, if Quicksilver relaunched itself (instead of being launched at login or via Finder), the `launchDate` will be unavailable, which is why you need to test the result.

### setQuickIconForObject

Example: `- (void)setQuickIconForObject:(QSObject *)object`

If you call `setIcon:` when adding objects to the catalog, they will show up at first but quickly disappear. Calling `setIcon:` from this method instead will work more reliably. Example:

    [object setIcon:[QSResourceManager imageNamed:@"GenericNetworkIcon"]];

Quicksilver calls this in real-time as objects need to be displayed, which is why it appears more reliably. (It's probably more efficient that way too, compared to storing an icon for everything in the catalog whether it gets used or not.)

As the name implies, you should only use this for icons that are ready to display quickly. Generally, that means icons or images that are already in memory or on a fast, local disk. If you need to do anything more expensive, like generate a Quick Look preview, add a badge to the icon, or fetch an image over the network, do it in `loadIconForObject:`.

### loadIconForObject

Example: `- (BOOL)loadIconForObject:(QSObject *)object`

This method is optional. After the "quick icon" has been set with `setQuickIconForObject:`, Quicksilver will ask your object source if it has this method, and if so, run it on a background thread.

This is where you should do more expensive image processing or fetching. If you end up with a valid image, you should call `setIcon:` again from here. If an icon already exists for the object, the main interface and results list will redraw the icon to reflect the change.

Some examples might be helpful.

  * The filesystem object source uses this method to replace the generic icon for files (based on type) with a Quick Look preview.
  * The URL object source replaces the generic URL icon on web searches with one that has the magnifying glass and favicon from the site overlaid.
  * The iTunes plug-in fetches album covers and video previews (via Quick Look) and uses them to replace the generic icon for those types.

### loadChildrenForObject

Example: `- (BOOL)loadChildrenForObject:(QSObject *)object`

This is very similar to `objectsForEntry:`, but instead of adding things to the catalog, it loads them on the fly when you right arrow into the parent object. You just need to create an array of `QSObject`s, but instead of returning them, you assign them to the parent object like this:

    [object setChildren:children];
    return TRUE;

These can be newly created objects or objects that are already in the catalog. If the children have already been added to the catalog, the most efficient thing to do is to retrieve them instead of recreating them. (See the later sections on getting specific objects by ID and by type.)

**Read up on identifiers in the [QSObject](../reference/qsobject.md) section before creating/using objects as children.**

### objectHasChildren

Example: `- (BOOL)objectHasChildren:(QSObject *)object`

This method is used to indicate to the user that an object is browsable (can be right arrowed into). If it returns `YES`, a little arrow is displayed on the very right of the object.

If you used `loadChildrenForObject:` so the user can right arrow into an object, you should indicate that to the user by having this method return `YES`.

**NOTE**: Returning `NO` (or leaving this method out) will hide the little arrow indicator, but the user will still be able to arrow into the object if you provided children for the object by using `loadChildrenForObject:`.

### isVisibleSource

Example: `- (BOOL)isVisibleSource`

This method determines whether or not your source shows up on the drop-down list for adding new custom catalog entries.

Return `NO` to keep this off of the drop-down. Return `YES` if you want users to be able to add custom entries of this type to their catalog. Keep in mind that you will also need to provide them with some sort of interface to do so.

See [Object Source Preferences](../reference/preferences.md#object-source-preferences) for details.

### Actions

If the direct object is irrelevant, you can add actions directly to the catalog. They will appear in the first pane with a default action of "Run" in the second pane. Here's an example of creating a `QSAction` programatically.

    NSDictionary *actionDict = [NSDictionary dictionaryWithObjectsAndKeys:
        @"QSBlahActionProvider", kActionClass,
        @"doSomething", kActionSelector,
        @"BlahIcon", kActionIcon,
        @"Do Something", @"name",
        nil];
    
    newObject = [QSAction actionWithDictionary:actionDict
        identifier:@"QSBlahDoSomething"
        bundle:nil];

You could have that in your `objectsForEntry:` method and add `newObject` to the array it returns.

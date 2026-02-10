# Validating Objects

## validActionsForDirectObject

Example: `- (NSArray *)validActionsForDirectObject:(QSObject *)dObject indirectObject:(QSObject *)iObject`

If you set `validatesObjects` to `YES` on an action in `Info.plist`, that action will never appear unless you add some corresponding code. This method must exist in `BlahAction.m` and return the identifier of any actions that you think will be safe to run based on whatever validation steps you've gone through. It should return an array of action names as strings. Perhaps you don't want the actions to work with strings longer than 100 characters or something. You could accomplish that with:

    NSString *myString = [[dObject arrayForType:QSBlahType] lastObject];
    NSMutableArray *newActions = [NSMutableArray arrayWithCapacity:1];
    if ([myString length] < 100) {
        [newActions addObject:@"FirstAction"];
        [newActions addObject:@"SecondAction"];
    }
    return newActions;

Keep in mind that Quicksilver has to run this validation code on every object that ever gets selected in the first pane in order to determine if this action is applicable or not before it can display the actions in the second pane. And not just for your plug-in. It's every validation method from every active plug-in every time a user selects something. It should go without saying at this point, but make sure your `validActionsForDirectObject:` method returns quickly!

## validIndirectObjectsForAction

Example: `- (NSArray *)validIndirectObjectsForAction:(NSString *)action directObject:(QSObject *)dObject`

This method gets called when going to the third pane (for actions that provide one). It should return an array of `QSObject`s that are valid for that action. For instance, selecting a file and choosing the "Move To…" action will only show folders in the third pane.

To make sure the third pane comes up in text entry mode instead of regular "search" mode, do something like this:

    return [NSArray arrayWithObject:[QSObject textProxyObjectWithDefaultValue:@""]];

You can set the default text to whatever and that text will appear (selected) in the third pane. The above example just makes it blank.

If the third pane will ask for some sort of search text, you should stick to the convention of other plug-ins (and Mac OS X in general) and set the default text to be whatever the user last searched for. To accomplish that:

    NSString *searchString = [[NSPasteboard pasteboardWithName:NSFindPboard] stringForType:NSStringPboardType];
    return [NSArray arrayWithObject:[QSObject textProxyObjectWithDefaultValue:searchString]];

When you return a simple array, the first object will be selected by default. To select a specific object, return a two element array. The first element should be the object you want selected. The second element should be the entire list of possible objects. For example:

    QSObject *selectedThing = [indirectObjects objectAtIndex:4];
    return @[selectedThing, indirectObjects];

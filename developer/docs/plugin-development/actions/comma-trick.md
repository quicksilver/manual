# The Comma Trick

If you want your actions to support the comma trick (where a user can select several things in the first pane and act on them), you'll have to write actions to loop through all the objects and do the appropriate thing. If you expect to get several objects of the same type, the easiest technique involves getting a quick representation of each. `QSObject`s have several properties but you can specify which one should be associated with a specific type when the object is created using `setObject:forType:`. Assuming you set these as strings, you can get at them like this:

    for (NSString *userSelectedThing in [dObject arrayForType:QSBlahType])
    {
        // code
    }

Note that the above code will also work if the user just passes a single item to your action.

If you need to get the full details of the `QSObject`s passed in, you can do something like the following in your action's code:

    for (QSObject *individual in [dObject splitObjects])
    {
        NSString *thisGuy = [individual name];
        NSString *somethingWeNeed = [individual objectForMeta:@"key"];
    }

`splitObjects` is safe to use on single `QSObject`s, so it will work for any case, but sometimes you need to know which you have. The best way to tell if you're dealing with single vs. multiple objects is to look at the count:

    if ([dObject count] == 1)
    {
        // single object
    } else {
        // multiple objects
    }

For actions that won't support the comma trick, you should use the object validation process to prevent those actions from ever showing up, rather than checking for multiple objects in the action itself.

# Proxy Objects

The property list entry that defines a proxy object is discussed in [QSProxies](registration.md#qsproxies). The `providerClass` defined in the plist should conform to the `QSProxyObjectProvider` protocol. The most important method there is `resolveProxyObject:`.

This method is responsible for returning the "real" object referred to by one or more proxies. If the class is only responsible for one proxy object, it usually returns an object blindly, but if it handles more than one, it needs to see which (usually by checking the identifier) before returning a value.

    - (QSObject *)resolveProxyObject:(QSProxyObject *)proxy
    {
        NSString *ident = [proxy identifier];
        if ([ident isEqualToString:@"QSBlahExampleProxy"]) {
            QSObject *resolved = nil;
            // do work to figure out what this object currently refers to
            return resolved;
        }
        return nil;
    }

There are other optional methods you can implement in the `providerClass` for proxy objects.

Proxies are often requested multiple times in rapid succession, so Quicksilver tries to avoid resolving them every time. You can control the amount of time a proxy will hold onto its current value before doing the work of resolving it again. The default is 3 seconds. 0 is not recommended, but might make sense when the value of the object is already in memory.

    - (NSTimeInterval)cacheTimeForProxy:(id)proxy
    {
        return 10.0;
    }

If the types for your proxy object are known in advance, just define them in the plist. Some proxy objects may refer to different types of `QSObject`s in different contexts. (Think about "Current Selection".) The type can be set dynamically to ensure that the correct actions appear in the second pane.

    - (NSArray *)typesForProxyObject:(QSProxyObject *)proxy
    {
        // figure out which types apply
        // return an array of type names (strings)
    }

There are other methods you can implement to dynamically assign details, icons, etc., but these aren't specific to proxy objects.

## Current Selection

If you're working on a plug-in for a specific application, you can often improve the behavior of Quicksilver's built-in "Current Selection" proxy object.

When a user asks for Current Selection, Quicksilver will first see if any plug-ins claim to know how to get a selection from the front-most application (based on its bundle identifier). If not, it will simply tell the application to "Copy" and hope the pasteboard contains something useful.

To claim support for a particular application, define a proxy object like any other, but use the application's bundle ID as the proxy object's identifier in the plist.

Note that when Quicksilver looks up this proxy and finds the provider class, it will send `[provider resolveProxyObject:nil]`. You might want to put the selection business in a dedicated class so you don't have to worry about what value was passed in. You can just blindly return the selection in that case.

If the Current Selection proxy is handled by the same class as other proxy objects, you'll need to do some testing to figure out if Current Selection is the one being requested. iTunes and iPhoto do something like this:

    if (!proxy || [[proxy identifier] isEqualToString:@"com.apple.iTunes"])

Why would you put other proxies in the same class with Current Selection? Because Current Selection only applies to the front-most application. Many useful triggers depend on getting the selection from a specific application, whether it's active or not, so you're probably also going to define a "Current Blah Selection" for that. You don't want to duplicate the code for getting the selection in two different classes, so you'll have to put them in the same place.

# Action Properties (QSActions)

The QSActions section contains an array of dictionaries. The key should be an internal identifier for your action, like `MakeStuffBetter`. Each action can have the following children.

name (string)
: The name the user will see (and search for) in the interface

description (string)
: A one-line description of what the action does. In interfaces that support it, this will appear in small text under the action's name.

commandFormat
: A sentence-like string that describes what's going to happen when you run the action. Enter `%@` as a placeholder for the direct object. For actions that take an indirect object, you can add a second placeholder. For example, "Move %@ to %@". In some cases, you might want to reverse the order of the two objects' names. That can be done by numbering them, as in "Search for %2$@ using %1$@".

icon (string)
: The image that will appear for this action in the interface

directTypes (array)
: A list of types this action applies to. It won't show up unless the object in the first pane has one of the types on this list.

directFileTypes (array)
: If one of your direct types is `NSFilenamesPboardType` (files), you can limit the types of files that match by providing a list of UTIs or extensions here.

indirectTypes (array)
: The types of objects that are allowed in the third pane (if this action uses it)

indirectOptional (boolean)
: Specifies whether or not the third pane is required

actionClass (string)
: The class that contains the method referred to by `actionSelector`

actionSelector (string)
: The method that does the work for this action. For instance, the `MakeStuffBetter` action might refer to a method called `makeStuffBetter:`. If the action takes an argument (like the name of a cute animal) in the third pane, you specify the name of the argument here as well, as in `makeStuffBetter:usingCuteAnimal:`.

reverseArguments (boolean)
: If true, the arguments will be sent to the `actionSelector` in the opposite order. Using the example above, an action that allowed cute animals in the first pane and something to make better in the third pane could reuse the `makeStuffBetter:usingCuteAnimal:` method you've already written.

alternateAction (string)
: The identifier of the alternate action

validatesObjects (boolean)
: This tells Quicksilver whether or not to run `validActionsForDirectObject:`. That method gives you much more fine-grained control in cases where simply checking the type isn't sufficient to decide whether or not an action should be available.

displaysResult (boolean)
: If true, the Quicksilver interface will reappear after your action runs, but only if your action returns a `QSObject`.

enabled (boolean)
: Whether or not this action should be available by default when your plug in is installed for the first time

precedence (float)
: A number between 0.0 and 4.0. You should generally only use this if the action applies to a new type created by your plug-in, and not for any of the types Quicksilver knows of by default. Most of the built-in default actions have a low precedence and you can very easily overpower them here. Users would not appreciate this action suddenly becoming the default for files or text.

runInMainThread (boolean)
: If true, this forces the action to be run in the main thread (for timers or actions that calculate a delay)

hidden (boolean)
: Whether or not the action should be directly usable by the user. You might want to set this for an alternate action.

resolvesProxy (boolean)
: By default, Quicksilver resolves proxy objects and passes the resulting "real" object on to the action. This prevents actions from having to test for and resolve proxies themselves. In rare cases, you might need to pass the proxy to an action as is. If so, set this to `NO`.

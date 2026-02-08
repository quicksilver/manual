# Abracadabra Mouse Gestures

For this section, install the Abracadabra Triggers plugin. This enables a new trigger type known as a Gesture to go along with Keyboard and Mouse triggers. It also installs an Abracadabra preference pane. 

Abracadabra lets you invoke a trigger by drawing a shape with the mouse. E.g., you can configure Quicksilver to activate the Open Safari trigger by drawing an S on the screen. You configure your shape by drawing with the mouse button down in the pane in the Settings tab of the trigger’s drawer. The “Show zooming trigger window” will show a bezel window that enlarges when a gesture trigger is recognized and executed (like the Display: Show Window option of a keyboard trigger).

In the Abracadabra Preference pane you configure how you invoke all gestures. That is, what mouse button you hold down and/or what modifier key you hold down while drawing any gesture. If you have a mouse with extra buttons it’s probably most convenient to use one of them for this as you’ll only need one hand to invoke the gesture. You can also choose the colors used to draw the shape on the screen as you draw and after you finish for a recognized gesture and an unrecognized gesture, as well as sounds to play. 

There’s also an option to Enable LaserKey Support which is a virtual keyboard device made by Cellulon. With it you can make gestures with your finger. Wherever I say mouse gestures here, LaserKey gestures is implied if you’re one of the lucky few to have one of these devices.

Simple gestures are best as you’ll have an easier time remembering them and Quicksilver will have an easier time recognizing them. You can create a gesture for any Quicksilver command (that is trigger). E.g., skipping to the next track in iTunes by drawing a line from left to right. Try a gesture for the **Quit** or **Hide** actions using the Current Application proxy object.

Gestures also go well with limiting the scope of a trigger and using the **Menu Bar Items…** action. This way you can make a trigger to invoke Safari’s Back command or Mail’s Reply command. This usually works best for things that don’t need the keyboard, e.g., navigating in Safari. Using a gesture to bring up a Find dialog probably doesn’t make much sense since you’ll need to type the text to find.

An interesting idea is using the Current Application proxy object and the **Menu Bar Items…** action to invoke an action common in all applications, e.g., Undo or Close. The problem is that many applications dynamically update their menus (e.g., “Undo Typing”) or slightly rename these commands (e.g., Close Window and Close Tab) so the trigger won’t work in all applications. Also there’s no way to select a menu command that is generic and not specific to an application, so this isn’t possible.
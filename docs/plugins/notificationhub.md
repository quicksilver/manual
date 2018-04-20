#Notification Hub

Provides a way to use several notifiers at once.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 1.1.0
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


## What is it?

This plugin adds a new Notify Mediator that can be used to use different
Notify mediators based on the notification type

## Usage

In the Handlers preference pane, select Notification Hub as the Notify
mediator. Then in the Notifiication Hub preference pane you can customize it
further.

The Default popup is what Notify Mediator to use if the given notification has
no type or isn't in the table.

Hit the add button to add an entry to the table. The first column is the
notification type. Double-click to edit to put in a custom type, or click the
popup at the right side of the column to select a known type. The second
column is the Notify Mediator to use for that notification type.

You can add several entries for a given notification type - each Notify
Mediator will be called for that notification.
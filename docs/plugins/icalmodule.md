#Calendar

Adds support for creating Events and To-Dos with Calendars on your Mac.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 1.1.2
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


## Calendar Plugin

This plugin adds actions for creating events and To-Dos from Quicksilver

### Actions

**Create Calendar Event**

This action takes text from Quicksilver's 1st pane, and adds it as an event to
your selected Calendar in Quicksilver's 3rd pane.  
Examples of text could be `Dinner with Tom next Tuesday` or `Visit mum at
3pm`.

You can improve how an event displays in your Calendar by separating the name
of the event and the time it takes place with two dashes `--`  
Using `Next Tuesday -- Dinner with Tom` will create an event called just
`Dinner with Tom` in your calendar.

**Create Calendar To-Do**

This action takes text from Quicksilver's 1st pane, and adds it as an To-Do to
your selected Calendar in Quicksilver's 3rd pane.  
If you do not see all your calendars appear in Quicksilver's 3rd pane, this is
because not all calendars support To-Dos.  
Examples of text could be `Do the shopping` or `Pick up the kids from school`.

You can set the priority of an event by prefixing your event with any number
of exclamation marks `!`  
_One_ exclamantion mark gives the To-Do a _low_ priority, _two_ give the To-Do
a _medium_ priority and _three_ gives it a _high_ priority.

`!! This is a medium priority todo`  
`This todo has no priority set`
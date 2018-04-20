# Event Triggers

Run triggers automatically based on system events.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 2.0.0
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


# Event Triggers

With this plug-in, Quicksilver can run actions automatically as things happen
on your system. For example:

  * When the screen saver activates, pause iTunes.
  * When the computer wakes from sleep, open Mail.
  * When the network changes, run a shell script.
  * When a disk named "Backup" is mounted, compress a specific folder and copy it to the disk.
  * When switching to the internal speakers (headphones disconnected), pause iTunes.

(Some examples require other plug-ins.)

## Built-in Events

You can assign triggers for the following events:

  * Application Launched
  * Application Quit
  * Quicksilver Launched
  * Quicksilver Launched (at Login)
  * Quicksilver Will Quit
  * Active Space Changed
  * Computer Will Shut Down
  * Computer Will Sleep
  * Computer Woke Up
  * External Display Changed
  * Fast Login
  * Fast Logout
  * Ethernet Changed
  * Disk Mounted
  * Disk Ejected
  * Disk Will Eject
  * Screen Saver Started
  * Screen Saver Stopped
  * Switched to A/C Power
  * Switched to Battery Power
  * Switched to UPS Power
  * Switched to Headphones
  * Switched to Internal Speakers
  * Switched to S/PDIF
  * Internet Became Available
  * Internet Became Unavailable

## Plug-in Events

Other plug-ins may define additional events. These are generally things that
happen when running an action in Quicksilver, rather than on the system in
general.

Events generated by Quicksilver should be marked with `☿`.

## Trigger Settings

Event

    Choose the event you want Quicksilver to watch for.
Delay

    When the event happens, wait a certain number of seconds before running the trigger. It doesn't need to be a whole number. For instance, 0.1 and 2.5 are valid values.
Ignore Repeats

    

For certain events, like "Application Launched", OS X might send multiple
redundant notifications in rapid succession. Use this setting to prevent the
trigger from running too many times.

If you enable this setting with a delay of _n_ seconds, when multiple events
occur within _n_ seconds of each other, the trigger will only run once ( _n_
seconds after the last notification is sent).

It might take some experimentation to get this right. A tip is to initially
set the trigger up to do something obvious, like show some text using the
Large Type action or append some text to a file, and see how many times it
runs.

### Match & Ignore Items

By default, an event trigger will run for **every occurrence** of the event.

For certain types of events, you can control whether or not the trigger runs
depending on the object the event was related to. (See below for more on the
Event Trigger Object.) For example, you might want to run a backup script when
a particular disk is mounted, but not every time _any_ disk is mounted. These
restrictions can be set up by adding objects to the match/ignore lists.

Select objects in the main Quicksilver interface and drag them to either the
Match Items or Ignore Items list. Multiple items can be added at once using
the comma trick.

## Event Trigger Object

This plug-in adds a proxy object called "Event Trigger Object" to the catalog.
It's only useful within the context of an event trigger.

When an event happens, it can pass something along. You can then use an event
trigger to run an action on that thing. For example, the iTunes plug-in
defines an "iTunes Track Changed" event. When this happens, the Event Trigger
Object will refer to the track that just started playing. So, for example, you
could create a trigger like

    
    
    Event Trigger Object ⇥ Add to Playlist… ⇥ Just Played
    

To see what the Event Trigger Object refers to for a particular event, check
the documentation in the plug-in that defines the event. For events that don't
explicitly provide an object, the Event Trigger Object will just be text
containing the event's name.

### Known Event Trigger Objects

For the events defined by this plug-in, the following objects will be
available.

Event | Event Trigger Object  
---|---  
Application Launched | The application that launched  
Application Quit | The application that quit  
Disk Mounted | The disk that was mounted  
Disk Ejected | The disk that was ejected  
Disk Will Eject | The disk that will eject  
  
* * *

This plug-in uses icons from the [Open Icon
Library](http://openiconlibrary.sourceforge.net/).
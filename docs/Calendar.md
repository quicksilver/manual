# Calendar

Quicksilver has some limited support for creating calendar events and to-do’s in iCal and Google Calendar. As of B51 the Entourage Module plugin only supports contacts and email but not calendars. Entourage 2008 can be configured to sync with iCal, see the Entourage section in Contacts, the option is in the same place as the option to sync with Address Book. Another option is to manage a text file of todos. See the Text section for the description of the Text Manipulation Actions plugin for some tips.

## iCal

The iCal Module plugin installs two actions: **Create iCal Event** and **Create iCal To-Do**. Using either of these actions will open iCal if it’s not already running though won’t open the window if it’s hidden or closed. As of B51 the features enabled by the plugin are limited. There’s no way to see or interact with existing events and to-dos, typing → to move into iCal, does nothing.

To create a new to-do, activate Quicksilver, enter text-mode by typing . or ' and enter the to-do text. Tab to the second pane and choose the **Create iCal To-Do** action, tab to the third pane and choose the calendar for the to-do.

A specially formatted to-do text allows a priority and a due date to be entered.  Precede the text with zero to three exclamation marks to set the priority in iCal. Zero !’s sets a priority of None, ! is Not important, !! is Important, and !!! is Very important. A due date is set by  preceding the text (and any priority !’s) with a date and two hyphens. The date is somewhat flexible, allowing `8/1`, `8/1/2006`, `tue`, and `next wed`. In the example image I use the text: `8/1--!Upload User Manual`. As of B51 it seems it always uses a US-centric date format, *month*/*date*, even if the system is set to a European convention of *date*/*month*. The only work around for this is to use month names such as `Feb`.

Events are similar to to-dos but have no priority and can have a time as well as a date. Creating  a new event is similar to creating a to-do; put text in the first pane, use the **Create iCal Event** action and specify a calendar in the third pane. The format of the text string is: datetime--text, that is a date time string separated from the description of the event by two hyphens.  If no date or time is specified the event is created now. If just a date is entered, the event is created at noon on the specified day. Times are entered as `1pm` (`1p` is not valid), `1:00` (which is am), or `1:05pm`, or `22:30`.  All created events are 1 hour long and Quicksilver provides no way to set a different duration. The created events use the whole string as the event name, so if `wed 6pm--dinner` is entered, that’s also the name of the event. 

The above is the supported syntax but it seems that by not using `--` the date and time can be put anywhere in the string and it will still work. E.g., `dinner - wed 6pm` or `wed dinner 6pm`, and the event is created at the right time and with the string at the front which is a little friendlier if it gets cropped in the iCal display.

With this plugin there’s no way to specify attendees, repeats, alarms or other iCal fields. There are a few scripts on the Quicksilver site that can be installed that will prompt for more info, but they are under-documented and a little complicated to get setup. Rather than enter event info into an AppleScript dialog I think it’s easier to just enter the info into iCal. 

If entering information directly into iCal seems easier than remembering a text syntax that supports only some of the fields, then try these commands which require the User Interface Access plugin be installed and iCal already be running:

- iCal (**Menu Bar Items…**) New Event
- iCal (**Menu Bar Items…**) New To Do

They will make iCal be the active application, opening the window and bringing it to the front if hidden or minimized. The new event or to-do is created and selected, ready to have the name changed and other information entered. Making triggers for the above would be very convenient but as of B51 triggers using the **Menu Bar Items…** action and the third pane filled in don’t save. Hopefully this will be fixed in a future version.

For a little more flexibility with creating events, some people like the free OSX service Calendar Creator. This installs two Services, Add Calendar Event and Add To Do. See Calendar Creator’s documentation for what it can parse. With the Quicksilver Services Menu Module plugin installed any text can be sent to these services via Quicksilver.

## Google Calendar Module

For those that eschew iCal and prefer Google’s Calendar, there’s the Google Calendar Module plugin. It adds one action **Google Calendar Event** that takes text as the object in the first pane and sends it to Google Calendar which can parse text like `Dinner with Michael 7pm tomorrow`. 

If needed, Quicksilver prompts for Google Calendar login info. In the event of login problems, use Keychain Access to check the keychain entry for calendar.google.com.

As of B51, people have reported various problems with this plugin.  The plugin does not use Google Calendar’s Quick Add function so the parsing of information isn’t always correct. Some people report the wrong date being entered. Also the entire string entered is used as the text of the event and newly created events don’t inherit the default reminder setting.

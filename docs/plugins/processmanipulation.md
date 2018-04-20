# Process Manipulation

Actions for monitoring and modifying application processes on your machine.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 1.1.2
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


## Overview

This plugin interacts with applications and the "Running Applications &
Processes" catalog entries. Most actions can be run directly on an application
(i.e. search for an application as usual, then tab and select an action).

Make sure to enable the actions you want, under Preferences > Actions > by
Plugin > Process Manipulation.

If you want to be able to control background/hidden applications, go to
Catalog > Applications > Running Applications & Processes > Info ("i" button
in the lower right) > Source Options > Check "Include background
applications". Then make sure "Running Applications & Processes" is selected.
Now, you can search for "Running Applications Processes" in the Quicksilver
command window and right-arrow to get a full list of processes.

IMPORTANT NOTE: Some applications have a lot of helper process. For example,
iTunes has an "iTunes Helper" process, and Google Chrome has a process for
each tab. If you're getting unexpected results, try opening `Activity
Monitor.app` and making sure you're not missing something.

## A list of 'All Processes'

To get a list of all currently running processes easily, without enabling the
"Running Applications & Processes" catalog entry, you can do so by right
arrowing (→ or /) into Activity Monitor.app

## Actions

### Lauching/Terminating

Force Quit (Kill)

    Immediately terminate the application/process (SIGQUIT).
Launch a Copy

    Open a second copy. OSX usually only allows one copy of an application to be running, so be careful.
Launch as Root

    Launch an application with root permissions. Again, be careful.

Quicksilver also has the following actions, even if you don't install this
plugin:

  * Open
  * Relaunch
  * Open at Login
  * Do Not Open at Login

### Information

Sample Process

    Sample the process for 5 seconds and return the result in the first pane.
List Open Files

    Search the open files of the process in the first pane.
Get Process Identifier (PID)

    Note that if an application has helper processes, the returned PID may not always be what you want. For example, iTunes.app will return the PID of `iTunesHelper`, and some applications may be a light frontend with a heavy kernel (which may be the process you're actually interested in).

### Signals

The operating system can interact with a process by sending it a signal.

See `man signal` or
<https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man3/signal.3.html>
for a full list of signals in OSX.

Pause Application (SIGSTOP)

    `SIGSTOP` is useful because it completely halts the operation of a process (without quitting it) and can be resumed later. It is similar to `Ctrl-Z` in a terminal/shell.
Resume Application (SIGCONT)

    Resumes an application halted with `SIGSTOP`. Note that when the program resumes, the unexpected pause might cause it to have issues with timeouts, file handles, etc. However, short pauses are usually harmless.
Send Signal...

    Specify an arbitrary signal in the third pane.

### Priority

What this plugin calls priority corresponds more to "niceness". This ranges
from -20 (least nice, highest priority) to 20 (nicest, lowest priority). Nicer
processes will more easily give up CPU time. See `man nice` and `man
setpriority`.

Note: You may need to enter your system password to change the priority of a
process. This generally happens when you increase the priority.

It can be useful to lower the priority of a process to make sure the operating
system stays responsive. Increasing priority isn't very useful unless you have
multiple programs vying for cycles.

Lower Priority

    Increase niceness (change by +5).
Raise Priority

    Decrease niceness (change by -5).
Minimize Priority

    Set niceness to 20.
Maximize Priority

    Set niceness to -20.
Get Priority (Niceness)

    Return the priority (niceness) of the application in the first pane.
Set Priority...

    Specify a priority in the third pane.
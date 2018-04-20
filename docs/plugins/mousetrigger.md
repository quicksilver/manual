# Mouse Triggers

Allows triggering with hot corners and edges of the main screen.

 Summary                    | &nbsp; 
---------------------------:|:--------------------
 Available on macOS version | 10.11, 10.12, 10.13
      for Quicksilver build | 4024


## Mouse Triggers Plugin

The mouse triggers plugin gives Quicksilver the ability to create triggers
which are activated using mouse movements, clicks and dragging/dropping.
Triggers are created in the same way as HotKey triggers, only their activation
differs.

## Creating Triggers

### Creating the Trigger

To create a trigger, open the Quicksilver [triggers
preferences](qs://preferences#QSTriggersPrefPane), click the '+' button and
select 'Mouse' from the dropdown list.  
Set up the command as you would when creating a normal trigger. If you would
like to create a drag/drop trigger, which enables you to drop items onto the
mouse trigger points, see the 'Mouse Trigger Dragged Object' proxy object
section below.

### Adjusting the Activation

To alter how the trigger is activated, open the trigger sidebar (by either
clicking the 'i' button or pressing ⌘I) and open the 'Settings' pane. From
this window, you can alter which mouse click (left, right, middle etc.)
activates the trigger, how many clicks are required, and how long the
associated mouse movement must be held for the trigger to activate.  
Below the 'Type' and 'Delay' options are options to select which screen the
trigger can be activated on, and which side or corner of the screen.

### Modifiers and the 'Anywhere' button

The modifiers section of the settings allow you to add modifier keys to the
mouse activation method. With modifiers enabled, a further 'Anywhere' button
appears in the 'Corners & Edges' screen. Clicking this allows the trigger to
be activated if the correct modifiers and mouse movements are made anywhere on
the screen. an example could be:

  * Type: Right Click **x 2** (click the right mouse button twice)
  * Delay: 1s (hold the last right click for 1s)
  * Screen: All Displays (trigger works on all displays)
  * Corners & Edges: Anywhere
  * Modifiers: ⌘⌥ (hold the ⌘ and ⌥ keys down whilst right clicking with the mouse)

## Proxy Objects

### Mouse Trigger Dragged Object

The 'Mouse Trigger Dragged Object' proxy object allows you to create triggers
for items that you drag onto or drop onto the screen edges or corners. An
example could be to move the dragged file into a specific folder on your hard
drive. It is best to set up triggers that use the 'Mouse Trigger Dragged
Object' proxy object to work with the Drag Entered, Drag Exited and Drag and
Drop 'Types' in the trigger settings pane.
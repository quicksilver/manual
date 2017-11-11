# Chat

The basic actions, **IM**, **IM Item...**, and **IM to Account...** are all part of the Chat Support default plugin. There is a Handler called Instant Messaging which defines which application to use for the basic actions. Currently there is support for iChat and Adium, each via their own plugins. Install one or both of these plugins and then in Quicksilver Preferences under Handlers set the Instant Messaging handler to one of them.

The **IM** and **IM Item…** actions work on an IM address or a contact (if at least one IM address is entered, the first one is used). **IM** opens a new chat window connected to the contact. Send text or a file directly from Quicksilver by using the **IM Item…** action. In the third pane specify a file to transfer or  enter text mode by typing . or ' and then text to send as a message. **IM to Account…** is the reverse of this, select a file or text in the first pane and the IM account or contact in the third. This is convenient if using <kbd>⌘</kbd><kbd>⎋</kbd> to bring selected items into Quicksilver's first pane.

The IM actions work with contacts from the Contacts (or other contacts plugin) that have IM addresses entered from the global catalog. Both the iChat and Adium plugins allow Quicksilver to show a results list of just online buddies by typing <kbd>→</kbd> into the iChat or Adium applications in the first pane. Quicksilver's matching algorithm is a great way to quickly find a buddy in a large buddy list.

Some people hide the client list window of their IM application and just use Quicksilver when they want to start a chat session. Personally I keep a small buddy list of just the people I chat with often and care if they are online. For other people I keep their IM addresses in Contacts and if I want to IM them I can bring up their contact or one of their IM accounts and use the IM action.

## iChat

The iChat Module plugin allows the IM actions to work with iChat. Bring up iChat in the first pane and notice the > in the results list. If iChat is running, typing <kbd>→</kbd> into it will show a results list of all online (including idle) buddies. Quicksilver will not start iChat as a result of typing <kbd>→</kbd>. Begin a chat by using the **IM** or **IM Item…** actions as described above. The **IM to Account...** action also works.

The iChat module plugin also supports the **Audio Chat** and **Video Chat** actions. These will start an audio or video chat as if the Invite to Audio Chat or Invite to Video Chat commands were selected from iChat's Buddies menu.

The iChat module plugin has one action specific to it, **Set iChat Status** which uses the text of the object pane as the away message (although in version 0.5.0 of the plugin this seems buggy).

## Adium

The original Adium plugin for Quicksilver only worked with Adium up to version 0.89.1. Now that Adium is past version 1.0, that plugin has been removed. No Adium plugin appears in the plugin list, but a new plugin that works with Adium 1.0 is under development  and is available from this forum thread: http://blacktree.cocoaforge.com/forums/viewtopic.php?t=6395. Version 30b2 is described here. Download the plugin, double-click it to install it in Quicksilver and in Quicksilver's Preferences under Handler, set Instant Messager to be Adium.

The Adium Module plugin allows the IM actions to work with Adium. Bring up Adium in the first pane and notice the > in the results list. If Adium is running, typing <kbd>→</kbd> into it will show a results list of all buddies including offline buddies and entries representing groups. The first item listed is Online Contacts, type <kbd>→</kbd> into that to see just the online (including idle) buddies. Similarly <kbd>→</kbd> will work in other groups to show their members but only the online ones. Quicksilver will not start Adium as a result of typing <kbd>→</kbd>. 

Begin a chat by using the **IM** or **IM Item…** actions as described above. The **IM to Account...** action also works. Using these actions on a group will open separate chats with each of the members. The **Audio Chat** and **Video Chat** actions are not supported because Adium 1.x does not support these features.

The Adium plugin also provides the ability to set the status from Quicksilver. Enter text in the first pane and then use either the **Set Available Status** or **Set Away Status** actions. The text becomes the status and depending on the action the status is set to available (green) or away (red). Consider using triggers for commonly set statuses.

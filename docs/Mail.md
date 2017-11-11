# Mail

Quicksilver has several common email actions (**Compose Email**, **Email to…**, **Email Item…**) that are described in detail in this section and also mentioned in [Files and Folders](Files and Folders.md) and [Contacts](Contacts.md). They are defined in the Email Support plugin which is normally hidden but can be seen by <kbd>⌥</kbd>-clicking on the All Plugins set in the Plugin preferences.

Quicksilver supports specific email applications via the Apple Mail Module, Gmail Module, Entourage 2004 Module and Mailsmith Module plugins. These plugins should all install the Email Support plugin if needed. If the email actions don’t appear in the action pane, check that they are enabled in the Actions preferences. If they aren’t listed at all or the Email handler described below doesn't appear in the Handlers Preferenece, install the Apple Mail Module plugin which will certainly install it.

After installing the plugin for the desired application, set the Email handler in Quicksilver’s Handler preferences to the application (e.g., Mail or Entourage).

For basic Quicksilver support of other mail programs, choose “Default”. This uses the system default mail application set in Mail.app Preferences in the General tab under Default Email Reader. This refers to what application handles mailto: URLs.

If a mail message is already being composed and the mail application allows file attachments to be dragged into the message, use Quicksilver to bring up the file quickly and **Paste** or drag directly from Quicksilver's first pane into the mail message.

Bring up a contact or email address in the first pane and use the **Compose Email** action to open a new blank email message with the To: field filled out in the mail application specified as the Email handler.  If the contact has more than one email address, the first one is used. To select a different address, bring up the Contacts contact, type <kbd>→</kbd> to see a results list of the contact’s information and select the desired email address. This may not work with contact plugins other than the Apple Contacts Module.

The **Compose Email** action opens a new blank message to be filled out, but Quicksilver also has the **Email Item…** and **Email To…** actions which send text and file attachments directly from the command window. Both of these actions have three variants. They are: **Email Item... (Compose)**, **Email Item... (Send)**, and **Email Item... (Send Directly)**, and there are similar ones for **Email To…**. The **Compose** variant uses the default email client (specified in the Email Handler) and opens a message compose window to be filled out. The **Send** variant also uses the default email client but doesn’t open a window; it sends the mail automatically. Both the **Compose** and **Send** variants will start the default email client if it’s not running. The **Send Directly** variant doesn’t use the default email client to send the message but does so directly from Quicksilver. As a result it's primary benefit is that the default email client does not need to be running. Note that if the default email client keeps a Sent folder (like Mail.app does) the outgoing message is not stored there. The **Send Directly** variant does get the SMTP configuration from the first mail account listed in Mail.app, so make sure that is setup correctly. 

The **Email Item…** actions use a contact or email address in the first pane and a file attachment or text to send in third pane. The **Email To…** actions are the same but entered in reverse; a file or text in the first pane, and a contact or email address in the third. The email address can be selected by typing <kbd>→</kbd> into a contact or by entering text mode and typing or pasting an address. 

If text is being sent it’s used as both the Subject and body of the message. To use a different subject use <kbd>></kbd><kbd>></kbd> to separate the subject and body using the form "subject>>message body". If files are being sent, the subject and body are set according to the Email Options Preference pane. Use the characters <kbd>%</kbd><kbd>@</kbd> in the template to have them replaced with the name of the file. If more than one file is sent using the comma trick they are replaced with some variation of “# Files in Folder” such as “2 Files on Desktop” or “2 [PDF Document] in Documents”.

The icons for the Email actions change based on what mail program is used to send the message.  In the previous image, Mail.app is configured as the Email handler so it’s icon is displayed for the **Email To…(Send)** action. In this image, the Quicksilver icon for the **Email To… (Send Directly)** action indicates Quicksilver is sending the mail, not Mail.app (because that’s what **Send Directly** does). However there’s a bug in B51, if there is only one mail handler installed, all the mail actions show a generic gear icon. I generated the screenshots in this section by having the Apple Mail Module plugin installed and selected as the handler and by also having the Gmail Module plugin installed, though even this doesn't always display correctly for me.

## Mail.app

The Apple Mail Module plugin installs actions to manipulate Apple Mail mailboxes and messages; including browsing through mailboxes in a results list. It installs a handler to select Apple Mail as the program to handle some mail actions. Note that the actions to send files and text as email are part of another plugin called E-mail Support which is installed automatically when the Apple Mail Module plugin is installed. For the various **Email To…** and **Email Item…** actions to work, make sure that the first mail account listed in the Maill.app account preferences has its Outgoing Mail Server (SMTP) configured correctly to send mail.

Activate Quicksilver and select Mail.app. Since it’s an application the default action is to open it. Notice there is a > in the results list next to Mail.app. Type <kbd>→</kbd> and the object pane changes to Inbox and the results list shows all local mailboxes, e.g., Inbox, Sent, and Trash as well as all custom mailboxes. IMAP mailboxes will not appear. To use them in Quicksilver drag them from Mail.app into the Catalog (e.g., under Custom). They won’t appear after typing <kbd>→</kbd> into Mail.app but they are selectable in the object pane.

Even though there is no > next to the mailboxes, typing <kbd>→</kbd> will move into the mailbox and show a results list of all the messages in that mailbox. The messages are listed in reverse chronological order, i.e., newest messages on top, for easy browsing.

The Apple Mail Module plugin installs three actions for messages: **Open**, **Delete**, and **Move to Mailbox...**. **Open** shows the message in a it's own window, **Delete** moves the message to Mail's Trash and **Move to Mailbox…** takes an argument in the third pane to specify the destination mailbox. For a mailbox object, the only Mail action available is **Open**. 

Using the **Open** action on Mail.app will open the last mailbox that was open. To easily get to the Inbox, create a trigger, in the first pane select Mail and then type <kbd>→</kbd> to select the Inbox, then choose *Open* as the action and bind this to a shortcut. I have <kbd>⌃</kbd><kbd>⌘</kbd><kbd>I</kbd> set to this to open my inbox.

There are two actions that are only available if Mail.app is in the object pane. One is **Get New Mail** which will get new mail in all accounts. If Mail is not running it will be started. If it is hidden it will still get new mail, but Mail will remain hidden. If there is no new mail, Mail will beep, even if hidden. The other action available on Mail.app is **Open New Mail**. It doesn't get new mail but if there are unread messages it will open a new window to show the message. If there is no new mail it will just beep. As of B51 triggers using these actions can't be saved.

Mail.app keeps a list of email addresses that have been sent to. The list is viewable by choosing Previous Recipients from the Window menu. Quicksilver's Apple Mail Module plugin also adds a catalog source under Modules called Recent Mail Addresses that accesses this list. It's useful to get to email addresses that aren't in the Contacts or other contact manager.

## Entourage

Quicksilver can't navigate email in Microsoft's Entourage but it can send email using the standard email actions: **Compose Email**, **Email Item…**, and **Email To…**.

Install the Entourage 2004 Module plugin. In Quicksilver's Preferences under Handlers choose Microsoft Entourage for Email. You may also want to set the  default Mail application for the system and in OS X this is counterintuitively set in the General tab of the Mail.app preferences. At least one person has the email actions working with Entourage 2008 using the Entourage 2004 Module plugin.

To use contacts stored in Entourage see the Entourage section under Contacts.

## Gmail

The only mail support Quicksilver has for Gmail is to use it to send email via the **Compose Email**, **Email Item…**, and **Email To…** actions. To configure this, first install the Apple Mail Module plugin and then install the Gmail Module plugin. As of B51, the Gmail plugin doesn't install the Email Support Module on its own, so that's why I suggest installing the Apple Mail plugin first. Then in Quicksilver's Preferences under Handlers choose Gmail Module. Note that the Gmail Module has nothing to do with Google Notifier.

Quicksilver will open the browser on a Gmail compose mail page, with the addresses filled in the To: field and the text "Hi" as both the subject and body of the message. As of version B51 there is no way to send an attachment with Gmail via Quicksilver. There is also no way to read mail via Gmail or browse mailboxes as there is with Mail.app.

## MailSmith

The only mail support Quicksilver has for MailSmith is to use it to send email via the **Compose Email**, **Email Item…**, and **Email To…** actions. To configure this, install the MailSmith Module plugin then in Quicksilver's Preferences under Handlers choose MailSmith.

## Other Mail Applications

In Quicksilver's Preferences under Handlers there is an option “Default”. This refers to the system default mail program which can be set in the Mail.app Preferences in the General tab under Default Email Reader. This sets the **Compose Email** action to use whatever application handles mailto: URLs. TODO: do the **Email to…** and **Email item…** actions work? Does the comma trick work?

## Teleflip

Teleflip is an online service that forwards email messages to United States cell phones as SMS messages. Currently the service is free up to 100 messages a month. Send email to an address of the form ###-###-####@teleflip.com filling in the cell phone number. The subject and body are sent, there is a 160 character limit. The Teleflip Module plugin makes it easy to send such messages from Quicksilver by constructing the address from a contact’s phone number. It installs two actions. With a phone number selected as an object use the **SMS Text via Teleflip…** action to send the text entered in the third pane via Teleflip. The reverse action is **SMS via Teleflip…**, use it to send text in the first pane to a phone number selected in the third pane. 

Note that a phone number object can also treated as text, so the **SMS via Teleflip…** action appears for phone numbers too. It will send the number as a message which can be convenient if that's what's desired. Bring up a phone number, type <kbd>.</kbd> to enter text mode and add more text if desired. Since this is probably less common, make sure **SMS Text via Teleflip…** is above (i.e., ranked higher than) **SMS via Teleflip…** in the action preferences.

# Note Taking Applications

## VoodooPad

For this section you’ll need the VoodooPad Module plugin installed. It adds three actions to Quicksilver: **Open Page**, **Append to VP Page…**, **Prepend to VP Page…**. It also adds a Catalog source called VoodooPad Documents under Modules which is *not* enabled by default. You’ll want to enable it by checking the box in the Catalog. It also adds a document scanner so if you add to the catalog a custom File & Folder Scanner source, you can choose VoodooPad Pages under Include Contents in the Source Options tab of the source. Unfortunately for B51 with VoodooPad 3.1.2 this didn’t work for me.

VoodooPad comes in three editions: VoodooPad Lite, VoodooPad, and VoodooPad Pro. Unfortunately the Quicksilver plugin will not work with VoodooPad Lite which is free. The plugin needs AppleScript support and that’s one of the features missing from the Lite edition. The plugin as downloaded will work with VoodooPad Pro which is the most expensive and full-featured edition. The plugin can be made to work with the plain VoodooPad edition by editing the script inside. Find the `VoodooPad Module.qsplugin` in the `~/Library/Application Support/Quicksilver/PlugIns/` directory in the Finder. Control-click on it and choose Show Package Contents to bring up a new Finder window, open the Contents folder and then the Resources folder. Open the `QSVoodooPadPluginAS.scpt` in Script Editor (you’ll need Voodoopad Pro.app for Script Editor to be able to open it) or your favorite text editor and change all the occurrences of “VoodooPad Pro” to “VoodooPad”. Save it and then it should work. 

You can bring up VoodooPad.app (or the Pro edition) and type <kbd>→</kbd> and you’ll see a list of VoodooPad documents (`.vdoc` files), but you can’t <kbd>→</kbd> into them. You can just type the name of VoodooPad page in one of those documents into Quicksilver’s first pane because of the catalog source. With a page in the first pane, you can use the **Open Page** action to bring up the page in VoodooPad. You can also add text in the first pane to the end of a page with the **Append to VP Page…** action and a page in the third pane. The **Prepend to VP Page…** action is similar but adds the text to the top of the page. You might want to configure a trigger for something like Current Selection (**Append to VP Page…**) To-Do to easily add selected text (via the proxy object) to a To-Do page in VoodooPad.

VoodooPad adds two services: **Append to Services Drop Page** and **Make New Page**, both of which become actions you can use on any text with the Services Menu Module plugin.

## Yojimbo

For this section you’ll need to install the Yojimbo Module Plugin. It adds four actions to Quicksilver, **Add to Yojimbo**,  **Archive to Yojimbo**, **Show in Yojimbo**, and **Append Text (Makes Plaintext)**. The first three are enabled by default, but the last one is disabled. To use it, you’ll need to enable it in the Action Preferences. It also adds a Catalog source under Modules called Yojimbo Items, which finds entries in your Yojimbo database.

Since the Yojimbo Items catalog source is enabled by default, you should be able to bring up any Yojimbo item by just activating Quicksilver and typing its name until it appears. You can also bring up the Yojimbo.app and type <kbd>→</kbd> to see a results list of all your  Yojimbo items. Given a Yojimbo item in the first pane, you can use the **Show in Yojimbo** action to open Yojimbo to that item. If you enable the action, you can also add to a Yojimbo item by using the **Append Text (Makes Plaintext)** action with a text argument in the third pane.

You can add text notes to Yojimbo by using the **Add to Yojimbo** action with a text object in the first pane. You can add URLs to Yojimbo in two ways. With an URL in the first pane, the **Add to Yojimbo** action will add it to Yojimbo’s Bookmarks and the **Archive to Yojimbo** action will add it to Yojimbo’s Archives.

## WikityWidget

[WikityWidget](http://inkspotting.com/wikity/) is a Dashboard widget that behaves a like a small wiki. Think of Sticky Notes on steroids. If you use this you’ll want to install the WikitWidget Module plugin. Be sure to install WikityWidget before you install the plugin, or else you might have problems with the QSWikitPlugin catalog source that is installed in Modules. The plugin also adds four actions: **search Wikit**, **delete Wikit**, **append to Wikit**, and **prepend To Wikit**.

WikityWidget uses the word Wikit to mean a page. With text in the first pane, you can add it to the beginning or end of a wikit page with the **prepend to Wikit**, and **append To Wikit** actions respectively. Both take a wikit page as the argument in the third pane. You can also search for a wikit with some text using the **search Wikit** action with the text to find in the first pane. It returns a results list of wikits matching the search string. 

Unfortunately there’s no action to open a wikit specified in the first pane (e.g., as the result of the **search Wikit** action) in the widget. There are three actions that you can use with a wikit in the first pane. You can delete the page with the **delete Wikit** action. You can also use the **prepend to Wikit**, and **append To Wikit** actions with text in the third pane. Yes these actions work with their arguments reversed.

# Random Notes

> This section is a random collection of notes I've gathered of things to be added to the manual. Please take these and either incorporate them in the main text or remove those that are out of date.

## Results List

There are a bunch of ways of choosing an item.

You can type the start of it and then using the mouse scroll through the results list and click on the item you want. That sounds like what you are doing.

You can continue typing the whole thing and it will eventually appear as the first choice. Over time, you should have to type less of the item to get it to the top as QS learns what you do often.

If the results list is appearing slowly go to the Command preference pane and set "Show Other Results" to "Immediately"

You can type the beginning of what you want and then <kbd>↓</kbd> into through the results list. <kbd>↑</kbd> and <kbd>Page-Up</kbd> and <kbd>Page-Down</kbd> and <kbd>Home</kbd> and <kbd>End</kbd> work as well. People like this method because it's not using the mouse, so it's faster (you don't have to move your hand to the mouse).

Even faster is to configure the "Spacebar behavior" in the Command Preference Pane to "Select Next Result". Now <kbd>space</kbd> acts like <kbd>↓</kbd> and you don't have to move your hand to the arrow-keys (<kbd>space</kbd> is right under your thumb).

You can explicitly assign default choices for a sequence of letters you type. Say you have a "Documents" folder and a `document1.txt` file. Type <kbd>D</kbd> and they both appear. In the results list right-click on Documents and choose "Set as Default for D" (for this to work it can't be the first choice in the list, since it's already the default)). Now activate QS again and type <kbd>d</kbd><kbd>o</kbd><kbd>c</kbd><kbd>u</kbd> and set that as the default for `document1.txt`. Now you can always choose "Documents" by typing "d" and `document1.txt` by typing <kbd>d</kbd><kbd>o</kbd><kbd>c</kbd><kbd>u</kbd>.

If you want to choose a default that's not at the beginning of the name use the **Assign Abbreviation** action to make an abbreviation (which behaves like a default but is separate). E.g., I do a lot of searching in the internet movie database, which is www.imdb.com. I want this assigned to <kbd>M</kbd> (for movies) but if I just type <kbd>M</kbd> I get a very long results list and imdb isn't towards the top and I don't want to scroll through the long list to find it to right-click to set a default. Instead select www.imdb.com in the first pane (type it all or do whatever works), and choose the **Assign Abbreviation** action then in the third pane type <kbd>M</kbd> (in text mode). Now if you activate quicksilver and type <kbd>M</kbd> www.imdb.com will appear in the first pane with the default action in the 2nd. Probably all you have to do is type <kbd>return</kbd>. Very fast.

If you want it even faster. Setup a trigger. This way you can bring up your choice with just one keystroke (perhaps something like <kbd>⌥</kbd><kbd>⌘</kbd><kbd>m</kbd>) or a mouse gesture, without even invoking QS first.

Show Children Split View

My `~/Applications/` has enough in it I've started putting some sub-folders.  But they don't show up in the catalog If i create a custom entry I get folders inside the `.apps` (e.g., Contents) I can't figure out how to select a folder in the Source Options.  Any hints? so I'd like my `.apps` and the folders in the catalog but not what is inside the packages

hmelman: can't you specify types of things that get added to the catalog?

how do you specify the type "folder"? (and I can't see a way to specify "application" unless you copy it from a copy of one of the built-in Application sources)

type folder is specified by 'fold' -- note that includes single quotes i think these things may be discoverable via appropriate Info.plist files

ok, that works but unfortunately includes folders inside .app's :( but I can create a 2nd source for just the top level folders that combined with a depth 3 of just applications gives me what I want

http://quicksilver.infogami.com/ExecutableFileActions

## Using Spotlight sources in the Catalog: 

http://blacktree.cocoaforge.com/forums//viewtopic.php?p=19515#19515


## iTunes artwork not displaying?

I was having this problem as well. Some tracks were displaying cover artwork correctly while others were displaying only the generic iTunes icon. All tracks had the artwork attached to the file. 

After searching these forums, (can't find the link) the answer turns out to be setting the proper ID3 tag for each track. It seems that version 2.3 or 2.4 works in QS but v.2.2 or less doesn't. 

Select all the tracks that aren't displaying correctly, go to the iTunes Advanced Menu and select Convert ID3 Tags... In the dialog box you'll be given the option to select which Tags you want. After you switch to v.2.3 or 2.4 you should be good to go.

## Adium 

The older Adium plugin (as of B51) works with Adium 0.89.1, it does not work with Adium 1.x. It can also be a little tricky to install if you’re upgrading from an older version. It’s actually two plugins (one for Quicksilver and one for Adium) that communicate with each other. Both parts come with the Quicksilver plugin and when you run it the first time it installs the Adium part as `~/Library/Application Support/Adium 2.0/PlugIns/Quicksilver.AdiumPlugin`. If the plugin isn’t working it’s probably an issue with the Adium part. To reinstall it do the following:
1. Quit QS and Adium 
2. Open Terminal and run the command: 
    `defaults delete com.blacktree.Quicksilver AdiumPluginInstalled`
3. Remove `~/Library/Application Support/Adium 2.0/PlugIns/Quicksilver.AdiumPlugin`. Note that the PlugIns directory might have a lowercase i, if so remove any Quicksilver.AdiumPlugin from there too.
4. Double-click on `~/Library/Application Support/Quicksilver/PlugIns/Adium Module.qsplugin`

## Nice trick from Rob McBroom with OpenMeta Plugin:

So I've started tagging all those one-offs with "Quicksilver Catalog" and then I added a custom entry that puts anything with that tag in the catalog, and I have a tag for things that I'm currently working on and a trigger for Current Document <kbd>⇥</kbd> *Add Tag…* <kbd>⇥</kbd> Work On. So as soon as I create something in TextMate, I can tag it or tag the current directory in Terminal even. Wish I could tag URLs.

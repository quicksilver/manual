# iTunes

The iTunes Module plugin installs:

- an iTunes preference pane
- catalog sources under Modules, iTunes for “iTunes Playlists” and “Control Scripts” 
- several iTunes related proxy objects
- four actions
- a trigger set with many unbound triggers

## Browsing

Activate Quicksilver and select iTunes in the first pane; iTunes does not have to be running. Typing <kbd>→</kbd> will show a new results list of several ways to browse the iTunes library:

- Recent Tracks
- Show Playing Track
- Browse Genres
- Browse Artists
- Browse Composers
- Browse Albums
- Browse Tracks
- Music Library
- all the playlists and smart playlists

If the iTunes Playlists catalog source is enabled, all of these items are also in the global catalog, i.e., available in the first pane after activating Quicksilver. However, specific songs, albums, artists are never in the global catalog, only these grouping objects are. This keeps the catalog at a reasonable size. Quicksilver startup might be slow if there’s a large iTunes library. If this is the case, consider disabling the iTunes Playlists catalog source.

Most of these have a > on the right side of the results list. Typing <kbd>→</kbd> moves into them showing  the selected artist, album, etc. If the Show Artwork option is checked in Quicksilver’s iTunes Preference pane then Quicksilver will look in the song file for album art and display it in the command window. The default action is **Play**.

To search quickly for a track, create a trigger for Music Library **(Show Contents**). Similar triggers for Browse Artists or Browse Albums are also useful. See below for the pre-installed triggers for these functions.

As shown on the left, individual tracks don’t have a > symbol to the right in the results list, however typing <kbd>→</kbd> still works. On the right, the new results list shows the metadata values found in the track file (in this case genre: Rock; Artist: Rusted Root; Composer: Michael Glabicki; Album: Remember) and allows browsing through the whole library matching the selection. Select Rusted Root and type <kbd>→</kbd> to see a results list of all albums by them including an All Albums proxy object. Select an album and type <kbd>→</kbd> to see a list of songs in it. Genres open to artists, artists and composers open to albums, and albums open to tracks.

Here’s a place where proxy objects shine. There is a proxy object called Track Now Playing; selecting it and typing <kbd>→</kbd> while iTunes is playing a song shows the track playing. So the generic proxy is replaced with the actual track object. Type <kbd>→</kbd> again to browse by genre, artist, album, etc. Create a trigger for Track Now Playing (**Show Contents**) to have quick access to all songs by the current artist or on the same album, etc. There are also proxy objects for Album Now Playing, Artist Now Playing and (the differently named) Current Playlist. 

There are two other iTunes proxy objects and they work with things selected in the iTunes application itself. Current iTunes Selection represents the selected track and Selected Playlist represents the selected playlist.

The default action for a track, album, artist, or genre is **Play**. Selecting an individual track and playing it will have iTunes do just that (Quicksilver doesn’t play it, iTunes does), starting iTunes if necessary. Selecting a set of tracks (either with the comma trick or by picking an album or artist) creates a playlist in iTunes called Quicksilver, populates it and starts playing it. There are also iTunes specific actions for **Play in Party Shuffle**, **Play in Next Party Shuffle** and **Add to End of Party Shuffle**. See the iTunes documentation for how to use Party Shuffle.

The iTunes **Play** and various Party Shuffle actions are probably the most commonly used, but since a track is also a file, all the file actions are accessible as well. Choosing **Open** will play the song just as **Play** does. **Reveal** will open a Finder window showing the track file in its folder. Anything Quicksilver can do to a file, it can do to a track, email it to a friend, add a tag, compress it, etc.

## Controlling iTunes and Triggers

The iTunes Plugin also installs scripts to control iTunes. These are found in the catalog under Modules, iTunes, Control Scripts. The scripts do things like play, pause, next song, mute, rate the track etc. To use them, select a script in the first pane and choose the **Run** action in the second.

Triggers for controlling iTunes are so popular that Quicksilver installs them by default in an iTunes triggers set. By default they are not assigned to shortcuts but it’s easy to do so. Shown here are the keys I’ve chosen. With these Triggers I can control iTunes without changing from whatever I’m doing. 

## Preferences

The plugin also adds a preferences pane in Quicksilver with some iTunes specific options. 

If the Show Artwork option is checked then Quicksilver looks in the song file for album art and displays it in the command window. 

If the art isn’t displaying for mp3 files that do have art it’s probably because the mp3 files use an older version of the ID3 tags that store metadata. To upgrade, select the tracks in iTunes and in iTunes’ Advanced menu choose Convert ID3 Tags…. (One person reported that he had to convert before adding artwork to the file and if the art was already there he had to remove it, convert and then re-add the art). 

The new feature in iTunes 7 to download artwork stores it in a new database (not inside the actual MP3 or AAC files) and as of B51 Quicksilver’s iTunes Module can’t display it. However, if there isn’t art in the song file Quicksilver can use one of the online art services to find the album. The plugins that do this are: Clutter Artwork, Synergy Artwork, Sofa Artwork and Music ARTchive Artwork. Obviously if the services are unavailable these plugins won’t work.

The Show ~Unknown Entries option does TODO.

The Group Compilations option creates a Compilations object to collect those songs marked as being in a compilation when displaying them in the context of an artist.

The Fast Browser Play option chooses albums, genres, etc. using a faster but less accurate algorithm. It may add tracks with similar names. 

Monitor Recent Tracks and Display Track Notifications pops up a small window when the playing song changes that shows the name, artist and album playing. I keep iTunes hidden and use the notifications to see the titles of songs as they change. To use Growl for notifications, install the Growl plugin and select it in the Handlers Preferences pane. For a more manual approach one of the triggers the iTunes plugin installs is Show Playing Track. Select a shortcut for it and use it to see a notification on demand. Display Track Notifications must be enabled for Show Playing Track to work.

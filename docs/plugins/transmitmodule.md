#Transmit 4

Favorites Access & Uploading.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 4.1.1
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


## Transmit Plugin

The Transmit Plugin allows you to interact with your Transmit favorites,
upload files to them, and open and mount FTP/SFTP etc. URLs in Transmit

### Catalog

The Transmit Plugin adds a 'Transmit Favorites' catalog entry to the
Quicksilver, which can be seen in the 'Plugins' section of the [Catalog
preferences](qs://preferences#QSCatalogPrefPane). Enabling this entry means
you can search for your Transmit favourites in Quicksilver's 1st pane.

You can also get a full list of your Transmit Favorites by finding
'Transmit.app' in Quicksilver's 1st pane, and pressing the right arrow key `→`
(or the forward slash key `/`).

### Actions

**Connect**

This action opens an FTP URL or a Transmit Favorite in Transmit. Supported URL
schemes are `ftp://`, `sftp://` and `ftps://`

**Mount as Disk**

The 'Mount as Disk' action uses TransmitDisk to mount the specified transmit
Favorites as a mounted disk on your Desktop. This action is only valid for
Transmit Favorite objects

**Upload to Site… and Upload File…**

These actions upload single or multiple files to a given Transmit Favorite.
The 'Upload to Site…' action takes a list of files (using Quicksilver's comma
trick) in Quicksilver's 1st pane and requires a Transmit Favorite in
Quicksilver's 3rd pane. The 'Upload File…' action is a reverse of this,
requiring a Transmit Favorite in the 1st pane and a list of files in the 3rd
pane.
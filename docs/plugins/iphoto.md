# iPhoto

Adds Albums to the catalog.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 2.0.1
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


## iPhoto Plugin

The iPhoto plugin for Quicksilver adds iPhoto's albums and events to the
Quicksilver catalog. These items are also available by entering into
iPhoto.app (using → or /). iPhoto albums and events within Quicksilver contain
all the pictures available within iPhoto; useful for copying or moving photos.  
The plugin also adds several actions for manipulating albums, and proxy
objects for dealing with selected items in iPhoto.

## Catalog

### iPhoto Albums

Adds your iPhoto albums and events to Quicksilver's catalogs. The same items
are available by entering into iPhoto.app (using → or /)

## Actions

### Start Slideshow

Available for iPhoto albums only. ( **Note: Not available for iPhoto events
due to a limitation by Apple** )

This action starts a slideshow for the selected album.

### Show

Available for iPhoto albums only. ( **Note: Not available for iPhoto events
due to a limitation by Apple** )

This action shows the selected album in iPhoto, and activates the application.

### Empty iPhoto Trash

This action is available when iPhoto.app is selected in Quicksilver's 1st
pane. Executing the action launches iPhoto and empties the iPhoto trash.

## Proxy Objects

### Current iPhoto Selection

Returns a list of the currently selected photos in iPhoto. If no photos are
selected, then the currently active album is returned.

### Current iPhoto Album

Returns the currently selected iPhoto album. Behaves in the same way as the
'Current iPhoto Selection' proxy object, except the current active album is
always return, even when photos are selected.
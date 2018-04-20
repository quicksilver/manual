# File Compression

File Compress/Decompress Actions.

 Summary                    | &nbsp; 
---------------------------:|:--------------------
 Available on macOS version | 10.11, 10.12, 10.13
      for Quicksilver build | 4024


## Overview

The File Compression Plugin allows compression and decompression of files
using Apple's Archive Utility application. In addition, it supports `7z` files
using [p7zip](http://p7zip.sourceforge.net/).

## Actions

Compress

    Compresses the object(s) in the first pane using the default compression type (see 'Preferences' section below)
Compress Using…

    Allows the object(s) in the first pane to be compressed using one of: `zip`, `tbz2`1, `tgz`, `cpio`, `cpgz`, `7z`
Decompress

    Decompress files using Archive Utility or `p7zip`

## Preferences

The plugin adds a preference pane to Quicksilver, allowing you to:

  * Choose whether to compress files to a temporary location first
  * Choose the default compression type to use for the 'Compress' action

## Trigger Events

Event Triggers can be run based on two events in this plugin: Compress and
Decompress. For both actions, the "Event Trigger Object" will refer to the
archive file.

## Decompressing Multiple Times

If you decompress multiple times into the same folder, Archive Utility will
rename files at the top-level to avoid a conflict. By contrast, `p7zip` will
rename files _within nested folders_ , so do not be surprised if decompressing
multiple times does not produce separate copies of a decompressed folder.

* * *

  1. The `tbz2` extension is used as opposed to `tbz`, since this is the OS-preferred extension. ↩
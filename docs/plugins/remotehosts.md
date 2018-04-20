# Remote Hosts

Provides actions that can be taken on computers.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 1.7.0
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


# Remote Hosts

## A Quicksilver plug-in for dealing with a large number of computers

Given a text file with a list of machines in it (either hostname, Fully
Qualified Domain Name, or IP address), this plug-in indexes them as "remote
host" objects and provides the following actions:

  * SSH
  * SSH as root
  * SSH as… [username in 3rd pane]
  * Telnet
  * Telnet to port… [port number in 3rd pane]
  * FTP
  * SFTP
  * SFTP Starting at Path…
  * HTTP
  * HTTPS
  * Screen Sharing (VNC)
  * Browse with CIFS
  * Mount share with CIFS… [share name in 3rd pane]
  * Browse with AFP
  * Mount share with AFP… [share name in 3rd pane]
  * MS Remote Desktop [requires the CoRD application]
  * Get Host Info

There is also a "Use as Remote Host" action that applies to text. If you type
a hostname by hand, paste it, or pull it from an application using ⌘⎋ or ⌘G,
this action will "convert" it to a remote host in Quicksilver so you can
connect to it, etc.

Some of the above actions also provide "alternate" actions. Hit ⌘↩ instead of
↩ to run the alternate.

Action | Alternate  
---|---  
SSH | SSH as root  
FTP | Get FTP URL  
HTTP | Get HTTP URL  
HTTPS | Get HTTPS URL  
  
The "Get XYZ URL" actions are useful in situations where you need to paste the
URL to a remote machine, or want to open it in something other than the
default application.

Selecting a host in Quicksilver and hitting → or / will provide the following
information (if available):

  * IP Addresses and aliases

Quicksilver treats these as strings, so you can use "Large Type", paste them
into the current application, send them via IM or e-mail, etc.

  * Lights-Out Management

The LOM address is itself another "remote host" in Quicksilver. With it
selected, you can use one of the above actions to connect to it.

  * Host Info URL

If you've defined a URL in the preferences that provides info for hosts, it
will appear here.

## Catalog Sources

The plug-in will scan `~/.hosts` for a list of machines by default. (You can
use any file. See below.) The file is treated as UTF-8. It should contain one
host per line. The hostname or FQDN should be the first thing on each line,
but other metadata is allowed (separated by a single space). A port can also
be specified. An example might look like this:

    
    
    server1.example.com
    server2
    server3.example.com ostype:linux
    server4.example.com ostype:linux lom:10.1.2.3 label:test
    server5.example.com:8080
    appleserver.example.com icon:com.apple.xserve ostype:macosx
    windows.example.com ostype:windows
    somehost ostype:solaris
    webhost1 groups:Web
    webhost2 groups:Web
    

You may already have a file like this for completion in your shell. If you
have existing metadata in this file, it shouldn't break anything, but it won't
necessarily be useful in Quicksilver.

The plug-in scans for items on each host's line that look like this:
`key:value`. All such data will be stored along with the host in Quicksilver's
catalog, but there are currently only a few that will affect its behavior.

  * `ostype`: OS type should be a short, generic word, like "solaris", "linux", "windows", etc. Currently, the only behavioral distinction is between "windows" and everything else. The other purpose served by `ostype` is to determine an icon for the host. Icons are included for the following OS types:
    * bsd
    * debian
    * fedora
    * gentoo
    * linux
    * netbsd
    * opensuse
    * redhat
    * solaris
    * suse
    * ubuntu
    * unix
    * windows
  * `icon`: You can specify an icon to use for a host if you don't like its default. This can be a bundle identifier, like "com.apple.Terminal", the name of an icon in the CoreTypes bundle like "com.apple.mac", or the path to an icon or image file. The usual types of images are supported, but they will most likely get squished into a square (depending on which Quicksilver interface you use).
  * `lom`: The Lights-Out Management address will only apply to fancy, rack-mounted servers that provide some sort of network-based LOM. If you don't know what this means, you probably don't need to worry about it. The information itself should be an IP address, hostname, or FQDN for the system's LOM interface.
  * `label`: By default, all hosts in your catalog will be labeled with their hostname, FQDN, or IP address (as it appears in your file). Setting a label in the file will append to the default, not replace it. Quicksilver searches the text in the label as you type to search for things. If you have many hosts with similar names, they can be hard to get to quickly. Using this item to append to the label can be useful to group or "tag" systems for faster searching.
  * `groups`: A comma separated list of groups you want the host to belong to. Names can't contain spaces at this time. More information on using groups can be found under Tips.

You can optionally pull hosts from `~/.ssh/known_hosts`. There is a preset
(disabled by default) under "Remote Hosts" in the Plugins section of the
Catalog. If you want to get hosts from an arbitrary file, add a new custom
catalog entry and choose "Remote Hosts" from the drop-down, then choose the
file for the new entry.

There is also a preset named "SSH Config Hosts" that will read hosts from
`~/.ssh/config`. These hosts will be ignored if they were found in one of the
other files (to preserve any metadata).

## Preferences

Display Hostnames

    

If hosts are defined using their fully qualified domain names, you can choose
to display only the hostname in the main interface.

You will still be able to search for the FQDN, and the FQDN will still be used
when running actions.

Host Info URL

    

If you have a web-based front end for an inventory or monitoring tool that can
provide information about individual hosts, you can define the URL here. Put
`***` in the URL where you want the hostname to appear. For example, if
http://info.domain.tld/summary/webhost1 provides information for `webhost1`,
you could define the URL as http://info.domain.tld/summary/***.

If this is left blank, the Get Host Info action will not be available.

Use hostname in URL

    

If you have hosts in your catalog using their Fully Qualified Domain Name, but
the info URL expects the hostname, enable this preference to remove the
domain.

### Tips

After installation, you may want to check the precedence of the actions and
make sure they're to your liking. The actions only apply to "remote hosts" in
the catalog, so moving them up rather high on the list shouldn't interfere
with other tasks. You may also want to disable some of the ones you never
think you'll use.

For more than a few machines, you should use a script to generate a `.hosts`
file from DNS, LDAP, a database, or some other authoritative source if
possible, rather than managing it by hand. You might also schedule a job to
update the file on a regular basis.

For hosts you want to frequently connect to at the same time, you can assign
them to one or more groups in the scanned file. Any groups you define will be
added to the catalog. You can search for them by name, or by name plus "Remote
Host Group". You can use the SSH and Telnet actions to connect to all hosts in
the group. Hitting → or / will reveal the group's members.

If you find yourself using "SSH as…" frequently, you may want to add something
like this to your `~/.ssh/config`:

    
    
    Host server.domain
      User someuser
    

See the `ssh_config(5)` man page for details.

For **iTerm** users, the SSH and Telnet actions are intentionally not specific
to Terminal. They simply send an address to the OS to be opened. Configure
your system to open `ssh://` and `telnet://` locations using iTerm if you want
to use that instead of Terminal.

Finally, don't forget the "comma trick". You can select multiple hosts using
the comma or ⌘A, then connect to them all at once.

## SSH Keys

You can optionally add your SSH public keys to the catalog by enabling the
preset in your Catalog preferences. This makes it easy to paste the key to a
remote machine, or into a message to a remote sysadmin.

If the key has a descriptive comment, that will be used as its name.
Otherwise, the file name will be used.

* * *

This plug-in uses icons from the [Open Icon
Library](http://openiconlibrary.sourceforge.net/).
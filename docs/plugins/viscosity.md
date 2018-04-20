# Viscosity

Access VPN connections in Viscosity.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 1.3.3
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


# Viscosity Plug-in

The VPN connections you've defined in Viscosity get added to the catalog. You
can either search for them directly or right arrow into the Viscosity
application.

There are two actions available for a Viscosity connection:

  * Connect to VPN
  * Disconnect from VPN

There are also two actions available if you select the Viscosity application
in the first pane:

  * Connect All VPNs
  * Disconnect All VPNs

When you first install the plug-in, these actions will be higher in priority
than "Open", which is normally the default for applications. If that's not
what you want, move them down the list in your Quicksilver preferences.

The plug-in tries to be smart about which actions to display. For instance,
you won't see "Disconnect from VPN" unless that connection is currently
active.

NOTE: If Viscosity isn't running, any of the "Connect…" actions will start it.
This is generally what you want, but be aware that if you've configured
certain VPNs to connect on launch, they will be connected regardless of what
you are trying to do via Quicksilver.

## Event Triggers

If the Event Triggers plug-in is installed, you can configure actions to run
when a VPN is connected or disconnected via Quicksilver. The Event Trigger
Object proxy will refer to the connection in question.
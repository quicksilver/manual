# Networking

Manage wireless connections, locations, and get information.

 Summary                    | &nbsp; 
---------------------------:|:--------------------
 Available on macOS version | 10.11, 10.12, 10.13
      for Quicksilver build | 4024


## Quicksilver Networking

### Catalog

#### Presets

  * Network Locations - Adds any netowrk locations you've configured in System Preferences to the catalog. (Disabled by default)
  * Wireless Interface - A virtual entry that represents your Wi-Fi connection. Use this to turn the interface on and off, or to view available networks by hitting → or /. (For 10.6 users, this will appear in the catalog under the name "AirPort".)

#### Proxy Objects

  * IP Address - The IP address(es) currently assigned to your computer.
  * External IP Address - The IP address remote sites will see when you connect to them.

### Actions

  * Switch to Location - when a network location is selected in the first pane, this will allow you to set it as the active location.
  * Turn Wi-Fi On - Enable power for the wireless interface. This action is only available when power is off. (The action is named "Turn AirPort On" for 10.6 users.)
  * Turn Wi-Fi Off - Disable power for the wireless interface. This action is only available when power is on. (The action is named "Turn AirPort Off" for 10.6 users.)
  * Toggle Wi-Fi Power - Toggle power for the wireless interface. Useful for creating triggers. (The action is named "Toggle AirPort Off" for 10.6 users.)
  * Disconnect Current Network - Disassociate from the current wireless network, but keep power for the interface on.
  * Connect to Network - Connect to the selected wireless network. This is only available for unsecured networks and secured networks for which you have credentials stored in your keychain.
  * Connect to Network (via Menubar) - For secured networks that can't be automatically joined, this action will attempt to click through the menu bar to select the network for you, which should result in you being prompted for credentials.
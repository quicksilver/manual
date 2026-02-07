# Plugins

Quicksilver is designed with a central core that implements some basic functionality, but most of the features are implemented in plugins. You can pick and choose which plugin functionality you want, but must install the plugins before that functionality is available. Managing the plugins including finding, installing, enabling, and removing is done entirely from within Quicksilver in the Plugins Preferences (though additional configuration in Preferences or the Catalog may be useful or necessary). You can bring it up from the menu, or by activating Quicksilver and typing <kbd>⌘</kbd><kbd>"</kbd>.

The plugins are shown in the right pane, with a checkbox showing if they are enabled, a column showing the version number, and the date the installed version was released. The left panel shows sets of plugins:

  * **Recommended** - Plugins can appear on this list based on the applications you have installed, files that might exist on your system, or because they’re considered generally useful. This is also the list Quicksilver presents during the initial setup process.
  * **Installed Plugins** - All installed plugins are listed here. Only those that are checked are enabled. Those not checked are installed, but disabled.
  * **Disabled** - Plugins you’ve installed, but disabled are shown here. These may be candidates for removal.
  * **Not Installed** - To quickly see if there are any potentially useful plugins you don’t yet have, you can see a list of ones you don’t have installed.
  * **All Plugins** - All available plugins from the update server are listed here. Checked plugins are installed and enabled, unchecked plugins are not installed. <kbd>⌥</kbd>-click on this to show some hidden plugins.

    This section can be expanded to show a list of categories. Plugins can be in more than one category.

Checking a plugin will enable it, downloading and installing it if necessary. Selecting a plugin and clicking the ⓘ button will open a drawer with additional details:

  * Author(s)
  * A short description
  * Installed version (if installed)
  * Latest version available from the update server (based on your version of Quicksilver and macOS)
  * Status, which normally shows “Loaded”. If a plugin fails to load for some reason, you might find a helpful message here.

Clicking the `?` button will open the plugin’s documentation in a new window. Reading this for any installed plugins is highly recommended. Some less obvious features and uses can be discovered in the docs.

Selecting one or more plugins and clicking the gear button opens a pop-up menu of things you can do to plugins including install, download, copy, and delete. Delete is the only one you’ll typically use from this menu. The last three items in the menu are options you can enable or not.

The Refresh button (circular arrow) will refresh the list of plugins from the update server.

To disable a plugin, uncheck it. Its features will no longer be available but its code will still be loaded into memory. To clean up this memory (possibly fixing stability issues), restart Quicksilver. The plugin is still installed on disk (so it will appear unchecked in the Installed Plugins view) until it is deleted.

If you expect to see a plugin in the list and don’t, try refreshing the list of plugins. 

If you’re having problems installing plugins check the ownership and permissions on `~/Library/Application Support/Quicksilver/PlugIns/` and its parent directory. Use the Finder’s Get Info command (from the File menu) to see the Ownership & Permissions of a folder. It should be owned by you and you should have permission to read and write it. Usually quitting Quicksilver and removing (or moving) the PlugIns folder or its parent Quicksilver folder and restarting Quicksilver (allowing it to recreate the folder) will solve any problems. Of course removing the Quicksilver folder will remove any customizations you’ve made.

#Keychain

Access to Keychain entries.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 1.1.3
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


# Keychain plugin

This plugin gives Quicksilver the ability to access data stored in Keychains
-- Safari passwords as well as any other data added by applications -- and
allows login names and associated passwords to be directly manipulated or
retrieved directly by copy/pasting.

## Catalog

Keychains

    This will add "login" and "System" keychains to your catalog as well as any others you have defined. You can also access keychains by selecting Keychain Access and hitting → or /. With a keychain selected, hit → or / to access individual items.

## Actions

With a keychain selected, the following actions will be available:

  * Lock
  * Unlock

With a keychain item selected, the following actions will be available:

  * Copy Account
  * Paste Account
  * Get Account
  * Copy Password
  * Paste Password
  * Get Password

### Terminology

Account

    The value from the "Account" field in Keychain Access. This is usually the username.
Password

    The password stored with this item. You will be prompted to allow Quicksilver access to an item if it hasn't been granted before.
Get

    Display the account or password as text in Quicksilver's first pane for further action.
Copy

    Copy the account or password to the clipboard.
Paste

    Paste the account or password to the active application.
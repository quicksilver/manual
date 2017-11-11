# Manual Style Guide

The original rationale for the manual was to be a comprehensive guide for Quicksilver. There were many short tutorials and How-To's for specific things online but nothing that covered all of Quicksilver in depth. Terminology was inconsistent (particularly what the three panes were called) and there weren't good explanations of why Quicksilver is a great application that everyone should use. There were pockets of info around and that did draw people of all skill levels to try it and given the nature of Quicksilver's configuration, it led to a lot of support questions from people who didn't install everything needed for a particular feature.

Given that Quicksilver has so many functions and each user tends to have specific use cases in mind (for some iTunes control was their introduction, for others it was email and contacts, for others finding and manipulating files)  I wanted the manual structured so that people could get directly to functionality that was interesting to them, find complete info, but be shown other things of interest while avoiding duplication as much as possible.

The Introduction is intended for everyone to read through from beginning to end. New users find out what to use Quicksilver for and experienced users have terminology defined and perhaps learn some advanced invocation methods. 

The Confiiguration section walks through all of Quicksilver's preferences in depth, particularly how to install plugins and setup triggers so later sections could just refer to it.

The Features section covers all the plugins, in detail. Each section includes general usage and configuration instructions, as well as troubleshooting hints and tips for using features more efficiently using advanced Quicksilver features. It includes every cool Quicksilver example I ever found. New users should be able to start using the features quickly and experienced users will probably find something new about many features. 

- Explain explicit installation steps for each feature at the top of the section. include which plugins to install, everything that plugin installs (actions, handlers, an advanced preference pane, a catalog source, etc.) and how to configure them (e.g., if an action is installed but disabled by default, tell the user to enable it).. 
- Explain what Quicksilver does, remember that it customizes itself for each user so be explicit about what the user types and Quicksilver's behavior and why the user might see different behavior if they type the same thing. Remember that people  rank actions differently particularly if different plugins are installed and catalogs are configured differently. 
- People come to Quicksilver with very different skill levels. Some are new to OS X and don't know details of how to install .dmg files or other common conventions. Remember that people use keyboards in different languages with keys in different places (e.g., ` and ~ behave the same because they're on the same key on US keyboards).
- When describing new features, include the version number it was added, e.g., "As of 1.4.1 QS ..." People using older versions will know something won't apply to them. This version decoration can removed as older versions not supporting the feature are unsupported.
- Including details of how to avoid common problems. E.g., don't add a catalog source that scans to infinite depth because it will use a lot of memory and make QS slow.
- Images of example commands should all be using the Bezel interface using the default colors. It's popular, built-in and smaller than Primer. Obviously use other interfaces if it's important for some feature/concept.
- Actions should be in **bold**
- Use `code` for file names and command line tools.
- Use `<kbd>` for input text, surrounding each key individually. E.g, <kbd>⌘</kbd><kbd>;</kbd>, <kbd>⌥</kbd><kbd>⌘</kbd><kbd>S</kbd>, <kbd>space</kbd>, <kbd>return</kbd>, and spelling out input strings  <kbd>D</kbd><kbd>e</kbd><kbd>s</kbd><kbd>k</kbd>
- Use the unicode symbols for various keys (as they appear in menu shortcuts). 
	- The order for modifiers should match what OS X does: <kbd>⌃</kbd><kbd>⌥</kbd><kbd>⇧</kbd><kbd>⌘</kbd> 
	- Use these for the arrow keys: <kbd>→</kbd>, <kbd>←</kbd>, <kbd>↑</kbd>, <kbd>↓</kbd> and <kbd>⌫</kbd> for delete and <kbd>⎋</kbd> for esc
	- The Quicksilver preference pane has buttons on the bottom bar, use these for them: ↻ ⓘ
- Use TODO to tag text to be changed/added.
- The current text explains things in prose and the pdf used a lot of images. Changing procedures to lists is probably a good thing. TODO: how to add images to the wiki? What directory should they be in and how should the URL be structured?

The reason to be explicit about things is to reduce the number of support questions. The reason to be comprehensive is to get people to find out and try new features.

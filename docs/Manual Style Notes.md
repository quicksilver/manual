# Manual Style Guide

## Rationale

The original rationale for the manual was to be a comprehensive guide for Quicksilver. There were many short tutorials and How-To’s for specific things online but nothing that covered all of Quicksilver in depth. Terminology was inconsistent (particularly what the three panes were called) and there weren’t good explanations of why Quicksilver is a great application that everyone should use. There were pockets of info around and that did draw people of all skill levels to try it and given the nature of Quicksilver’s configuration, it led to a lot of support questions from people who didn’t install everything needed for a particular feature.

Given that Quicksilver has so many functions and each user tends to have specific use cases in mind (for some iTunes control was their introduction, for others it was e-mail and contacts, for others finding and manipulating files)  I wanted the manual structured so that people could get directly to functionality that was interesting to them, find complete info, but be shown other things of interest while avoiding duplication as much as possible.

## Sections

The Introduction is intended for everyone to read through from beginning to end. New users find out what to use Quicksilver for and experienced users have terminology defined and perhaps learn some advanced invocation methods. 

The Configuration section walks through all of Quicksilver’s preferences in depth, particularly how to install plugins and setup triggers so later sections could just refer to it.

The Features section covers all the plugins, in detail. Each section includes general usage and configuration instructions, as well as troubleshooting hints and tips for using features more efficiently using advanced Quicksilver features. It includes every cool Quicksilver example I ever found. New users should be able to start using the features quickly and experienced users will probably find something new about many features. 

## Formatting

  * When giving examples of something to type, wrap each physical key in a `<kbd>` tag. For example, <kbd>⌘</kbd><kbd>A</kbd>, not <kbd>⌘A</kbd>. Don’t hesitate to use multiple characters to represent a single physical key if it makes sense, like <kbd>Space</kbd>.
  * Indent ordered and unordered lists by two characters before the asterisk or number. It makes them stand out better in the plain-text version, and if you ever need to include a second paragraph, the indentation of the text will look more natural. (Markdown requires follow-on paragraphs to be indented by 4 spaces. If the bullet is indented by 2, the text for the first line will naturally start at 4, lining it up with subsequent lines.)
  * Wrap the following in ticks to have them formatted using a fixed-width font:
    * File names
    * File extensions
    * Inline commands
    * Inline code snippets
  * Action names should be in **bold**.
  * Images of example commands should use the Bezel interface with the default colors. It’s popular, built-in, and smaller than Primer. Obviously use other interfaces if it’s important for some feature/concept.
  * Use bidirectional (a.k.a. smart or curly) quotes when speaking to the reader. Use unidirectional (a.k.a. straight) quotes in contexts where it makes sense, such as code snippets where bidirectional quotes would actually prevent the code from working.

    Many plain-text editors might not do this for you. macOS allows you to type bidirectional double quotes with <kbd>⌥</kbd><kbd>[</kbd> and <kbd>⌥</kbd><kbd>⇧</kbd><kbd>[</kbd>, while the single-quote equivalents are <kbd>⌥</kbd><kbd>]</kbd> and <kbd>⌥</kbd><kbd>⇧</kbd><kbd>]</kbd>.

  * Use the unicode symbols for various keys (as they appear in menu shortcuts)
    * Enter the applicable modifiers in the correct order: <kbd>⌃</kbd> <kbd>⌥</kbd> <kbd>⇧</kbd> <kbd>⌘</kbd>
  	* Use these where appropriate: <kbd>→</kbd>, <kbd>←</kbd>, <kbd>↑</kbd>, <kbd>↓</kbd>, <kbd>⌫</kbd>, and <kbd>⎋</kbd>. If you don’t know how to type the character that represents a particular key, you can almost certainly find it somewhere else in this manual and copy it.
  	* The Quicksilver preference pane has buttons on the bottom bar. Use these when referring to them: ↻ ⓘ
  * Put images in the `images` directory.

## Keep in Mind

  * Explain explicit installation steps for each feature at the top of the section. Include which plugins to install, everything that plugin installs (actions, handlers, an advanced preference pane, a catalog source, etc.) and how to configure them (e.g., if an action is installed but disabled by default, tell the user to enable it). 
  * Explain what Quicksilver does. Remember that it customizes itself for each user so be explicit about what the user types and Quicksilver’s behavior and why different users might see different behavior if they type the same thing. Remember that people rank actions differently (particularly if different plugins are installed) and catalogs are configured differently. 
  * People come to Quicksilver with very different skill levels. Some are new to macOS and don’t know details of how to install applications from `.dmg` files or other common conventions. Remember that people use keyboards in different languages with keys in different places.
  * When describing new features, include the version number it was added, e.g., “As of version 1.4.1…”. People using older versions will know something won’t apply to them. This version decoration can removed as older versions not supporting the feature are unsupported.
  * Include details of how to avoid common problems. e.g., Don’t add a catalog source that scans to infinite depth because it will use a lot of memory and make Quicksilver slow.
  * Use “TODO” to tag text to be changed/added.
  * The current text explains things in prose and the original PDF used a lot of images. Changing procedures to lists is probably a good thing.

The reason to be explicit about things is to reduce the number of support questions. The reason to be comprehensive is to get people to find out and try new features.

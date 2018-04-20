#Web Search

Allows searching the web.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 2.8.0
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


## Web Search Plugin

The Web Search Plugin for Quicksilver allows you to search websites from
within Quicksilver. By default, the Web Search Plugin includes a list of the
most commonly used websites for searching (e.g. Google, YouTube, Wikipedia).
You can also specify your own websites to search (see 'Custom Web Searches'
below).

### Actions

**Find With...**

The 'Find With...' action takes text in Quicksilver's 1st pane, and a web
search in the 3rd pane. An example could be:  
'Steve Jobs' ⇥ Find With... ⇥ Google.com

**Search For...**

'Search For...' works in a similar way to the 'Find With...' action but in
reverse; it takes a web search in the 1st pane and text in Quicksilver's 3rd
pane. E.g.  
Google.com ⇥ Search For... ⇥ 'Steve Jobs'

**Show Results For Search...**

This action works in exactly the same way as the 'Search For...' action, but
returns the results to Quicksilver's 1st pane in the form of links on the
results page. This action is an [alternate
action](http://qsapp.com/wiki/Alternate_Actions) to the 'Search For...'
action.

### Default Web Searches (Catalog)

The plugin contains two default web search lists (simple and advanced). The
simple list is enabled by default. To view the entries in each list, go to the
[Catalog Preferences](qs://preferences#QSCatalogPrefPane) and click the
'Plugins' tab. You should see two entries: 'Web Searches (Full List)' and 'Web
Searches (Simple)'. Enable/disable them, and expand the sidebar to see their
contents.

To request the addition of a new website to either list, post on the [support
forums](http://groups.google.com/group/blacktree-quicksilver/topics?gvc=2).

### Custom Web Searches (Catalog)

To create custom web searches, open the [Catalog
Preferences](qs://preferences#QSCatalogPrefPane), and create a new 'Web Search
List' catalog entry by clicking the '+' button in the bottom left hand corner
of the window.

**Typical Search Forms**

The easiest way to create a custom search URL is to search for `***` in the
website in question. Once you have done this, copy and paste the URL from your
browser into a new 'Web Search List' entry.

**POST Search Forms**

Certain websites use POST search forms (instead of GET forms), where the
search Query is not present in the URL, but is passed as a POST parameter
(viewing the website HTML is required). For these websites, you can create QSS
'POST' URLs.  

To achieve this, open a custom 'Web Search List', and expand the sidebar by
clicking the 'i' button (or pressing ⌘I).  
From the sidebar, add a new URL, with a prefix of either `qssp-http` or `qssp-
https` depending on whether the website is using http or https.  
After you have entered the URL of the search form, add `?key=***` to the end,
where `key` is the _name_ of the input as seen in the form online. An example
of a full search URL could be:

    
    
    qssp-http://google.com/?searchterm=***
    

### Credits

Favicons images for web search objects within Quicksilver are provided by
[Grabicon](https://grabicon.com)
# Intro

I wanted to write a plug-in. I found a bit of documentation on adding Actions, but that was about it. The rest was trial and error and stabbing in the dark (with some help from looking at existing plug-ins). I hope to spare others some of this frustration by documenting what I discovered. This is mainly a collection of random notes, rather than a step-by-step guide.

I'll assume you're working on a plug-in called "Blah" when giving examples.

## Getting Started

To compile most plug-ins, you'll need to build Quicksilver itself [from source][qssource]. (It'll put the stuff you need in `/tmp/QS`.) To build your plug-in with the Debug configuration, you'll need to first build Quicksilver with its Debug configuration. Same for the Release configuration.

To create a new plug-in:

  1. [Install Cookiecutter][icc]
  2. Run `cookiecutter https://github.com/quicksilver/plugin_template`
  3. Open the new project in Xcode

You should now have a plug-in that will build. If you want to use [Scripting Bridge](scripting-bridge.md), see the additional steps in that section.

Now might be a good time to create your Git repository and make the initial commit.

Many of the items in the template's `Info.plist` are named "SomethingTemplate". This prevents Quicksilver from having to process unused features. If you need to use settings in any of these sections, just rename them, removing "Template" from the end.

[qssource]: https://github.com/quicksilver/Quicksilver
[icc]: https://cookiecutter.readthedocs.io/en/latest/installation.html
